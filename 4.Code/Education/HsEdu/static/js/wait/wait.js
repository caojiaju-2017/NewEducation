var appID = "wx6d45e5e461e41f06";
var appsecret = "726c202ca673beff13e4bc7dd0d5d01a";

window.onload=function()
{
    // setTimeout(
    //     function()
    //     {
    //         window.location.replace("./");
    //     }, 3000
    // )    ;

    $.weixinLogin();
};

$(document).ready(function()
{
});

$.extend({
    weixinLogin:function () {
            var urlCode = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=" + appID + "&redirect_uri=http%3a%2f%2fwww.chuweinews.com&response_type=code&scope=snsapi_userinfo&state=abc#wechat_redirect";
            location.href = urlCode;
        }
});
