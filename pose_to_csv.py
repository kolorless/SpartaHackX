import cv2
import mediapipe as mp
import time
import csv

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

start_time = time.time()
time_limit = 5
csv_filename = "time_series_raw.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    header = ['timestamp'] + [f'landmark_{i}_x' for i in range(33)] + [f'landmark_{i}_y' for i in range(33)] + [f'landmark_{i}_z' for i in range(33)]
    writer.writerow(header)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    timestamp = time.time() - start_time
    if timestamp > time_limit:
        break

    if results.pose_landmarks:
        landmarks = []
        for i, landmark in enumerate(results.pose_landmarks.landmark):
            landmarks.append(landmark.x)
            landmarks.append(landmark.y)
            landmarks.append(landmark.z)

        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp] + landmarks)

        h, w, _ = frame.shape
        for i, landmark in enumerate(results.pose_landmarks.landmark):
            x, y = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            cv2.putText(frame, f"{i}", (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

    cv2.imshow("Live Pose Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
