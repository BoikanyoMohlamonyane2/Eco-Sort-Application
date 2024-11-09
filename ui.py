import tkinter as tk
from camera import capture_until_object_detected
from qr_code import display_qr_code
from PIL import Image, ImageTk

class WasteManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("EcoSort")
        master.attributes('-fullscreen', True)  # Set the window to fullscreen
        master.configure(bg="#f2f2f2")

        # Banner Frame with increased height
        self.banner_frame = tk.Frame(master, bg="#4CAF50", height=150)
        self.banner_frame.pack(fill='x')

        # Load and display company logo in banner
        logo_image = Image.open(r"C:\Users\thama\Documents\Project\EcoSort-Application\images\web-cam.png")
        logo_image = logo_image.resize((60, 60))  # Adjust size if needed
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        self.logo_label = tk.Label(self.banner_frame, image=self.logo_photo, bg="#4CAF50")
        self.logo_label.pack(side="left", padx=20, pady=10)

        # Banner Label with text
        self.banner_label = tk.Label(
            self.banner_frame,
            text="EcoSort - Smart Waste Management",
            font=("Helvetica", 30, "bold"),  # Increased font size
            fg="white",
            bg="#4CAF50",
            pady=30
        )
        self.banner_label.pack(side="left")

        # Welcome label
        self.welcome_label = tk.Label(
            master,
            text="Welcome to EcoSort! Helping you manage waste efficiently and responsibly.",
            font=("Arial", 16),
            fg="#333333",
            bg="#f2f2f2",
            pady=20
        )
        self.welcome_label.pack()

        # Dump Waste Button
        self.dump_waste_button = tk.Button(
            master,
            text="Dump Waste",
            command=self.start_capture,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 18, "bold"),
            relief="raised",
            bd=5,
            activebackground="#45a049",
            cursor="hand2"
        )
        self.dump_waste_button.pack(pady=10, padx=10, fill='both', expand=True)

        # Register Button
        self.register_button = tk.Button(
            master,
            text="Register",
            command=self.register_action,
            bg="#2196F3",
            fg="white",
            font=("Arial", 18, "bold"),
            relief="raised",
            bd=5,
            activebackground="#1e88e5",
            cursor="hand2"
        )
        self.register_button.pack(pady=10, padx=10, fill='both', expand=True)

        # Label to display object detection details
        self.details_label = tk.Label(
            master,
            text="",
            font=("Arial", 14),
            fg="green",
            bg="#f2f2f2"
        )
        self.details_label.pack(pady=20)

        # Bind Escape key to exit fullscreen
        master.bind("<Escape>", self.exit_fullscreen)

    def start_capture(self):
        capture_until_object_detected("water bottle", self.details_label)

    def register_action(self):
        display_qr_code(self.master)

    def exit_fullscreen(self, event):
        self.master.attributes('-fullscreen', False)
