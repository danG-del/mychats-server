# app.py — El núcleo del backend WebSocket
# 🧠 Narrador: "El servidor despierta. Las líneas están abiertas."


import asyncio
import websockets
import os

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print("[CONNECTED] Nuevo cliente")
    try:
        async for message in websocket:
            print(f"[RECEIVED] {message}")
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        connected_clients.remove(websocket)
        print("[DISCONNECTED] Cliente desconectado")

async def main():
    port = int(os.environ.get("PORT", 8001))  # Render asigna el puerto en PORT
    print(f"[STARTING] Servidor WebSocket en puerto {port}")
    async with websockets.serve(handler, "0.0.0.0", port):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
