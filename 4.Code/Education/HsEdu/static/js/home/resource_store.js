$.extend({
    openResourceDetail: function (codeName) {
        // alert("fas");
        var openId = $.cookie("OpenId");
        // alert(openId);
        window.location = "/res_detail.html?Command=Open_Resource&code=" + codeName + "&openid=" + openId;
    },
});