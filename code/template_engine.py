#!/usr/bin/env python3

import sys

# Checking if argparse is installed
try:
	import argparse
except ImportError:
	sys.stderr.write("[Error] The python module \"argparse\" is not installed\n")
	sys.stderr.write("[--] Would you like to install it now using 'sudo easy_install' [Y/N]? ")
	answer = sys.stdin.readline()
	if answer[0].lower() == "y":
		sys.stderr.write("[--] Running \"sudo easy_install argparse\"\n")
		from subprocess import call
		call(["sudo", "easy_install", "argparse"])
	else:
		sys.exit("[Error] Exiting due to missing dependency \"argparser\"")

parser = argparse.ArgumentParser(prog="template_engine.py")
parser.add_argument("name", nargs='?', help="Set the name for the script to create", default="new_script.py")
args = parser.parse_args()


def main():
	output_file = open(args.name, "w")

	output_file.write('''#!/usr/bin/env python3
"""
Modify this line to briefly discribe the functionality of %s

Copyright (C) 2017  Martin Engqvist Lab
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
from dotenv import load_dotenv, find_dotenv
from os.path import join, dirname, isdir

### Load environmental variables from the project root directory ###
# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

# now you can get the variables using their names, for example:
# database_url = os.environ.get("DATABASE_URL")
# other_variable = os.environ.get("OTHER_VARIABLE")

# get the current working directory
CURRENT_DIR = os.getcwd()

# project root directory
PROJ_ROOT_DIR = dirname(dotenv_path)

# internal data raw directory
INT_RAW_DIR = join(PROJ_ROOT_DIR, 'data/raw_internal/')

# external data raw directory
EXT_RAW_DIR = join(PROJ_ROOT_DIR, 'data/raw_external/')

# clean data directory
CLEAN_DIR = join(PROJ_ROOT_DIR, 'data/clean/')

# output directory
OUT_DIR = join(PROJ_ROOT_DIR, 'results/')

# figure output directory
FIG_DIR = join(PROJ_ROOT_DIR, 'results/figures/')

# picture output directory
PIC_DIR = join(PROJ_ROOT_DIR, 'results/pictures/')


#### Your code here ####


''' % args.name)



if __name__ == "__main__":
	main()
