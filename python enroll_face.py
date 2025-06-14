import cv2
import os

KNOWN_FACES_DIR = "known_faces"
os.makedirs(KNOWN_FACES_DIR, exist_ok=True)

name = input("Enter the name for the new face: ").strip()
if not name:
    print("Name cannot be empty!")
    exit(1)

filename = f"{KNOWN_FACES_DIR}/{name}.jpg"

cap = cv2.VideoCapture(0)
print("[INFO] Press 'c' to capture image.")

while True:
    ret, frame = cap.read()
    cv2.imshow("Enroll Face", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('c'):
        cv2.imwrite(filename, frame)
        print(f"[INFO] Image saved as {filename}")
        break
    elif key & 0xFF == ord('q'):
        print("Quit without saving.")
        break
cap.release()
cv2.destroyAllWindows()
