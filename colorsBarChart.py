import numpy as np
import argparse
from math import pi
from bokeh.io import output_file, show
from bokeh.plotting import figure


def main(color_data_file):
    colors = np.loadtxt(color_data_file, comments="%", dtype=str)
    print(colors[0])
    data_range = len(colors)
    data = list(range(0, data_range))

    fig = figure(plot_height=250, title='Title',
                 toolbar_location=None, tools='')

    fig.vbar(x=data, top=1, width=0.9, color=colors)

    output_file('plot.html', title='Bokeh Plot', mode=None, root_dir=None)

    show(fig)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'color_data_file', help='path to the data file containing a list of colors')
    args = parser.parse_args()

    return [args.color_data_file]


if __name__ == "__main__":
    args = parse_arguments()
    main(*args)
