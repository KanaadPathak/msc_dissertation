**README FILE**


NOTE: ALL OF THE INPUT DATASET IS NOT PRESENT IN THE SUBMISSION FILE DUE TO THE SIZE CONSTRAINTS OF MYPLACE SUBMISSION. A REPRESENTATION OF THE FOLDER STRUCTURE IS PRESENT IN THE `SAMPLE IMAGES` FOLDER

The full dataset can be requested from the original author from the link:

+-----------------------------+
| https://bit.ly/ich-dataset  |
+-----------------------------+

The specific folder to use within the dataset is the `HHP/cropped pas stained images hhp` folder. Beware that the dataset is over 16GB in size, download at your own risk.



Steps to install environment:
1. run the requirements  file by issuing the command 'pip install -r requirements.txt'


Steps for data pre-processing:
1. Navigate to the folder with all downloaded images
2. Run the convert.py file present in the `/Processing Scipts` folder
3. Run the `File Processing Pipeline.ipynb` file to split the data into train and test folders.


All the models execpt for the object detection model can be run from the corresponding python notebooks.
The object detection model requires the setup of supervisely and permission to my workspace to use.
However, the files required to setup your own supervisely cluster are present in the `Supervisely Scripts` folder

Steps to Initialise Supervisely:
1. Navigate to the `Supervisely Scripts` folder
2. Run the `init_supervisely` script
3. Run the `stop_supervisely` script to stop the instance

NOTE: THIS WON'T WORK AS IT HAS BEEN SETUP TO USE MY ACCESS API KEY WHICH IS LINKED TO MY PERSONAL COMPUTER.


An example of the output images from the Object Detection model is present in the `Output Images` folder. To achieve the same output, use the following steps

1. Download the JSON files from the image inference from supervise.ly
2. Navigate to the `Processing Scripts` folder
3. Run the script titled `rectangle_draw.py` [before running this, make sure all images and JSON files are in a single folder]

A more detailed explanation of the object detection inference is present in the video attached.





