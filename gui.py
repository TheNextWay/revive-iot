from pathlib import Path

import tkinter as tk
from tkinter import LEFT, RIGHT, Button, PhotoImage, ttk
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")

window = tk.Tk()

window.geometry("1920x1080")

frame_info = ttk.Frame(window, 
                       width=1920, 
                       height=40)
frame_info.pack(pady=40,
                padx=80,
                fill="both",
                side="top")


logo_image = ctk.CTkImage(light_image=Image.open("assets/frame0/logo.png"),
                        dark_image=Image.open("assets/frame0/logo-d.png"),
                        size=(254, 61))

wa_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/whatsapp.png"),
                        dark_image=Image.open("assets/frame0/whatsapp-d.png"),
                        size=(25, 25))

temperature_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/temperature.png"),
                                dark_image=Image.open("assets/frame0/temperature-d.png"),
                                size=(25, 25))

capacity_icon = ctk.CTkImage(light_image=Image.open("assets/frame0/database.png"),
                            dark_image=Image.open("assets/frame0/database-d.png"),
                            size=(25, 25))

font_info = ctk.CTkFont(family="Plus Jakarta Sans", 
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




button_image_1 = PhotoImage(
    file="assets/frame0/button_1.png")

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)

frame_action = ttk.Frame(window, 
                       width=960, 
                       height=900,
                       )

frame_action.pack(padx=50, side="left")

ctk.CTkLabel(frame_action, image=textile, text="").pack()

def button_event():
    print("button pressed")

button = ctk.CTkButton(frame_action,hover=True,hover_color="white", text="", image=button_image_1, command=button_event, fg_color='transparent', )
button.pack(pady=40
                )


# window.resizable(False, False)
# window.attributes('-fullscreen', True)
window.mainloop()
