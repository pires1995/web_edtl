setInterval(function(){
    $.get('/notifications/approver/app/badge/',function(data) {
        document.getElementById("notifapprbadge").innerHTML = data.value;
    });
}, 3000);