$.extend({
    openChat: function (codeName) {
        // alert(codeName);
        window.parent.location = "/msg_chat.html?Command=Open_ChatRoom&code=" + codeName;
    },
});