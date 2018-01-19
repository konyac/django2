from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse
from app01 import models


# Create your views here.

def idnex(request):
    '''
    
    :param request: 
    :return: 
    '''
    '''
    obj = models.UserType(caption= '管理员')
    obj.save()

    models.UserType.objects.create(caption = "普通用户")

    user_dict = {"caption":"超级管理员"}
    models.UserType.objects.create(**user_dict)
    '''
    # user_info_dict = {'user': "alex",
    #                   "email": '123@163.com',
    #                   "pwd": 123,
    #                   "user_type": models.UserType.objects.get(nid=1)}
    # user_info_dict = {'user': "eric",
    #                   "email": '123@163.com',
    #                   "pwd": 456,
    #                   "user_type_id": 1}
    # models.UserInfo.objects.create(**user_info_dict)
    # ret = models.UserType.objects.all()
    # print(type(ret), ret, ret.query)
    #
    # for item in ret:
    #     print(type(item), item, item.caption, item.nid)
    # ret = models.UserType.objects.values('nid')
    # print(type(ret), ret, ret.query)
    # for item in ret:
    #     print(type(item), item)
    ret = models.UserType.objects.values_list('nid')
    print(type(ret),ret)
    return HttpResponse('OK')
