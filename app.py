import asyncio
import websockets
import json
# import tkinter as tk
import cv2
import base64
import numpy as np
from face_recognition_system import register

# Function to handle WebSocket communication
async def websocket_handler(websocket, path):
    try:
        async for message in websocket:
            # print(websocket)
            if message=="stop":
                await websocket.send(json.dumps( {"status": "False", "message": "stop"}))
            else:
                 response = await recognize_face(message)
                 await websocket.send(json.dumps(response))
    except Exception as e:
        print(f"WebSocket Error: {str(e)}")

# Function to recognize a face
def bs64_to_frame(bs64):
        if bs64:
            decoded_bytes = base64.b64decode(bs64)
            decoded_image = np.frombuffer(decoded_bytes, dtype=np.uint8)
            decoded_image = cv2.imdecode(decoded_image, flags=cv2.IMREAD_COLOR)
            return decoded_image
        else:
            return 'Unable to process image'





def bytes_to_frame(byte_array):
    # Convert byte array to numpy array
    nparr = np.frombuffer(byte_array, np.uint8)
    
    # Decode numpy array into image
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    return frame

async def recv_and_display(frame):
    # while True:
       
    #     # image = frame.to_ndarray()
    cv2.imshow("Video Stream", frame)
    #     # print(frame)
    #     # print(register.getFace(image))
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pass


async def recognize_face(message):
    try:
        # Perform face recognition here
        # print(message)
        print("type(message)",type(message))
        by= bytes_to_frame(message)
        # print(register.getFace(by))

       
        # print(by)
        # base64_image_data = base64.b64encode(message)
        # bs64=base64_image_data.decode()
        # frame=bs64_to_frame(bs64)
        
        
        # asyncio.ensure_future(recv_and_display(by))
        data =register.getFace(by)
        print("data",type(data))
        # await send_message("testing meaasge")
        # For demonstration purposes, return a response indicating the recognition result
        
        return data
    except Exception as e:
        return {"status": False, "message": str(e)}




if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(websockets.serve(websocket_handler, "0.0.0.0", 8081))
    loop.run_forever()
    # start_server = websockets.serve(websocket_handler,"61.247.233.47", 8081)
    # asyncio.get_event_loop().run_until_complete(start_server)
   





