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
        description='Convert water dataset to png format')
    parser.add_argument('dataset_path', help='water dataset folder path')
    parser.add_argument('--tmp_dir', help='path of the temporary directory')
    parser.add_argument('-o', '--out_dir', help='output path')
    args = parser.parse_args()
    return args

def convert_to_train_id(f):
    label = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    id_to_trainid = {
        64: 2 
    }
    label_copy = 1 * np.ones(label.shape, dtype=np.uint8)
    for k, v in id_to_trainid.items():
        k_mask = label == k
        label_copy[k_mask] = v
        n = int(np.sum(k_mask))
    cv2.imwrite(f, label_copy)
    pass

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
            convert_to_train_id(os.path.join(root, name))
            #os.remove(os.path.join(root, name))

    print('Removing the temporary files...')

    print('Done!')


if __name__ == '__main__':
    main()
