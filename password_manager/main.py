from tkinter import *
from tkinter import messagebox



def save():
  website=website_entry.get()
  email=email_entry.get()
  password=password_entry.get()
  
  if len(website)==0 or len(password)==0:
    messagebox.showerror(title="Oops",message="Please make sure all entries are filled!!")
  else:
    is_ok=messagebox.askokcancel(title=website,message=f"These are the detailes entered:\nEmail:{email}"
                          f"\nWebsite:{website}\nPassword:{password}\nIs it okay to save?")
    if is_ok:
      with open("password_manager\data.txt","a") as file:
        file.write(f"{website}|{email}|{password}")
        
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        
      

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
img=PhotoImage(file="password_manager\lock.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website")
website_label.grid(column=0,row=1)
email_label=Label(text="Email")
email_label.grid(column=0,row=2)
password_label=Label(text="Password")
password_label.grid(column=0,row=3)

website_entry=Entry(width=53)
website_entry.grid(row=1,column=1,columnspan=2)
email_entry=Entry(width=53)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"shreyabharadwaj039@gmail.com")
password_entry=Entry(width=53)
password_entry.grid(row=3,column=1)


add_button=Button(text="Add",width=45,command=save)
add_button.grid(row=4,column=1)




window.mainloop()