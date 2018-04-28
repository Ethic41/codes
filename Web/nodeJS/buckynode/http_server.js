var http = require("http");

function onRequest(request, response){
  console.log("A user made a Requst"+request.url);
  response.writeHead(200, {"Context-Type":"text/plain"});
  response.write("Welcome To Our Server...");
  response.end();
}

http.createServer(onRequest).listen(4134);
console.log("Server Started on port: 4134...");
