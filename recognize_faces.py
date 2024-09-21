import cv2
import face_recognition
import os
import pickle

# Function to recognize and verify faces
def recognize_faces():
    known_faces = []
    known_details = []

    # Load all face encodings and details
    for member in os.listdir("members"):
        member_folder = os.path.join("members", member)
        if os.path.isdir(member_folder):
            encoding_path = os.path.join(member_folder, "face_encoding.pkl")
            details_path = os.path.join(member_folder, "details.txt")
            if os.path.exists(encoding_path) and os.path.exists(details_path):
                with open(encoding_path, "rb") as f:
                    known_faces.append(pickle.load(f))
                with open(details_path, "r") as f:
                    known_details.append(f.read())

    # Capture video
    cap = cv2.VideoCapture(0)
    print("Detecting face... Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"
            details = ""

            if True in matches:
                match_index = matches.index(True)
                name = known_details[match_index].split('\n')[0].split(': ')[1]
                details = known_details[match_index]

            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            cv2.putText(frame, details, (left + 6, bottom + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow("Face Recognition", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

recognize_faces()
