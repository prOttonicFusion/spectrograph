import sys
import cv2
import numpy as np
from PIL import Image


def main():
    video_path = sys.argv[1]
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        # Convert to PIL image
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img)

        # Crop frame to remove border
        aspect_ratio = 16/4.0
        width, height = pil_img.size
        left = 0
        right = width
        content_height = 1/aspect_ratio * width
        border = (height - content_height) * 0.5
        top = border
        bottom = border + content_height
        pil_img = pil_img.crop((left, top, right, bottom))

        # Get primary color
        main_color = get_primary_color(pil_img)
        print(rgbToHex(main_color))

        # Attempt to read next frame
        success, image = vidcap.read()
        count += 1


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
