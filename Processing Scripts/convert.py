# =============================================================================
# Created By  : Kanaad Pathak
# Created Date: Fri 24 Apr 2020 04∶32∶25 PM BST 2020
# Course : MSc AIA 2020 | University of Strathclyde | United Kingdom
# =============================================================================
"""
Purpose : This module is built to convert the TIFF files present in the directories to JPEG format; and subsequently remove the TIFF
	  file using the shell script.

Original Directory structure before modification:
	\ Dir_1
		|-- image_1.tif
	\ Dir_2
		|-- image_2.tif

Directory structure after program execution:
	\ Dir
		|-- image_1.tif
		|-- image_2.tif

"""
# =============================================================================


# =============================================================================
# IMPORT BLOCK
# =============================================================================

import os
from PIL import Image
import subprocess
from tqdm import tqdm

# =============================================================================



'''
Function : Convert File
Input : None
Output : Converted JPEG file

Corner Cases : No exception handling for other file formats, use with caution

'''


def convert_files():
    path = os.getcwd()
    for root, dirs, files in os.walk(path, topdown=False):

        for name in tqdm(files):

            # print(os.path.join(root, name))
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                    print ("A jpeg file already exists for %s" % name)
                # If a jpeg is *NOT* present, create one from the tiff.
                else:
                    outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                    # print(f'Name of outfile : {name[7:]}')
                    try:
                        im = Image.open(os.path.join(root, name))
                        # print ("Generating jpeg for %s" % name)
                        im.thumbnail(im.size)
                        im.save(outfile, "JPEG", quality=70)

                        # for removing the 'Copy of' from the file name
                        original_1 = name.replace('tif','jpg')
                        original = os.path.join(root,original_1)
                        new_file = original_1[8:]
                        new_file = os.path.join(root,new_file)
                        os.rename(original,new_file) 
                    except Exception as  e:
                        print (f'Exception {e} occoured')

'''
Function : Clean TIFF
Input : None
Output : Subprocess call to shell script for removal of TIF files from all directories and bring every file one level up.

Corner Case : Will not execute shell scripts with SUDO requirements.

'''


def clean_tiff():
    subprocess.call(['./removal.sh'])


def main():

    convert_files()
    clean_tiff()


if __name__ == "__main__":
    main()
