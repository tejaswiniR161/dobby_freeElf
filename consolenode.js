var http = require('http');
var url = require('url');
var fs = require('fs');

http.createServer(function (req, res) {
  var q = url.parse(req.url, true);
  //var filename = "." + q.pathname;
  var filename = __dirname+q.pathname;
  filename=filename.substring(0,filename.length-1);
  console.log(req.url);
  console.log(filename);
  fs.readFile(filename, function(err, data) {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      res.end("404 Not Found");
    }  
      console.log("hit");
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write("<textarea style='width:100%;height:100%;background-color: #ece2e2;' readonly>"+"Output : \n"+data+"</textarea>");
    res.end();
  });
  
}).listen(8900);