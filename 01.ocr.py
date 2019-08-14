#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

# open image
image = Image.open('ocr_img.jpg')
code = pytesseract.image_to_string(image, lang='chi_sim')  #eng
print(code)