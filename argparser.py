import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threads",
                        type=int,
                        default=1024,
                        help="number of threads")
    parser.add_argument("--timeout",
                        type=int,
                        default=10,
                        help="ping timeout")
    parser.add_argument("--count",
                        type=int,
                        default=3,
                        help="ping count")
    parser.add_argument("--interval",
                        type=int,
                        default=1,
                        help="ping interval")
    return parser.parse_args()
