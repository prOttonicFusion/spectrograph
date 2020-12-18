# Movie Spectrograph
Visualize video files as spectrums consisting of the primary colors of each frame

## Prerequisites
- Python 3
- [Numpy](https://numpy.org/)
- [Pillow](https://pillow.readthedocs.io/)
- [OpenCV for Python](https://pypi.org/project/opencv-python/)
- [Bokeh](https://bokeh.org/) (used only by the visualization tools)

## Usage
To extract the most used colors of each fram, simply run
```
python3 spectrograph.py <path-to-video-file>
```
By default, the color codes are outputted to the standard output as hex codes. The output can be piped to a file e.g. as
```
python3 spectrograph.py video.mp4 > frame-colors.dat
```

The output of the analysis script can then be visualized using the provided `linearSpectrum.py` script:
```
python3 linearSpectrum.py frame-colors.dat
```