// Create a WorldWindow for the canvas.
var wwd = new WorldWind.WorldWindow("canvasOne");

wwd.addLayer(new WorldWind.AtmosphereLayer())
wwd.addLayer(new WorldWind.BMNGOneImageLayer());
wwd.addLayer(new WorldWind.BMNGLandsatLayer());

let latitudeText = document.querySelector('.latitude');
let longitudeText = document.querySelector('.longitude');
let timeText = document.querySelector('.time');
let speedText = document.querySelector('.speed');
let altitudeText = document.querySelector('.altitude');


var num = 1;

function findISS() {

    fetch("https://api.wheretheiss.at/v1/satellites/25544")
    .then(response => response.json())
    .then(data => {
        lat = data.latitude.toFixed(2);
        long = data.longitude.toFixed(2);
        speed = data.velocity.toFixed(2);
        altitude = data.altitude.toFixed(2);
        console.log(lat, long);
        lat = parseFloat(lat)
        long = parseFloat(long)
        speed = parseFloat(speed)
        altitude = parseFloat(altitude)
        timestamp = new Date(data.timestamp * 1000).toUTCString();
        

        

    if (num == 1) {
        wwd.navigator.lookAtLocation.latitude = lat;
        wwd.navigator.lookAtLocation.longitude = long;
    }

    num = 10;

    var placemarkLayer = new WorldWind.RenderableLayer();
    wwd.addLayer(placemarkLayer);

    var placemarkAttributes = new WorldWind.PlacemarkAttributes(null);

    placemarkAttributes.imageOffset = new WorldWind.Offset(
        WorldWind.OFFSET_FRACTION, 0.3,
        WorldWind.OFFSET_FRACTION, 0.0);

    placemarkAttributes.labelAttributes.offset = new WorldWind.Offset(
        WorldWind.OFFSET_FRACTION, 0.5,
        WorldWind.OFFSET_FRACTION, 1.0);

    placemarkAttributes.imageSource = "./images/line1.png";

    var position = new WorldWind.Position(lat, long, 100.0);
    var placemark = new WorldWind.Placemark(position, false, placemarkAttributes);

   
    placemarkLayer.addRenderable(placemark);



    latitudeText.innerText = lat;
    longitudeText.innerText = long;
    timeText.innerText = timestamp;
    speedText.innerText = `${speed} km/hr`;
    altitudeText.innerText = `${altitude} km`;


    })

}


findISS()
setInterval(findISS, 4000);



// Add WMS imagery
var serviceAddress = "https://neo.sci.gsfc.nasa.gov/wms/wms?SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0";
var layerName = "MOD_LSTD_CLIM_M";

var createLayer = function (xmlDom) {
    var wms = new WorldWind.WmsCapabilities(xmlDom);
    var wmsLayerCapabilities = wms.getNamedLayer(layerName);
    var wmsConfig = WorldWind.WmsLayer.formLayerConfiguration(wmsLayerCapabilities);
    var wmsLayer = new WorldWind.WmsLayer(wmsConfig);
    wwd.addLayer(wmsLayer);
};

var logError = function (jqXhr, text, exception) {
    console.log("There was a failure retrieving the capabilities document: " +
        text +
    " exception: " + exception);
};

$.get(serviceAddress).done(createLayer).fail(logError);

