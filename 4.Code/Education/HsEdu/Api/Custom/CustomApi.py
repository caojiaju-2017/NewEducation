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

