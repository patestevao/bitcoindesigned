/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');


$(document).ready(function(){

    toggleDonate();

    $(window).scroll(function(){
        toggleDonate();
    });
    $('#donate-copy-button').click(function(){
        var copyText = $("#donate-address");
        $(copyText).focus();
        $(copyText).select();
        document.execCommand("copy");
        copyFeedback();
    });

    $("#donate-qr-code-button").click(function() {
        $('#qr-code-container').toggle(200);
    });

    $("#qr-code-close-button").click(function() {
        $("#qr-code-container").hide(200);
    });
});

function copyFeedback() {
    $(".donate-feedback").show(200).delay(800).hide(200);
}

function toggleDonate() {
    var windowScroll = $(window).scrollTop();
    var targetPosition = $(".tagline").offset().top;
    if( windowScroll >= targetPosition) {
        $("#donate-container").show(250);
    } else {
        $("#donate-container").hide(250);
    }
}
// function copyAddress() {
//     var copyText = document.getElementById("donate-address");
//     copyText.select();
//     document.execCommand("copy");
//     alert("Copied!");
// }

// document.getElementById("donate-copy-button").onclick = copyAddress;