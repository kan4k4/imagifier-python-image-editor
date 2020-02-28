from PIL import Image, ImageOps, ImageTk, ImageEnhance, ImageFilter
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

root= tk.Tk()
root.title('Image Toolbox')

canvasTop = tk.Canvas(root, width = 800, height = 100)
canvasTop.grid(row=1, column=1, columnspan=7)
canvasTop.image = ImageTk.PhotoImage(file='imagifier_logo.png')
canvasTop.create_image(100,50, image=canvasTop.image, anchor='center')

label2 = tk.Label(root,text="Brightness")
label2.config(font=('helvetica'), height=1)
label2.grid(row=6, column=12)

label3 = tk.Label(root,text="Saturation")
label3.config(font=('helvetica'), height=1)
label3.grid(row=6, column=13)

label4 = tk.Label(root,text="Contrast")
label4.config(font=('helvetica'), height=1)
label4.grid(row=6, column=14)

canvas = tk.Canvas(root, width = 900, height = 700)
canvas.grid(row=2, column=1, rowspan=16, columnspan=7)

ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")

def appendResult ():
    global result
    canvas.image = ImageTk.PhotoImage(result)
    canvas.create_image(410,250, image=canvas.image, anchor='center')

def getPhoto ():
    global photo, result
    original_photo = filedialog.askopenfilename()
    photo = Image.open(original_photo)
    result = photo
    size = (880, 620)
    result.thumbnail(size)
    appendResult()
    
upload =ttk.Button(root, text="Import File", width=50, command=getPhoto)
upload.grid(row=13, column=3, rowspan=7)

def convertBW ():
    global photo, result
    result = photo.convert('L')
    contrastUp()
    result = result.filter(ImageFilter.SHARPEN)
    appendResult()

b1 = ttk.Button(root, text="Black & White", width=15, command=convertBW)
b1.grid(row=2, column=13)

def invertPhoto ():
    global photo, result
    result = ImageOps.invert(photo)
    appendResult()

b2 = ttk.Button(root, text="Invert Colours", width=15, command=invertPhoto)
b2.grid(row=3, column=13)

def manganify ():
    global photo, result

    convertBW()
    result = result.filter(ImageFilter.CONTOUR).filter(ImageFilter.SMOOTH)
    for i in range(4):
        contrastUp()
    appendResult()

b7 = ttk.Button(root, text="Manganify", width=15, command=manganify)
b7.grid(row=4, column=13)

def brightnessUp ():
    global photo, result
    enhancer = ImageEnhance.Brightness(result)
    factor = 1.1
    result = enhancer.enhance(factor)
    appendResult()

b3 = tk.Button(root, text="+",width=2, command=brightnessUp)
b3.grid(row=5, column=12)

def brightnessDown ():
    global photo, result
    enhancer = ImageEnhance.Brightness(result)
    factor = 0.9
    result = enhancer.enhance(factor)
    appendResult()

b4 = tk.Button(root, text="-", width=2, command=brightnessDown)
b4.grid(row=7, column=12)

def saturationUp ():
    global photo, result
    enhancer = ImageEnhance.Color(result)
    factor = 1.1
    result = enhancer.enhance(factor)
    appendResult()

b8 = tk.Button(root, text="+", font=('helvetica'), width=2, command=saturationUp)
b8.grid(row=5, column=13)

def saturationDown ():
    global photo, result
    enhancer = ImageEnhance.Color(result)
    factor = 0.9
    result = enhancer.enhance(factor)
    appendResult()

b8 = tk.Button(root, text="-", font=('helvetica'), width=2, command=saturationDown)
b8.grid(row=7, column=13)

def contrastUp ():
    global photo, result
    enhancer = ImageEnhance.Contrast(result)
    factor = 1.2
    result = enhancer.enhance(factor)
    appendResult()

b3 = tk.Button(root, text="+",width=2, command=contrastUp)
b3.grid(row=5, column=14)

def contrastDown ():
    global photo, result
    enhancer = ImageEnhance.Contrast(result)
    factor = 0.9
    result = enhancer.enhance(factor)
    appendResult()

b4 = tk.Button(root, text="-", width=2, command=contrastDown)
b4.grid(row=7, column=14)

def resizePhoto ():
    global photo, result
    size = (result.size[0]/1.3,  result.size[1]/1.3)
    result.thumbnail(size)
    appendResult()

b5 = ttk.Button(root, text="Thumbnail Resize", width=15, command=resizePhoto)
b5.grid(row=8, column=13)

def resetPhoto ():
    global photo, result
    result = photo
    canvas.image = ImageTk.PhotoImage(photo)
    canvas.create_image(410,250, image=canvas.image, anchor='center')

b6 = ttk.Button(root, text="Reset", width=15, command=resetPhoto)
b6.grid(row=9, column=13)

def saveFile ():
    global result
    export = filedialog.asksaveasfilename(defaultextension='.jpg')
    result.save(export)

b7 = ttk.Button(root, text="Save File", width=15, command=saveFile)
b7.grid(row=13, column=13)

root.mainloop()
