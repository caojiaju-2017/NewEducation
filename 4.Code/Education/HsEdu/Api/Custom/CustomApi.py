#!/usr/bin/env python
# -*- coding: utf-8 -*-

from include import *
class CustomApi(object):
    @staticmethod
    @csrf_exempt
    def CommandDispatch(req):
        # 检验签名信息
        if not checkSign(req):
            loginResut = json.dumps({"ErrorInfo": "Sign Invalid", "ErrorId": 99999, "Result": None})
            return HttpResponse(loginResut)

        # 检查是否登陆
        if not isLogin(req):
            renterDict = {}
            return render(req, 'wait.html', renterDict)

        command = req.GET.get('Command').upper()
        # if  command  == "List_Messages".upper():
        #     return CustomApi.ListMessages(req)




