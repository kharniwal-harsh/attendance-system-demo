import face_recognition
import os
import pickle

def register_face(image_path, roll_number):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        raise Exception("No face detected in the image.")
    elif len(encodings) > 1:
        raise Exception("Multiple faces detected. Use a photo with only one face.")

    data = {
        "roll_number": roll_number,
        "encoding": encodings[0]
    }

    os.makedirs("encodings", exist_ok=True)
    with open(f'encodings/{roll_number}.pkl', 'wb') as f:
        pickle.dump(data, f)

def delete_face_encoding(roll_number):
    file_path = f'encodings/{roll_number}.pkl'
    if os.path.exists(file_path):
        os.remove(file_path)
