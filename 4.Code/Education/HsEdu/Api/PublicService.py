#!/usr/bin/env python
# -*- coding: utf-8 -*-
from include import *

SignKey = 'Sign'
def checkSign(request):
    global SignKey
    '''
    检查签名是否合法
    :param dicts:  参数字典
    :param signString: 请求者传递的签名信息
    :return:True 签名正确   False  签名不正确
    '''

    # 获取Post参数
    postDict=getPostData(request)

    # 获取Get参数
    getDict = getGetParamData(request)

    # 合并参数
    dictMerged = dict(postDict, **getDict)

    # 剔除签名键值
    if not dictMerged.has_key(SignKey):
        return False
    sign =dictMerged[SignKey]
    del dictMerged[SignKey]

    # 开始签名
    sortDicts = sorted(dictMerged.iteritems(),key=lambda  asd:asd[0])
    signStr = ""
    for oneParam in sortDicts:
        signStr = signStr + "%s=%s"%(oneParam[0],oneParam[1])

    signStr = signStr + HsShareData.SigCode

    md5M = md5.new()
    md5M.update(signStr)
    signData =md5M.hexdigest()

    if signData == sign:
        return True

    return True

def isLogin(request):
    '''
    检查请求中是否包含账号信息
    :param request:
    :return:
    '''
    return True

def getPostData(request):
    '''
    获取post参数
    :param request:
    :return:
    '''
    postDataList = {}
    dataListTemp = {}
    if request.method == 'POST':
        for key in request.POST:
            postDataList[key] = request.POST.getlist(key)[0]

    import json
    if not postDataList or len(postDataList) == 0:
        try:
            bodyTxt = request.body
            dataListTemp = json.loads(bodyTxt)
        except Exception,ex:
            pass

    for onePairKey in dataListTemp.keys():
        postDataList[onePairKey.lower()] = dataListTemp[onePairKey]
    return  postDataList

def getGetParamData(request):
    '''
    提取请求Get参数
    :param request:
    :return:
    '''
    urlFullPath = request.get_full_path()
    values = urlFullPath.split('?')[-1]

    getParamsDataList={}
    for key_value in values.split('&'):
        onePairs = key_value.split('=')

        if len(onePairs) != 2:
            continue
        getParamsDataList[onePairs[0].lower()] = onePairs[1]
    return  getParamsDataList

def commitCustomDataByTranslate(objHandles):
    '''
    提交数据修改-事务
    :param objHandles:
    :return:
    '''
    with transaction.atomic():
        for oneObject in objHandles:
            if not oneObject.dbHandle:
                continue

            try:
                if oneObject.operatorType == 0:
                    oneObject.dbHandle.save()
                elif oneObject.operatorType == 1:
                    oneObject.dbHandle.delete()
            except Exception,ex:
                return  False

    return True
