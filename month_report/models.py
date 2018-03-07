# from django.db import models
#
#
# class ReportReg(models.Model):
#     P_CODE = models.CharField(max_length=9, null=True, verbose_name='省份代码')
#     PROVINCE = models.CharField(max_length=50, null=True, verbose_name='省份')
#     EASY_RE_NUM = models.IntegerField(null=True, verbose_name='简单注册人数')
#     DIFI_RE_NUM = models.IntegerField(null=True, verbose_name='注册人数')
#     CUR_RE_NUM = models.IntegerField(null=True, verbose_name='本年度注册人数')
#     JAU = models.IntegerField(null=True, verbose_name='一月注册人数')
#     FAN = models.IntegerField(null=True, verbose_name='二月注册人数')
#     MAR = models.IntegerField(null=True, verbose_name='三月注册人数')
#     AIR = models.IntegerField(null=True, verbose_name='四月注册人数')
#     MAY = models.IntegerField(null=True, verbose_name='五月注册人数')
#     TRU = models.IntegerField(null=True, verbose_name='六月注册人数')
#     JUL = models.IntegerField(null=True, verbose_name='七月注册人数')
#     AUG = models.IntegerField(null=True, verbose_name='八月注册人数')
#     SEP = models.IntegerField(null=True, verbose_name='九月注册人数')
#     OCT = models.IntegerField(null=True, verbose_name='十月注册人数')
#     NOV = models.IntegerField(null=True, verbose_name='十一月注册人数')
#     DEC = models.IntegerField(null=True, verbose_name='十二月注册人数')
#
#     class Meta:
#         db_table = "report_reg"
