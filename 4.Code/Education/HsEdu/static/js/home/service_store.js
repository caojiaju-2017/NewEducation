window.onload=function()
{
    var width = $(document).width();
    var leftImageWd = $("#left_img").width();
    var rightImageWd = $("#right_img").width();

    var sepWd = (width - leftImageWd - rightImageWd) / 3;

    $("#left_img").css('marginLeft', sepWd);
    $("#right_img").css('marginRight', sepWd);

    var leftImagHd = $("#left_img").height();
    var rightImagHd = $("#right_img").height();

    if (leftImagHd > rightImagHd) {
        $("#right_img").height(leftImagHd);
    }
    else {
        $("#left_img").height(rightImagHd);
    }
};

$(document).ready(function() {


});
$.extend({
    openServiceDetail: function (codeName) {
        window.parent.location = "/srv_detail.html?Command=Open_Service&code=" + codeName;
    },
});