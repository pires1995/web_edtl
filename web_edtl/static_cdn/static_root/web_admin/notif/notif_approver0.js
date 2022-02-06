setInterval(function(){
    $.get('/notifications/approver/badge/',function(data) {
        document.getElementById("notifapprbadge").innerHTML = data.value;
    });
}, 3000);