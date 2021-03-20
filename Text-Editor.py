from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os,sys
import win32print
import win32api

root =Tk()
root.title('Pages!')
root.iconbitmap('E:/mohans docs/feather.ico')
root.geometry("1070x665")


#set variable for open file
global open_status_name
open_status_name = False

global selected
selected = False

# create new  file function
def new_file():
    my_text.delete("1.0",END)
    #update status bar
    root.title('New File - Pages!')
    status_bar.config(text="New File               ")
    open_status_name = False
    
    
# create open file function
def open_file():
    #delete previous text
    my_text.delete("1.0",END)
    
    #grab filename
    text_file =filedialog.askopenfilename(initialdir="E:/python/",title="Open File",filetypes=(("Text Files","*.txt"),("HTML Files", "*.html"),("All Files", "*.*")))   
    
    # check to see if there is a file name
    if text_file:
        #make filenameglobal so we can access it later
        global open_status_name
        open_status_name = text_file
    # update status bar
    name= text_file
    status_bar.config(text=f'{name}     ') 
    name.replace("C:/python/","")
    root.title(f'{name} - Pages!')      

    #open the file
    text_file = open(text_file, "r")
    stuff = text_file.read()
    #add file to text box
    my_text.insert(END,stuff) 
    # close open file
    text_file.close() 
    
# save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="c:/python/",title="Save File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("All Files","*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved:{name}     ') 
        name = name.replace("C:/python/","")
        root.title(f'{name} - Pages!')
        
        #save file 
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0,END))
        #close the file
        text_file.close()
        
# save file function
def save_file():
    
    if open_status_name:
        #save file 
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0,END))
        #close the file
        text_file.close()
        status_bar.config(text=f'Saved:{open_status_name}     ') 
    else:
        save_as_file()
         
        
# def cut function
def cut_text(e):
    global selected 
    # check if keyboard shortcut used  
    if e:
        selected = root.clipboard_get()
    else:    
        if my_text.selection_get():
           # grab selected text from text box
           selected = my_text.selection_get()
           # delete selectes text from text box
           my_text.delete("sel.first","sel.last")
           #clear clipboard and append the selected 
           root.clipboard_clear()
           root.clipboard_append(selected)
        
        
    

# def copy function
def copy_text(e):
    global selected
    # check to see if we use keyboard shorcuts
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        # grab selected text from text box
        selected = my_text.selection_get()
        #clear clipboard and append the selected 
        root.clipboard_clear()
        root.clipboard_append(selected)






# def paste function
def paste_text(e):
    global selected
    # check to see if key bord shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        
        if selected:
           position = my_text.index(INSERT)
           my_text.insert(position,selected)
           
           
# bold text
def bold_text():
    bold_font = font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight="bold")
    
    # configure a  tag
    my_text.tag_configure("bold",font=bold_font)
    
    # current tags
    current_tags = my_text.tag_names("sel.first")
    
    # if statment to see whether bold is aldredy used 
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first","sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

# italics 
def italic_text():
    italics_font = font.Font(my_text,my_text.cget("font"))
    italics_font.configure(slant="italic")
    
    # configure a  tag
    my_text.tag_configure("italic",font=italics_font)
    
    # current tags
    current_tags = my_text.tag_names("sel.first")
    
    # if statment to see whether bold is aldredy used 
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first","sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")



#change selected text color
def color_text():
    #pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
       
    
       color_font = font.Font(my_text,my_text.cget("font"))
   
    
    # configure a  tag
       my_text.tag_configure("colored",font=color_font,foreground=my_color)
    
    # current tags
       current_tags = my_text.tag_names("sel.first")
    
    # if statment to see whether bold is aldredy used 
       if "colored" in current_tags:
         my_text.tag_remove("colored", "sel.first","sel.last")
       else:
         my_text.tag_add("colored", "sel.first", "sel.last")


# change  bg color
def bg_color():
     my_color = colorchooser.askcolor()[1]
     if my_color:
         my_text.config(bg=my_color)

# all text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
         my_text.config(fg=my_color)
    
# print file  function
def print_file():
    
    #grab filename
    file_to_print =filedialog.askopenfilename(initialdir="E:/python/",title="Open File",filetypes=(("Text Files","*.txt"),("HTML Files", "*.html"),("All Files", "*.*")))
    if file_to_print:
        win32api.ShellExecute(0,"print",file_to_print,None,".",0)
# create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

#create main frame
my_frame=Frame(root)
my_frame.pack(pady=5)

#create our scrollbox for the text box
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

# horizontal scroll bar
hor_scroll = Scrollbar(my_frame,orient = 'horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)


# create text box
my_text=Text(my_frame,width=95,height=25,font=("helivetica,12"),undo = True,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack()

#configure thr scroll
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)  

#create menu
my_menu=Menu(root)
root.config(menu=my_menu)

# add file menu
file_menu =Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save As..",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print file",command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)  # destroy is used for quit button


#add edit menu
edit_menu =Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Undo",command=my_text.edit_undo,accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo",command=my_text.edit_redo,accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Cut",command=lambda : cut_text(False),accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy",command=lambda : copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste",command=lambda : paste_text(False),accelerator="(Ctrl+v)")

#add colour menu
color_menu =Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Colors",menu=color_menu)
color_menu.add_command(label="change selected text",command=color_text)
color_menu.add_command(label="All text",command=all_text_color)
color_menu.add_command(label="Background",command=bg_color)
#add status bar to bottom of app
status_bar = Label(root,text ='ready     ',anchor=E)
status_bar.pack(fill=X,side = BOTTOM,ipady=10)




#edit bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)
                
# create buttons
# bold button
bold_button=  Button(toolbar_frame,text="Bold",command = bold_text)
bold_button.grid(row=0,column=0,sticky=W,padx=3)
# italics button
italics_button=  Button(toolbar_frame,text="Italics",command = italic_text)
italics_button.grid(row=0,column=1,padx=3)
# undo / redo button
undo_button=  Button(toolbar_frame,text="Undo",command = my_text.edit_undo)
undo_button.grid(row=0,column=2,padx=3)
redo_button=  Button(toolbar_frame,text="Redo",command = my_text.edit_redo)
redo_button.grid(row=0,column=3,padx=3)

#text colour
color_text_button  = Button(toolbar_frame,text="Text color",command=color_text)
color_text_button.grid(row=0,column=4,padx=3)

root.mainloop()



# here i have used win32print & win32api
# this is used to print the text file so in order to use this u have to set a default printer to your computer 
# you can set it using the control panel








