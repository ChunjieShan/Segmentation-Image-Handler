#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
import sys


class SegmentationImageHandler():
    """A segmentation image handler"""
    def __init__(self, txt_file, image_dir, mask_dir):
        """TODO: to be defined.

        :txt_file: The goal txt file which contains image and label path that you want to write in.
        :image_dir: The image dataaset directory.
        :mask_dir: The Mask dataset directory.

        """
        self._image_dir = image_dir
        self._mask_dir = mask_dir
        self._txt_file = txt_file
        self._image_list = []
        self._mask_list = []
        self.generalize_image_list()
        self.generalize_mask_list()
        self.generalize_list()
        print(self._image_dir)
        print(self._image_list[0])
        print(self._mask_list[0])
        print(len(self._mask_list))

    def generalize_image_list(self):
        for root, dirs, files in os.walk(self._image_dir):
            self._image_list = files
            self._image_list.sort()

    def generalize_mask_list(self):
        for root, dirs, files in os.walk(self._mask_dir):
            self._mask_list = files
            self._mask_list.sort()

    def generalize_list(self):
        txt_file = open(self._txt_file, 'w')
        for i in range(0, len(self._image_list)):
            txt_file.write(self._image_list[i] + ' ' + self._mask_list[i] +
                           '\n')


if __name__ == "__main__":
    txt_file = './train_shuffle.txt'
    os.system("touch train_shuffle.txt")
    image_dir = sys.argv[1]
    mask_dir = sys.argv[2]

    SegmentationImageHandler(txt_file, image_dir, mask_dir)
