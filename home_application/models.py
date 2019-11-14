# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Test(models.Model):
    """
    报警信息
    """

    cc_biz_id = models.IntegerField(blank=True, null=True, verbose_name="业务id")
    # cc_biz_name = models.CharField(max_length=20, default='', verbose_name='业务名称')
    ip = models.CharField(max_length=30, null=True, verbose_name="ip")
    alarm_type = models.CharField( max_length=50, null=True, verbose_name="报警类型")
    # alarm_title = models.CharField(max_length=128, default='', verbose_name='报警标题')
    # alarm_content = models.CharField(max_length=128, default='', verbose_name='报警内容')
    source_time = models.DateTimeField(verbose_name="报警时间", auto_now=True)

