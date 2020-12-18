# movie-colors
Extract the primary color of each frame in a video file

## Prerequisites
Video analysis script:
- Python 3
- [Numpy](https://numpy.org/)
- [Pillow](https://pillow.readthedocs.io/)
- [OpenCV for Python](https://pypi.org/project/opencv-python/)
- [Bokeh](https://bokeh.org/) (used only by the visualization tools)

## Usage
Simple! Just run it as
```
python3 movieColors.py <path-to-video-file>
```
By default, the primary color codes are outputted to the standard output as hex codes. The output can be piped to a file e.g. as
```
python3 movieColors.py video.mp4 > frame-colors.dat
```

The output of the analysis script can be visualized using the provided `colorsBarChart.py` script:
```
python3 colorsBarChart.py frame-colors.dat
```