import os
import cv2
import mediapipe as mp
import pandas as pd

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)


def extract_keypoints(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    keypoints = []

    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            keypoints.append([landmark.x, landmark.y, landmark.z])
    return keypoints


root_folder = 'archive'

for exercise_folder in os.listdir(root_folder):
    exercise_path = os.path.join(root_folder, exercise_folder)

    if os.path.isdir(exercise_path):
        print(f"Processing folder: {exercise_folder}")

        columns = ['image_name'] + [f'keypoint_{i}_x' for i in range(33)] + \
                  [f'keypoint_{i}_y' for i in range(33)] + [f'keypoint_{i}_z' for i in range(33)]
        df = pd.DataFrame(columns=columns)

        for image_file in os.listdir(exercise_path):
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(exercise_path, image_file)
                image = cv2.imread(image_path)

                keypoints = extract_keypoints(image)
                flattened_keypoints = [image_file]

                for i in range(33):
                    if i < len(keypoints):
                        flattened_keypoints.extend(keypoints[i])
                    else:
                        flattened_keypoints.extend([float('nan')] * 3)

                df.loc[len(df)] = flattened_keypoints

        csv_filename = f"{exercise_folder.replace(' ', '_').lower()}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Data saved to '{csv_filename}'")

print("Processing complete.")
