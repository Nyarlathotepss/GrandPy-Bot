
$("button#btn").click(function(){
$.ajax({
    url: "/home/",
    type: "POST",
    data: {"question": $("input#question").val()},
    success: function(resp){
        $("div#response").append(resp.data)
    }})
 })


function initMap(lat, lon) {
    var place = {lat:lat, lng:lon };
    var map = new google.maps.Map(
    document.getElementById('content_gmap'), {zoom: 4, center: place});
    var marker = new google.maps.Marker({position: place, map: map});
}

function displayDialog(dialog_to_show) {
    if dialog_to_show.forEach /2 == 0:
        <div class="container">
        <img src="/static/invite.jpg" alt="Avatar">
        <p>{{value}}</p>
        </div>
    else:
        <div class="container darker">
        <img src="/static/grandpy-bot.jpg" alt="Avatar" class="right">
        <p>{{value}}</p>
        </div>
}