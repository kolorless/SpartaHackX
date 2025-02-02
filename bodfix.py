import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Load Time Series Sample
time_series_sample = pd.read_csv("time_series_raw.csv")

# Extract keypoints from the last recorded frame
sample_features = time_series_sample.iloc[-1, 1:].values  # Ignore timestamp

# Step 2: Load Exercise Data
exercise_data = []
exercise_labels = []
root_folder = os.getcwd()  # Folder containing exercise CSVs (same directory as this script)

# Define the number of keypoints and features
num_keypoints = 33
num_features = num_keypoints * 3  # x, y, z for each keypoint

# Debugging information
print(f"Expected number of features per row: {num_features}")

for csv_file in os.listdir(root_folder):
    if csv_file.endswith('.csv'):
        file_path = os.path.join(root_folder, csv_file)
        df = pd.read_csv(file_path)

        # Drop the first column (image_name) to extract keypoints
        df_features = df.iloc[:, 1:].values

        # Ensure each row has the same number of elements (33 keypoints, 3 dimensions per keypoint)
        for row in df_features:
            if len(row) != num_features:
                print(f"Skipping row with incorrect length: {len(row)}")
                continue  # Skip rows with incorrect length
            exercise_data.append(row)
            exercise_labels.append(csv_file.replace('.csv', ''))  # Use filename as label

# Convert to NumPy arrays
exercise_data = np.array(exercise_data, dtype=np.float32)  # Explicitly cast to float32
X = exercise_data
y = np.array(exercise_labels)

# Step 3: Encode Labels & Normalize Data
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

sample_features_scaled = scaler.transform([sample_features])  # Normalize input sample

# Step 4: Train a Simple Neural Network
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(len(label_encoder.classes_), activation='softmax')  # Multi-class output
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test))

# Step 5: Predict Exercise
predicted_class_index = np.argmax(model.predict(sample_features_scaled))
predicted_exercise = label_encoder.inverse_transform([predicted_class_index])[0]

print(f"Predicted Exercise: {predicted_exercise}")
