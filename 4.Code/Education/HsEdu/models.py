# TEMPLATE_DIRS ['E:\\GitWorkSpace\\NewEducation\\4.Code\\Education\\HsEdu\\templates']
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class HsOrders(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True,null=True)  # Field name made lowercase.
    ordertime = models.DateTimeField(db_column='OrderTime', blank=True, null=True)  # Field name made lowercase.
    goodscode = models.CharField(db_column='GoodsCode', max_length=32, blank=True,null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    downloadinfo = models.CharField(db_column='DownLoadInfo', max_length=1024, blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_orders'


class HsRelaxReply(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    relaxcode = models.CharField(db_column='RelaxCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sendcode = models.CharField(db_column='SendCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.
    replytime = models.DateTimeField(db_column='ReplyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_relax_reply'


class HsResources(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    resgrade = models.CharField(db_column='ResGrade', max_length=32, blank=True, null=True)  # Field name made lowercase.
    resclass = models.CharField(db_column='ResClass', max_length=32, blank=True,  null=True)  # Field name made lowercase.
    reslevel = models.CharField(db_column='ResLevel', max_length=32, blank=True,null=True)  # Field name made lowercase.

    restitle = models.CharField(db_column='ResTitle', max_length=64, blank=True, null=True)  # Field name made lowercase.
    resinfo = models.CharField(db_column='ResInfo', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    resimage = models.CharField(db_column='ResImage', max_length=32, blank=True, null=True)  # Field name made lowercase.

    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    viewcount = models.IntegerField(db_column='ViewCount', blank=True, null=True)  # Field name made lowercase.
    orgname = models.CharField(db_column='OrgName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    orgimage = models.CharField(db_column='OrgImage', max_length=64, blank=True, null=True)  # Field name made lowercase.
    orginfo = models.CharField(db_column='OrgInfo', max_length=640, blank=True, null=True)  # Field name made lowercase.
    previewurl = models.CharField(db_column='PreviewUrl', max_length=480, blank=True,null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'hs_resources'


class HsResourceInfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rescode = models.CharField(db_column='ResCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField(db_column='Index', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    introduce = models.CharField(db_column='Introduce', max_length=2000, blank=True,null=True)  # Field name made lowercase.
    restype = models.IntegerField(db_column='ResType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_resource_info'


class HsResourcesSecretInfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rescode = models.CharField(db_column='ResCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    downloadurl = models.CharField(db_column='DownloadUrl', max_length=2000, blank=True,null=True)  # Field name made lowercase.
    dlpsswd = models.CharField(db_column='DLPsswd', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_resource_secret'


class HsCustom(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    wxaccount = models.CharField(db_column='WxAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    headimage = models.CharField(db_column='HeadImage', max_length=2000, blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_custom'


class HsNews(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    urlname = models.CharField(db_column='UrlName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=32, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=32, blank=True, null=True)  # Field name made lowercase.
    newstime = models.CharField(db_column='NewsTime', max_length=20, blank=True,null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_news'


class HsSuggests(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    reltime = models.DateTimeField(db_column='RelTime', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_suggests'

class HsResRemark(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    rcode = models.CharField(db_column='RCode', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=64, blank=True,null=True)  # Field name made lowercase.
    reltime = models.DateTimeField(db_column='RelTime', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'hs_res_remark'


class HsSysConfig(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ckey = models.CharField(db_column='CKey', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cvalue = models.CharField(db_column='CValue', max_length=128, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ctype = models.IntegerField(db_column='CType', blank=True, null=True)  # Field name made lowercase.
    cexpress = models.CharField(db_column='CExpress', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_sys_config'


class HsWxTicket(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ticket = models.CharField(db_column='Ticket', unique=True, max_length=64, blank=True,null=True)  # Field name made lowercase.
    signtime = models.CharField(db_column='SignTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.CharField(db_column='TimeStamp', max_length=32, blank=True,null=True)  # Field name made lowercase.
    noncestr = models.CharField(db_column='NonceStr', max_length=20, blank=True,null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=64, blank=True, null=True)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    timeoutsecond = models.IntegerField(db_column='TimeOutSecond', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_wx_ticket'


class HsNewsInfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ncode = models.CharField(db_column='NCode', unique=True, max_length=32, blank=True,null=True)  # Field name made lowercase.
    tindex = models.IntegerField(db_column='TIndex', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    imagename = models.CharField(db_column='ImageName', max_length=64, blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_newsinfo'


class HsWXConfig(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    appid = models.CharField(db_column='AppId', unique=True, max_length=200, blank=True,null=True)  # Field name made lowercase.
    appsecret = models.CharField(db_column='AppSecret', unique=True, max_length=200, blank=True,null=True)  # Field name made lowercase.
    apikey = models.CharField(db_column='ApiKey', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mchid = models.CharField(db_column='MchId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nonestr = models.CharField(db_column='NoneStr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notifyurl = models.CharField(db_column='NotiryUrl', max_length=200, blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_newsinfo'              