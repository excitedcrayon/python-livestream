# python-livestream

A simple snippet which utilizes websockets to deliver captured video data and send it via the ws:// protocol for consumption across the network

## What you need

- This code was compiled using Python version 3.10.0
- Platform : Windows 10
- IDE : Visual Studio Code

## Installation

- Python

```
    // for cv2 module
    pip install opencv-python

    // for websockets module
    pip install websockets
```

## Python Tech Stack (video_stream.py)

- Modules uses from the python script are;

* asyncio - creates an event loop that will run forever until the program is stopped or cancelled
* cv2 - opencv module which captures and records video from the camera device
* websockets - opens a connection for the ws:// protocol
* base64 - the video is converted to single frames and then converted to a string for data:image/jpeg;base64,xxxx format

## JavaScript Tech Stack (index.html)

- WebSockets API built into the browser
- We dynamically create an image and use requestAnimationFrame to redraw the images (animation)

## Demo

- The demo.mp4 video file will show the outcome of this research
