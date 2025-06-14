# Face Recognition Project

A simple real-time face recognition system using Python, OpenCV, and [face_recognition](https://github.com/ageitgey/face_recognition).

## Setup

1. **Clone the repository**
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Enroll Known Faces

Run the enrollment script and follow prompts:
```
python enroll_face.py
```
- Enter the person's name.
- Press `c` to capture their face from webcam.
- Repeat for each person.

## Run Face Recognition

Start the recognition system:
```
python main.py
```
- It will identify faces from the webcam using enrolled faces in `known_faces/`.
- Press `q` to quit.

## Notes

- Add more reference images (named as `<person>.jpg`) in `known_faces/` for better accuracy.
- Works best in good lighting and with clear front-facing images.
