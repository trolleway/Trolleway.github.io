#!/usr/bin/python
# -*- coding: utf-8 -*-

from run import Website_generator

if __name__ == "__main__":
    processor = Website_generator()
    processor.json_from_dir('/opt/storage/2021/2021-08_stupino','https://trolleway.com/storage')