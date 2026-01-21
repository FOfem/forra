import customtkinter as ctk
from datetime import datetime

##################################################
#                                                #
#   FORRACORP. LTD | THE X-THEME SENTINEL 2.3    #
#   Feature: Chrono-Logic & Triple Static Theme  #
#   Principal Architect: Ubi Fredrick            #
#                                                #
##################################################

class DigitalSentinel(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Orchestration ---
        self.title("ForraCorp Digital Sentinel")
        self.geometry("1450x750")
        
        # UI Hierarchy
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # --- Theme Definitions ---
        self.THEMES = {
            "System": "system",
            "Dark": "dark",
            "Light": "light"
        }
        self.mode = ctk.StringVar(value="Static") # Static or Dynamic

        # --- UI Components ---
        # 1. Temporal Display
        self.date_label = ctk.CTkLabel(self, text="", font=("Boulder", 85, "bold", "italic"), text_color="#C0C0C0")
        self.date_label.grid(row=0, column=0, pady=(20, 0), sticky="s")

        self.time_label = ctk.CTkLabel(self, text="", font=("Boulder", 312, "bold"))
        self.time_label.grid(row=1, column=0, pady=0, sticky="n")

        # 2. Control Panel (Frame for Buttons)
        self.control_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.control_frame.grid(row=2, column=0, pady=20)

        # Static Theme Selectors
        self.btn_system = ctk.CTkButton(self.control_frame, text="SYSTEM", width=120, command=lambda: self.set_static("System"))
        self.btn_system.grid(row=0, column=0, padx=10)

        self.btn_dark = ctk.CTkButton(self.control_frame, text="DARK", width=120, fg_color="#131339", command=lambda: self.set_static("Dark"))
        self.btn_dark.grid(row=0, column=1, padx=10)

        self.btn_light = ctk.CTkButton(self.control_frame, text="LIGHT", width=120, fg_color="#E6E6FF", text_color="black", command=lambda: self.set_static("Light"))
        self.btn_light.grid(row=0, column=2, padx=10)

        # Dynamic Mode Toggle
        self.dyn_toggle = ctk.CTkSwitch(self.control_frame, text="DYNAMIC CHRONO-MODE", command=self.toggle_mode, font=("Boulder", 18))
        self.dyn_toggle.grid(row=1, column=0, columnspan=3, pady=20)

        self.update_sentinel()

    def set_static(self, theme_key):
        self.mode.set("Static")
        self.dyn_toggle.deselect()
        ctk.set_appearance_mode(self.THEMES[theme_key])

    def toggle_mode(self):
        if self.dyn_toggle.get() == 1:
            self.mode.set("Dynamic")
        else:
            self.mode.set("Static")

    def update_sentinel(self):
        now = datetime.now()
        hour = now.hour

        # --- Dynamic Theme Logic ---
        if self.mode.get() == "Dynamic":
            if 6 <= hour < 18:
                ctk.set_appearance_mode("light")
            else:
                ctk.set_appearance_mode("dark")

        # Update Display
        self.time_label.configure(text=now.strftime("%H:%M:%S"))
        self.date_label.configure(text=now.strftime("%A, %B %d, %Y").upper())
        self.after(200, self.update_sentinel)

if __name__ == "__main__":
    app = DigitalSentinel()
    app.mainloop()