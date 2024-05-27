# Copyright (c) OpenMMLab. All rights reserved.
import argparse
import glob
import math
import os
import os.path as osp
from PIL import Image
import numpy as np
import cv2


def parse_args():
    parser = argparse.ArgumentParser(
        description='filter all non water pic')
    parser.add_argument('dataset_path', help='water dataset folder path')
    args = parser.parse_args()
    return args

def filter(root, name, idx):
    f = os.path.join(root, name)
    label = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    print(not label.any() == 2)
    if(not label.any() == 2 and not idx % 50 == 0):
        img_path = os.path.join(root[:-2],'images', name)
        print(img_path)
        os.remove(img_path)
        os.remove(f)
    pass

def main():
    args = parse_args()

    dataset_path = args.dataset_path

    print('Find the data', dataset_path)

    for root, dirs, files in os.walk(dataset_path, topdown=False):
        idx = 0
        for name in files:
            print(str(idx) + ": " + os.path.join(root, name))
            filter(root, name, idx)
            idx += 1
            #os.remove(os.path.join(root, name))

    print('Done!')


if __name__ == '__main__':
    main()
