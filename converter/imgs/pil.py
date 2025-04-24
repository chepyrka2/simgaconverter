from PIL import Image
i1 = Image.open('chooseeng.png')
g1 = i1.convert('LA')
g1.save('chooseengc.png')