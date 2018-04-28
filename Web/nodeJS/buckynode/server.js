var http = require("http");

function onRequest(request, response){
  console.log("A user requested "+request.url);
  response.writeHead(200, {"Content-Type":"text/plain"});
  response.write("You have successfully connected....");
  response.end();
}

var server = http.createServer(onRequest).listen(4134);
console.log("Server Started on port: "+server.address().port);
