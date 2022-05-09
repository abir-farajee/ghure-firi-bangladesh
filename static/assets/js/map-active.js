var map;function initialize_map(){if($('.map').length){var myLatLng=new google.maps.LatLng(40.716269,-74.004566);var mapOptions={zoom:17,center:myLatLng,scrollwheel:false,zoomControl:false,scaleControl:false,mapTypeControl:false,streetViewControl:false};map=new google.maps.Map(document.getElementById('map'),mapOptions);}else{return false;}
var marker1LatLng=new google.maps.LatLng(40.715756,-74.005339);Loc1=new RichMarker({position:marker1LatLng,map:map,draggable:false,flat:true,content:'<div class="map-cb-wrap" id="Loc1">'+
'<div class="locmark"><div class="maptb"><img src="assets/images/map-marker.png" alt="icon"></div></div>'+
'<div class="cmb-wrap">'+
'<img src="assets/images/listing/1.jpg" alt="bg" class="img-responsive">'+
'<div class="loc-thumb">Cafe</div>'+
'<div class="content">'+
'<h3><a href="">Elevator Cafe & Commons</a></h3>'+
'<span>SE Main St, Pl</span>'+
'<div class="bottom-text"><ul class="ratting"><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li></ul><ul><li><strong>4.6</strong> (129 Reviews)</li></ul></div>'+
'</div> <!-- end .content -->'+
'</div> <!-- end .cmb-wrap -->'+
'</div>'});google.maps.event.addListener(Loc1,'click',function(){$('.map-cb-wrap').removeClass('open');$('#Loc1').toggleClass('open');});var markerposition1=new google.maps.LatLng(40.716715,-74.003352);Loc2=new RichMarker({position:markerposition1,map:map,draggable:false,flat:true,content:'<div class="map-cb-wrap" id="Loc2">'+
'<div class="locmark"><div class="maptb"><img src="assets/images/map-marker.png" alt="icon"></div></div>'+
'<div class="cmb-wrap">'+
'<img src="assets/images/listing/1.jpg" alt="bg" class="img-responsive">'+
'<div class="loc-thumb">Cafe</div>'+
'<div class="content">'+
'<h3><a href="">Elevator Cafe & Commons</a></h3>'+
'<span>SE Main St, Pl</span>'+
'<div class="bottom-text"><ul class="ratting"><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li></ul><ul><li><strong>4.6</strong> (129 Reviews)</li></ul></div>'+
'</div> <!-- end .content -->'+
'</div> <!-- end .cmb-wrap -->'+
'</div>'});google.maps.event.addListener(Loc2,'click',function(){$('.map-cb-wrap').removeClass('open');$('#Loc2').toggleClass('open');});var markerposition2=new google.maps.LatLng(40.716622,-74.007976);Loc3=new RichMarker({position:markerposition2,map:map,draggable:false,flat:true,content:'<div class="map-cb-wrap" id="Loc3">'+
'<div class="locmark"><div class="maptb"><img src="assets/images/map-marker.png" alt="icon"></div></div>'+
'<div class="cmb-wrap">'+
'<img src="assets/images/listing/1.jpg" alt="bg" class="img-responsive">'+
'<div class="loc-thumb">Cafe</div>'+
'<div class="content">'+
'<h3><a href="">Elevator Cafe & Commons</a></h3>'+
'<span>SE Main St, Pl</span>'+
'<div class="bottom-text"><ul class="ratting"><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li></ul><ul><li><strong>4.6</strong> (129 Reviews)</li></ul></div>'+
'</div> <!-- end .content -->'+
'</div> <!-- end .cmb-wrap -->'+
'</div>'});google.maps.event.addListener(Loc3,'click',function(){$('.map-cb-wrap').removeClass('open');$('#Loc3').toggleClass('open');});var markerposition3=new google.maps.LatLng(40.714898,-74.004500);Loc4=new RichMarker({position:markerposition3,map:map,draggable:false,flat:true,content:'<div class="map-cb-wrap" id="Loc4">'+
'<div class="locmark"><div class="maptb"><img src="assets/images/map-marker.png" alt="icon"></div></div>'+
'<div class="cmb-wrap">'+
'<img src="assets/images/listing/1.jpg" alt="bg" class="img-responsive">'+
'<div class="loc-thumb">Cafe</div>'+
'<div class="content">'+
'<h3><a href="">Elevator Cafe & Commons</a></h3>'+
'<span>SE Main St, Pl</span>'+
'<div class="bottom-text"><ul class="ratting"><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li></ul><ul><li><strong>4.6</strong> (129 Reviews)</li></ul></div>'+
'</div> <!-- end .content -->'+
'</div> <!-- end .cmb-wrap -->'+
'</div>'});google.maps.event.addListener(Loc4,'click',function(){$('.map-cb-wrap').removeClass('open');$('#Loc4').toggleClass('open');});return false;}
google.maps.event.addDomListener(window,'load',initialize_map);