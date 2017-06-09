(function($){
  var client_id ='xcfyt56fd';
  var ws = new  WebSocket('ws://149.202.59.217:9001');
  this.send = function (message, callback) {
      this.waitForConnection(function () {
          ws.send(JSON.stringify(message));
          if (typeof callback !== 'undefined') {
            callback();
          }
      }, 1000);
  };

  this.waitForConnection = function (callback, interval) {
      if (ws.readyState === 1) {
          callback();
      } else {
          var that = this;
          setTimeout(function () {
              that.waitForConnection(callback, interval);
          }, interval);
      }
  };
  this.send({
    event: 'join_channel',
    data: {
      client_id: client_id
    }
  });
  ws.onmessage = function(event){
    data = JSON.parse(event.data)
    $(document).trigger("rpi:message", [data.val])
  }
})(jQuery)
