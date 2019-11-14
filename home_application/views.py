# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
from blueapps.account.decorators import login_exempt
from django.views.decorators.csrf import csrf_exempt
from .models import Test


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')


@login_exempt
@csrf_exempt
def test(request):
    """
    测试故障自愈HTTP回调
    :param request:
    :return:
    """
    ip = request.POST.get('ip')  # 告警主机ip
    # source_type = request.POST.get('source_type')  # 告警源
    alarm_type = request.POST.get('alarm_type')  # 告警类型
    source_time = request.POST.get('source_time')  # 告警时间
    cc_biz_id = request.POST.get('cc_biz_id')   # 业务id
    dic = {'alarm_type': alarm_type, 'ip': ip, 'source_time': source_time, 'cc_biz_id': cc_biz_id}
    Test.objects.create(**dic)
    result = dict()
    result['code'] = 200
    result['message'] = "Success"
    return HttpResponse(json.dumps(result), content_type='application/json')
