import os
import shutil
import sys
from os.path import isfile
import fileinput


def convert_to_pihole(file):
    # Nothing to do, since pihole already uses the expected host file format
    # Adjust this only if pihole adjusts its formatting
    # In that case, see convert_to_adguard for inspiration

    return None


def convert_to_adguard(file_path):
    with fileinput.FileInput(files=[file_path], inplace=True) as f:  # This allows for inplace file modification
        for line in f:
            clean_line = line.strip().strip("\n")

            if len(clean_line) != 0:  # blank line in host file
                if clean_line[0] != "#":  # a comment in hose file
                    clean_line = "||" + clean_line + "^"
            print(clean_line)


source_dir = os.getcwd()
input_dir = os.path.join(source_dir, "input")
target_dir = os.path.join(source_dir, "output")

if not os.path.exists(input_dir):
    os.makedirs(input_dir)
    print("Input folder created for first time")
    print("Add host files to the folder and re-run the program again")
    sys.exit()

input_files = [f for f in os.listdir(input_dir) if isfile(os.path.join(input_dir, f))]

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# copies the source host files (from input folder) to adguard and pihole files (in output folder)
# This copy overwrites files that already exist in the output folder
# Finally, it converts the files into formats accepted by pihole and adguard
for input_file in input_files:
    adguard_file = os.path.join(target_dir, "adguard_" + input_file)
    pihole_file = os.path.join(target_dir, "pihole_" + input_file)
    shutil.copy(os.path.join(input_dir, input_file), adguard_file)
    shutil.copy(os.path.join(input_dir, input_file), pihole_file)

    convert_to_pihole(pihole_file)
    convert_to_adguard(adguard_file)
