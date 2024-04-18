#Project description for student: In this project you will create an online banking program. 
#Users need to have an account number and PIN to identify themselves as owners of an account. 
#Once users get into the system they will have standard options: check balance, deposit, and withdraw.
#Additionally, a new user or bank administrator can also create a new account, close account, 
#and modify an account (such as edit name, PIN, or any other personal identification required to open an account).

import mysql.connector


# Program to make a simple 
# login screen 


import tkinter as tk

root=tk.Tk()

# setting the windows size
root.geometry("300x300")

def submit():
	name=name_var.get()
	password=passw_var.get()			
	print("The name is : " + name)
	print("The password is : " + password)
	name_var.set("")
	passw_var.set("")
	menu_screen(name, password)



# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
# defining a function that will
# get the name and password and 
# print them on the screen

title_label = tk.Label(root, text='American Banking Incorperated', fg='red')	
# creating a label for 
# name using widget Label
name_label = tk.Label(root, text = 'Username ID', font=('calibre',10, 'bold'))

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

menu_screen_label = tk.Label(root, text='American Banking Incorperated', fg='red', font=('caibre',20,'bold'))
account_name = tk.Label(root, text='name', fg='red', font=('caibre',10,'bold'))
account_number = tk.Label(root, text='number:', fg='red', font=('caibre',10,'bold'))
account_pin = tk.Label(root, text='pin:', fg='red', font=('caibre',10,'bold'))
account_balance = tk.Label(root, text='balance:', fg='red', font=('caibre',10,'bold'))

withdrawal_button=tk.Button(root, text='withdraw')
deposit_button=tk.Button(root, text='deposit')
create_account=tk.Button(root, text='new account')
delete_account=tk.Button(root, text='delete account')

def title_menu():
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




def menu_screen(user_Id, user_Pin):
	connection = mysql.connector.connect(user = 'newuser', database = 'sample', password = 'truepassword')
	cursor = connection.cursor()
	testQuery = (f"select * from user_account where account_pin = {user_Pin} and account_number = {user_Id}")
	cursor.execute(testQuery)

	for item in cursor:
		print(item)

	item = str(item)
	print(item)
	query_split = item.split(",")
	print(query_split)

	for original_object in query_split:
		print(original_object)
		object_index = query_split.index(original_object)
		query_split.pop(object_index)
		object = original_object.replace("'", "").replace(" ","").replace("(","").replace(")","")
		query_split.insert(object_index, object)
#		query_split.insert(object_index, )
		print(object)
	print(query_split)

	cursor.close()
	connection.close()

	title_label.destroy()
	name_label.destroy()
	name_entry.destroy()
	passw_label.destroy()
	passw_entry.destroy()
	sub_btn.destroy()

	root.geometry("400x400")
	root.configure(bg='white')

	menu_screen_label.pack(anchor='center')
	account_name.pack(anchor='center')
	account_pin.pack(anchor='center')
	account_balance.pack(anchor='center')



#	account_name.configure(text= user_account_name)

	delete_account.pack(side='bottom')
	create_account.pack(side='bottom')
	withdrawal_button.pack(side='bottom')
	deposit_button.pack(side='bottom')

#	menu_screen_label.configure(width=)
	#access and create account

	root.mainloop()
title_menu()