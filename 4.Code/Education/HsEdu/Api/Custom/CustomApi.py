#!/usr/bin/env python
# -*- coding: utf-8 -*-

from include import *
class CustomApi(object):

    @staticmethod
    @csrf_exempt
    def CommandDispatch(request):
        # 检验签名信息
        if checkSign(request):
            loginResut = json.dumps({"ErrorInfo": "Sign Invalid", "ErrorId": 99999, "Result": None})
            return HttpResponse(loginResut)

        # 检查是否登陆
        if not isLogin(request):
            renterDict = {}
            return render(request, 'wait.html', renterDict)

        command = request.GET.get('Command').upper()
        if  command  == "Open_Resource".upper():
            return CustomApi.Open_Resource(request)
        elif command == "Open_Service".upper():
            return CustomApi.Open_Service(request)
        elif command == "view_remark".upper():
            return CustomApi.Open_Remark(request)
        elif command == "Get_Orders".upper():
            return CustomApi.Open_OrdersPage(request)
        elif command == "View_Order".upper():
            return CustomApi.ViewOrder(request)
        elif command == "Open_Contact".upper():
            return CustomApi.OpenContact(request)
        elif command == "Send_Suggest".upper():
            return CustomApi.SendSuggest(request)
        elif command == "Release_Suggest".upper():
            return CustomApi.ReleaseSuggest(request)
        elif command == "View_MyCheck".upper():
            return CustomApi.ViewMyCheck(request)

    @staticmethod
    def Open_Resource(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        renterDictAarry = []
        for index in range (20):
            renterDictAarry.append(index)

        renterDict['Res_Datas'] = renterDictAarry
        return render(request, './home/res/res_detail.html',renterDict )

    @staticmethod
    def Open_Service(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/srv/srv_detail.html',renterDict )

    @staticmethod
    def Open_Remark(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/remark/view_remark.html',renterDict )

    @staticmethod
    def Open_OrdersPage(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        resultList = []
        for index in range(10):
            oneRecord = {}
            oneRecord["code"] = "aaa_000%d"%index
            oneRecord["time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            oneRecord["title"] = "Title_000%d"%index

            resultList.append(oneRecord)

        renterDict['My_Orders'] = resultList
        return render(request, './home/usercenter/res_order.html',renterDict )

    @staticmethod
    def ViewOrder(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/usercenter/order_detail_info.html',renterDict )

    @staticmethod
    def OpenContact(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        configs = HsSysConfig.objects.all()
        for oneCfg in configs:
            if oneCfg.ckey == "SYS_QQ":
                renterDict["SYS_QQ"] = oneCfg.cvalue
            elif oneCfg.ckey == "SYS_PHONE":
                renterDict["SYS_PHONE"] = oneCfg.cvalue
            elif oneCfg.ckey == "SYS_EWM":
                renterDict["SYS_EWM"] = oneCfg.cvalue

        return render(request, './home/usercenter/cooperation.html',renterDict )

    @staticmethod
    def SendSuggest(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/usercenter/suggest.html',renterDict )

    @staticmethod
    def ViewMyCheck(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/usercenter/mycheck.html',renterDict )



    @staticmethod
    def ReleaseSuggest(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        postDataList = {}
        postDataList = getPostData(request)

        ucode = postDataList["ucode".lower()]
        title = postDataList["title".lower()]
        customname = postDataList["customname".lower()]
        customphone = postDataList["customphone".lower()]
        detail = postDataList["detail".lower()]

        newSuggest = HsSuggests()
        newSuggest.code = uuid.uuid1().__str__().replace("-", "")
        newSuggest.phone = customphone
        newSuggest.content = detail
        newSuggest.reltime =time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        newSuggest.title = title
        newSuggest.usercode = ucode
        newSuggest.username = customname

        commitDataList = []
        commitDataList.append(CommitData(newSuggest, 0))

        # 事务提交
        try:
            result = commitCustomDataByTranslate(commitDataList)

            if not result:
                loginResut = json.dumps({"ErrorInfo": "数据库操作失败", "ErrorId": 99999, "Result": None})
                return HttpResponse(loginResut)
        except Exception, ex:
            print ex
            loginResut = json.dumps({"ErrorInfo": "数据库操作失败", "ErrorId": 99999, "Result": None})
            return HttpResponse(loginResut)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
        return HttpResponse(loginResut)