import cv2
import face_recognition
import os
import pickle

def register_new_member(name, age, id_number):
    # Create a folder for the new member
    member_folder = f"members/{name}"
    os.makedirs(member_folder, exist_ok=True)
    
    # Save the member details
    with open(os.path.join(member_folder, "details.txt"), "w") as f:
        f.write(f"Name: {name}\nAge: {age}\nID: {id_number}\n")
    
    # Capture the face
    cap = cv2.VideoCapture(0)
    print("Capturing face... Press 's' to capture")
    
    while True:
        ret, frame = cap.read()
        cv2.imshow("Capture Face", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            face_locations = face_recognition.face_locations(frame)
            
            if face_locations:
                face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
                
                # Save the face encoding
                with open(os.path.join(member_folder, "face_encoding.pkl"), "wb") as f:
                    pickle.dump(face_encoding, f)
                
                print("Face captured and details saved.")
                break
            else:
                print("No face detected. Try again.")
    
    cap.release()
    cv2.destroyAllWindows()

# Input from users
name = input("Enter name: ")
age = input("Enter age: ")
id_number = input("Enter ID number: ")
register_new_member(name, age, id_number)
