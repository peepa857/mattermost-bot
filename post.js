const request = require("request");
var headers = {
  "Content-Type": "application/json",
  Authorization: "Bearer ecp785yaab8u5rtxsxuzdokwae",
};
var dataString =
  '{"channel_id":"snxudatqktnk5k74o5g6t3fbuo", "message":"This is a message from a bot", "props":{"attachments": [{"pretext": "Look some text","text": "This is text"}]}}';
var options = {
  url: "http://localhost:8065/api/v4/posts",
  method: "POST",
  headers: headers,
  body: dataString,
};
function callback(error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body);
  }
}
request(options, callback);
