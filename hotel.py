from tkinter import *
import random
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Restaurant Billing System")

        title=Label(self.root,text="Restaurant Billing System",bd=12,relief=RIDGE,
                    font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)

        # =================================== Variables ======================================
        # Starter Items
        self.samosa = IntVar()
        self.paneer_tikka = IntVar()
        self.chicken_tikka = IntVar()
        self.veg_pakora = IntVar()
        self.papdi_chaat = IntVar()
        self.tomato_soup = IntVar()
        self.masala_papad = IntVar()

        # Main Course
        self.butter_chicken = IntVar()
        self.pasta = IntVar()
        self.basmati_rice = IntVar()
        self.paneer_masala = IntVar()
        self.palak_paneer = IntVar()
        self.daal = IntVar()
        self.chole_bhature = IntVar()

        # Snacks
        self.noodles = IntVar()
        self.aloo_tikki = IntVar()
        self.dahi_vada = IntVar()
        self.pav_bhaji = IntVar()
        self.bhel_puri = IntVar()
        self.soup = IntVar()
        self.pakora_snack = IntVar()

        # Billing and Tax Variables
        self.total_starter = StringVar()
        self.total_main = StringVar()
        self.total_snack = StringVar()
        self.tax_starter = StringVar()
        self.tax_main = StringVar()
        self.tax_snack = StringVar()

        # Customer details
        self.c_name = StringVar()
        self.phone = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        # =============================== Customer Details Frame =============================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)

        Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)
        Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)
        Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)
        Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)

        # ================================ Starter Items =====================================
        starter_frame=LabelFrame(self.root,text="Starters",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        starter_frame.place(x=5,y=180,height=380,width=325)

        Label(starter_frame,text="Samosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        Entry(starter_frame,borderwidth=2,width=15,textvariable=self.samosa).grid(row=0,column=1,padx=10)

        Label(starter_frame,text="Paneer Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        Entry(starter_frame,borderwidth=2,width=15,textvariable=self.paneer_tikka).grid(row=1,column=1,padx=10)

        Label(starter_frame,text="Chicken Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        Entry(starter_frame,borderwidth=2,width=15,textvariable=self.chicken_tikka).grid(row=2,column=1,padx=10)

        Label(starter_frame,text="Vegetable Pakora",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        Entry(starter_frame,borderwidth=2,width=15,textvariable=self.veg_pakora).grid(row=3,column=1,padx=10)

        Label(starter_frame,text="Papdi Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        Entry(starter_frame,borderwidth=2,width=15,textvariable=self.papdi_chaat).grid(row=4,column=1,padx=10)

        Label(starter_frame,text="Tomato Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        Entry(starter_frame,borderwidth=2,width=15,textvariable=self.tomato_soup).grid(row=5,column=1,padx=10)

        Label(starter_frame,text="Masala Papad",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        Entry(starter_frame,borderwidth=2,width=15,textvariable=self.masala_papad).grid(row=6,column=1,padx=10)

        # ================================ Main Course =====================================
        main_frame=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        main_frame.place(x=340,y=180,height=380,width=325)

        Label(main_frame,text="Butter Chicken",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        Entry(main_frame,borderwidth=2,width=15,textvariable=self.butter_chicken).grid(row=0,column=1,padx=10)

        Label(main_frame,text="Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        Entry(main_frame,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        Label(main_frame,text="Basmati Rice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        Entry(main_frame,borderwidth=2,width=15,textvariable=self.basmati_rice).grid(row=2,column=1,padx=10)

        Label(main_frame,text="Paneer Masala",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        Entry(main_frame,borderwidth=2,width=15,textvariable=self.paneer_masala).grid(row=3,column=1,padx=10)

        Label(main_frame,text="Palak Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        Entry(main_frame,borderwidth=2,width=15,textvariable=self.palak_paneer).grid(row=4,column=1,padx=10)

        Label(main_frame,text="Daal",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        Entry(main_frame,borderwidth=2,width=15,textvariable=self.daal).grid(row=5,column=1,padx=10)

        Label(main_frame,text="Chole Bhature",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        Entry(main_frame,borderwidth=2,width=15,textvariable=self.chole_bhature).grid(row=6,column=1,padx=10)

        # ================================ Snacks =====================================
        snack_frame=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        snack_frame.place(x=677,y=180,height=380,width=325)

        Label(snack_frame,text="Noodles",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        Entry(snack_frame,borderwidth=2,width=15,textvariable=self.noodles).grid(row=0,column=1,padx=10)

        Label(snack_frame,text="Aloo Tikki Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        Entry(snack_frame,borderwidth=2,width=15,textvariable=self.aloo_tikki).grid(row=1,column=1,padx=10)

        Label(snack_frame,text="Dahi Vada",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        Entry(snack_frame,borderwidth=2,width=15,textvariable=self.dahi_vada).grid(row=2,column=1,padx=10)

        Label(snack_frame,text="Pav Bhaji",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        Entry(snack_frame,borderwidth=2,width=15,textvariable=self.pav_bhaji).grid(row=3,column=1,padx=10)

        Label(snack_frame,text="Bhel Puri",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        Entry(snack_frame,borderwidth=2,width=15,textvariable=self.bhel_puri).grid(row=4,column=1,padx=10)

        Label(snack_frame,text="Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        Entry(snack_frame,borderwidth=2,width=15,textvariable=self.soup).grid(row=5,column=1,padx=10)

        Label(snack_frame,text="Pakora",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        Entry(snack_frame,borderwidth=2,width=15,textvariable=self.pakora_snack).grid(row=6,column=1,padx=10)

        # ============================ Bill Area ==========================================
        bill_frame=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        bill_frame.place(x=1010,y=188,width=330,height=372)

        Label(bill_frame,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

        scrol_y=Scrollbar(bill_frame,orient=VERTICAL)
        self.txtarea=Text(bill_frame,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # ========================== Billing Buttons ====================================
        button_frame=Frame(self.root,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,y=580,width=500,height=95)

        Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=self.total).grid(row=0,column=0,padx=12)
        Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=self.clear).grid(row=0,column=1,padx=10,pady=6)
        Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=self.exit1).grid(row=0,column=2,padx=10,pady=6)

        self.intro()

    # ========================== Functions ======================================
    def intro(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
        self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
        self.txtarea.insert(END,"\n====================================\n")
        self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
        self.txtarea.insert(END,"\n====================================\n")

    def total(self):
        if self.c_name.get()=="" or self.phone.get()=="":
            messagebox.showerror("Error", "Fill the complete Customer Details!!")
            return

        # Starter Prices
        self.price_samosa = self.samosa.get()*20
        self.price_paneer_tikka = self.paneer_tikka.get()*50
        self.price_chicken_tikka = self.chicken_tikka.get()*70
        self.price_veg_pakora = self.veg_pakora.get()*30
        self.price_papdi_chaat = self.papdi_chaat.get()*25
        self.price_tomato_soup = self.tomato_soup.get()*35
        self.price_masala_papad = self.masala_papad.get()*15

        total_starter_price = (
            self.price_samosa + self.price_paneer_tikka + self.price_chicken_tikka +
            self.price_veg_pakora + self.price_papdi_chaat + self.price_tomato_soup +
            self.price_masala_papad
        )
        self.total_starter.set(str(total_starter_price)+" Rs")
        self.tax_starter.set(str(round(total_starter_price*0.05,2))+" Rs")

        # Main Course Prices
        self.price_butter_chicken = self.butter_chicken.get()*120
        self.price_pasta = self.pasta.get()*100
        self.price_rice = self.basmati_rice.get()*80
        self.price_paneer_masala = self.paneer_masala.get()*90
        self.price_palak_paneer = self.palak_paneer.get()*85
        self.price_daal = self.daal.get()*60
        self.price_chole_bhature = self.chole_bhature.get()*70

        total_main_price = (
            self.price_butter_chicken + self.price_pasta + self.price_rice +
            self.price_paneer_masala + self.price_palak_paneer +
            self.price_daal + self.price_chole_bhature
        )
        self.total_main.set(str(total_main_price)+" Rs")
        self.tax_main.set(str(round(total_main_price*0.01,2))+" Rs")

        # Snacks Prices
        self.price_noodles = self.noodles.get()*40
        self.price_aloo_tikki = self.aloo_tikki.get()*25
        self.price_dahi_vada = self.dahi_vada.get()*20
        self.price_pav_bhaji = self.pav_bhaji.get()*50
        self.price_bhel_puri = self.bhel_puri.get()*30
        self.price_soup = self.soup.get()*35
        self.price_pakora_snack = self.pakora_snack.get()*25

        total_snack_price = (
            self.price_noodles + self.price_aloo_tikki + self.price_dahi_vada +
            self.price_pav_bhaji + self.price_bhel_puri + self.price_soup +
            self.price_pakora_snack
        )
        self.total_snack.set(str(total_snack_price)+" Rs")
        self.tax_snack.set(str(round(total_snack_price*0.1,2))+" Rs")

        # Total Bill
        self.total_bill = total_starter_price + total_main_price + total_snack_price + \
                          round(total_starter_price*0.05,2) + round(total_main_price*0.01,2) + round(total_snack_price*0.1,2)
        self.total_bill_str = str(self.total_bill)+" Rs"

        self.show_bill()

    def show_bill(self):
        self.intro()
        if self.samosa.get()!=0:
            self.txtarea.insert(END,f"Samosa\t\t{self.samosa.get()}\t{self.price_samosa}\n")
        if self.paneer_tikka.get()!=0:
            self.txt
