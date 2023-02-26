import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpserver
import ssl


class PingPongWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print(f"Received message: {message}")
        self.write_message("pong")

    def on_close(self):
        print("WebSocket closed")


def make_app():
    return tornado.web.Application([
        (r"/", PingPongWebSocket),
    ])


if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app, ssl_options={
        "certfile": "server.crt",
        "keyfile": "server.key",
    })
    server.listen(8888)
    print("Server started")
    tornado.ioloop.IOLoop.current().start()
