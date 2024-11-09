import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def display_qr_code(parent):
    qr_data = "EcoSort Registration: Scan to Register"
    qr_img = qrcode.make(qr_data)
    qr_img = qr_img.resize((300, 300))
    qr_code_image = ImageTk.PhotoImage(qr_img)

    qr_window = tk.Toplevel(parent)
    qr_window.title("EcoSort - Registration QR Code")
    qr_window.geometry("400x400")
    qr_window.configure(bg="#f2f2f2")
    center_window(qr_window)

    qr_code_label = tk.Label(qr_window, image=qr_code_image, bg="#f2f2f2")
    qr_code_label.image = qr_code_image  # Keep reference
    qr_code_label.pack(expand=True, fill='both')

    qr_window.after(8000, qr_window.destroy)

def center_window(window):
    window.update_idletasks()  # Update "requested size" from geometry manager
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
