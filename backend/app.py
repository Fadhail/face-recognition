from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np

app = Flask(__name__)

# Load Face Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def label_face(roi_gray):
    # Dummy face recognition logic
    return "Detected Face"

def generate_frames():
    cap = cv2.VideoCapture(0)  # 0 for default camera

    while True:
        success, frame = cap.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            label = label_face(roi_gray)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture_attendance', methods=['POST'])
def capture_attendance():
    data = request.json
    # Process the captured data here
    # For example, saving it into a database or keeping records
    # Here, we're just going to return the received data for demonstration
    return jsonify({"message": "Attendance recorded", "data": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
