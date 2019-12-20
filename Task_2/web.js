var http = require('http');

var fs = require('fs');



function handle_incoming_request (req, res) {

    console.log("INCOMING REQUEST: " + req.method + " " + req.url);

    load_sensor_data(function(err, readings){

    if (err) { 

       console.log("Couldn't read file");

    }

    console.log(readings);
    var dataArray = readings.split(',');
    console.log(dataArray);


    res.writeHead(200, { "Content-Type" : "application/json" });

    res.end(JSON.stringify({temperature : dataArray[0], humidity : dataArray[1], windspeed : dataArray[2], time : dataArray[3], location : dataArray[4]}));

   });

}



function load_sensor_data(callback) {

   fs.readFile(

   "sensorlog.txt",'utf8',

   function (err, readings) {

   if (err) {

   callback(err);

return;



}

callback(null, readings);

}

);

}

var s = http.createServer(handle_incoming_request);


s.listen(8080);