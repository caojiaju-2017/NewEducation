$.extend({
    favoruteResource: function (codeName) {
        alert("s");
    },

    contactNow: function (codeName) {

    },

    buyResource: function (codeName) {

    },

    remarkResource: function (codeName) {
        window.location = "/view_remark.html?Command=View_Remark&code=" + codeName;
    },
});