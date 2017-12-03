function DropDown(el)
{
    // alert("a");
    this.dd = el;
    this.initEvents();
};
DropDown.prototype = {
    initEvents : function() {
        // alert("b");
        var obj = this;

        obj.dd.on('click', function(event){
            // alert("c");
            $(this).toggleClass('active');
            event.stopPropagation();
        });
    }
};
$(function() {
    var dd = new DropDown( $('#dd') );
    // alert("d");
    $(document).click(function() {
        // alert("e");
        // all dropdowns
        $('.wrapper-dropdown-2').removeClass('active');
    });
});
