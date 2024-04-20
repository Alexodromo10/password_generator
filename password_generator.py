import random
import customtkinter
from CTkColorPicker import *

app = customtkinter.CTk()
app.geometry("1000x600")
app.title("Simple Password Generator")
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
customtkinter.set_appearance_mode("dark")
password = ""
bg = customtkinter.CTkFrame(master=app)
bg.pack(expand=True, fill="both")


#password generator
font = customtkinter.CTkFont("Product Sans", size=20)
logofont= customtkinter.CTkFont("Product Sans Bold", size=40)

# saving passwords
#------------
data = 0
try:
    data = open("created_passwords", "r").read()
except FileNotFoundError:
    data = 0
    print("No created passwords file exists. Creating a new one . . .")
    
data = open("created_passwords", "w")
#------------
def optionmenu_callback(choice):
    if choice == "Dark Mode":
        customtkinter.set_appearance_mode("dark")
    elif choice == "Light Mode":
        customtkinter.set_appearance_mode("light")
    elif choice == "System":
        customtkinter.set_appearance_mode("system")

combobox = customtkinter.CTkOptionMenu(master=bg,
                                       values=["Dark Mode", "Light Mode", "System"],
                                       command=optionmenu_callback, 
                                       font=font, corner_radius=30)
combobox.place(relx=0.9, rely=0.9, anchor="center")
combobox.set("System")  # set initial value
label2 = customtkinter.CTkLabel(master=bg, text="Succesfully copied to clipboard!", bg_color="transparent", font=font)
label2.place(relx=0.5, rely=2, anchor="center")
logo_label = customtkinter.CTkLabel(master=bg, text="Simple password \ngenerator", font=logofont, fg_color="transparent")
logo_label.place(relx=0.5, rely=0.15, anchor="center")
hey = customtkinter.CTkLabel(text="Hey! You can write ONLY numerical characters", font=font, master=bg)

def open_input_dialog_event():
    global password, hey, data
    try:
        label.place(relx=0.5, rely=2, anchor="center")
        dialog = customtkinter.CTkInputDialog(text="Type the number of characters of your new password", title="Create Password", font=font)
        password = ""
        label2.place(relx=0.5, rely=2, anchor="center")
        for i in range(int(dialog.get_input())):
            password += random.choice(chars)

        label.place(relx=0.5, rely=0.6, anchor="center")
        label.configure(text=password)
        hey.place(relx=0.5, rely=2,anchor="center")
        data.write(password + "\n")
    except ValueError:
        hey.place(relx=0.5, rely=0.6, anchor="center")
        open_input_dialog_event()

def click_handler():
    app.clipboard_clear()
    app.clipboard_append(password)
    app.update()
    label2.place(relx=0.5, rely=0.6, anchor="center")
    label.place(relx=0.5, rely=2, anchor="center")
    
string_input_button = customtkinter.CTkButton(master=bg, text="Create New Password", command=open_input_dialog_event, corner_radius=32, font=font)
string_input_button.place(relx=0.5, rely=0.5, anchor="center")

label = customtkinter.CTkButton(master=bg, text=password, command=click_handler, font=font, corner_radius=30)
label.place_forget()

def darken_hex_color(hex_color, factor):
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]
    
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    r = max(0, int(r * factor))
    g = max(0, int(g * factor))
    b = max(0, int(b * factor))
    
    dark_hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    
    return dark_hex_color

def color_picker():
    global theme, color
    pick_color = AskColor()
    color = pick_color.get()
    darkened_color = darken_hex_color(color, 0.3)  # Darken by 50%
    darkened_hover_color = darken_hex_color(color, 0.7)  # Darken by 50%

    combobox.configure(fg_color=color)
    label.configure(fg_color=color, hover_color=darkened_hover_color)
    string_input_button.configure(fg_color=color, hover_color=darkened_hover_color)
    colortheme.configure(fg_color=color, hover_color=darkened_hover_color)
    bg.configure(fg_color=darkened_color)
    
colortheme= customtkinter.CTkButton(master=bg, text="Choose theme color", font=font, text_color="white", command=color_picker, corner_radius=30)
colortheme.place(relx=0.5, rely=0.9, anchor="center")

app.mainloop()