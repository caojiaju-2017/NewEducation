var openId;
var openName;
var openHeadImage;

var currentType = 0

var isFinishLoad = false;
var currentPageIndex = 0;
var currentPageSize = 10;
var queryLock = false;

var isResLoadFinishLoad = false;
var currentResLoadPageIndex = 0;
var currentResLoadPageSize = 10;
var queryResLoadLock = false;

var oneTemplate = '<a class="list-group-item row" style="border-bottom:1px solid #000;height:240px" onclick="$.openNews(\'{Code}\')">\n' +
    '                    <div class="col-xs-3 col-sm-3 col-md3" style="margin-top: 10px">\n' +
    '                        <img class="col-xs-12 col-sm-12 col-md12" src="/static/Images/newsPic/{Image}"\n' +
    '                             style="width: 200px;height: 180px;margin-top: 10px;border-radius: 10px;padding-left: 0px;padding-right: 0px"/>\n' +
    '                    </div>\n' +
    '\n' +
    '                    <div class="col-xs-9 col-sm-9 col-md9"\n' +
    '                         style="font-size: 40px;word-break: break-all;word-wrap: break-word;">\n' +
    '                        <div class="col-xs-12 col-sm-12 col-md12" style="font-weight: bold">\n' +
    '                            {Title}\n' +
    '                        </div>\n' +
    '                        <div class="col-xs-12 col-sm-12 col-md12"\n' +
    '                             style="font-size: 30px;word-break: break-all;word-wrap: break-word">\n' +
    '                            {Info}\n' +
    '                        </div>\n' +
    '\n' +
    '                        <div class="col-xs-12 col-sm-12 col-md12"\n' +
    '                             style="font-size: 30px;word-break: break-all;word-wrap: break-word;text-align: end;color: #0c8a90">\n' +
    '                            {Date}\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                </a>';

var oneResourceTmpl = "<a onclick=\"$.openResourceDetail('{Code}')\" class=\"list-group-item row\"\n" +
    "                   style=\"height: 260px;padding-left: 0px;padding-right: 0px\">\n" +
    "                    <div class=\"col-xs-3 col-sm-3 col-md3 img text-center\"\n" +
    "                         style=\"height: 100%\">\n" +
    "                        <img src=\"/static/Images/newsPic/news10008.jpg\" class=\"img-thumbnail\"\n" +
    "                             style=\"margin-left: 0px;position: relative;top: 50%;transform: translateY(-50%);width: 94%;height: 80%;border-radius: 20px\"/>\n" +
    "                    </div>\n" +
    "                    <div class=\"col-xs-6 col-sm-6 col-md6\" style=\";padding-left: 0px;padding-right: 0px\">\n" +
    "                        <div class=\"col-xs-12 col-sm-12 col-md12\" style=\"margin-top: 20px\">\n" +
    "                            <span class=\"label label-primary\" style=\"font-size: 25px\">{ResGrade}</span>\n" +
    "                            <span class=\"label label-success\" style=\"font-size: 25px\">{ResLevel}</span>\n" +
    "                            <span class=\"label label-info\" style=\"font-size: 25px\">{ResClass}</span>\n" +
    "                        </div>\n" +
    "\n" +
    "                        <div class=\"col-xs-12 col-sm-12 col-md12\"\n" +
    "                             style=\"font-size: 30px;padding-left: 20px;color: #000;margin-top: 20px;color: #606060\">\n" +
    "                            {ResInfo}\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                    <div class=\"col-xs-3 col-sm-3 col-md3 time\"\n" +
    "                         style=\"font-size: 30px;padding-left: 0px;padding-right: 0px\">\n" +
    "                        <div class=\"col-xs-12 col-sm-12 col-md12\" style=\"color: #000\">\n" +
    "                            {Name}\n" +
    "                        </div>\n" +
    "                        <div class=\"col-xs-12 col-sm-12 col-md12\" style=\"color: #ec971f \">\n" +
    "                            价格：{Price}元\n" +
    "                        </div>\n" +
    "\n" +
    "                        <div class=\"col-xs-12 col-sm-12 col-md12\" style=\"color: #8c8c8c\">\n" +
    "                            浏览量：<span class=\"badge\" style=\"font-size: 20px\">{ViewCount}</span>\n" +
    "                        </div>\n" +
    "\n" +
    "                        <div class=\"col-xs-12 col-sm-12 col-md12\" style=\"color: #8c8c8c\">\n" +
    "                            交易量：<span class=\"badge\" style=\"font-size: 20px\">{BuyCount}</span>\n" +
    "                        </div>\n" +
        "                    <div class=\"col-xs-12 col-sm-12 col-md12 img buy-center\"\n" +
        "                         style=\"\">\n" +
        "                        <img src=\"/static/Images/Icon/buy.jpg\" class=\"img-circle\" style=\"width: 60px;height: 40px\"/>\n" +
        "                    </div>\n" +

    "                    </div>\n" +
    "\n" +
    "                </a>";

var bottomSep = '<div style="height: 110px;width: 100%"></div>';
window.onload = function () {
//     openId = getUrlParam('OpenId');
//     openName = getUrlParam('WxName');
//     openHeadImage = getUrlParam('HeadImg');
//
//     $.cookie("OpenId", openId);
//     $.cookie("WxName", openName);
//     $.cookie("HeadImg", openHeadImage);
//
// //    设置头像数据
//     $("#uName").text(openName);
//     $("#user_head").attr('src',openHeadImage);
};

$(document).ready(function () {
    // var iframeHeight = $(document).height();
    // $("#main_frame_id").height(iframeHeight - 105);
    //
    $(window).scroll(function () {
        var srollPos = $(window).scrollTop();
        var documentHd = $(document).height();
        var winHd = $(window).height();


        totalheight = parseFloat($(window).height()) + parseFloat(srollPos);

        if (srollPos + winHd > documentHd * 0.9) {
            // alert(currentType);
            if (currentType == 0) {
                if (!isFinishLoad && !queryLock) {
                    queryLock = true;
                    // 加载数据
                    currentPageIndex = currentPageIndex + 1;
                    $.query_vote_number();
                }
            }
            else {
                if (!isResLoadFinishLoad&& !queryResLoadLock) {
                    queryResLoadLock = true;
                    // 加载数据
                    currentResLoadPageIndex = currentResLoadPageIndex + 1;
                    $.searchResource();
                }
            }
        }
    });

    var bIndex = $.cookie("BrowserIndex");
    if (bIndex == 1)
    {
        $.showResource();
    }
    else if (bIndex == 0)
    {
        $.showHome()
    }
    else if (bIndex == -1)
    {
        $.showUser();
    }
});

$.extend({
    setUserInfo: function (openid,username,headimg) {
        // alert('afsd');
        // alert(openid);
        // alert(username);
        // alert(headimg);
        $.cookie("OpenId", openid);
        $.cookie("WxName", username);
        $.cookie("HeadImg", headimg);

        //    设置头像数据
        $("#uName").text(username);
        $("#user_head").attr('src',headimg);
    },
    showResource: function () {

        $("#res_div").show();
        $("#home_div").hide();
        $("#usercenter_div").hide();
        currentType = 1;

        $.cookie("BrowserIndex",1);
    },
    getMyOrder: function () {
			//javascrtpt:window.parent.location.href='./res_order.html?Command=Get_Orders&Type=1'
			var openId = $.cookie("OpenId");
			location.href='./res_order.html?Command=Get_Orders&Type=1&openId=' + openId;
    },    
    showHome: function () {
        $("#res_div").hide();
        $("#home_div").show();
        $("#usercenter_div").hide();
        currentType = 0;

        $.cookie("BrowserIndex",0);
    },
    showUser: function () {
        $("#res_div").hide();
        $("#home_div").hide();
        $("#usercenter_div").show();
        currentType = -1;

        $.cookie("BrowserIndex",-1);
    },
    openNews: function (codeName) {
        window.location = "/view_news.html?Command=View_News&Code=" + codeName;
    },
    StringFormat: function () {
        if (arguments.length == 0)
            return null;
        var str = arguments[0];
        for (var i = 1; i < arguments.length; i++) {
            var re = new RegExp('\\{' + (i - 1) + '\\}', 'gm');
            str = str.replace(re, arguments[i]);
        }
        return str;
    },
    format: function (source, args) {
        var result = source;
        if (typeof(args) == "object") {
            if (args.length == undefined) {
                for (var key in args) {
                    if (args[key] != undefined) {
                        var reg = new RegExp("({" + key + "})", "g");
                        result = result.replace(reg, args[key]);
                    }
                }
            } else {
                for (var i = 0; i < args.length; i++) {
                    if (args[i] != undefined) {
                        var reg = new RegExp("({[" + i + "]})", "g");
                        result = result.replace(reg, args[i]);
                    }
                }
            }
        }
        return result;
    },

    get_query_cmd: function () {
        var rtnCmd = "/api/ctm/?Command=Query_News&pageindex={0}&pagesize={1}";
        rtnCmd = $.StringFormat(rtnCmd, currentPageIndex, currentPageSize);
        return rtnCmd;
    },
    query_vote_number: function (fcode) {
        var cmdString = $.get_query_cmd();
        // 提取用户名
        $.get(cmdString,
            function (data) {
                // 检查查询状态
                var ErrorId = data.ErrorId;
                var Result = data.Result;
                var Datas = Result;
                if (ErrorId == 200) {
                    if (Datas.length <= 0 || Datas.length < currentPageSize) {
                        isFinishLoad = true;
                    }

                    for (i = 0; i < Datas.length; i++) {
                        var oneCode1 = Datas[i];

                        var abcTemp = {};
                        abcTemp["Title"] = oneCode1.Title;
                        abcTemp["Info"] = oneCode1.Info;
                        abcTemp["Date"] = oneCode1.Date;
                        abcTemp["Image"] = oneCode1.Image;
                        abcTemp["Code"] = oneCode1.Code;

                        var oneT = $("#newsList").html();

                        $("#newsList").html(oneT + $.format(oneTemplate, abcTemp));
                    }
                    var oneT = $("#newsList").html();

                    $("#newsList").html(oneT + bottomSep);
                    queryLock = false;
                }

            },
            "json");//这里返回的类型有：json,html,xml,text
    },
    changeSelect: function (btnId, selVal) {
        $("#" + btnId).html(selVal + "<span class=\"caret\"></span>");
    },


    get_resquery_cmd: function (xueli, xuenian, subjiect, filter) {
        var rtnCmd = "/api/ctm/?Command=Query_Res&pageindex={0}&pagesize={1}&filter={2}&grade={3}&class={4}&subject={5}";
        rtnCmd = $.StringFormat(rtnCmd, currentResLoadPageIndex, currentResLoadPageSize, filter, xueli, xuenian, subjiect);
        return rtnCmd;
    },
    searchResource: function () {
        // 取出值
        var xueli = $("#dropdownMenu1").html();
        var xuenian = $("#dropdownMenu2").html();
        var kemu = $("#dropdownMenu3").html();
        var fliter = $("#fliter_input").val();

        // 去掉无效空格和分行
        xueli = xueli.replace("<span class=\"caret\"></span>", "");
        xueli = $.trim(xueli)
        xueli = xueli.replace("/\s/g", "");

        xuenian = xuenian.replace("<span class=\"caret\"></span>", "");
        xuenian = $.trim(xuenian)
        xuenian = xuenian.replace("/\s/g", "");

        kemu = kemu.replace("<span class=\"caret\"></span>", "");
        kemu = $.trim(kemu)
        kemu = kemu.replace("/\s/g", "");

        // 开始判断---未选中时处理
        if (xueli == "学历") {
            xueli = "";
        }

        // 开始判断---未选中时处理
        if (xuenian == "学年") {
            xuenian = "";
        }

        // 开始判断---未选中时处理
        if (kemu == "科目") {
            kemu = "";
        }

        // 准备发送查询指令
        var cmdString = $.get_resquery_cmd(xueli, xuenian, kemu, fliter);
        // alert(cmdString);
        // 提取用户名
        $.get(cmdString,
            function (data) {
                // 检查查询状态
                var ErrorId = data.ErrorId;
                var Result = data.Result;
                var Datas = Result;
                if (ErrorId == 200) {
                    if (Datas.length <= 0 || Datas.length < currentPageSize) {
                        isResLoadFinishLoad = true;
                    }

                    for (i = 0; i < Datas.length; i++) {
                        var oneCode1 = Datas[i];

                        var abcTemp = {};
                        abcTemp["ResGrade"] = oneCode1.ResGrade;
                        abcTemp["ResLevel"] = oneCode1.ResLevel;
                        abcTemp["ResClass"] = oneCode1.ResClass;
                        abcTemp["ResInfo"] = oneCode1.ResInfo;
                        abcTemp["Name"] = oneCode1.Name;
                        abcTemp["Price"] = oneCode1.Price;
                        abcTemp["ViewCount"] = oneCode1.ViewCount;
                        abcTemp["BuyCount"] = oneCode1.BuyCount;
                        abcTemp["ResImage"] = oneCode1.ResImage;
                        abcTemp["Code"] = oneCode1.Code;

                        var oneT = $("#res_item_div").html();

                        $("#res_item_div").html(oneT + $.format(oneResourceTmpl, abcTemp));
                        // $("#res_item_div").html(oneT + oneResourceTmpl);
                    }
                    // var oneT = $("#res_item_div").html();
                    //
                    // $("#res_item_div").html(oneT + bottomSep);
                    queryResLoadLock = false;
                }

            },
            "json");//这里返回的类型有：json,html,xml,text
    },
    beginSearch: function () {
        isResLoadFinishLoad = false;
        currentResLoadPageIndex = 0;
        currentResLoadPageSize = 10;
        queryResLoadLock = false;
        $("#res_item_div").html("");
        $.searchResource();

    },
});
