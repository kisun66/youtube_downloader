$('#scan').on('click', () => {
    console.log('버튼눌림');
    $('.contents').css({
        "filter": "blur(5px)"
    });
    $('body').css({
        "background-color": "rgba(0, 0, 0, 0.7);"
    });
    $('.loading_').css({
        "display": "flex"
    })
    setTimeout(() => {
        $('#scan_form').submit();
    }, 1000);
});

$('#download').on('click', () => {
    $('#download_form').submit();
})