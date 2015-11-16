var map;
// Inicializando o mapa do openstreetmap no index
function initmap()
{
  map = new L.Map('map');

  // create the tile layer with correct attribution
  var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 12});
  map.setView(new L.LatLng(-20.297618, -40.295777),12);
  map.addLayer(osm);
  getData();
}

//Configuracoes iniciais do mapa
function getData()
{
  var latitude;
  var longitude;
  var nome;

  $.ajax({
		type: "get",
		url: "http://localhost:5000/pontos",
		cache: false,
	  Accept : "application/json",
    contentType: "application/json",
		success: function(response){

			$.each(JSON.parse(response),function(idx, obj){

            $.each(JSON.parse(obj), function(key, value){
              if (key == "latitude")
                latitude = value;
              else if (key=="longitude") {

                 longitude = value;
              }
              else{
                L.marker([latitude, longitude]).addTo(map).bindPopup("<br> <b>Cidade: </b>"+value+"</br>");
              }
		        });
		    });

		},
		error: function(response, status, error){
        alert("Que coisa feia ... deu erro");
		}
	});


  //L.marker([-20.3477821, -40.2949528]).addTo(map);
}
