# app.py — El núcleo del backend WebSocket
# 🧠 Narrador: "El servidor despierta. Las líneas están abiertas."


# app.py — WebSocket dentro de FastAPI
# 🧠 Narrador: "El servidor despierta, ahora con capa HTTP."

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
import os

app = FastAPI()
connected_clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    print("[CONNECTED] Nuevo cliente")
    try:
        while True:
            message = await websocket.receive_text()
            print(f"[RECEIVED] {message}")
            for client in connected_clients:
                if client != websocket:
                    await client.send_text(message)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("[DISCONNECTED] Cliente desconectado")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"[STARTING] Servidor FastAPI en puerto {port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port)
