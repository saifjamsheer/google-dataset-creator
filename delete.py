from imutils import paths
from pathlib import Path
import os
import cv2
import argparse

"""
Script that deletes duplicate images from a dataset. This
can be used in conjunction with 'create.py' to delete
any duplicate images before manual pruning is done. 

"""