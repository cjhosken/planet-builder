from argparse import *
import os
import sys
import builder

parser = ArgumentParser(description="planetbuilder is a command line script that will generate equirectangular textures from a specified space engine texture pack.")
parser.add_argument("-s", "--source", help="Path to parent folder containing the folders: pos_x, neg_y...")
parser.add_argument("-r", "--res", help="Resolution of the LOD. To check all possibles resolution, navigate into your textures folder and check the first character of your files. (eg. '5_0_0.png', 5). If no resolution is specified then the script will use the highest resolution avaliable.")

args = parser.parse_args()

if not args.source:
    print("Error: You have not specified a source!")
    sys.exit()
else:
    if not os.path.isdir(args.source):
        print("Error: Your source needs to be a directory!")
        sys.exit()
    else:
        PATH = args.source
        RESLIST = []
        for folder in os.listdir(PATH):
            if os.path.isdir(os.path.join(PATH, folder)):
                for file in os.listdir(os.path.join(PATH, folder)):
                    if file[0] not in RESLIST:
                        RESLIST.append(file[0])
                break
        
        RESLIST.sort()

        RES = RESLIST[-1]
        if args.res:
            if args.res not in RESLIST:
                print(f"Error: {args.res} is not a valid resolution!")
                sys.exit()
            else:
                RES = args.res
        
        RES = int(RES)
        builder.ImageBuilder(PATH, RES)
