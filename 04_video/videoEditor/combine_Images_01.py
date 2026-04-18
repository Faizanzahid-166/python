#  1 from cv2 ------------------------------------------------------------------------

# import cv2
# import os

# image_folder = "images"

# images = [img for img in os.listdir(image_folder) if img.endswith((".png",".jpg",".jpeg"))]

# if not images:
#     print("No images found")
#     exit()

# first = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, _ = first.shape

# video = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc(*'XVID'), 1, (width, height))
# # video = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height))

# for image in images:
#     path = os.path.join(image_folder, image)
#     img = cv2.imread(path)

#     if img is None:
#         print("Skipping:", image)
#         continue

#     img = cv2.resize(img, (width, height))
#     video.write(img)

# video.release()

# print("Video created successfully!")


# 2 from moviepy------------------------------------------------------------------------
# videoEditor/combine-images.py
from moviepy import ImageSequenceClip
from PIL import Image
import os
import numpy as np
import sys

def run_combination():
    # Look one level up from videoEditor into upload/images
    image_folder = os.path.join(os.getcwd(), "upload", "images")
    output_file = "video.mp4"

    if not os.path.exists(image_folder):
        print(f"Error: Folder not found at {image_folder}")
        return

    images = [
        os.path.join(image_folder, img)
        for img in os.listdir(image_folder)
        if img.endswith((".png", ".jpg", ".jpeg"))
    ]
    images.sort()

    if not images:
        print("No images found in upload/images!")
        return

    # Process images
    first_img = Image.open(images[0])
    target_size = first_img.size
    resized_images = []

    for img_path in images:
        img = Image.open(img_path).convert("RGB")
        if img.size != target_size:
            img = img.resize(target_size)
        resized_images.append(np.array(img))

    # Create video
    seconds_per_image = 1
    clip = ImageSequenceClip(resized_images, durations=[seconds_per_image]*len(resized_images))
    clip.write_videofile(output_file, fps=24, codec="libx264", audio=False)
    print(f"Success! Video saved as {output_file}")

if __name__ == "__main__":
    run_combination()
# 3-------------------------------------------------------------------------
# from manim import *

# class Hello(Scene):
#     def construct(self):
#         text = Text("Hello World")
#         self.play(Write(text))

