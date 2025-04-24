from tkinter.filedialog import askopenfilename
import PIL
from PIL import Image
import datetime
import arcade as a
import configparser

choose = None
config = configparser.ConfigParser()
config.read('lang.ini')
fontee = a.load_font('font/PixelifySans-VariableFont_wght.ttf')
exts = PIL.Image.registered_extensions()
supported_extensions = [ex for ex, f in exts.items() if f in Image.OPEN]
ses = ''
for i in supported_extensions:
    ses = ses + i
lang = config['LANG']['lang']
print(lang)
def choosefile():
    global file
    tempfile = askopenfilename()
    sup = False
    for i in supported_extensions:
        if tempfile.endswith(i):
            sup = True
    if sup == True:
        file = tempfile
    else:
        print("Неправилный формат!")
        exit(0)


def convert():
    global file, choose
    typeshi = input(f'{'Тип файла?' if lang == 'rus' else 'What type do you need?'} PNG (1), JPG (2), GIF (3), BMP (4) TIFF (5) ')
    if typeshi == '1' or typeshi == '1' or typeshi == '4' or typeshi == '5':
        pallete = 'RGBA'
    else:
        pallete = 'RGB'
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

        print("Не введен доступный." if lang == 'rus' else "Wrong input")
        exit(0)
    try:
        if file != None:
            img = Image.open(file)
            im = img.convert(pallete)
            im.save(f'converted {datetime.datetime.now()}.{mode}')
            choose = 0
        else:
            return
        choose = 0
    except BaseException as e:
        print(f"Ошибка! Файл не конвертирован! Ошибка: {e}" if lang == 'rus' else f'Error! {e}')
        choose = 0

while choose !=  3:
    try:
        choose = int(input('Convert an image (1) Check suppoerted extensions for input (2) Exit (3)' if lang == 'eng' else 'Конвертировать изображение (1) Узнать форматы которые можно вставить (2) Выход (3)'))
        if not choose in range(1, 4):
            choose = 0
    except ValueError:
        print('Not a number!' if lang == 'eng' else 'Не число!')
    if choose == 1:
        choosefile()
        convert()
        exit(0)

    if choose == 2:
        print(ses)
        choose = 0
    if choose == 3:
        exit(0)



# class Button(a.Sprite):
#     def  __init__(self, id, x, y):
#         self.id = id
#         self.waiting = False
#         self.delay = 0
#         if id == 1:
#             self.sp = 'imgs/png.png'
#             self.spc = 'imgs/pngc.png'
#         elif id == 2:
#             self.sp = 'imgs/jpg.png'
#             self.spc = 'imgs/jpgc.png'
#         elif id == 3:
#             self.sp = 'imgs/gif.png'
#             self.spc = 'imgs/gifc.png'
#         elif id == 4:
#             self.sp = 'imgs/bmp.png'
#             self.spc = 'imgs/bmpc.png'
#         elif id == 5:
#             self.sp = 'imgs/tiff.png'
#             self.spc = 'imgs/tiffc.png'
#         elif id == 6:
#             if lang == 'eng':
#                 self.sp = 'imgs/chooseeng.png'
#                 self.spc = 'imgs/chooseengc.png'
#             else:
#                 self.sp = 'imgs/choosserus.png'
#                 self.spc = 'imgs/chooserusc.png'
#         super().__init__(self.sp, 3, x, y)
#     def click(self):
#         if id == 6:
#             choosefile()
#         else:
#             convert(str(self.id))
#         self.waiting = True
#         self.texture = self.spc
# class MainWin(a.Window):
#     def __init__(self):
#         self.w = 600
#         self.h = 800
#         self.search = Button(6, 100, 600)
#         self.png = Button(1, 70, 150)
#         self.jpg = Button(2, 190, 150)
#         self.gif = Button(3, 310, 150)
#         self.bmp = Button(4, 430, 150)
#         self.tiff = Button(5, 550, 150)
#         self.buttonlist = a.SpriteList()
#         self.buttonlist.append(self.png)
#         self.buttonlist.append(self.search)
#         self.buttonlist.append(self.jpg)
#         self.buttonlist.append(self.bmp)
#         self.buttonlist.append(self.tiff)
#         self.buttonlist.append(self.gif)
#
#         super().__init__(self.w, self.h, 'converter', antialiasing= False)
#     def on_draw(self):
#         self.clear()
#         a.set_background_color(a.color.WHITE)
#         self.buttonlist.draw()
#     def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
#         for btn in self.buttonlist:
#             if btn.collides_with_point((x,y)):
#                 choosefile()
# win = MainWin()
# a.run()
#


