import customtkinter as ctk
from tkinter import PhotoImage, Label
import time

# Fake password
CORRECT_PASSWORD = "192919"

# App setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("T.A.S.C - Classified Access Terminal")
app.geometry("1000x700")           # Perfect size
app.resizable(True, True)           # Minimize/Maximize buttons enabled
app.minsize(900, 650)

# Background image (optional)
try:
    bg_image = PhotoImage(file="tasc_bg.jpg")
    bg_label = Label(app, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    app.configure(bg="#000000")

# Main Frame — width & height ab sirf constructor mein
main_frame = ctk.CTkFrame(
    master=app,
    width=560,
    height=680,
    corner_radius=20,
    fg_color="#0a0a0a",
    border_width=4,
    border_color="#00ff00"
)
main_frame.place(relx=0.5, rely=0.5, anchor="center")
main_frame.pack_propagate(False)   # Yeh zaroori hai fixed size ke liye

# ==================== SAB CONTENT YAHAN ====================

title = ctk.CTkLabel(main_frame, text="T.A.S.C", font=("Orbitron", 80, "bold"), text_color="#00ff41")
title.pack(pady=(40, 5))

subtitle = ctk.CTkLabel(main_frame, text="Tactical Advanced Strategic Command",
                        font=("Courier New", 16), text_color="#00ff00")
subtitle.pack(pady=(0, 25))

welcome = ctk.CTkLabel(main_frame, text="» WELCOME TO T.A.S.C «",
                       font=("Consolas", 20, "bold"), text_color="#39ff14")
welcome.pack(pady=10)

ctk.CTkLabel(main_frame, text="AGENT ID", font=("Courier", 16, "bold"), text_color="#00ff00").pack(pady=(30,5))
username_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter username...", width=340, height=50,
                              font=("Courier", 14), corner_radius=12)
username_entry.pack(pady=5)

ctk.CTkLabel(main_frame, text="PASSCODE", font=("Courier", 16, "bold"), text_color="#00ff00").pack(pady=(20,5))
password_entry = ctk.CTkEntry(main_frame, placeholder_text="      ", width=340, height=50, show="•",
                              font=("Courier", 14), corner_radius=12)
password_entry.pack(pady=5)

status_label = ctk.CTkLabel(main_frame, text="", font=("Courier", 16), text_color="#ff0000")
status_label.pack(pady=15)

# Shake animation
def shake():
    def move(count=10, distance=15):
        if count == 0:
            main_frame.place(relx=0.5, rely=0.5, anchor="center")
            return
        offset = distance if count % 2 == 0 else -distance
        main_frame.place(relx=0.5, rely=0.5, anchor="center", x=offset)
        app.after(50, lambda: move(count-1, distance))
    move()

# Login function
def login():
    if password_entry.get() == CORRECT_PASSWORD:
        status_label.configure(text="ACCESS GRANTED", text_color="#00ff00")
        app.after(1500, show_access_granted)
    else:
        status_label.configure(text="ACCESS DENIED - INTRUDER ALERT", text_color="#ff0000")
        shake()

# Login button
login_btn = ctk.CTkButton(main_frame, text=">> EXECUTE LOGIN <<", width=340, height=60,
                          font=("Courier", 20, "bold"), corner_radius=15,
                          fg_color="#001100", hover_color="#003300",
                          border_width=4, border_color="#00ff00",
                          command=login)
login_btn.pack(pady=30)

# Enter key se login
password_entry.bind("<Return>", lambda e: login())
username_entry.bind("<Return>", lambda e: login())

# Access Granted Screen
def show_access_granted():
    for widget in main_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(main_frame, text="ACCESS GRANTED", font=("Orbitron", 60, "bold"), text_color="#00ff00").pack(pady=80)
    ctk.CTkLabel(main_frame, text="CLASSIFIED LEVEL: OMEGA", font=("Courier", 22), text_color="#00ff41").pack(pady=20)
    ctk.CTkLabel(main_frame, text="Agent authenticated. Welcome back, Commander.",
                 font=("Courier", 16), text_color="#39ff14").pack(pady=10)

    terminal = ctk.CTkTextbox(main_frame, width=500, height=200, font=("Courier", 13), text_color="#00ff41",
                        fg_color="#000000", corner_radius=15)
    terminal.pack(pady=30)

    lines = [
        "> Neural interface: ONLINE",
        "> Satellite uplink: SECURE",
        "> Ghost protocol: ACTIVATED",
        "> Loading mission briefing...",
        "> Target acquired.",
        "\n[ SYSTEM READY - AWAITING ORDERS ]"
    ]
    def type_line(i=0):
        if i < len(lines):
            terminal.insert("end", lines[i] + "\n")
            app.update()
            app.after(800, lambda: type_line(i+1))
    type_line()

# Startup messages
def startup():
    msgs = [
        "Initializing quantum core...",
        "Bypassing NSA backdoor...",
        "Engaging stealth mode...",
        "System online. Awaiting credentials..."
    ]
    def show(i=0):
        if i < len(msgs):
            status_label.configure(text=msgs[i], text_color="#00ff41")
            app.after(1400, lambda: show(i+1))
        else:
            status_label.configure(text="Enter credentials to continue.", text_color="#00ff41")
    show()

# Run startup & focus
app.after(800, startup)
app.after(100, lambda: password_entry.focus())

app.mainloop()
