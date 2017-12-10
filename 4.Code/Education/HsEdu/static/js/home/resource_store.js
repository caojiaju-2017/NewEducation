$.extend({
    openResourceDetail: function (codeName) {
        window.parent.location = "/res_detail.html?Command=Open_Resource&code=" + codeName;
    },
});