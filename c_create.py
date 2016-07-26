import argparse

from shutil import copyfile

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of C file to be created")
args = parser.parse_args()

c_filename = args.filename + ".c"
print(" Filename: {}".format(c_filename))

copyfile("hello_world.c", c_filename)
