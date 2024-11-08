import mysql.connector
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import joblib

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()
class Login_Window:
    def __init__(self,master):
        self.master= master
        self.master.title("Login")
        master.geometry('1200x600')
        master.iconbitmap('Images\heartIcon.ico')
        master_width = 1200
        master_height= 600
        master.geometry(f"{master_width}x{master_height}+{30}+{20}")

        #--------------Image---------------
        self.my_pic = Image.open("Images/img7.jpg")

        # Resize Image
        self.resized = self.my_pic.resize((1300,800),Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resized)
        self.bg_image=Label(self.master,image=self.new_pic).place(x=0,y=0,relwidth=1,relheight=1)

        #---------------Login-----------------
        Frame_login=Frame(self.master,bg="white").place(x=100,y=120,height=340,width=450)

        title = Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",
                      bg="white").place(x=110,y=120)

        lbl_user = Label(Frame_login,text="Email",font=("times new roman",20),fg="black",
                                bg="white").place(x=115,y=220)

        self.txt_user=Entry(Frame_login,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_user.place(x=115,y=260,width=390,height=30)

        #----------------Password----------------
        lbl_pass = Label(Frame_login,text="Password",font=("times new roman",20),fg="black",
                         bg="white").place(x=115,y=300)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15,"bold"),
                            bg="lightgray",show="*")
        self.txt_pass.place(x=115,y=340,width=390,height=30)

        #--------------Forgot Password Button-----------
        #forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",
                          #bg="white",fg="#d77337",bd=0,font=("times new roman",12),
                          #activeforeground="green",activebackground="white",).place(x=112,y=380)

        #-----------------Login Button-------------------
        Login_btn=Button(self.master,command=self.login_fun,cursor="hand2",text="Login",fg="white",
                         bg="#d77337",font=("times new roman",20),activebackground="green4",
                           activeforeground="black").place(x=290,y=430)

        #----------------Sign Up Button-----------------
        Register_btn = Button(Frame_login, text="Sign up", cursor="hand2",command=self.register_window,
                            bg="white", fg="#d77337", bd=0, font=("times new roman", 12),
                            activeforeground="green", activebackground="white", ).place(x=450, y=380)
    def register_window(self):
        self.new_window=Toplevel(self.master)
        self.app=Register(self.new_window)

    def login_fun(self):

        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.master)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Jarus@2k0", database="sys")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass =%s ",(
                                                                    self.txt_user.get(),
                                                                    self.txt_pass.get(),
            ))

            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","Invalid User Name & Password")
            else:
                open_main= messagebox.askyesno("YesNo","Do you wnat to Log in")
                if open_main>0:
                    self.new_window= Toplevel(self.master)
                    #self.app = signature(self.new_window)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()



# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    REGISTER    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
class Register:
    def __init__ (self,root):
        self.root = root
        self.root.title("Register")
        root.iconbitmap('Images\heartIcon.ico')
        master_width = 840
        master_height = 500
        root.geometry(f"{master_width}x{master_height}+{200}+{85}")
        #root.resizable(False,False)

        #======================Variables====================
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_con_pass = StringVar()


        # --------------Image---------------
        self.my_pic = Image.open("Images/img8.jpg")

        # Resize Image
        self.resized = self.my_pic.resize((1300,800), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resized)
        self.bg_image = Label(self.root, image=self.new_pic).place(x=0, y=0, relwidth=1, relheight=1)


        # ---------------Login-----------------
        Frame_Register = Frame(self.root, bg="white").place(x=100,y=120, height=300, width=655)

        #---------------Frame(Register)---------------
        title = Label(self.root, text="Register Here", font=("Impact", 30, "bold"), fg="#d77337",
                      bg="white").place(x=110,y=120)

        #----------------Name------------------
        lbl_name = Label(self.root,text="Full Name", font=("times new roman", 20), fg="black",
                         bg="white").place(x=115,y=220)
        self.txt_name = Entry(self.root , textvariable=self.var_name,
                              font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_name.place(x=115,y=260,width=300,height=30)

        #----------------Email------------------
        lbl_email = Label(self.root, text="Email",font=("times new roman", 20), fg="black",
                         bg="white").place(x=440,y=220)
        self.email_name = Entry(self.root, textvariable=self.var_email,
                                font=("times new roman", 15, "bold"), bg="lightgray")
        self.email_name.place(x=440,y=260,width=300,height=30)

        # ----------------Password------------------
        lbl_pass = Label(self.root, text="Password", font=("times new roman", 20), fg="black",
                          bg="white").place(x=115,y=300)

        self.pass_name = Entry(self.root,textvariable=self.var_pass,
                               font=("times new roman", 15, "bold"), bg="lightgray")
        self.pass_name.place(x=115,y=340,width=300,height=30)

        # ----------------Confirm Password------------------
        lbl_Con_pass = Label(self.root, text="Confirm Password", font=("times new roman", 20), fg="black",
                         bg="white").place(x=440,y=300)

        self.Con_pass = Entry(self.root, textvariable=self.var_con_pass,
                               font=("times new roman", 15, "bold"), bg="lightgray")
        self.Con_pass .place(x=440,y=340,width=300,height=30)

        # -----------------Register Button-------------------
        Register_btn = Button(self.root, cursor="hand2",command=self.register_data, text="Register", fg="white",
                           bg="#d77337", font=("times new roman", 20), activebackground="red3",
                           activeforeground="black").place(x=440, y=395)

        # -----------------LoginButton-------------------
        Login_btn = Button(self.root, cursor="hand2", command=self.return_login, text="Login Now", fg="white",
                              bg="cyan4", font=("times new roman", 20), activebackground="green4",
                              activeforeground="black").place(x=570, y=395)



    #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxFunction declarationxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    def register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_pass.get()=="" or self.var_con_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!= self.var_con_pass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Jarus@2k0",database="sys")
            my_cursor=conn.cursor()
            query = ("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","already exist",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s)",(
                                                                            self.var_name.get(),
                                                                            self.var_email.get(),
                                                                            self.var_pass.get(),
                                                                            ))
                messagebox.showinfo("Success", "Succesfully Registered", parent=self.root)
            conn.commit()
            conn.close()

    def return_login(self):
        self.root.destroy()
main()