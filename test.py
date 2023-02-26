import unittest
import websocket
import threading
import time
import ssl


class TestWebSocketPingPong(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=start_server)
        cls.server_thread.start()
        # Wait for the server to start
        time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        stop_server()

    def test_ping_pong(self):
        ws = websocket.create_connection("wss://localhost:8888", sslopt={
            "cert_reqs": ssl.CERT_NONE
        })
        ws.send("ping")
        pong = ws.recv()
        self.assertEqual(pong, "pong")
        ws.close()


def start_server():
    from server import make_app
    import tornado.ioloop
    import tornado.httpserver
    server = tornado.httpserver.HTTPServer(make_app(), ssl_options={
        "certfile": "server.crt",
        "keyfile": "server.key",
    })
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()


def stop_server():
    import tornado.ioloop
    tornado.ioloop.IOLoop.current().stop()


if __name__ == '__main__':
    unittest.main()
