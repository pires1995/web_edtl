setInterval(function(){
    $.get('/notifications/approver/app/body/',function(data) {
        document.getElementById("notifyapprovedbody").innerHTML = data.value1;
    });
}, 3000);