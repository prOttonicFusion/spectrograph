"""
Plot a spectrum from a data file of color codes
"""

__author__ = "prOttonicFusion"
__version__ = "0.1.0"
__license__ = "MIT"

import numpy as np
import argparse
from math import pi
from bokeh.io import output_file, export_png, show
from bokeh.plotting import figure


def main(color_data_file, html='', png='', title='', show_axes=False, show_grid=False):
    colors = np.loadtxt(color_data_file, comments="%", dtype=str)
    data_range = len(colors)
    data = list(range(0, data_range))

    fig = figure(plot_height=250, title=title,
                 toolbar_location=None, tools='')

    fig.vbar(x=data, top=1, width=0.9, color=colors)

    if not show_axes:
        fig.axis.visible = False

    if not show_grid:
        fig.xgrid.grid_line_color = None
        fig.ygrid.grid_line_color = None
        fig.outline_line_color = None

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
                        help='set the output file name and save as HTML, default: none', default='')
    parser.add_argument('--png',
                        help='set the output file name and save as png, default: none', default='')
    parser.add_argument('--title',
                        help='set plot title, default: none', default='')
    parser.add_argument('--show_axes',
                        help='show plot axes, default: False', action='store_true', default=False)
    parser.add_argument('--show_grid',
                        help='show plot grid, default: False', action='store_true', default=False)
    args = parser.parse_args()

    return [args.color_data_file, args.html, args.png, args.title, args.show_axes, args.show_grid]


if __name__ == "__main__":
    args = parse_arguments()
    main(*args)
