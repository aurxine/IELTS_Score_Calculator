import pandas as pd
import argparse
import numpy as np
import os

# Default file path
file_path = "/home/dhrubo/IELTS_Scores.csv"

# Initialize parser
parser = argparse.ArgumentParser(description= "Calculate IELTS band from the score and save it in a file")


# Adding arguments
parser.add_argument("--path", type = str, default = file_path,
                    help = "File path to be saved")

parser.add_argument("--scores", type = int, nargs = "*", 
                    choices = range(0, 41), metavar = "[0-40]", 
                    help = "Scores [L] [R] [W] [S]")

parser.add_argument("-L", type = int, 
                    choices = range(0, 41), metavar = "[0-40]", 
                    help = "'Listening' score")

parser.add_argument("-R", type = int, 
                    choices = range(0, 41), metavar = "[0-40]", 
                    help = "'Reading' score")

parser.add_argument("-W", type = int, 
                    choices = range(0, 41), metavar = "[0-40]", 
                    help = "'Writing' score")

parser.add_argument("-S", type = int,
                    choices = range(0, 41), metavar = "[0-40]", 
                    help = "'Speaking' score")

parser.add_argument("--band", type = int,
                    choices = range(0, 41), metavar = "[0-40]", 
                    help = "Band score")


def BandScore(score):
    # print(score)
    if score is None:
        return None

    if score in range(4, 6):
        return 2.5
    if score in range(6, 8):
        return 3
    if score in range(8, 10):
        return 3.5
    if score in range(10, 13):
        return 4
    if score in range(13, 15):
        return 4.5
    if score in range(15, 19):
        return 5
    if score in range(19, 23):
        return 5.5
    if score in range(23, 27):
        return 6
    if score in range(27, 30):
        return 6.5
    if score in range(30, 33):
        return 7
    if score in range(33, 35):
        return 7.5
    if score in range(35, 37):
        return 8
    if score in range(37, 39):
        return 8.5
    if score in range(39, 41):
        return 9

def CalculateScore(args):
    '''
    args["scores"]:             all the scores [Listening, Reading, Writing, Speaking]
    args["L"]:                  Listening
    args["R"]:                  Reading
    args["W"]:                  Writing
    args["S"]:                  Speaking
    '''
    if args["scores"] is not None:
        args["L"] = args["scores"][0]
        args["R"] = args["scores"][1]
        args["W"] = args["scores"][2]
        args["S"] = args["scores"][3]
    
    
    return [BandScore(args['L']), BandScore(args['R']), BandScore(args['W']), BandScore(args['S'])]


if __name__ == '__main__':
    # Read arguments from command line
    args_dict = vars(parser.parse_args())

    # print(args_dict)
    if args_dict["band"] is not None:
        print(BandScore(args_dict["band"]))
    # print(CalculateScore(args_dict))

    # if not os.path.isfile(args_dict["path"]):
    #     print("no file")

