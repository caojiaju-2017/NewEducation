var  openId;
var openName ;
var openHeadImage;

window.onload=function()
{
    openId = getUrlParam('OpenId');
    openName = getUrlParam('WxName');
    openHeadImage = getUrlParam('HeadImg');

    $.cookie("OpenId",openId);
    $.cookie("WxName",openName);
    $.cookie("HeadImg",openHeadImage);
};

$(document).ready(function()
{
    var iframeHeight = $(document).height();
    $("#main_frame_id").height(iframeHeight - 105);
});


$.extend({

});
