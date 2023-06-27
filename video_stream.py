# /usr/bin/python3

import asyncio
import cv2
import websockets
import base64


async def stream_video(websocket, path):
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break

        _, buffer = cv2.imencode(".jpg", frame)
        print(buffer)  # this will print a list [255 216 255 .... (x) 255 217]
        frame_bytes = base64.b64encode(buffer.tobytes()).decode(
            "utf-8"
        )  # Convert bytes to string
        await websocket.send(frame_bytes)
    capture.release()


def start():
    try:
        start_server = websockets.serve(stream_video, "localhost", 9500)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    except Exception as e:
        print(f"An error has occured {e}")


start()

"""
start_server = websockets.serve(stream_video, "localhost", 9500)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
"""
