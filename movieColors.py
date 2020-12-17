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


def get_primary_color(source_img, palette_size=32):
    # Scale down image to conserve resources
    img = source_img.copy()
    img.thumbnail((100, 100))

    # Reduce color palette (using k-means)
    img_reduced = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)

    # Get list of colors in image
    palette = img_reduced.getpalette()

    # Find most common color
    color_counts = sorted(img_reduced.getcolors(), reverse=True)
    primary_index = color_counts[0][1]
    primary_color = palette[primary_index*3:primary_index*3+3]

    return primary_color


def rgbToHex(rgb_color):
    r, g, b = rgb_color
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


if __name__ == "__main__":
    main()
