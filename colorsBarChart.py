import numpy as np
import argparse
from math import pi
from bokeh.io import output_file, export_png, show
from bokeh.plotting import figure


def main(color_data_file, html, png):
    colors = np.loadtxt(color_data_file, comments="%", dtype=str)
    data_range = len(colors)
    data = list(range(0, data_range))

    fig = figure(plot_height=250, title='Title',
                 toolbar_location=None, tools='')

    fig.vbar(x=data, top=1, width=0.9, color=colors)

    if html != '':
        output_file(html, mode=None, root_dir=None)

    if png != '':
        export_png(fig, filename=png)

    show(fig)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'color_data_file', help='path to the data file containing a list of colors')
    parser.add_argument('--html',
                        help='set the output file name and save as HTML', default='')
    parser.add_argument('--png',
                        help='set the output file name and save as png', default='')
    args = parser.parse_args()

    return [args.color_data_file, args.html, args.png]


if __name__ == "__main__":
    args = parse_arguments()
    main(*args)
