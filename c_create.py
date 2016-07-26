import argparse
import fileinput

from shutil import copyfile

def createMakefile(my_filename):
    search_text = "filename"
    replace_text = my_filename

    fh_makefile = open('Makefile.template', 'r')
    makefile_data = fh_makefile.read()
    fh_makefile.close()

    new_data = makefile_data.replace(search_text, replace_text)

    f = open('Makefile', 'w')
    f.write(new_data)
    f.close()


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of C file to be created")
args = parser.parse_args()

c_filename = args.filename
print(" Filename: {}".format(c_filename))

copyfile("hello_world.c", c_filename + ".c")

createMakefile(c_filename)
