"""
Extract the primary colors from each frame of a video file
"""

__author__ = "prOttonicFusion"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
import cv2
import argparse
import numpy as np
from PIL import Image


def analyze_movie(
        video_path, aspect_ratio=0, palette_size=32, frames=-1, step=1, show_frames=False, show_last_frame=False, color_format='hex'
):
    """Parses and prints out the primary color of every STEPth video frame

    Parameters
    ----------
    video_path : str
        The path to the video file
    aspect_ratio : float, optional
        The aspect ratio used for cropping a video with vertical borders
    palette_size: int, optional
        Number of distinct colors in color space (Default: 32)
    frames: int, optional
        Number of frames to parse, with -1 meaning all frames (Default: -1)
    step: int, optional
        The step size between frames (Default: 1)
    show_frames: bool, optional
        Show each processed frame for debugging purposes (Default: False)
    show_last_frame: bool, optional
        Show last frame for debugging purposes (Default: False)
    color_format: 'hex' or 'rgb'
        Specify the output color format (Default: hex)
    """

    # Parse video frame-by-frame
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    pil_img = None
    count = 0
    while success and frames == -1 or count < frames:
        if count % step == 0:
            # Convert to PIL image
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(img)

            # Crop frame to remove border
            if aspect_ratio != 0:
                width, height = pil_img.size
                left = 0
                right = width
                content_height = 1/aspect_ratio * width
                border = (height - content_height) * 0.5
                top = border
                bottom = border + content_height
                pil_img = pil_img.crop((left, top, right, bottom))

            # Get primary color
            main_color = get_primary_color(
                pil_img, palette_size, show_img=show_frames)

            if color_format == 'hex':
                main_color = rgbToHex(main_color)
                
            print(main_color)

        # Attempt to read next frame
        success, image = vidcap.read()
        count += 1

    if show_last_frame:
        pil_img.show()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('video_path', help='path to the video file')
    parser.add_argument('--aspect_ratio', '-a',
                        help='specify the aspect ratio using the format 4:3 to crop out border, default: 0', default=0)
    parser.add_argument('--palette_size', '-p',
                        help='number of distinct colors in color space, default 32', type=int, default=32)
    parser.add_argument('--frames', '-f',
                        help='number of video frames to parse, with -1 being all, default: -1', type=int, default=-1)
    parser.add_argument('--step', '-s',
                        help='step size, i.e. parse every STEPth frames, default: 1', type=int, default=1)
    parser.add_argument('--show_frames',
                        help='show each processed frame for debugging purposes', action='store_true', default=False)
    parser.add_argument('--show_last_frame',
                        help='show last frame for debugging purposes', action='store_true', default=False)
    parser.add_argument('--color_format',
                        help='specify the color format as hex or rgb, default: hex', default='hex')
    args = parser.parse_args()

    if isinstance(args.aspect_ratio, str):
        splitted = args.aspect_ratio.split(':')
        try:
            args.aspect_ratio = float(splitted[0])/float(splitted[1])
        except:
            raise(Exception('Unable to parse aspect ratio'))

    if args.show_frames and args.frames == -1:
        input("Warning: This will open each video frame in a new window. To continue, press enter")

    return [args.video_path,
            args.aspect_ratio,
            args.palette_size,
            args.frames,
            args.step,
            args.show_frames,
            args.show_last_frame,
            args.color_format]


def get_primary_color(source_img, palette_size, show_img=False):
    """Get the primary color of an image by scaling it down and reducing
       the color palette

    Parameters
    ----------
    source_img : Image
        The PIL image to use as source
    palette_size: int
        The number of distinct colors to reduce the image color palette to
    show_img: bool, optional
        Sets whether the modified image should be displayed

    Returns
    ----------
    primary_color : tuple
        A RGB tuple describing the frame's most common color
    """

    # Scale down image to conserve resources
    img = source_img.copy()
    img.thumbnail((100, 100))

    # Reduce color palette (using k-means)
    img_reduced = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)
    if show_img:
        img_reduced.show()

    # Get list of colors in image
    palette = img_reduced.getpalette()

    # Find most common color
    color_counts = sorted(img_reduced.getcolors(), reverse=True)
    primary_index = color_counts[0][1]
    primary_color = palette[primary_index*3:primary_index*3+3]

    return primary_color


def rgbToHex(rgb_color):
    """Converts a RGB tuple to a hex color string"""
    r, g, b = rgb_color
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


if __name__ == "__main__":
    args = parse_arguments()
    analyze_movie(*args)
