var map;
// Inicializando o mapa do openstreetmap no index
function initmap()
{
  map = new L.Map('map');

  // create the tile layer with correct attribution
  var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 12});
  map.setView(new L.LatLng(-20.297618, -40.295777),10);
  map.addLayer(osm);
  getData();
}

//Configuracoes iniciais do mapa
function getData()
{
  var latitude;
  var longitude;
  var nome;
  var chuva;

  $.ajax({
		type: "get",
		url: "http://localhost:5000/estacoes",
		cache: false,
	  Accept : "application/json",
    contentType: "application/json",
		success: function(response){

			$.each(JSON.parse(response),function(idx, obj){

            $.each(JSON.parse(obj), function(key, value){

              if (key == "chuva"){
                  chuva = value;
              }
              if (key == "latitude"){
                  latitude = value
              }

              if (key == "longitude"){
                longitude = value;
              }

              if (key == "municipio"){
                nome = value;
              }
              if (chuva!= null && latitude!=null & longitude!= null & nome!=null){
                  L.marker([latitude, longitude]).addTo(map).bindPopup("<b>Cidade: </b>"+value+" <br> <b>Chuva: </b>"+chuva+" mm");
                  chuva = latitude = longitude = nome = null;
              }
		        });
		    });

		},
		error: function(response, status, error){
        alert("Que coisa feia ... deu erro");
		}
	});

}
