# import os
# Path=os.getcwd()
# current_directory=str(os.getenv())



# print(current_directory+r'models\n_version_1_30.pt')
import os

current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'face_recognition_system', 'models', 'n_version_1_30.pt')

print(file_path)

