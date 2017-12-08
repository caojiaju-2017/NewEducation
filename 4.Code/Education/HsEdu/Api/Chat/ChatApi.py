#!/usr/bin/env python
# -*- coding: utf-8 -*-

from include import *
class ChatApi(object):
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
        if  command  == "List_Messages".upper():
            return ChatApi.ListMessages(request)
        elif command == "List_SubMsg".upper():
            return ChatApi.goMsgListPage(request)
        elif command == "Open_ChatRoom".upper():
            return ChatApi.goChatRoom(request)
        elif command == "View_Msg".upper():
            return ChatApi.goViewMsg(request)

    @staticmethod
    def ListMessages(request):
        return

    @staticmethod
    def goChatRoom(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/msg/msg_chat.html',renterDict )

    @staticmethod
    def goMsgListPage(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        msgList = []

        for index in range(14):
            oneMsg = {}
            oneMsg['code'] = uuid.uuid1().__str__().replace("-", "")
            oneMsg['name'] = "关于学生伙食费缴纳说明"
            oneMsg['simpleInfo'] = "新闻通稿基本都是模仿平面媒体的稿件形式来写的，按照基本的形式来分，可以分为消息稿和通讯稿。简单的说，可以按照这样的标准来对两种文体进行区别。报纸上新闻正文前面有某某报*月*日讯（消息头）记者某某人，然后才是新闻正文的，就是消息。上来就是文章，最后才署作者名字的新闻，多数是通讯。企业的新闻通稿就是要模仿这些不同的文体，把需要传达的内容预先写好。?"
            oneMsg['msgtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            msgList.append(oneMsg)

        renterDict['Msg_CodeDatas'] = msgList
        return render(request, './home/msg/msg_subList.html',renterDict )

    @staticmethod
    def goViewMsg(request):
        if (not HsShareData.IsDebug):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'warning_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        renterDict = {}
        return render(request, './home/msg/msg_view.html',renterDict )