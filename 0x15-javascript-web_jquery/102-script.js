window.addEventListener('DOMContentLoaded', function () { 
    $('input#btn_translate').click(function () {
        const lan = $('input#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
            $('div#hello').text(data.hello);
        });
    });
});