import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of C file to be created")
args = parser.parse_args()

c_filename = args.filename
print(" Filename: {}".format(c_filename))
