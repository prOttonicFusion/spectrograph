# Spectrograph
Visualize movies and other videos as color spectrums based on the primary colors of each frame

![Sample 1](https://github.com/prOttonicFusion/spectrograph/blob/main/samples/LoTR_Fellowship-of-the-Ring.png)
![Sample 2](https://github.com/prOttonicFusion/spectrograph/blob/main/samples/Star-Wars_A_New_Hope.png)

## Prerequisites
- Python 3
- [Numpy](https://numpy.org/)
- [Pillow](https://pillow.readthedocs.io/)
- [OpenCV for Python](https://pypi.org/project/opencv-python/)
- [Bokeh](https://bokeh.org/) (optional, used for visualization only)

## Usage
To extract the color data into a file, simply run
```
python3 spectrograph.py <video-file> > <output-file>
```
e.g.
```
python3 spectrograph.py video.mp4 > frame-colors.dat
```

The output of the analysis script can then be visualized using the provided `linearSpectrum.py` script:
```
python3 linearSpectrum.py frame-colors.dat
```
Both scripts can be run using the `-h` flag to get a complete list of available commands and options.
