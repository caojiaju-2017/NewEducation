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
        if command == "Open_Resource".upper():
            return CustomApi.Open_Resource(request)
        elif command == "Query_Res".upper():
            return CustomApi.Query_Res(request)
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
        elif command == "View_MyOrganization".upper():
            return CustomApi.ViewMyOrganization(request)
        elif command == "View_Tasks".upper():
            return CustomApi.ViewTasks(request)
        elif command == "View_News".upper():
            return CustomApi.ViewNews(request)
        elif command == "Query_News".upper():
            return CustomApi.QueryNews(request)
        elif command == "WX_PAY_SUCCESS".upper():
            return CustomApi.WxPaySuccess(request)

    @staticmethod
    def WxPaySuccess(request):
        postDataList = {}
        postDataList = getPostData(request)

        ordercoce = postDataList["ordercoce"]
        openid = postDataList['openid']

        orderHandle = HsOrders.objects.filter(code=ordercoce).first()
        if not orderHandle:
            logger.error('Order Data Not found')
            loginResut = json.dumps({"ErrorInfo": "订单数据不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        if orderHandle.usercode != openid:
            logger.error('Order open id not same')
            loginResut = json.dumps({"ErrorInfo": "订单购买者数据异常", "ErrorId": 20002, "Result": None})
            return HttpResponse(loginResut)
        orderHandle.state = 6

        try:
            orderHandle.save()
            logger.error('Order save success')
        except Exception,ex:
            logger.error('Order save faild' + ex.message)
            pass

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
        return HttpResponse(loginResut)

    @staticmethod
    def Open_Resource(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'warning_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        code = request.GET.get('code')
        openid = request.GET.get('openid')
        logger.error("Resource code =%s" % (code))

        renterDict = {}

        resourceHandle = HsResources.objects.filter(code=code).first()

        if not resourceHandle:
            return render(request, '404.html', {})

        renterDict['Name'] = resourceHandle.restitle
        renterDict['Price'] = resourceHandle.price
        renterDict['Introduce'] = resourceHandle.resinfo
        renterDict['PreviewUrl'] = resourceHandle.previewurl
        renterDict['OrgName'] = resourceHandle.orgname
        renterDict['OrgImage'] = resourceHandle.orgimage
        renterDict['OrgInfo'] = resourceHandle.orginfo

        resourceItems = HsResourceInfo.objects.filter(rescode=code).order_by('index')
        renterDictAarry = []
        for oneItem in resourceItems:
            oneItemDict = {}
            oneItemDict["Index"] = oneItem.index
            oneItemDict["Title"] = oneItem.title
            oneItemDict["Info"] = oneItem.introduce
            renterDictAarry.append(oneItemDict)

        renterDict['Res_Datas'] = renterDictAarry
        renterDict['Res_Code'] = code

        # 检查当前用户是否购买了该资源
        orderHandle = HsOrders.objects.filter(goodscode=code,usercode=openid,state=6).first()

        logger.error("Check Order Info,Resource code =%s,UserCode=%s" % (code,openid))

        if orderHandle:
            renterDict['Res_Priv'] = 1
            renterDict['Priv_Title'] = "查看"
        else:
            renterDict['Res_Priv'] = 0
            renterDict['Priv_Title'] = "购买"

        return render(request, './home/res/res_detail.html', renterDict)

    @staticmethod
    def Query_Res(request):
        pageIndex = int(request.GET.get('pageindex'))
        pageSize = int(request.GET.get('pagesize'))
        filterS = request.GET.get('filter')
        grade = request.GET.get('grade')  # 学历
        gclass = request.GET.get('class')  # 班级
        subject = request.GET.get('subject')  # 科目

        logger.error("pageindex=%d,pageSize=%d,filter=%s,grade=%s,gclass=%s,subject=%s" % (
            pageIndex, pageSize, filterS, grade, gclass, subject))

        pageIndex = int(request.GET.get('pageindex'))
        pageSize = int(request.GET.get('pagesize'))

        gradeid = getNameId(0, grade)
        gclassid = getNameId(1, gclass)
        subjectid = getNameId(2, subject)
        ipreques = request.META['REMOTE_ADDR']

        logger.error("gradeid=%d,gclassid=%d,subjectid=%d,filterS=%s" % (
            gradeid, gclassid, subjectid, filterS))

        resArray = []
        resDatas = None

        resDatas = queryResource(gradeid, gclassid, subjectid, filterS)
        logger.error("queryResource ,get record count=%d" % len(resDatas))
        resDatas = resDatas[pageIndex * pageSize:pageIndex * pageSize + pageSize]
        for oneRes in resDatas:
            resDict = {}
            resDict['ResGrade'] = getName(0, oneRes.resgrade)
            resDict['ResLevel'] = getName(1, oneRes.reslevel)
            resDict['ResClass'] = getName(2, oneRes.resclass)
            resDict['ResInfo'] = oneRes.resinfo[:50]
            resDict['ResImage'] = oneRes.resimage
            resDict['Price'] = oneRes.price
            resDict['Name'] = oneRes.name
            resDict['ViewCount'] = oneRes.viewcount
            resDict['BuyCount'] = 14
            resDict['ResTitle'] = oneRes.restitle
            resDict['OrgName'] = oneRes.orgname
            resDict['Code'] = oneRes.code
            resDict['ResImage'] = oneRes.resimage

            resArray.append(resDict)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": resArray})
        return HttpResponse(loginResut)

    @staticmethod
    def Open_Remark(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'warning_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/remark/view_remark.html', renterDict)

    @staticmethod
    def Open_OrdersPage(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'warning_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        try:
            openId = request.GET.get('openId')
        except:
            openId = None

        logger.error('WX OpenId=====================================' + openId)
        renterDict = {}
        resultList = []

        orderDatas = HsOrders.objects.filter(usercode=openId, state=6)
        for oneOrder in orderDatas:
            oneRecord = {}
            oneRecord["code"] = oneOrder.code
            oneRecord["goodscode"] = oneOrder.goodscode
            oneRecord["time"] = oneOrder.ordertime

            resHandle = HsResources.objects.filter(code=oneOrder.goodscode).first()

            oneRecord["title"] = resHandle.restitle
            oneRecord["simpleimage"] = resHandle.resimage
            logger.error('resHandle.resimage=====================================' + resHandle.resimage)
            resultList.append(oneRecord)

        renterDict['My_Orders'] = resultList
        return render(request, './home/usercenter/res_order.html', renterDict)

    @staticmethod
    def ViewOrder(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'warning_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        try:
            resCode = request.GET.get('code')
        except:
            resCode = None

        logger.error('orderCode=====================================' + resCode)

        orderHandler = None
        if resCode:
            # 查询订单数据
            orderHandler = HsResourcesSecretInfo.objects.filter(rescode=resCode).first()

        renterDict = {}
        configs = HsSysConfig.objects.all()
        for oneCfg in configs:
            if oneCfg.ckey == "SYS_QQ":
                renterDict["SYS_QQ"] = oneCfg.cvalue
            elif oneCfg.ckey == "SYS_PHONE":
                renterDict["SYS_PHONE"] = oneCfg.cvalue
            elif oneCfg.ckey == "SYS_EWM":
                renterDict["SYS_EWM"] = oneCfg.cvalue

        if orderHandler:
            renterDict['BaiduNetUrl'] = orderHandler.downloadurl
            renterDict['BaiduNetUrlPswd'] = orderHandler.dlpsswd
        else:
            renterDict['BaiduNetUrl'] = "资源链接失效"
            renterDict['BaiduNetUrlPswd'] = '资源失效'
        return render(request, './home/usercenter/order_detail_info.html', renterDict)

    @staticmethod
    def OpenContact(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'warning_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        renterDict = {}
        configs = HsSysConfig.objects.all()
        for oneCfg in configs:
            if oneCfg.ckey == "SYS_QQ":
                renterDict["SYS_QQ"] = oneCfg.cvalue
            elif oneCfg.ckey == "SYS_PHONE":
                renterDict["SYS_PHONE"] = oneCfg.cvalue
            elif oneCfg.ckey == "SYS_EWM":
                renterDict["SYS_EWM"] = oneCfg.cvalue

        return render(request, './home/usercenter/cooperation.html', renterDict)

    @staticmethod
    def SendSuggest(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'warning_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/usercenter/suggest.html', renterDict)

    @staticmethod
    def ViewNews(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'warning_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})
        renterDict = {}

        Code = request.GET.get('Code')

        newsHandle = HsNews.objects.filter(code=Code).first()

        renterDict["NewsTitle"] = newsHandle.title
        renterDict["NewsCode"] = newsHandle.code

        if not newsHandle:
            return render(request, './home/news/view_news.html', renterDict)

        Items = HsNewsInfo.objects.filter(ncode=Code).order_by('tindex')

        arr = []
        for one in Items:
            abc = {}
            abc["Index"] = one.tindex
            abc["StepName"] = "第%d:" % (one.tindex + 1)
            abc["Title"] = one.title
            abc["Info"] = one.info
            abc["Image"] = one.imagename
            arr.append(abc)

        renterDict["TitleInfos"] = arr

        # return render(request, './home/news/' + newsInfo.urlname, renterDict)
        return render(request, './home/news/view_news.html', renterDict)

    @staticmethod
    def QueryNews(request):
        pageIndex = int(request.GET.get('pageindex'))
        pageSize = int(request.GET.get('pagesize'))
        # start = int(request.GET.get('start'))

        ipreques = request.META['REMOTE_ADDR']
        results = HsNews.objects.filter().order_by('-newstime')[pageIndex * pageSize:pageIndex * pageSize + pageSize]

        rtnResult = []
        for index, one in enumerate(results):
            oneNews = {}
            oneNews['Title'] = one.title
            oneNews["Info"] = one.info[0:60]
            oneNews['Date'] = one.newstime
            oneNews['Image'] = one.image
            oneNews['Code'] = one.code
            rtnResult.append(oneNews)

        # print rtnResult
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnResult})
        return HttpResponse(loginResut)

    @staticmethod
    def ReleaseSuggest(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'warning_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        postDataList = {}
        postDataList = getPostData(request)

        ucode = postDataList["ucode".lower()].encode('utf-8')
        title = postDataList["title".lower()].encode('utf-8')
        customname = postDataList["customname".lower()].encode('utf-8')
        customphone = postDataList["customphone".lower()].encode('utf-8')
        detail = postDataList["detail".lower()].encode('utf-8')

        # 推送邮件
        try:
            bodyData = "用户%s：通过微店反馈意见 \n他的电话为：%s \n 意见详细描述为：%s" % (customname, customphone, detail)
            # BaseEmail.sendMail(bodyData, title)
            # sendmailThread = threading.Thread(target=BaseEmail.sendMail, args=(bodyData,title,))
            # sendmailThread.setDaemon(True)
            # sendmailThread.start()
        except Exception, ex:
            raise ex
            logger.error('send mail failed!=====================================')

        newSuggest = HsSuggests()
        newSuggest.code = uuid.uuid1().__str__().replace("-", "")
        newSuggest.phone = customphone
        newSuggest.content = detail
        newSuggest.reltime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
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
