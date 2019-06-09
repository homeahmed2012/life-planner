var fs = require('fs');
var http = require("http");
var serveStatic = require('serve-static');

http.createServer(function (request, response) {


   var serve = serveStatic('.', {'index': ['index.html', 'index.htm']});
   // Send the HTTP header
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/html'});

   var file = fs.createReadStream('templates/index.html');
   file.pipe(response);
}).listen(8081);

// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');

