from tkinter import *
import  random
from PIL import Image, ImageTk

root = Tk()
root.geometry('400*400')
root.title("Dice Game")
Label(root, text = '').pack()
Label(root, text= 'Hi from nandha',font = ('Helvetica', 12), fg= 'black', bg = 'light green' ).pack()

dice = ['A1.png', 'A2.png', 'A3.png', 'A4..png', 'A5.png', 'A6.png']
diceimg = ImageTk.PhotoImage(Image.open(random.choice(dice)))
imgla = Lable(root, image = diceimg)
imgla.image = diceimg

Imgla.pack(expand = True)
def rolling_dice():
    diceimg = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    imgla.configure(image=DiceImage)
    # keep a reference
    imgla.image = DiceImage
# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)


button.pack( expand=True)

root.mainloop()

