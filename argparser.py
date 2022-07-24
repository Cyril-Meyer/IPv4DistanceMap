import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threads",
                        type=int,
                        default=1024,
                        help="number of threads")
    return parser.parse_args()
