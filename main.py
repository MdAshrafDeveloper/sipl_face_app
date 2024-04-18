# from flask import Flask, render_template
# from flask_socketio import SocketIO
# import json

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('message')
# def handle_message(message):
#     # print('Received message: ' + message)
#     try:
#          socketio.emit("message", json.dumps("Hi user"))
          
#     except Exception as e:
#         print(f"WebSocket Error: {str(e)}")
        




# @app.route('/testing',methods=['GET'])
# def testing():
#     try:

#                 return json.dumps("OK")
#     except Exception as e:    
#         return json.dumps("")





# if __name__ == '__main__':
#     # socketio.run(app)
#     socketio.run(app,debug=True,host="61.247.233.47")




import asyncio
import websockets
import json
# import tkinter as tk
import cv2
import base64
import numpy as np
from face_recognition_system import register


from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    # print('Received message: ' + message)
    try:
        print('Received message: ' , type(message))
        response =  recognize_face(message)
        print("done")
        socketio.emit("message", json.dumps(response))

    except Exception as e:
        print(f"WebSocket Error: {str(e)}")
        





    # socketio.emit('message', "hello flutter")  







# async def websocket_handler(websocket, path):
#     try:
#         async for message in websocket:
#             # print(websocket)
#             if message=="stop":
#                 await websocket.send(json.dumps( {"status": "False", "message": "stop"}))
#             else:
#                  response = await recognize_face(message)
#                  await websocket.send(json.dumps(response))
#     except Exception as e:
#         print(f"WebSocket Error: {str(e)}")
        

        
        
        
        
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

def recognize_face(message):
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
    # socketio.run(app)
    socketio.run(app, debug=True, host='0.0.0.0')







