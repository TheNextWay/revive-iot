from pathlib import Path
import asyncio
import random
import string
from .IoT import maketoken
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from PIL import ImageTk
import pyglet
import qrcode


items = {
    1 : {
        "id":1,
        "transaction_id":1,
        "point":15,
        "condition":"Good",
        "clothing_type":"Kaos",
        "fabric": {
           1: {
            "type" : "Katun",
            "percentage":80
           },
           2: {
            "type" : "Poliester",
            "percentage":20
           }
        }
    },
    2 : {
        "id":2,
        "transaction_id":1,
        "point":15,
        "condition":"Good",
        "clothing_type":"Celana",
        "fabric": {
            1: {
                "type" : "Katun",
                "percentage":100
            },
        }
    },
    3 : {
        "id":3,
        "transaction_id":1,
        "point":15,
        "condition":"Good",
        "clothing_type":"Kain",
        "fabric": {
            1: {
                "type" : "Katun",
                "percentage":100
            },
        }
    },
    4 : {
        "id":4,
        "transaction_id":1,
        "point":20,
        "condition":"Good",
        "clothing_type":"Jaket",
        "fabric": {
            1: {
                "type" : "Katun",
                "percentage":100
            },
        }
    },
    5 : {
        "id":5,
        "transaction_id":1,
        "point":30,
        "condition":"Good",
        "clothing_type":"Kaos",
        "fabric": {
            1: {
                "type" : "Katun",
                "percentage":100
            },
        }
    },
    6 : {
        "id":5,
        "transaction_id":1,
        "point":30,
        "condition":"Good",
        "clothing_type":"Kaos",
        "fabric": {
            1: {
                "type" : "Katun",
                "percentage":100
            },
        }
    },
    7 : {
        "id":5,
        "transaction_id":1,
        "point":30,
        "condition":"Good",
        "clothing_type":"Kaos",
        "fabric": {
            1: {
                "type" : "Katun",
                "percentage":100
            },
        }
    },
    8 : {
        "id":5,
        "transaction_id":1,
        "point":30,
        "condition":"Good",
        "clothing_type":"Kaos",
        "fabric": {
            1: {
                "type" : "Katun",
                "percentage":100
            },
        }
    },
    9 : {
        "id":5,
        "transaction_id":1,
        "point":30,
        "condition":"Good",
        "clothing_type":"Kaos",
        "fabric": {
            1: {
                "type" : "Katun",
                "percentage":100
            },
        }
    },
}

tsm={
   "coordinate": "-7.938878, 112.579912",
   "status": "normal",
   "ip_address": "108.122.028",
   "temperature": "35",
   "capacity": "50",
   "max_capacity": "150",
   "cs_contact": "082245676151",
}
ctk.set_appearance_mode("light")

pyglet.font.add_file('assets/PlusJakartaSans-SemiBold.ttf')
pyglet.font.add_file('assets/PlusJakartaSans-Regular.ttf')

def clear_all():
    pass

class navbar(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=1920, height=40)

        self.wa_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/whatsapp.png"),
                                    dark_image=Image.open("assets/frame0/whatsapp-d.png"),
                                    size=(25, 25))
        self.temperature_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/temperature.png"),
                                              dark_image=Image.open("assets/frame0/temperature-d.png"),
                                              size=(25, 25))
        self.capacity_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/database.png"),
                                          dark_image=Image.open("assets/frame0/database-d.png"),
                                          size=(25, 25))
        self.logo_image = ctk.CTkImage(light_image=Image.open("assets/frame0/logo.png"),
                                       dark_image=Image.open("assets/frame0/logo-d.png"),
                                       size=(254, 61))

        self.font_info = ctk.CTkFont(family="Plus Jakarta Sans Semibold",
                                      size=20,
                                      weight='bold')

        ctk.CTkLabel(self, image=self.wa_icon, compound=tk.LEFT, padx=10, text=("CS",tsm["cs_contact"]),
                     text_color=("#0B7156", 'white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self, image=self.temperature_icon, padx=10, compound=tk.LEFT, text=(tsm["temperature"],"°C"),
                     text_color=("#0B7156", 'white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self, image=self.capacity_icon, compound=tk.LEFT, padx=10, text=(tsm["capacity"],"/",tsm["max_capacity"]),
                     text_color=("#0B7156", 'white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self, compound=tk.LEFT, image=self.logo_image, text="").pack(side="left")

class navbar_green(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.style = ttk.Style()
        self.style.configure('NavbarGreen.TFrame', background='#0B7156')  # Atur latar belakang melalui konfigurasi gaya
        self.configure(style='NavbarGreen.TFrame')  # Gunakan gaya yang telah dikonfigurasi


        self.wa_icon = ctk.CTkImage(Image.open("assets/frame0/whatsapp-d.png"),
                                    size=(25, 25))
        self.temperature_icon = ctk.CTkImage(Image.open("assets/frame0/temperature-d.png"),
                                              size=(25, 25))
        self.capacity_icon = ctk.CTkImage(Image.open("assets/frame0/database-d.png"),
                                          size=(25, 25))
        self.logo_image = ctk.CTkImage(Image.open("assets/frame0/logo-d.png"),
                                       size=(254, 61))

        self.font_info = ctk.CTkFont(family="Plus Jakarta Sans Semibold",
                                      size=20,
                                      weight='bold')

        ctk.CTkLabel(self, bg_color="#0B7156", image=self.wa_icon, compound=tk.LEFT, padx=10, text=("CS",tsm["cs_contact"]),
                     text_color=('white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self,bg_color="#0B7156", image=self.temperature_icon, padx=10, compound=tk.LEFT,text=(tsm["temperature"],"°C"),
                     text_color=('white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self, bg_color="#0B7156",  image=self.capacity_icon, compound=tk.LEFT, padx=10,text=(tsm["capacity"],"/",tsm["max_capacity"]),
                     text_color=('white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self,bg_color="#0B7156",  compound=tk.LEFT, image=self.logo_image, text="").pack(side="left")

class navbar_red(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.style = ttk.Style()
        self.style.configure('NavbarRed.TFrame', background='#FF263E')  # Atur latar belakang melalui konfigurasi gaya
        self.configure(style='NavbarRed.TFrame')  # Gunakan gaya yang telah dikonfigurasi


        self.wa_icon = ctk.CTkImage(Image.open("assets/frame0/whatsapp-d.png"),
                                    size=(25, 25))
        self.temperature_icon = ctk.CTkImage(Image.open("assets/frame0/temperature-d.png"),
                                              size=(25, 25))
        self.capacity_icon = ctk.CTkImage(Image.open("assets/frame0/database-d.png"),
                                          size=(25, 25))
        self.logo_image = ctk.CTkImage(Image.open("assets/frame0/logo-d.png"),
                                       size=(254, 61))

        self.font_info = ctk.CTkFont(family="Plus Jakarta Sans Semibold",
                                      size=20,
                                      weight='bold')

        ctk.CTkLabel(self, bg_color="#FF263E", image=self.wa_icon, compound=tk.LEFT, padx=10, text=("CS",tsm["cs_contact"]),
                     text_color=('white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self,bg_color="#FF263E", image=self.temperature_icon, padx=10, compound=tk.LEFT,text=(tsm["temperature"],"°C"),
                     text_color=('white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self, bg_color="#FF263E",  image=self.capacity_icon, compound=tk.LEFT, padx=10,text=(tsm["capacity"],"/",tsm["max_capacity"]),
                     text_color=('white'), font=self.font_info).pack(side='right')

        ctk.CTkLabel(self,bg_color="#FF263E",  compound=tk.LEFT, image=self.logo_image, text="").pack(side="left")




window = tk.Tk()

window.geometry("1280x720")

def show_frame(frame):
    frame.tkraise()
    
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame_maintain = tk.Frame(window)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

for frame in (frame1, frame2, frame3,frame4, frame_maintain):
    frame.grid(row=0,column=0,sticky='nsew')

logo_image = ctk.CTkImage(light_image=Image.open("assets/frame0/logo.png"),
                        dark_image=Image.open("assets/frame0/logo-d.png"),
                        size=(254, 61))


shirt = ctk.CTkImage(Image.open("assets/frame0/shirt.png"),
                        size=(75, 75))

pants = ctk.CTkImage(Image.open("assets/frame0/pants.png"),
                        size=(75, 75))

jacket = ctk.CTkImage(Image.open("assets/frame0/jacket.png"),
                        size=(75, 75))

fabric = ctk.CTkImage(Image.open("assets/frame0/fabric.png"),
                        size=(75, 75))


font_info = ctk.CTkFont(family="Plus Jakarta Sans Semibold", 
                        size=20,
                        weight='bold')  



textile = ctk.CTkImage(Image.open("assets/frame0/textiles.png"),
                                  size=(564, 232.73))


#==================================== Frame 1 Code ==========================
navbar_frame_1 = navbar(frame1)
navbar_frame_1.pack(pady=40, padx=80, fill="both", side="top")



frame_action = ttk.Frame(frame1, 
                       width=960, 
                       height=900)

frame_action.pack(padx=50, side="left")

ctk.CTkLabel(frame_action, image=textile, text="").pack()

def button_event():
    show_frame(frame2)
    frame2.after(3000, lambda: show_frame(frame3))  # Menjadwalkan beralih ke frame3 setelah 5 detik


ctk.CTkButton(frame_action, corner_radius=20,command=lambda:button_event(), text="Selesai Menyetor", font=('Plus Jakarta Sans Semibold',48), fg_color="#1BAE80",hover_color="#0B7156",  text_color="#F6FAF7", height=115, width=740).pack(pady=80)
        

items_frame = ttk.Frame(frame1, borderwidth=5,width=960, height=830)
items_frame.pack(anchor="center")


text_item = ctk.CTkFont(family="Plus Jakarta Sans Semibold", 
                        size=64)  

def item_component(item):
    frame_item = ttk.Frame(items_frame, borderwidth=10,  width=535, height=155)
    frame_items = ttk.Frame(frame_item,  width=535, height=100)

    match item["clothing_type"]:
        case "Kaos":
            ctk.CTkLabel(frame_item, image=shirt, text="").pack(side="left", anchor="nw", pady=25)

            
        case "Celana":
            ctk.CTkLabel(frame_item, image=pants, text="").pack(side="left", anchor="nw", pady=25)

            
        case "Jaket":
            ctk.CTkLabel(frame_item, image=jacket, text="").pack(side="left", anchor="nw", pady=25)


        case "Kain":
            ctk.CTkLabel(frame_item, image=fabric, text="").pack(side="left", anchor="nw", pady=25)


    
    ctk.CTkLabel(frame_items,text_color="#2D3648", font=('Plus Jakarta Sans Semibold',64), text=(1,"x", item["clothing_type"])).pack(anchor="nw")
    
    frame_fabric_type = ttk.Frame(frame_items, width=535, height=155)

    for x in item["fabric"]:
        ctk.CTkButton(frame_fabric_type, text=(item["fabric"][x]["percentage"],"%", item["fabric"][x]["type"]), font=('Plus Jakarta Sans Semibold',14), border_color="#2D3648",fg_color="transparent",border_width=2, hover=False, text_color="#2D3648", height=30).pack(side="right", anchor='w',padx=5)
        frame_fabric_type.pack(anchor="w")


    frame_item.pack(anchor="nw")
    frame_items.pack(anchor="nw", padx=20)

for item in items.items():
  item_component(item[1])

#================================ Frame 2 code==========================================
success_icon = ctk.CTkImage(Image.open("assets/frame1/success.png"),
                        size=(404, 404))

navbar_frame_2 = navbar_green(frame2)
navbar_frame_2.pack(pady=40, padx=80, fill="both", side="top")


frame2.configure(background="#0B7156")
ctk.CTkLabel(frame2, image=success_icon, compound="top",text_color="white" , text="Yeayy, Berhasill", font=('Plus Jakarta Sans Semibold',64), ).pack(fill="y")
ctk.CTkLabel(frame2, compound="top",text_color="white" , text='Pakaianmu Sudah kami terima semua!', font=('Plus Jakarta Sans Semibold',50), ).pack()

#================================= Frame 3 code==========================================
navbar_frame_3 = navbar(frame3)
navbar_frame_3.pack(pady=40, padx=80, fill="both", side="top")

frame3_left = ttk.Frame(frame3, width=960, height=830)
# def countdown(t): 
#     while t: 
#         mins, secs = divmod(t, 60) 
#         timer = '{:02d}:{:02d}'.format(mins, secs) 
#         ctk.CTkLabel(frame3_left, text_color="#2D3648" , text=(timer), font=('Plus Jakarta Sans Semibold',32), ).pack(anchor="w",pady=30)
#         time.sleep(1) 
#         t -= 1
      
# t = 3000
  
# countdown(t)  


# qr generation
def create_qrcode(text):
    qr = qrcode.QRCode(border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(back_color="#f0f0f0")
    return img

letters = string.ascii_letters
rand_string = ''.join(random.choice(letters) for i in range(10))
imgs = create_qrcode(maketoken(321,rand_string)).resize((550, 550))

ctk.CTkLabel(frame3_left, text_color="#2D3648" , text='321', font=('Plus Jakarta Sans Semibold',145), ).pack(anchor="w", )
ctk.CTkLabel(frame3_left, text_color="#2D3648" , text='Revive Poin', font=('Plus Jakarta Sans',128) ).pack()

frame3_left.pack(anchor="w", padx=100, pady=80, side="left",)

frame3_right = ttk.Frame(frame3, width=960, height=830)
qr = ImageTk.PhotoImage(imgs)

ctk.CTkLabel(frame3_right, text_color="#2D3648" , text='Pindai dengan aplikasi Revive', font=('Plus Jakarta Sans Semibold',32), ).pack()
ctk.CTkLabel(frame3_right, image=qr,text='').pack()


frame3_right.pack(anchor="e", side="right", padx=50)


frame3_btn = tk.Button(frame3_right, text='Enter',command=lambda:success_scan())
frame3_btn.pack(fill='x', ipady=15)

def success_scan():
    show_frame(frame4)
    frame4.after(3000, lambda: show_frame(frame1))  # Menjadwalkan beralih ke frame3 setelah 5 detik

# ======================= frame4 ===============
navbar_frame_4 = navbar_green(frame4)
navbar_frame_4.pack(pady=40, padx=80, fill="both", side="top")
hi_icon = ctk.CTkImage(Image.open("assets/frame4/hi.png"),
                        size=(404, 404))

frame4.configure(background="#0B7156")
ctk.CTkLabel(frame4, image=hi_icon, compound="top",text_color="white" , text=('Hi,',' Arsyad Ali Mahardika'), font=('Plus Jakarta Sans',64), ).pack(fill="y")
ctk.CTkLabel(frame4, compound="top",text_color="white" , text='Poinmu Berhasil ditambahkan', font=('Plus Jakarta Sans Semibold',64), ).pack()


# ============= frame_maintain ===================


navbar_frame_maintain = navbar_red(frame_maintain)
navbar_frame_maintain.pack(pady=40, padx=80, fill="both", side="top")

engineering = ctk.CTkImage(Image.open("assets/frame_maintain/engineering.png"),
                        size=(825, 500))

frame_maintain.configure(background="#FF263E")
ctk.CTkLabel(frame_maintain, image=engineering, compound="top",text_color="white" , text='' ).pack(expand=True)




# ================ End Code =============


if tsm["status"] == "maintain":
    show_frame(frame_maintain)
else:
    show_frame(frame1)  



window.resizable(False, False)
window.attributes('-fullscreen', True)
window.mainloop()

