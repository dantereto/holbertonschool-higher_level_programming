window.addEventListener('DOMContentLoaded', function () {
    $('INPUT#language_code').keypress(function (event) {
        const key = event.which;
        if (key === 13) {
          $('input#btn_translate').click();
          return false;
        }
});
    
    $('input#btn_translate').click(function () {
        const lan = $('input#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
            $('div#hello').text(data.hello);
        });
    });
});
