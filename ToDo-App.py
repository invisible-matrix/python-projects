from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle


root = Tk()
root.title('ToDO-List')
root.geometry("500x500")


# define font
my_font = Font(family="Arial",size=20,)

#define frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#create list box
my_list = Listbox(my_frame,font=my_font,width=30,height=5,bg="SystemButtonFace",bd=0,fg="#464646",highlightthickness = 0,selectbackground="#a6a6a6",activestyle="none")                
my_list.pack(side=LEFT,fill=BOTH)


#stuff =["walk","buy bike","learn"]

#for item in stuff:
#    my_list.insert(END,item)

# create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

# add scroll bar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# create entry box
my_entry = Entry(root,font=("helivatica",24),width=24)
my_entry.pack(pady=20)

#create  a button frame
button_frame=Frame(root)
button_frame.pack(pady=20)

#adding functions
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)


def cross_item():
    #cross of item
    my_list.itemconfig(my_list.curselection(),fg="#dedede")
    #get rid of the bar
    my_list.selection_clear(0,END)
    

def uncross_item():
    #cross of item
    my_list.itemconfig(my_list.curselection(),fg="#464646")
    #get rid of the bar
    my_list.selection_clear(0,END)


def delete_uncross_item():
    count=0
    while count< my_list.size():
        if my_list.itemcget(count,"fg") == "#dedede":
           my_list.delete(my_list.index(count))
        else:   
           count+=1



def save_list():
    file_name = filedialog.asksaveasfilename(initialdir="E:/mohan docs/todo-data",title="Save file",
                                             filetypes=(("Dat Files","*.dat"),("All Files","*.*")))
 
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        count=0
        while count< my_list.size():
            if my_list.itemcget(count,"fg") == "#dedede":
               my_list.delete(my_list.index(count))
            else:   
               count+=1
        # grab all the stuff from the list
        stuff = my_list.get(0,END)
        
        # open the file
        output_file = open(file_name,'wb')
        
        #actual add the stuff to the file
        pickle.dump(stuff,output_file)
            
        
            
            
            
def open_list():
    file_name = filedialog.askopenfilename(initialdir="E:/mohan docs/todo-data",title="Open file",filetypes=(("Dat Files","*.dat"),("All Files","*.*")))
    
    if file_name :
        my_list.delete(0,END)
        
        # open file
        input_file = open(file_name,'rb')
        
        # load the data from the file
        stuff = pickle.load(input_file)
        
        # output stuff on the screen
        for item in stuff:
            my_list.insert(END,item)

def clear_list():
    my_list.delete(0,END)




# create menu
my_menu = Menu(root)
root.config(menu=my_menu)


#add items to the menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
# add dropdowns
file_menu.add_command(label="Save list",command=save_list)
file_menu.add_command(label="Open list",command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear list",command=clear_list)


# add buttons
delete_button = Button(button_frame,text="Delete item",command = delete_item)
add_button = Button(button_frame,text="Add item",command = add_item)
cross_button = Button(button_frame,text="Cross item",command = cross_item)
uncross_button = Button(button_frame,text="Uncross item",command = uncross_item)
delete_uncross_button = Button(button_frame,text=" delete uncross",command = delete_uncross_item)


delete_button.grid(row = 0,column = 0)
add_button.grid(row = 0,column = 1,padx=20)
cross_button.grid(row = 0,column = 2)
uncross_button.grid(row = 0,column = 3,padx=20)
delete_uncross_button.grid(row=0,column=4,padx=20)

root.mainloop()