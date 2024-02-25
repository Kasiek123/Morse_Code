import customtkinter as ctk

ctk.set_appearance_mode("dark")


class MainGui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Morse Code")
        self.minsize(800, 500)

        self.morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
            ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
            '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
        }

        self.textbox = ctk.CTkTextbox(master=self,
                                      width=700,
                                      height=200,
                                      font=("Arial", 13, "bold"))
        self.textbox.pack(padx=10, pady=10)

        self.button_frame = ctk.CTkFrame(master=self,
                                         fg_color="transparent")
        self.button_frame.pack()

        self.button_encode = ctk.CTkButton(master=self.button_frame,
                                           text="Encode",
                                           command=self.encode)
        self.button_encode.pack(side="left", padx=10, pady=10)

        self.button_decode = ctk.CTkButton(master=self.button_frame,
                                           text="Decode",
                                           )
        self.button_decode.pack(side="left", padx=10, pady=10)

        self.textbox_result = ctk.CTkTextbox(master=self,
                                             width=700,
                                             height=200,
                                             font=("Arial", 20))
        self.textbox_result.pack(padx=10, pady=10)

    def encode(self):
        encoded_words = []
        self.textbox_result.delete("1.0", ctk.END)

        # tutaj pomysl zeby znalec tekst przed "\n" i go przetlumaczyc potem po "\n" i tez przetlumaczyc ale w nowej linijce
        for words in self.textbox.get("0.0", "end").upper().strip().split("\n"):
            for character in words:
                encoded_words.append(self.morse_code_dict[character])

        self.textbox_result.insert(index=0.0, text=" ".join(encoded_words))
        self.textbox_result.configure(state="disabled")


if __name__ == "__main__":
    app = MainGui()
    app.mainloop()
