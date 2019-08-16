



function initMap() {
  var place = {lat:{{latitude}}, lng:{{longitude}} };
  var map = new google.maps.Map(
      document.getElementById('content_gmap'), {zoom: 4, center: place});
  var marker = new google.maps.Marker({position: place, map: map});
}


$("button#btn").click(function(){
$.ajax({
    url: "/home/",
    type: "POST",
    data: {"question": $("input#question").val()},
    success: function(resp){
        $("div#response").append(resp.data)
    }})
 })