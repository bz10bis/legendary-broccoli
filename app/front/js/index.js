// function loadJSON(callback) {
//
//     var xobj = new XMLHttpRequest();
//     xobj.overrideMimeType("application/json");
//     xobj.open('GET', '../../dataset/departements.geojson', true); // Replace 'my_data' with the path to your file
//     xobj.onreadystatechange = function () {
//         if (xobj.readyState === 4 && xobj.status === "200") {
//             // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
//             callback(xobj.responseText);
//         }
//     };
//     xobj.send(null);
// }
//
// $(document).ready(function () {
//     var map = L.map('map', {
//         center: ['14.6276432', '-60.98892379999995'],
//         zoom: 11
//     });
//
//     loadJSON(function(response) {
//         // Parse JSON string into object
//         var datas = JSON.parse(response);
//         console.log(datas);
//         L.geoJSON(datas).addTo(map);
//     });
//
//
//     // L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
//     //     attribution: 'Données de la carte &copy; <a href="http://www.openstreetmap.org/#map=5/51.500/-0.100">Open Street Map</a>',
//     //     maxZoom: 18
//     // }).addTo(map);
// });