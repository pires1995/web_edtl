setInterval(function(){
    $.get('/notifications/approver/finance/body/',function(data) {
        document.getElementById("notifyfinancebody").innerHTML = data.value1;
    });
}, 3000);