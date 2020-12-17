import sys
import cv2
import numpy as np
from PIL import Image

# Read video file

# Check need for color correction

# Parse frames to PIL images

# Extract primary color

def main():
    img_path = sys.argv[1]
    img = Image.open(img_path)

    main_color = get_primary_color(img)
    print('Dominant color: ', rgbToHex(main_color))

if __name__ == "__main__":
    main()