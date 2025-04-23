from PIL import Image

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PIL
from PIL import Image
import arcade
import os
import datetime

exts = PIL.Image.registered_extensions()
supported_extensions = {ex for ex, f in exts.items() if f in Image.OPEN}
print(supported_extensions)