function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: {lat: 0, lng: 0 }
  });


  map.addListener('click', function(e) {
    // Check if the click point has an address and add a markup in the map
    // also save in the database
    validateSaveAndMark(e.latLng, map)
  });
}


function placeMarkerAndPanTo(latLng, map) {
  var marker = new google.maps.Marker({
    position: latLng,
    map: map
  });
  map.panTo(latLng);
}


function validateSaveAndMark(latLng, map) {
  var geoCode = String(latLng).replace(/[() ]/g,'').split(","),
  lat = geoCode[0],
  lng = geoCode[1],
  data = {'latitude': lat, 'longitude': lng}
  url = document.querySelector('#api_data').dataset.url;
  $.post(url, data)
    .done(function(response) {
      var address = JSON.parse(response).address,
        html = '<li>' + address + '</li>';
      // add pointer in the map
      placeMarkerAndPanTo(latLng, map)
      // add the address in the underneath the map
      $('#content #address').append(html)
    })

}