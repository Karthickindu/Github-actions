
const http = require("http");
const fs = require("fs");
const path = require("path");

const port = process.env.PORT || 8080;

const server = http.createServer((req, res) => {
    if (req.url === "/" || req.url === "/index.html") {
        fs.readFile(path.join(__dirname, "index.html"), (err, data) => {
            if (err) {
                res.writeHead(500);
                return res.end("Server Error");
            }

            res.writeHead(200, {
                "Content-Type": "text/html; charset=utf-8"
            });
            res.end(data);
        });
    } else {
        res.writeHead(404);
        res.end("Page Not Found");
    }
});

server.listen(port, "0.0.0.0", () => {
    console.log(`ShopEasy running on port ${port}`);
});
