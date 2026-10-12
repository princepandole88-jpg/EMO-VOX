# gui_wireframe.py - EMO-VOX UI Mockup
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class EmoVoxUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EMO-VOX Companion")
        self.geometry("380x520")
        
        # Header / Status Badge
        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.pack(fill="x", padx=10, pady=10)
        
        self.status_label = ctk.CTkLabel(self.header_frame, text="Status: Active | Emotion: Neutral", font=("Arial", 12, "bold"))
        self.status_label.pack(pady=5)
        
        # Conversation History Output Area
        self.chat_history = ctk.CTkTextbox(self, width=350, height=340)
        self.chat_history.pack(padx=10, pady=5)
        self.chat_history.insert("0.0", "EMO-VOX: Hello! I am online and tracking your mood.\n\n")
        
        # Bottom Input Controls
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(fill="x", padx=10, pady=10)
        
        self.mic_button = ctk.CTkButton(self.input_frame, text="🎤 Speak", width=80)
        self.mic_button.pack(side="left", padx=5)
        
        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Type message...")
        self.entry.pack(side="right", fill="x", expand=True, padx=5)

if __name__ == "__main__":
    app = EmoVoxUI()
    app.mainloop()

