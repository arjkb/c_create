import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of C file to be created")
args = parser.parse_args()
print(" Filename: {}".format(args.filename))
