$(function () {
    $.post('/officials', {
        data: {
            address: '16300 lake ridge dr maple grove mn 55311'
        }
    }).done(function (res) {
        console.log(res);
    });
});