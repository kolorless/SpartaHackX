import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("decline_bench_press.csv")

image_names = df["image_name"].unique()

for image_name in image_names:
    fig, ax = plt.subplots(figsize=(6, 6))

    keypoints_at_image = df[df["image_name"] == image_name]

    keypoints_x = [keypoints_at_image[f"keypoint_{i}_x"].values[0] for i in range(33)]
    keypoints_y = [keypoints_at_image[f"keypoint_{i}_y"].values[0] for i in range(33)]

    min_x, max_x = min(keypoints_x), max(keypoints_x)
    min_y, max_y = min(keypoints_y), max(keypoints_y)

    margin = 0.1
    ax.set_xlim(min_x - margin, max_x + margin)
    ax.set_ylim(min_y - margin, max_y + margin)

    ax.scatter(keypoints_x, keypoints_y, c='blue', label=f"Image: {image_name}")

    ax.set_title(f"Pose Keypoints for Image: {image_name}")
    ax.set_xlabel("Normalized X")
    ax.set_ylabel("Normalized Y")

    ax.legend(loc='upper right')
    plt.grid(True)
    plt.show(block=True)
