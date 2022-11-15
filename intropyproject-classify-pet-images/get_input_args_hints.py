#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args_hints.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                   
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function that retrieves the following 3 command line inputs from
#          the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Creates parse 
    parser = argparse.ArgumentParser()

# This code is adding an argument to the parser. The argument is called dir and it is a string.
# The default value is pet_images/. The help is the path to the folder of images.
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to folder of images')
# This is adding an argument to the parser. The argument is called arch and it is a string.
# The default value is vgg. The help is the CNN Model Architecture as --arch with default value 'vgg'
    parser.add_argument('--arch', default = 'vgg', 
                        help='CNN Model Architecture as --arch with default value \'vgg\' ' )
# This is adding an argument to the parser. The argument is called dogfile and it is a string.
# The default value is dognames.txt. The help is the Text File with Dog Names as --dogfile with
# default value 'dognames.txt'
    parser.add_argument('--dogfile', default = 'dognames.txt',
                        help='Text File with Dog Names as --dogfile with default value \'dognames.txt\'')

    return parser.parse_args()
