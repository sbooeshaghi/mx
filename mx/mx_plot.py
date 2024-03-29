import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from scipy.io import mmread
from scipy.optimize import curve_fit
from .utils import nd


def setup_mx_plot_args(parser):
    # plot ###################################################
    plot_info = "Plot figures for a matrix"
    parser_format = parser.add_parser(
        "plot", description=plot_info, help=plot_info, add_help=True
    )

    # plot subparser arguments
    parser_format.add_argument(
        "-o",
        "--output",
        default=None,
        type=str,
        required=True,
        help="Output path to save plot",
    )
    parser_format.add_argument(
        "-gi",
        "--genes-in",
        default=None,
        type=str,
        required=True,
        help="Input path for genes.txt",
    )


    parser_format.add_argument(
        "-bi",
        "--bcs-in",
        default=None,
        type=str,
        required=True,
        help="Input path for bcs.txt",
    )

    parser_format.add_argument(
        "-m", "--method", required=False, default="knee", choices=["knee"]
    )

    parser_format.add_argument(
        "matrix", metavar="matrix.mtx", type=str, help="Path to matrix.mtx file"
    )
    return parser_format


def validate_mx_plot_args(parser, args):
    mtx_fn = args.matrix
    plot_fn = args.output
    barcodes_fn = args.bcs_in
    genes_fn = args.genes_in
    method = args.method


    run_mx_plot(mtx_fn, plot_fn, method, barcodes_fn, genes_fn)


def run_mx_plot(mtx_fn, plot_fn, method, barcodes_fn, genes_fn):
    mtx = mmread(mtx_fn).tocsr()
    fig, ax = plt.subplots(figsize=(10,10))
    if method == "knee":

        ax = mx_plot_knee(mtx, ax)
    else:
        raise NotImplementedError()
    fig.savefig(plot_fn, dpi=300)


def yex(ax):
    lims = [
        np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
        np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
    ]

    # now plot both limits against eachother
    ax.plot(lims, lims, c="k", alpha=0, zorder=0)
    ax.set(**{"aspect": "equal", "xlim": lims, "ylim": lims})
    return ax

def mx_plot_knee(mtx, ax):
    fsize = 20
    plt.rcParams.update({"font.size": fsize})
    x = np.sort(np.array(mtx.sum(axis=1)).flatten())[::-1]

    y = np.arange(x.shape[0])
    ax.scatter(x,y)
    ax.set(**{
        "xscale": "log",
        "yscale": "log",
        "xlabel": "UMI count",
        "ylabel": "Number of cells"
    })
    yex(ax)
    
    return ax