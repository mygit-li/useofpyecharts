from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.template import loader
from pyecharts import Bar, Geo
from celery_test.tasks import celery_send_email


def exc_sql(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def m_report(request):
    template = loader.get_template('m_report.html')
    context = {
        "data": m_report_inner()
    }
    return HttpResponse(template.render(context, request))


def m_report_inner():
    cols = """select 年度,本年度新增 from report_reg_year_analyse"""
    data_list = exc_sql(cols)
    attr = [i[0] for i in data_list]
    print(attr)
    v1 = [i[1] for i in data_list]
    print(v1)

    bar = Bar('注册情况')
    bar.add('会员按年度统计', attr, v1, is_stack=True, mark_point=['max', 'min', 'all'])
    return bar.render_embed()


def index(request):
    template = loader.get_template('ddd.html')
    context = {
        "data": line3d()
    }
    return HttpResponse(template.render(context, request))


def line3d():
    from pyecharts import Line3D

    import math
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return line3d.render_embed()


def guo_report(request):
    # select    province, difi_re_num    from REPORT_REG
    ret = """select city, difi_re_num  from REPORT_REG a, province_to_city b where a.province=b.province"""
    data_list = exc_sql(ret)
    attr = [i[0] for i in data_list]
    value = [i[1] for i in data_list]
    geo = Geo("全国各地用户注册图", width=1200, height=600)
    geo.add("各省注册量", attr, value, type="effectScatter", border_color="#ffffff", symbol_size=2,
            is_label_show=True, label_text_color="#00FF00", label_pos="inside", symbol_color="yellow",
            geo_normal_color="#006edd", geo_emphasis_color="#0000ff")
    data = {'data': geo.render_embed()}
    return render(request, 'guo_report.html', data)


def add_task_to_celery(request):
    celery_send_email.delay(u'邮件主题', 'test_mail_message', 'lijianwei@mail.haoyisheng.com',
                            ['lijianwei@mail.haoyisheng.com'])
    return HttpResponse('hello world')
