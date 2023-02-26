import websocket
import ssl


def main():
    ws = websocket.create_connection("wss://localhost:8888", sslopt={
        "cert_reqs": ssl.CERT_NONE
    })
    ws.send("ping")
    pong = ws.recv()
    print(pong)
    ws.close()


if __name__ == "__main__":
    main()
