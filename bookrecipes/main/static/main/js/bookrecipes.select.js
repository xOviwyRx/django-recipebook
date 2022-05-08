$(document).ready(function () {
    $('.js-select').select2({
        placeholder: '...',
        allowClear: true,
        width: 'resolve'
    }).change(function(){
        $('.js-form').submit();
    });
});