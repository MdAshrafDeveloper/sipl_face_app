from flask import  Flask, jsonify,render_template, request
from flask_restful import reqparse
import json
from face_recognition_system.register import*

app = Flask(__name__)


parser = reqparse.RequestParser()
parser.add_argument('imageBase64', type=str)
parser.add_argument('imageBase642', type=str)
parser.add_argument('employeeName', type=str)
parser.add_argument('employeeCode', type=str)
parser.add_argument('department', type=str)
parser.add_argument('companyCode', type=str)

@app.route('/FaceRegistration',methods=['POST'])
def FaceRegistration():
    try:
        request.get_json(force=True)
        args = parser.parse_args()
        # file_path='content/images/APIImage/1.jpg'
       
        image_data =args['imageBase64']
        imageBase642=args['imageBase642']
        employee_name=args['employeeName']
        employee_code=args['employeeCode']
        department=args['department']
        companyCode=args['companyCode']

        # employee_face_image='content/images/newImages/'+employee_code+'.PNG'
        try:
                # with open(employee_face_image, "wb") as file:
                #     file.write(image_data)
                data=  register(face_base64_1=image_data,face_base64_2=imageBase642,id=employee_code,
                                name=employee_name,dept=department,companyCode=companyCode
                                )
                return data
        except Exception as e:
                return json.dumps("")
    except Exception as e:    
        return json.dumps("")
    




@app.route('/GetEmployeeDetails',methods=['POST'])
def GetEmployeeDetails():
    try:
        request.get_json(force=True)
        args = parser.parse_args()
        emp_id =args['employeeCode']
        companyCode=args['companyCode']
        try:
                data=  get_Details(emp_id.upper(),companyCode)
                return data
        except Exception as e:
                return json.dumps("")
    except Exception as e:    
        return json.dumps("")
    




@app.route('/UpdateEmplyee',methods=['POST'])
def UpdateEmplyee():
    try:
        request.get_json(force=True)
        args = parser.parse_args()
        # file_path='content/images/APIImage/1.jpg'
       
        face_base64_1 =args['imageBase64']
        face_base64_2=args['imageBase642']
        name=args['employeeName']
        emp_id=args['employeeCode']
        dept=args['department']
        companyCode=args['companyCode']
        try:

              data = updateEmployee(emp_id=emp_id,
                                    name=name,
                                    dept=dept,
                                    face_base64_1=face_base64_1,
                                    face_base64_2=face_base64_2,
                                    companyCode=companyCode
                                    )   
              return data
        except Exception as e:
                return json.dumps("")
    except Exception as e:    
        return json.dumps("")



if __name__ == '__main__':
    # socketio.run(app)
    # socketio.run(app, debug=True, host="61.247.233.47")
    # socketio.run(app)
    # socketio.run(app,debug=True,host="61.247.233.47")
 
    app.run() 