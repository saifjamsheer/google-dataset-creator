from imutils import paths
from pathlib import Path
import os
import cv2
import argparse
import requests

"""
Script that downloads images from a text file of Google Image urls.
This script is used to create datasets for deep learning projects
in a simple and efficient matter. Manual pruning may have to be
done to ensure that the images within the dataset are relevant.

Note: The user must specify the path of 'urls.txt'.

"""
parser = argparse.ArgumentParser()
# Path for the url text file 
path = '/Users/saif/Downloads/urls.txt'
parser.add_argument("-u", "--urls", help="path of urls.txt", default=path)
args = vars(parser.parse_args())
# Path for the destination of the downloaded images
output_path = str(Path(__file__).parent / "dataset")

# Getting the list of urls for all images
rows = open(args["urls"]).read().strip().split("\n")
total = 0

# Loop through the urls of the images
for url in rows:
    try:
        r = requests.get(url, timeout=60)
        # save the image to disk
        p = '/'.join([output_path, "{}.jpg".format(str(total).zfill(8))])
        f = open(p, "wb")
        f.write(r.content)
        f.close()
        # update the counter
        print("[INFO] Downloaded: {}".format(p))
        total += 1
    except:
	    print("[INFO] Error downloading: {}".format(p))

# Loop through the images in the output path to determine
# if image should be deleted
for image_path in paths.list_images(output_path):
	# Initialize variable that determines if an image
    # should be deleted
	delete = False
	# Attempt to load the image
	try:
		image = cv2.imread(image_path)
		if image is None:
			delete = True
	except:
		print("[INFO] Error loading: {}".format(image_path))
		delete = True
	# check to see if the image should be deleted
	if delete:
		print("[INFO] Deleting: {}".format(image_path))
		os.remove(image_path)