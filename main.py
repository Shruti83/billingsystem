from tkinter import *
import math, random, os, tempfile
from tkinter import messagebox, ttk
import win32api
import win32print




class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x800+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Cafe Coffee Day", bd=12, relief=GROOVE, bg=bg_color, fg="white",font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # variables
        # bubble tea variables
        self.cap = IntVar()
        self.moc = IntVar()
        self.cafl = IntVar()
        self.cho = IntVar()
        self.cof = IntVar()

        # ice tea variables
        self.fraf = IntVar()
        self.vani = IntVar()
        self.tea = IntVar()
        self.lem = IntVar()
        self.org = IntVar()

        # button frame variables
        self.bubble_tea_price = StringVar()
        self.ice_tea_price = StringVar()
        self.cold_drinks_price=StringVar()
        self.total_cost = StringVar()
        self.total_tax = StringVar()

        # Customer details variables
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        #Cold drinks variables
        self.th=IntVar()
        self.ma=IntVar()
        self.li=IntVar()
        self.sp=IntVar()
        self.org1=IntVar()





        # Customer Details Frame
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, bg=bg_color, fg="gold", text="Customer details",
                        font=("times new roman", 15, "bold"))
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="White", font=("times new roman", 14, "bold")).grid(
            row=0, column=0, padx=10, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cphn_lbl = Label(F1, text="Customer Phone No.", bg=bg_color, fg="White",
                         font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=10, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                            column=3,
                                                                                                            pady=5,
                                                                                                            padx=10)

        c_bill_lbl = Label(F1, text="Bill No", bg=bg_color, fg="White", font=("times new roman", 14, "bold")).grid(
            row=0, column=5, padx=10, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=6, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=15, bd=7, font="arial 12 bold").grid(row=0,
                                                                                                                column=9,
                                                                                                                pady=10,
                                                                                                                padx=10)
        # Bubble Tea Frame
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bubble Tea Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=335, height=350)

        cof_lbl = Label(F2, text="CAPPUCCINO", font=("times new roman", 15, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=0, column=0, pady=10, padx=10, sticky="w")
        cof_txt = Entry(F2, width=10, textvariable=self.cap, font=("times new roman", 15, "bold"), bd=5,
                        relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        cof1_lbl = Label(F2, text="MOCHA", font=("times new roman", 15, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=1, column=0, pady=10, padx=10, sticky="w")
        cof1_txt = Entry(F2, width=10, textvariable=self.moc, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        cof2_lbl = Label(F2, text="CAFFE LATTE", font=("times new roman", 15, "bold"), fg="lightgreen",
                         bg=bg_color).grid(row=2, column=0, pady=10, padx=10, sticky="w")
        cof2_txt = Entry(F2, width=10, textvariable=self.cafl, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        cof3_lbl = Label(F2, text="CHOCOLATE", font=("times new roman", 15, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=3, column=0, pady=10, padx=10, sticky="w")
        cof3_txt = Entry(F2, width=10, textvariable=self.cho, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        cof4_lbl = Label(F2, text="COFFEE", font=("times new roman", 15, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=4, column=0, pady=10, padx=10, sticky="w")
        cof4_txt = Entry(F2, width=10, textvariable=self.cof, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        # ICE Tea Frame
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Ice Tea Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=345, y=180, width=335, height=350)

        ice_lbl = Label(F3, text="COFFEE FRAFFE", font=("times new roman", 15, "bold"), fg="lightgreen",
                        bg=bg_color).grid(row=0, column=0, pady=10, padx=10, sticky="w")
        ice_txt = Entry(F3, width=9, textvariable=self.fraf, font=("times new roman", 15, "bold"), bd=5,
                        relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        ice1_lbl = Label(F3, text="VANILIS FRAFFE", font=("times new roman", 15, "bold"), fg="lightgreen",
                         bg=bg_color).grid(row=1, column=0, pady=10, padx=10, sticky="w")
        ice1_txt = Entry(F3, width=9, textvariable=self.vani, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        ice2_lbl = Label(F3, text="TEA FRAFFE", font=("times new roman", 15, "bold"), fg="lightgreen",
                         bg=bg_color).grid(row=2, column=0, pady=10, padx=10, sticky="w")
        ice2_txt = Entry(F3, width=9, textvariable=self.tea, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        ice3_lbl = Label(F3, text="LEMON TEA", font=("times new roman", 15, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=3, column=0, pady=10, padx=10, sticky="w")
        ice3_txt = Entry(F3, width=9, textvariable=self.lem, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        ice4_lbl = Label(F3, text="ORANGE TEA", font=("times new roman", 15, "bold"), fg="lightgreen",
                         bg=bg_color).grid(row=4, column=0, pady=10, padx=10, sticky="w")
        ice4_txt = Entry(F3, width=9, textvariable=self.org, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        #drinks menu frame
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=685, y=180, width=310, height=350)

        dr_lbl = Label(F4, text="THUMBS UP", font=("times new roman", 15, "bold"), fg="lightgreen",
                        bg=bg_color).grid(row=0, column=0, pady=10, padx=10, sticky="w")
        dr_txt = Entry(F4, width=9, textvariable=self.th, font=("times new roman", 15, "bold"), bd=5,
                        relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        dr1_lbl = Label(F4, text="MAZZA", font=("times new roman", 15, "bold"), fg="lightgreen",
                         bg=bg_color).grid(row=1, column=0, pady=10, padx=10, sticky="w")
        dr1_txt = Entry(F4, width=9, textvariable=self.ma, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        dr2_lbl = Label(F4, text="LIMKA", font=("times new roman", 15, "bold"), fg="lightgreen",
                         bg=bg_color).grid(row=2, column=0, pady=10, padx=10, sticky="w")
        dr2_txt = Entry(F4, width=9, textvariable=self.li, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        dr3_lbl = Label(F4, text="SPRITE", font=("times new roman", 15, "bold"), fg="lightgreen", bg=bg_color).grid(
            row=3, column=0, pady=10, padx=10, sticky="w")
        dr3_txt = Entry(F4, width=9, textvariable=self.sp, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        dr4_lbl = Label(F4, text="ORANGE", font=("times new roman", 15, "bold"), fg="lightgreen",
                         bg=bg_color).grid(row=4, column=0, pady=10, padx=10, sticky="w")
        dr4_txt = Entry(F4, width=9, textvariable=self.org1, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        # Bill Area Frame
        F4 = Frame(self.root, bd=10, relief=GROOVE, pady=10, padx=10)
        F4.place(x=993, y=180, width=400, height=350)
        bill_title = Label(F4, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F4, orient=VERTICAL)
        self.txtArea = Text(F4, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtArea.yview())
        self.txtArea.pack(fill=BOTH, expand=1)

        # Button Frame
        F5 = LabelFrame(self.root, bd=10, relief=GROOVE, bg=bg_color, fg="gold", text="Bill Menu",
                        font=("times new roman", 15, "bold"))
        F5.place(x=0, y=505, relwidth=1, height=190)
        m1_lbl = Label(F5, text="Total Bubble Tea price", bg=bg_color, fg="lightgreen",
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=10, pady=1, sticky="w")
        m1_txt = Entry(F5, width=15, textvariable=self.bubble_tea_price, font=("times new roman", 10, "bold"), bd=7,
                       relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        m2 = Label(F5, text="Total Ice Tea price", bg=bg_color, fg="lightgreen",
                   font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=10, pady=1, sticky="w")
        m2_txt = Entry(F5, width=15, textvariable=self.ice_tea_price, font=("times new roman", 10, "bold"), bd=7,
                       relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        m5 = Label(F5, text="Total Cold Drinks price", bg=bg_color, fg="lightgreen",
                   font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=10, pady=1, sticky="w")
        m2_txt = Entry(F5, width=15, textvariable=self.cold_drinks_price, font=("times new roman", 10, "bold"), bd=7,
                       relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        m3 = Label(F5, text="Total Tax", bg=bg_color, fg="lightgreen", font=("times new roman", 14, "bold")).grid(row=0,column=2, padx=10,pady=1,sticky="w")
        m3_txt = Entry(F5, width=15, textvariable=self.total_tax, font=("times new roman", 10, "bold"), bd=7,
                       relief=SUNKEN).grid(row=0, column=3, pady=10, padx=10)

        m4=Label(F5, text="Total Cost", bg=bg_color, fg="lightgreen", font=("times new roman", 14, "bold")).grid(row=1,column=2,padx=10,pady=1,sticky="w")
        m4_txt = Entry(F5, width=15, textvariable=self.total_cost, font=("times new roman", 10, "bold"), bd=7,
        relief=SUNKEN).grid(row=1, column=3, pady=5, padx=5)

        btn_f = Frame(F5, bd=7, relief=GROOVE)
        btn_f.place(x=630, width=700, height=150)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="cadetblue", fg="white", bd=5, padx=15,
                           pady=15, height=2, width=4, font="arial 15 bold").grid(row=0, column=0, padx=20, pady=15)
        GBill_btn = Button(btn_f, command=self.bill_area, text="Bill", bg="cadetblue", fg="white", bd=5, padx=20,
                           pady=15, height=2, width=4,
                           font="arial 15 bold").grid(row=0, column=1, padx=20, pady=15)
        PBill_btn = Button(btn_f, command=self.locprinter, text="Print", bg="cadetblue", fg="white", bd=5, padx=20,
                           pady=15, height=2, width=4,
                           font="arial 15 bold").grid(row=0, column=2, padx=20, pady=15)
        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="cadetblue", fg="white", bd=5, padx=20,
                           pady=15,
                           height=2, width=4,
                           font="arial 15 bold").grid(row=0, column=3, padx=20, pady=15)
        exit_btn = Button(btn_f, text="Exit", command=self.exit_app, bg="cadetblue", fg="white", bd=5, padx=15, pady=15,
                          height=2, width=4,
                          font="arial 15 bold").grid(row=0, column=4, padx=20, pady=15)
        self.welcome_bill()



    def total(self):
        self.b_cap = (self.cap.get() * 50)
        self.b_moc = (self.moc.get() * 70)
        self.b_cafl = (self.cafl.get() * 100)
        self.b_cho = (self.cho.get() * 70)
        self.b_cof = (self.cof.get() * 50)

        self.total_bubble_tea_price = float(
            self.b_cap +
            self.b_moc +
            self.b_cafl +
            self.b_cho +
            self.b_cof

        )
        self.bubble_tea_price.set(str(self.total_bubble_tea_price))

        self.i_fraf = (self.fraf.get() * 50)
        self.i_vani = (self.vani.get() * 70)
        self.i_tea = (self.tea.get() * 100)
        self.i_lem = (self.lem.get() * 70)
        self.i_org = (self.org.get() * 50)

        self.total_ice_tea_price = float(
            self.i_fraf +
            self.i_vani +
            self.i_tea +
            self.i_lem +
            self.i_org
        )
        self.ice_tea_price.set(str(self.total_ice_tea_price))

        self.dr_th = (self.th.get() * 20)
        self.dr_ma = (self.ma.get() * 20)
        self.dr_li = (self.li.get() * 20)
        self.dr_sp = (self.sp.get() * 20)
        self.dr_org1 = (self.org1.get() * 50)

        self.total_cold_drinks_price = float(
            self.dr_th +
            self.dr_ma +
            self.dr_li +
            self.dr_sp +
            self.dr_org1
        )
        self.cold_drinks_price.set(str(self.total_cold_drinks_price))

        # self.total_cost.set(str(self.total_cost))
        self.t_tax = round((self.total_bubble_tea_price + self.total_ice_tea_price+self.total_cold_drinks_price) * 0.1)
        self.total_tax.set(str(self.t_tax))
        self.total_cost1 = float(
            self.total_bubble_tea_price +
            self.total_ice_tea_price +
            self.total_cold_drinks_price +
            self.t_tax
        )
        self.total_cost.set(str(self.total_cost1))


    def welcome_bill(self):
        self.txtArea.delete('1.0', END)
        self.txtArea.insert(END, "\tWelcome to Caffe Coffee Day")
        self.txtArea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtArea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtArea.insert(END, f"\nPhone Number:{self.c_phon.get()}")
        self.txtArea.insert(END, f"\n=========================================")
        self.txtArea.insert(END, f"\nProducts\t\tQTY\tPrice")
        self.txtArea.insert(END, f"\n=========================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer details are must be provided")
        elif self.bubble_tea_price.get() == "0.0" and self.ice_tea_price.get() == "0.0" and self.cold_drinks_price=="0.0":
            messagebox.showerror("Error", "No Products were purchased")
        else:

            self.welcome_bill()
        # Bubble tea
        if self.fraf.get() != 0:
            self.txtArea.insert(END, f"\n Coffe Fraffe\t\t{self.fraf.get()}\t{self.i_fraf}")
        if self.vani.get() != 0:
            self.txtArea.insert(END, f"\n Vanilis Fraffe\t\t{self.vani.get()}\t{self.i_vani}")
        if self.tea.get() != 0:
            self.txtArea.insert(END, f"\n Tea Fraffe\t\t{self.tea.get()}\t{self.i_tea}")
        if self.cho.get() != 0:
            self.txtArea.insert(END, f"\n Chocolate\t\t{self.cho.get()}\t{self.b_cho}")
        if self.cof.get() != 0:
            self.txtArea.insert(END, f"\n Coffee\t\t{self.cof.get()}\t{self.b_cof}")

        # Ice tea
        if self.cap.get() != 0:
            self.txtArea.insert(END, f"\n Cappuccino\t\t{self.cap.get()}\t{self.b_cap}")
        if self.moc.get() != 0:
            self.txtArea.insert(END, f"\n Mocha\t\t{self.moc.get()}\t{self.b_moc}")
        if self.cafl.get() != 0:
            self.txtArea.insert(END, f"\n Caffe Latte\t\t{self.cafl.get()}\t{self.b_cafl}")
        if self.lem.get() != 0:
            self.txtArea.insert(END, f"\n Lemon Tea\t\t{self.lem.get()}\t{self.i_lem}")
        if self.org.get() != 0:
            self.txtArea.insert(END, f"\n Orange Tea\t\t{self.org.get()}\t{self.i_org}")

        # Cold Drinks
        if self.th.get() != 0:
                self.txtArea.insert(END, f"\n Thumbs Up\t\t{self.th.get()}\t{self.dr_th }")
        if self.ma.get() != 0:
                self.txtArea.insert(END, f"\n Mazza\t\t{self.ma.get()}\t{self.dr_ma}")
        if self.li.get() != 0:
                self.txtArea.insert(END, f"\n Limka\t\t{self.li.get()}\t{self.dr_li}")
        if self.sp.get() != 0:
                self.txtArea.insert(END, f"\n Sprite\t\t{self.sp.get()}\t{self.dr_sp}")
        if self.org1.get() != 0:
                self.txtArea.insert(END, f"\n Orange\t\t{self.org1.get()}\t{self.dr_org1}")

        self.txtArea.insert(END, f"\n-----------------------------------------")
        if self.total_tax.get() != "0.0":
            self.txtArea.insert(END, f"\n Total Tax\t\t\t{self.total_tax.get()}")
        if self.total_cost != "0.0":
            self.txtArea.insert(END, f"\n Total Cost\t\t\t{self.total_cost1}")
        self.txtArea.insert(END, f"\n-----------------------------------------")
        self.save_bill()

    # CLEAR
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear data?")
        if op > 0:
            # self.txtArea.delete('1.0', END)
            # bubble tea variables
            self.cap.set(0)
            self.moc.set(0)
            self.cafl.set(0)
            self.cho.set(0)
            self.cof.set(0)

            # ice tea variables
            self.fraf.set(0)
            self.vani.set(0)
            self.tea.set(0)
            self.lem.set(0)
            self.org.set(0)

            # cold drinks variables
            self.th.set(0)
            self.ma.set(0)
            self.li.set(0)
            self.sp.set(0)
            self.org1.set(0)

            # button frame variables
            self.bubble_tea_price.set("")
            self.ice_tea_price.set("")
            self.cold_drinks_price.set("")
            self.total_cost.set("")
            self.total_tax.set("")

            # Customer details variables
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    # print file



    def installed_printer(self):
        printers = win32print.EnumPrinters(2)
        for p in printers:
            return (p)

    printerdef = ''



    def locprinter(self):
        pt = Toplevel()
        pt.geometry("250x250")
        pt.title("Choose Printer")
        var1 = StringVar()
        LABEL = Label(pt, text="Select Printer", bg='goldenrod2', fg='black').pack(fill=X)
        PRCOMBO = ttk.Combobox(pt, width=35)
        print_list = []
        printers = list(win32print.EnumPrinters(2))
        for i in printers:
            print_list.append(i[2])
        print(print_list)
        # put printers in combobox
        PRCOMBO['values'] = print_list
        defprinter = win32print.GetDefaultPrinter()
        print("Default selected printer:", defprinter)
        PRCOMBO.set(defprinter)
        PRCOMBO.pack(padx=5, pady=5)

        def print_bill(self):
            q = self.txtArea.get('1.0', 'end-1c')
            print(q)
            print(self.printerdef)

            win32print.SetDefaultPrinter(printerdef)
            filename = tempfile.mktemp('.txt')
            open(filename, 'w').write(q)
            win32api.ShellExecute(
                0, "printto",
                filename,
                '"%s"' % win32print.GetDefaultPrinter(),
                ".",
                0
            )
            messagebox.showinfo(title="sucess", message="Print Sucessful", detail="Printing done")

        def select():
            global printerdef
            printerdef = PRCOMBO.get()
            pt.destroy()
            print_bill(self)
        B1=ttk.Button(pt,text="Print",width=30,command=select).pack(pady=10)

    # save bill
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtArea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill No.:{self.bill_no.get()} Saved Sucessfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtArea.delete('1.0', END)
                for d in f1:
                    self.txtArea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()

