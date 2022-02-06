setInterval(function(){
    $.get('/notifications/approver/body/',function(data) {
        document.getElementById("notifapprbody1").innerHTML = data.value1;
    });
}, 3000);