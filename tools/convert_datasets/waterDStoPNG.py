# Copyright (c) OpenMMLab. All rights reserved.
import argparse
import glob
import math
import os
import os.path as osp
from PIL import Image
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert water dataset to png format')
    parser.add_argument('dataset_path', help='water dataset folder path')
    parser.add_argument('--tmp_dir', help='path of the temporary directory')
    parser.add_argument('-o', '--out_dir', help='output path')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    dataset_path = args.dataset_path
    if args.out_dir is None:
        out_dir = osp.join(dataset_path, 'water')
    else:
        out_dir = args.out_dir

    print('Making directories...')
#    mmcv.mkdir_or_exist(osp.join(out_dir, 'train', 'images'))
#    mmcv.mkdir_or_exist(osp.join(out_dir, 'train', 'gt'))
#    mmcv.mkdir_or_exist(osp.join(out_dir, 'val', 'images'))
#    mmcv.mkdir_or_exist(osp.join(out_dir, 'val', 'gt'))

    print('Find the data', dataset_path)

    for root, dirs, files in os.walk(dataset_path, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".png"):
                    print
                    "A png file already exists for %s" % name
                # If a jpeg is *NOT* present, create one from the tiff.
                else:
                    outfile = os.path.splitext(os.path.join(root, name))[0] + ".png"
                    im = Image.open(os.path.join(root, name))
                    print
                    "Generating png for %s" % name
                    im.thumbnail(im.size)
                    im.save(outfile, "PNG")
                    os.remove(os.path.join(root, name))

    print('Removing the temporary files...')

    print('Done!')


if __name__ == '__main__':
    main()
