"""
Command-line interface for the chaosmaps package
"""

import argparse
import matplotlib.pyplot as plt
from .visualization import plot_time_series, plot_bifurcation_map


def main():
    """Main entry point for the chaosmaps CLI"""
    parser = argparse.ArgumentParser(description='Explore chaos theory through the logistic map.')
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Time series command
    time_parser = subparsers.add_parser('time', help='Plot time series of logistic map')
    time_parser.add_argument('-r', type=float, default=3.7, help='r parameter value')
    time_parser.add_argument('-x', '--x0', type=float, default=0.5, help='Initial x value')
    time_parser.add_argument('-n', '--iterations', type=int, default=200, help='Number of iterations')
    time_parser.add_argument('-o', '--output', type=str, help='Output file path')

    # Bifurcation command
    bifurcation_parser = subparsers.add_parser('bifurcation', help='Create bifurcation diagram')
    bifurcation_parser.add_argument('-x', '--x0', type=float, default=0.5, help='Initial x value')
    bifurcation_parser.add_argument('--rmin', type=float, default=2.5, help='Minimum r value')
    bifurcation_parser.add_argument('--rmax', type=float, default=4.0, help='Maximum r value')
    bifurcation_parser.add_argument('-p', '--points', type=int, default=1000, help='Number of r values')
    bifurcation_parser.add_argument('-t', '--transient', type=int, default=800,
                                    help='Transient iterations to discard')
    bifurcation_parser.add_argument('-o', '--output', type=str, help='Output file path')

    args = parser.parse_args()

    if args.command == 'time':
        fig, ax = plot_time_series(args.iterations, args.r, args.x0)
        if args.output:
            plt.savefig(args.output, dpi=300, bbox_inches='tight')
        else:
            plt.show()

    elif args.command == 'bifurcation':
        fig, ax = plot_bifurcation_map(
            x0=args.x0,
            r_min=args.rmin,
            r_max=args.rmax,
            n_points=args.points,
            transient=args.transient,
            save_path=args.output
        )
        if not args.output:
            plt.show()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()