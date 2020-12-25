from imutils import paths
from pathlib import Path
import os
from cv2 import cv2
import argparse

"""
Script that deletes duplicate images from a dataset. This
can be used in conjunction with 'create.py' to delete
any duplicate images before manual pruning is done. 

"""
def dhash(image, hashSize=8):
    # Convert the image to grayscale and resize it
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
    # Compute the horizontal gradient between adjacent pixels
    diff = resized[:, 1:] > resized[:, :-1]
    # Converts the image to a hash and returns it
    hash = sum([2**i for (i,j) in enumerate(diff.flatten()) if j])
    return hash

# Path of the dataset of images
output_path = str(Path(__file__).parent / "dataset")
hashes = dict()

# List of paths of the images in the datasets
image_paths = list(paths.list_images(output_path))

for image_path in image_paths:
    # Load input image
    image = cv2.imread(image_path)
    # Compute the hash of the image
    h = dhash(image)
    # Store all images in a dictionary of hashes
    path = hashes.get(h, [])
    path.append(image_path)
    hashes[h] = path

# Iterate through the hashes
for h, paths in hashes.items():
    # Checking if a duplicate exists
    if len(paths) > 1:
        # Deleting all duplicates
        for path in paths[1:]:
            print("[INFO] Deleting: {}".format(path))
            os.remove(path)