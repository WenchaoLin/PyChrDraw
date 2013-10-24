#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: 09.10.2013
#@author: Aleksey Komissarov
#@contact: ad3002@gmail.com

import sys
sys.path.append("c:/Users/Master/Dropbox/workspace")
sys.path.append("/Users/akomissarov/Dropbox/workspace")
import Image, ImageDraw, ImageFont
import yaml

# fix for Windows-specific bug with png extension registering
from PIL.PngImagePlugin import _save, PngImageFile, _accept
Image.register_open("PNG", PngImageFile, _accept)
Image.register_save("PNG", _save)
Image.register_extension("PNG", ".png")
Image.register_mime("PNG", "image/png")

from PyChrDraw.draw_chromosome import *

if __name__ == '__main__':

        with open("human_chrs.yaml") as fh:
                settings = yaml.load(fh)

        chrs = settings["chromosome_sizes"]
        width = settings["canvas"]["width"]
        height = settings["canvas"]["height"]
        im = Image.new("RGBA", (width, height), "#ffffff")
        draw = ImageDraw.Draw(im)


        files = settings["orphans"]
        name2chr = settings["ncbi_names"]
        for file_name in files:
                bands2chr, max_value = load_bands_from_bed(file_name, last_column_color=True)
                print max_value
                new_bands2chr = {}
                for key in bands2chr:
                    new_key = key.split("|")[3]
                    if new_key in name2chr:
                        new_key = name2chr[new_key]
                        print key, "-->", new_key, "Size:", len(bands2chr[key])
                    else:
                        print "No key", new_key, "Size", len(bands2chr[key])
                new_bands2chr[new_key] = bands2chr[key]
                bands2chr = new_bands2chr
                exit()


        # x = settings["canvas"]["left_corner"]
        # y = settings["canvas"]["top_corner"]
        # keys = settings["chromosome_order"]
        # real_chr_size = settings["canvas"]["real_chr_size"]
        # space_between_chr = settings["canvas"]["space_between_chr"]
        # chr_width = settings["canvas"]["chr_width"]

        # mouse_chrs, bands2chr = normalize_chromosome_sizes(mouse_chrs, real_chr_size, bands=bands2chr)

        # for key in keys:
        #         length = mouse_chrs[key]
        #         draw_horizontal_chromosome(draw, x, y, length, bands=bands2chr[key], chr_width=chr_width, name=key, scale=1, stars=None)
        #         y += space_between_chr
        # im.save("output_file.png")