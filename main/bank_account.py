# Program to make a simple 
# login screen 

import bank_menu as menu

import tkinter as tk

root=tk.Tk()

# setting the windows size
root.geometry("300x300")

# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()


# defining a function that will
# get the name and password and 
# print them on the screen
def submit():

	name=name_var.get()
	password=passw_var.get()
	
	print("The name is : " + name)
	print("The password is : " + password)
	
	name_var.set("")
	passw_var.set("")

	if name == "hello" and password == "1234":
		root.destroy()
		menu.mainmenu()
	

title_label = tk.Label(root, text='American Banking Incorperated', fg='red')	
# creating a label for 
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
title_label.grid(row=0, column=1)
name_label.grid(row=1,column=0)
name_entry.grid(row=1,column=1)
passw_label.grid(row=2,column=0)
passw_entry.grid(row=2,column=1)
sub_btn.grid(row=3,column=1)

# performing an infinite loop 
# for the window to display
root.mainloop()
