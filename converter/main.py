from tkinter.filedialog import askopenfilename
import PIL
from PIL import Image
import datetime

exts = PIL.Image.registered_extensions()
supported_extensions = {ex for ex, f in exts.items() if f in Image.OPEN}
file = askopenfilename()
sup = False
pallete = 'RGB'
for i in supported_extensions:
    if file.endswith(i):
        sup = True


typeshi = input('Тип файла? PNG (1), JPG (2), GIF (3), BMP (4) TIFF (5) ')
if typeshi == '1' or typeshi == '1' or typeshi == '4' or typeshi == '5':
    pallete = 'RGBA'
if typeshi == '1':
    mode = 'png'
elif typeshi == '2':
    mode = 'jpg'
elif typeshi == '3':
    mode = 'gif'
elif typeshi == '4':
    mode = 'bmp'
elif typeshi == '5':
    mode = 'tiff'
else:
    print("Не введен доступный.")
    exit(0)
try:
    if sup:
        img = Image.open(file)
        im = img.convert(pallete)
        im.save(f'converted {datetime.datetime.now()}.{mode}')
    else:
        print("Не тот тип!")
except BaseException as e:
    print(f"Ошибка! Файл не конвертирован! Ошибка: {e}")