from pathlib import Path

import tkinter as tk
from tkinter import LEFT, RIGHT, Button, PhotoImage, ttk
import customtkinter as ctk
from PIL import Image
import pyglet
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
   "status": "ON",
   "ip_address": "108.122.028",
   "temperature": "35",
   "capacity": "50",
   "max_capacity": "150",
   "cs_contact": "082245676151",
}
ctk.set_appearance_mode("light")

pyglet.font.add_file('assets/PlusJakartaSans-SemiBold.ttf')
window = tk.Tk()

window.geometry("1280x720")

frame_info = ttk.Frame(window, 
                       width=1920, 
                       height=40)
frame_info.pack(pady=40,
                padx=80,
                fill="both",
                side="top")


wa_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/whatsapp.png"),
                        dark_image=Image.open("assets/frame0/whatsapp-d.png"),
                        size=(25, 25))

logo_image = ctk.CTkImage(light_image=Image.open("assets/frame0/logo.png"),
                        dark_image=Image.open("assets/frame0/logo-d.png"),
                        size=(254, 61))

temperature_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/temperature.png"),
                                dark_image=Image.open("assets/frame0/temperature-d.png"),
                                size=(25, 25))

capacity_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/database.png"),
                            dark_image=Image.open("assets/frame0/database-d.png"),
                            size=(25, 25))

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



ctk.CTkLabel(
    frame_info, 
    image=wa_icon, 
    compound=LEFT, 
    padx=10,  
    text="CS 082245676151", 
    text_color=("#0B7156",'white'), 
    font=font_info).pack(side = 'right' )

ctk.CTkLabel(
    frame_info, 
    image=temperature_icon, 
    padx=10 ,compound=LEFT, 
    text="40o", 
    text_color=("#0B7156",'white'), 
    font=font_info).pack(side = 'right')

ctk.CTkLabel(
    frame_info, 
    image=capacity_icon, 
    compound=LEFT, 
    padx=10, 
    text="51/150", 
    text_color=("#0B7156",'white'), 
    font=font_info).pack(side = 'right' )

ctk.CTkLabel(
    frame_info,
    compound=LEFT, 
    image=logo_image, 
    text="" ).pack(side="left")


textile = ctk.CTkImage(Image.open("assets/frame0/textiles.png"),
                                  size=(564, 232.73))

frame_action = ttk.Frame(window, 
                       width=960, 
                       height=900)

frame_action.pack(padx=50, side="left")

ctk.CTkLabel(frame_action, image=textile, text="").pack()

def button_event():
    print("button pressed")


ctk.CTkButton(frame_action, corner_radius=20,command=button_event(), text="Selesai Menyetor", font=('Plus Jakarta Sans Semibold',48), fg_color="#1BAE80",hover_color="#0B7156",  text_color="#F6FAF7", height=115, width=740).pack(pady=80)
        

items_frame = ttk.Frame(window, borderwidth=5,width=960, height=830)
items_frame.pack(anchor="center")


text_item = ctk.CTkFont(family="Plus Jakarta Sans Semibold", 
                        size=64)  




def item_component(item):
    frame_item = ttk.Frame(items_frame, borderwidth=10,  width=535, height=155)
    frame_items = ttk.Frame(frame_item,  width=535, height=100)

    match item["clothing_type"]:
        case "Kaos":
            ctk.CTkLabel(frame_item, image=shirt, text="").pack(side="left", anchor="nw", pady=25)
            ctk.CTkLabel(frame_items,text_color="#2D3648", font=('Plus Jakarta Sans Semibold',64), text=(1,"x", item["clothing_type"])).pack(anchor="nw")

            
        case "Celana":
            ctk.CTkLabel(frame_item, image=pants, text="").pack(side="left", anchor="nw", pady=25)
            ctk.CTkLabel(frame_items,text_color="#2D3648", font=('Plus Jakarta Sans Semibold',64), text=(1,"x", item["clothing_type"])).pack(anchor="nw")

            
        case "Jaket":
            ctk.CTkLabel(frame_item, image=jacket, text="").pack(side="left", anchor="nw", pady=25)
            ctk.CTkLabel(frame_items,text_color="#2D3648", font=('Plus Jakarta Sans Semibold',64), text=(1,"x", item["clothing_type"])).pack(anchor="nw")


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
  

window.resizable(False, False)
window.attributes('-fullscreen', True)
window.mainloop()
