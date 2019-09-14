
$(document).ready(function(){
    $("#myForm").submit(function(event){
        event.preventDefault();
        var form = $("#question").val();
        $.ajax({
            url: "/home/",
            type: "POST",
            contentType : "application/json; charset=UTF-8",
            dataType : "json",
            data: JSON.stringify(form),
            success: function(resp) {
                console.log(resp);
                displayDialog(resp.dialog_to_show);
                var latitude = parseInt(resp.latitude);
                var longitude = parseInt(resp.longitude);
                initMap(latitude, longitude);
            }
        })
    })
})

function initMap(latitude, longitude) {
    var place = {lat:latitude, lng:longitude};
    var map = new google.maps.Map(
    document.getElementById('content_gmap'), {zoom: 4, center: place});
    var marker = new google.maps.Marker({position: place, map: map});
}


function displayDialog(list) {
    for (var i = 0; i < list.length; i++) {
        if (i /2 == 0) {
            var newDiv = document.createElement('div');
            newDiv.setAttribute('class', 'container');
            var avatar = document.createElement('img');
            avatar.setAttribute('src', '/static/invite.jpg', 'alt',  'Avatar');
            newDiv.appendChild(avatar);
            var para = document.createElement('p');
            para.textContent = list[i];
            newDiv.appendChild(para);
            var currentDiv = document.getElementById('content_dialog');
            currentDiv.appendChild(newDiv)
            }
        else {
            var newDiv1 = document.createElement('div');
            newDiv1.setAttribute('class', 'container dark');
            var avatar1 = document.createElement('img');
            avatar1.setAttribute('src', '/static/grandpy-bot.jpg', 'alt', 'Avatar', 'class', 'right');
            newDiv1.appendChild(avatar1);
            var para1 = document.createElement('p');
            para1.textContent = list[(i++)];
            newDiv1.appendChild(para1)
            var currentDiv1 = document.getElementById('content_dialog');
            currentDiv1.appendChild(newDiv1)
            }
     }
}
