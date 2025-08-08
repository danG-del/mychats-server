# app.py — El núcleo del backend WebSocket
# 🧠 Narrador: "El servidor despierta. Las líneas están abiertas."

import asyncio
import websockets

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print("[CONNECTED] Nuevo cliente")
    try:
        async for message in websocket:
            print(f"[RECEIVED] {message}")
            # 🧠 Narrador: "Replicamos el mensaje. Todos lo ven."
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        connected_clients.remove(websocket)
        print("[DISCONNECTED] Cliente desconectado")

async def main():
    print("[STARTING] Servidor WebSocket en puerto 8001")
    async with websockets.serve(handler, "0.0.0.0", 8001):
        await asyncio.Future()  # Mantiene el servidor corriendo

if __name__ == "__main__":
    asyncio.run(main())
