import xml.etree.ElementTree
import os
import cv2
import numpy as np

def convert(input_path, fileFormat, output_path):
    all_images = []