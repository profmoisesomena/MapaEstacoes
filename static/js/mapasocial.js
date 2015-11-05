var map;
// Inicializando o mapa do openstreetmap no index
function initmap(pontos)
{
  alert("oi");
  init();

}

//Configuracoes iniciais do mapa
function init()
{
  map = new L.Map('map');

  // create the tile layer with correct attribution
  var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
  var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 12});
  map.setView(new L.LatLng(-20.297618, -40.295777),12);
  map.addLayer(osm);

  L.marker([-20.297618, -40.295777]).addTo(map);
  L.marker([-20.3477821, -40.2949528]).addTo(map);
}
