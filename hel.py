import customtkinter as ctk
from tkinter import Canvas, PhotoImage, Label
import time
import threading

# Fake password
CORRECT_PASSWORD = "192919"

# App setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("1200x800")
app.title("T.A.S.C - Classified Access Terminal")
app.resizable(False, False)

# Background image (optional)
try:
    bg_image = PhotoImage(file="tasc_bg.jpg")
    bg_label = Label(app, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    app.configure(bg="#000000")

# MAIN FRAME — width aur height yahan constructor mein daal rahe hain (purane version ke liye)
frame = ctk.CTkFrame(app, corner_radius=20, fg_color="#0a0a0a", border_width=3, border_color="#00ff00",
                     width=520, height=620)   # ← yahan daala
frame.place(relx=0.5, rely=0.5, anchor="center")         # ← yahan se width/height hata diya
frame.pack_propagate(False)  # ← ye line zaroori hai taaki size fixed rahe

# Title & text
title = ctk.CTkLabel(frame, text="T.A.S.C", font=("Orbitron", 78, "bold"), text_color="#00ff41")
title.pack(pady=(50, 5))

subtitle = ctk.CTkLabel(frame, text="Tactical Advanced Strategic Command", 
                       font=("Courier New", 16), text_color="#00ff00")
subtitle.pack(pady=(0, 30))

welcome = ctk.CTkLabel(frame, text="» WELCOME TO T.A.S.C «", 
                      font=("Consolas", 20, "bold"), text_color="#39ff14")
welcome.pack(pady=10)

# Login fields
ctk.CTkLabel(frame, text="AGENT ID", font=("Courier", 16), text_color="#00ff00").pack(pady=(30,5))
username_entry = ctk.CTkEntry(frame, placeholder_text="Enter username...", width=320, height=50,
                             font=("Courier", 14), corner_radius=10)
username_entry.pack(pady=5)

ctk.CTkLabel(frame, text="PASSCODE", font=("Courier", 16), text_color="#00ff00").pack(pady=(20,5))
password_entry = ctk.CTkEntry(frame, placeholder_text="      ", width=320, height=50, show="•",
                             font=("Courier", 14), corner_radius=10)
password_entry.pack(pady=5)

status_label = ctk.CTkLabel(frame, text="", font=("Courier", 14), text_color="#ff0000")
status_label.pack(pady=20)

# Access granted screen
def show_access_granted():
    for widget in frame.winfo_children():
        widget.destroy()
    
    ctk.CTkLabel(frame, text="ACCESS GRANTED", font=("Orbitron", 56, "bold"), text_color="#00ff00").pack(pady=100)
    ctk.CTkLabel(frame, text="CLASSIFIED LEVEL: OMEGA", font=("Courier", 20), text_color="#00ff41").pack(pady=20)
    ctk.CTkLabel(frame, text="Agent authenticated.", font=("Courier", 16), text_color="#39ff14").pack(pady=10)

    terminal = ctk.CTkTextbox(frame, width=460, height=180, font=("Courier", 12), text_color="#00ff41")
    terminal.pack(pady=30)
    lines = [
        "> Neural interface: ONLINE",
        "> Satellite uplink: SECURE",
        "> Ghost protocol: ACTIVATED",
        "> Loading mission briefing...",
        "> Target acquired.",
        "\n[ SYSTEM READY ]"
    ]
    for line in lines:
        terminal.insert("end", line + "\n")
        app.update()
        time.sleep(0.7)

# Login function
def login():
    if password_entry.get() == CORRECT_PASSWORD:
        status_label.configure(text="ACCESS GRANTED", text_color="#00ff00")
        app.after(1500, show_access_granted)
    else:
        status_label.configure(text="ACCESS DENIED", text_color="#ff0000")
        shake(frame, 6, 15)

# Shake effect
def shake(widget, n=6, d=15):
    if n == 0:
        widget.place(relx=0.5, rely=0.5, anchor="center")
        return
    x = d if n % 2 == 0 else -d
    widget.place(relx=0.5, rely=0.5, anchor="center", x=x)
    app.after(60, lambda: shake(widget, n-1, d))

# Login button
login_btn = ctk.CTkButton(frame, text=">> EXECUTE LOGIN <<", width=320, height=55,
                         font=("Courier", 18, "bold"), corner_radius=12,
                         fg_color="#002200", hover_color="#003300",
                         border_width=3, border_color="#00ff00",
                         command=login)
login_btn.pack(pady=40)

# Startup messages
def startup():
    msgs = ["Initializing quantum core...", "Bypassing NSA backdoor...", "Engaging stealth mode...", "Ready."]
    for msg in msgs:
        status_label.configure(text=msg, text_color="#00ff41")
        app.update()
        time.sleep(1.2)
    status_label.configure(text="Enter credentials.")

app.after(500, startup)

app.mainloop()
