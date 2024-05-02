from tkinter import *
from tkinter import messagebox
import tempfile
import os

def validate_numbers_only(x : str):
    return x.isdigit()

def xmain():

    root=Tk()
    vcmd = (root.register(validate_numbers_only), '%P')

    root.title('Connect Now')
    root.geometry('1280x720')


    #=====================variables===================
    Title2=StringVar()
    Description2=StringVar()
    Hours2=StringVar()
    Minutes2=StringVar()
    Link2=StringVar()

    cb=StringVar()
    cw=StringVar()
    cr=StringVar()
    cg=StringVar()
    total_cost=StringVar()
    # ===========Function===============







    def receipt():
        textarea.delete(1.0,END)
        textarea.insert(END,' \tEvent details\t  ')
        textarea.insert(END,f'\nTitle\t\t{Title2.get()}\t  {cb.get()}')
        textarea.insert(END,f'\n\nDescription\t\t{Description2.get()}\t  {cw.get()}')
        textarea.insert(END,f'\n\nHours\t\t{Hours2.get()}\t  {cr.get()}')
        textarea.insert(END,f'\n\nMinutes\t\t{Minutes2.get()}\t  {cg.get()}')

        textarea.insert(END,f'\nLink\t\t{Link2.get()}\t{total_cost.get()}')
        textarea.insert(END, f"\n================================")


    def print():
        q=textarea.get('1.0','end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'Print')


    def reset():
        textarea.delete(1.0,END)
        Title2.set(0)
        Description2.set(0)
        Hours2.set(0)
        Minutes2.set(0)
        Link2.set(0)

        cb.set('')
        cw.set('')
        cr.set('')
        cg.set('')
        total_cost.set('')

    def exit():
        if messagebox.askyesno('Exit','Do you really want to exit'):
            root.destroy()

    title=Label(root,pady=5,text="Connect Now",bd=12,bg="grey",fg='white',font=('times new roman', 35 ,'bold'),relief=GROOVE,justify=CENTER)
    title.pack(fill=X)

    #===============Event Details=================
    F1 = LabelFrame(root, text='Post your event', font=('times new romon', 18, 'bold'), fg='black',bg="grey",bd=15,relief=RIDGE)
    F1.place(x=5, y=90,width=800,height=500)

    #=====================Heading==========================


    n=Label(F1, text='Event Details', font=('Helvetic',25, 'bold'), fg='black',bg='grey')
    n.grid(row=0,column=1,padx=30,pady=15)



    #===============Event Details Area============


    Title1=Label(F1, text='Title', font=('times new rommon',20, 'bold'), fg='black',bg="grey")
    Title1.grid(row=1,column=0,padx=20,pady=15)
    b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Title2,justify=CENTER)
    b_txt.grid(row=1,column=1,padx=20,pady=15)


    Description1=Label(F1, text='Description', font=('times new rommon',20, 'bold'), fg='black',bg="grey")
    Description1.grid(row=2,column=0,padx=20,pady=15)
    w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Description2,justify=CENTER)
    w_txt.grid(row=2,column=1,padx=20,pady=15)


    Hours1=Label(F1, text='Hours', font=('times new rommon',20, 'bold'), fg='black',bg="grey")
    Hours1.grid(row=3,column=0,padx=20,pady=15)
    r_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Hours2,justify=CENTER, validate="all", validatecommand=vcmd )
    r_txt.grid(row=3,column=1,padx=20,pady=15)


    Minutes1=Label(F1, text='Minutes', font=('times new rommon',20, 'bold'), fg='black',bg="grey")
    Minutes1.grid(row=4,column=0,padx=20,pady=15)
    g_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Minutes2,justify=CENTER, validate="all", validatecommand=vcmd)
    g_txt.grid(row=4,column=1,padx=20,pady=15)


    t=Label(F1, text='Link', font=('times new rommon',20, 'bold'), fg='black',bg="grey")
    t.grid(row=5,column=0,padx=20,pady=15)
    t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=Link2,justify=CENTER)
    t_txt.grid(row=5,column=1,padx=20,pady=15)


    #=====================Posting area====================
    F2=Frame(root,relief=GROOVE,bd=10)
    F2.place(x=820,y=90,width=430,height=500)
    bill_title=Label(F2,text='Events',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
    scrol_y=Scrollbar(F2,orient=VERTICAL)
    scrol_y.pack(side=RIGHT,fill=Y)
    textarea=Text(F2,font='arial 15',yscrollcommand=scrol_y.set)
    textarea.pack(fill=BOTH)
    scrol_y.config(command=textarea.yview)



    #=====================Buttons========================
    F3 =Frame(root,bg='grey',bd=15,relief=RIDGE)
    F3.place(x=5, y=590,width=1270,height=120)



    btn2 = Button(F3, text='Publish', font='arial 25 bold', padx=5, pady=5, bg='white',fg='black',width=10,command=receipt)
    btn2.grid(row=0,column=1,padx=10,pady=10)



    btn4 = Button(F3, text='Refresh', font='arial 25 bold', padx=5, pady=5, bg='white',fg='black',width=10,command=reset)
    btn4.grid(row=0,column=3,padx=10,pady=10)

    btn5 = Button(F3, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='white',fg='black',width=10,command=exit)
    btn5.grid(row=0,column=4,padx=10,pady=10)





    root.mainloop()



# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="grey").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="grey", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def clear_windows_and_start_main():
    global main_screen
    global xmain
    main_screen.destroy()
    xmain()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=clear_windows_and_start_main).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting/popup



def delete_login_success():
    login_success_screen.destroy()



def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Connect Now Login", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()



