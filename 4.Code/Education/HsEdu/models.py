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


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class HsActiveMedia(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    actcode = models.CharField(db_column='ActCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mediafile = models.CharField(db_column='MediaFile', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_active_media'


class HsActives(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=20, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    stoptime = models.DateTimeField(db_column='StopTime', blank=True, null=True)  # Field name made lowercase.
    tmpcode = models.CharField(db_column='TmpCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_actives'


class HsBankAccount(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bankindex = models.IntegerField(db_column='BankIndex', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    bankaccount = models.CharField(db_column='BankAccount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_bank_account'


class HsClass(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    teachcode = models.CharField(db_column='TeachCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    stopdate = models.DateField(db_column='StopDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_class'


class HsClassResources(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    rescode = models.CharField(db_column='ResCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    classcode = models.CharField(db_column='ClassCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_class_resources'


class HsClassStudents(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    classcode = models.CharField(db_column='ClassCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    stucode = models.CharField(db_column='StuCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    innercode = models.CharField(db_column='InnerCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_class_students'


class HsClassSubjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    subcode = models.CharField(db_column='SubCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    teachcode = models.CharField(db_column='TeachCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    introimage = models.CharField(db_column='IntroImage', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_class_subjects'


class HsDeposits(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    applytime = models.DateTimeField(db_column='ApplyTime', blank=True, null=True)  # Field name made lowercase.
    applycount = models.FloatField(db_column='ApplyCount', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_deposits'


class HsMedias(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    mediafile = models.CharField(db_column='MediaFile', max_length=40, blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_medias'


class HsMsg(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    sendcode = models.CharField(db_column='SendCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    receivecode = models.CharField(db_column='ReceiveCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.
    msgtime = models.DateTimeField(db_column='MsgTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_msg'


class HsMsgTemplate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    tmpcontent = models.TextField(db_column='TmpContent', blank=True, null=True)  # Field name made lowercase.
    lastmodifytime = models.DateTimeField(db_column='LastModifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_msg_template'


class HsNotices(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    simpleinfo = models.CharField(db_column='SimpleInfo', max_length=128, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.
    releasetime = models.DateTimeField(db_column='ReleaseTime', blank=True, null=True)  # Field name made lowercase.
    attach1 = models.CharField(db_column='Attach1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    attach2 = models.CharField(db_column='Attach2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    attach3 = models.CharField(db_column='Attach3', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_notices'


class HsOrders(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ordertime = models.DateTimeField(db_column='OrderTime', blank=True, null=True)  # Field name made lowercase.
    goodscode = models.CharField(db_column='GoodsCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    downloadinfo = models.CharField(db_column='DownLoadInfo', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_orders'


class HsOrgBasetable(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    langitude = models.FloatField(db_column='Langitude', blank=True, null=True)  # Field name made lowercase.
    businesscontact = models.CharField(db_column='BusinessContact', max_length=64, blank=True, null=True)  # Field name made lowercase.
    businessphone = models.CharField(db_column='BusinessPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_org_basetable'


class HsOrgConfig(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    idcardimage1 = models.CharField(db_column='IDCardImage1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idcardimage2 = models.CharField(db_column='IDCardImage2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    idcardno = models.CharField(db_column='IDCardNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    orgimage = models.CharField(db_column='OrgImage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    orgid = models.CharField(db_column='OrgID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bankaccount = models.CharField(db_column='BankAccount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bankbranch = models.CharField(db_column='BankBranch', max_length=64, blank=True, null=True)  # Field name made lowercase.
    externdata1 = models.CharField(db_column='ExternData1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    externdata2 = models.CharField(db_column='ExternData2', max_length=64, blank=True, null=True)  # Field name made lowercase.
    externdata3 = models.CharField(db_column='ExternData3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    protcode = models.CharField(db_column='ProtCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgkey = models.CharField(db_column='OrgKey', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_org_config'


class HsOrgParents(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    parentcode = models.CharField(db_column='ParentCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    stopdate = models.DateField(db_column='StopDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_org_parents'


class HsOrgProtocol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    procode = models.CharField(db_column='ProCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    stopdate = models.DateField(db_column='StopDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_org_protocol'


class HsOrgStudents(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    stucode = models.CharField(db_column='StuCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_org_students'


class HsOrgSubjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    syscode = models.CharField(db_column='SysCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_org_subjects'


class HsOrgTeachers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    teachphone = models.CharField(db_column='TeachPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    subcode1 = models.CharField(db_column='SubCode1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    subcode2 = models.CharField(db_column='SubCode2', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_org_teachers'


class HsOrgWxconfig(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    wxappid = models.CharField(db_column='WXAppid', max_length=16, blank=True, null=True)  # Field name made lowercase.
    wxsecret = models.CharField(db_column='WXSecret', max_length=32, blank=True, null=True)  # Field name made lowercase.
    wxorigid = models.CharField(db_column='WxOrigId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wxtoken = models.CharField(db_column='WxToken', max_length=32, blank=True, null=True)  # Field name made lowercase.
    encodingaeskey = models.CharField(db_column='EncodingAESKey', max_length=64, blank=True, null=True)  # Field name made lowercase.
    callbackaddress = models.CharField(db_column='CallbackAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_org_wxconfig'


class HsParentStudent(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    parentcode = models.CharField(db_column='ParentCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    stucode = models.CharField(db_column='StuCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_parent_Student'


class HsParents(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    wxaccount = models.CharField(db_column='WxAccount', unique=True, max_length=64, blank=True, null=True)  # Field name made lowercase.
    wxheadimage = models.CharField(db_column='WxHeadImage', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_parents'


class HsPersonResource(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    rescode = models.CharField(db_column='ResCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rindex = models.IntegerField(db_column='RIndex', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_person_resource'


class HsPersonSetResources(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    personcode = models.CharField(db_column='PersonCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    accesscount = models.IntegerField(db_column='AccessCount', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    salecount = models.IntegerField(db_column='SaleCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_person_set_resources'


class HsProtocolDetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    procode = models.CharField(db_column='ProCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pndex = models.IntegerField(db_column='Pndex', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_protocol_detail'


class HsProtocols(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_protocols'


class HsRelaxMsg(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    sendcode = models.CharField(db_column='SendCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.
    releasetime = models.DateTimeField(db_column='ReleaseTime', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_relax_msg'


class HsRelaxReply(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    relaxcode = models.CharField(db_column='RelaxCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sendcode = models.CharField(db_column='SendCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.
    replytime = models.DateTimeField(db_column='ReplyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_relax_reply'


class HsResourceType(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_resource_type'


class HsSaleAccount(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=64, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=12, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    accountleft = models.CharField(db_column='AccountLeft', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lockmount = models.FloatField(db_column='LockMount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_sale_account'


class HsSaleOrder(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=200, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    requiredate = models.DateField(db_column='RequireDate', blank=True, null=True)  # Field name made lowercase.
    customname = models.CharField(db_column='CustomName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    customphone = models.CharField(db_column='CustomPhone', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_sale_order'


class HsSaleOrderAttach(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    applycode = models.CharField(db_column='ApplyCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    attchfile = models.CharField(db_column='AttchFile', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_sale_order_attach'


class HsSaleProtocol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    procode = models.CharField(db_column='ProCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    stopdate = models.DateField(db_column='StopDate', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_sale_protocol'


class HsServiceAccount(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    passwd = models.CharField(db_column='Passwd', max_length=32, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=64, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=64, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    accountleft = models.FloatField(db_column='AccountLeft', blank=True, null=True)  # Field name made lowercase.
    lockmount = models.FloatField(db_column='LockMount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_service_account'


class HsServiceProtocol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    procode = models.CharField(db_column='ProCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    stopdate = models.DateField(db_column='StopDate', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_service_protocol'


class HsSetResources(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    accesscount = models.IntegerField(db_column='AccessCount', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    salecount = models.IntegerField(db_column='SaleCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_set_resources'


class HsStuCheckin(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    stucode = models.CharField(db_column='StuCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    checktime = models.DateTimeField(db_column='CheckTime', blank=True, null=True)  # Field name made lowercase.
    longutide = models.FloatField(db_column='Longutide', blank=True, null=True)  # Field name made lowercase.
    langutide = models.FloatField(db_column='Langutide', blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_stu_checkin'


class HsStudents(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    passwd = models.CharField(db_column='Passwd', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    wxaccount = models.CharField(db_column='WxAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    wxheadimage = models.CharField(db_column='WxHeadImage', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_students'


class HsSuggests(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    usercode = models.CharField(db_column='UserCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    reltime = models.DateTimeField(db_column='RelTime', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qqcode = models.CharField(db_column='QQCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_suggests'


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


class HsSysSubujects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=64, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=64, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    orgname = models.CharField(db_column='OrgName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lantudite = models.FloatField(db_column='Lantudite', blank=True, null=True)  # Field name made lowercase.
    longdite = models.FloatField(db_column='Longdite', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_sys_subujects'


class HsTaskType(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_task_type'


class HsTasks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    tasktype = models.IntegerField(db_column='TaskType', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    simpleinfo = models.CharField(db_column='SimpleInfo', max_length=128, blank=True, null=True)  # Field name made lowercase.
    detaiinfo = models.TextField(db_column='DetaiInfo', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    stoptime = models.DateTimeField(db_column='StopTime', blank=True, null=True)  # Field name made lowercase.
    authorcode = models.CharField(db_column='AuthorCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    maincode = models.CharField(db_column='MainCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_tasks'


class HsTeachCheckin(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    stucode = models.CharField(db_column='StuCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    checktime = models.DateTimeField(db_column='CheckTime', blank=True, null=True)  # Field name made lowercase.
    longutide = models.FloatField(db_column='Longutide', blank=True, null=True)  # Field name made lowercase.
    langutide = models.FloatField(db_column='Langutide', blank=True, null=True)  # Field name made lowercase.
    orgcode = models.CharField(db_column='OrgCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_teach_checkin'


class HsTeacher(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    wxaccount = models.CharField(db_column='WxAccount', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    passwd = models.CharField(db_column='Passwd', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_teacher'
