
//$(function () {
//    $('.jsdemo-notification-button button').on('click', function () {
//        var placementFrom = $(this).data('placement-from');
//        var placementAlign = $(this).data('placement-align');
//        var animateEnter = $(this).data('animate-enter');
//        var animateExit = $(this).data('animate-exit');
//        var colorName = $(this).data('color-name');
//        showNotification(colorName, null, placementFrom, placementAlign, animateEnter, animateExit);
//    });
//});

function showNotification(colorName, text) {

    if (colorName === undefined || colorName === 'undefined' || colorName === null || colorName === '') { colorName = 'bg-info'; }
    if (text === undefined || text === 'undefined' || text === null || text === '') { return; }
    var allowDismiss = false;

    $.notify({
        message: text,
    },
        {
            element: 'body',
            position: null,
            type: colorName,
            allow_dismiss: allowDismiss,
            newest_on_top: true,
            showProgressbar: false,
            timer: 1000,
             placement: { from: "top", align: "right"},
            //animate: { enter: 'animated fadeInDown', exit: 'animated fadeOutUp' },
            animate: { enter: 'animated fadeInRight', exit: 'animated fadeOutRight' },
            offset: 20,
            spacing: 10,
            z_index: 1031,
            delay: 5000,
            timer: 1000,
            url_target: '_blank',
            mouse_over: null,
            onShow: null,
            onShown: null,
            onClose: null,
            onClosed: null,
            icon_type: 'class',
            template:
            '<div data-notify="container" class="bootstrap-notify-container alert alert-dismissible {0} ' + (allowDismiss ? "p-r-35" : "") + '" role="alert">' +
            '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
            '<span data-notify="icon"></span> ' +
            '<span data-notify="title">{1}</span> ' +
            '<span data-notify="message">{2}</span>' +
            '<div class="progress" data-notify="progressbar">' +
            '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
            '</div>' +
            '<a href="{3}" target="{4}" data-notify="url"></a>' +
            '</div>'
        });
}