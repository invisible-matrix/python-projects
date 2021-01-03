from tkinter import *
import random, string


# setting the window
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("MATRIX-PASSWORD GENERATOR")

Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 ').pack()

# getting the lenth of password from the user 
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 6, to_ = 32 , textvariable = pass_len , width = 15).pack()

# function to generate the password by given length 
pass_str = StringVar()
def Generator():
    password = ''

    
    for y in range(pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
    
    
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

# to display the password
Entry(root , textvariable = pass_str).pack()


root.mainloop()

# this project is done by spyder IDE ,if using the project save it in .py format .