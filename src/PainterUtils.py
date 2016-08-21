"""
Created on Jun 30, 2015

@author: Erwin Rossen
"""

import os.path
from PIL import Image, ImageChops


def append_default_extension(filename, default_extension='.png'):
    """If a filename has no extension yet, add the default extension to it"""
    if '.' in filename:
        return filename
    else:
        return filename + default_extension


def get_img_dir(dir_name):
    """Determine the correct image directory"""
    src_dir = os.path.dirname(__file__)
    folder = os.path.join(src_dir, '..', 'img', dir_name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


def flags_dir():
    """Determine the flags directory"""
    src_dir = os.path.dirname(__file__)
    flags_dir = os.path.join(src_dir, '..', 'img', 'flags')
    if not os.path.exists(flags_dir):
        os.makedirs(flags_dir)
    return flags_dir


def flag_drawings_dir():
    """Determine the flag_drawings directory"""
    flag_drawings_dir = get_img_dir('flag_drawings')
    if not os.path.exists(flag_drawings_dir):
        os.makedirs(flag_drawings_dir)
    return flag_drawings_dir


def read_flag_drawing(filename_in):
    """Open an image from a file in the flag_drawings directory"""
    full_filename_in = os.path.join(flag_drawings_dir(), append_default_extension(filename_in))
    img = Image.open(full_filename_in)
    return img


def write_flag_drawing(img, filename_out):
    """Write an image to a file in the flag_drawings directory"""
    save_img(img, 'flag_drawings', filename_out)


def save_img(img, dirname, filename, cmyk=False):
    """Save an image to a file in the indicated img directory"""
    full_img_dir = get_img_dir(dirname)
    if cmyk:
        # Transform image to full color CMYK before saving
        img_cmyk = img.convert('CMYK')
        full_filename_out = os.path.join(full_img_dir, append_default_extension(filename, '.pdf'))
        img_cmyk.save(full_filename_out, quality=95, optimize=True)
    else:
        # Save directly to RGB
        full_filename_out = os.path.join(full_img_dir, append_default_extension(filename))
        img.save(full_filename_out, quality=95, optimize=True)


def trim_img(img):
    """Trim the edges of an image"""
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img


if __name__ == '__main__':
    pass
