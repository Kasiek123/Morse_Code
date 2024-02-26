import customtkinter as ctk

ctk.set_appearance_mode("dark")


class MorseCode(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Morse Code")
        self.minsize(800, 500)

        self.morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            'Ą': '.-.-', 'Ć': '-.-..', 'Ę': '..-..', 'Ł': '.-..-', 'Ń': '--.--', 'Ó': '---.', 'Ś': '...-...',
            'Ż': '--..-.', 'Ź': '--..-',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
            ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
            '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
        }

        self.textbox = ctk.CTkTextbox(master=self, width=700, height=200, font=("Arial", 13, "bold"))
        self.textbox.pack(padx=10, pady=10)

        self.button_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.button_frame.pack()

        self.button_encode = ctk.CTkButton(master=self.button_frame, text="Encode", command=self.encode)
        self.button_encode.pack(side="left", padx=10, pady=10)

        self.button_decode = ctk.CTkButton(master=self.button_frame, text="Decode", command=self.decode)
        self.button_decode.pack(side="left", padx=10, pady=10)

        self.button_clear = ctk.CTkButton(master=self.button_frame, text="Clear", command=self.clear)
        self.button_clear.pack(side="left", padx=10, pady=10)

        self.textbox_result = ctk.CTkTextbox(master=self, width=700, height=200, font=("Arial", 27))
        self.textbox_result.pack(padx=10, pady=10)

    def encode(self):
        self.textbox_result.configure(state="normal")
        self.textbox_result.delete("1.0", ctk.END)
        encoded_words = []

        for words in self.textbox.get("0.0", "end").upper().strip():
            if words == "\n":
                encoded_words.append("/")
            else:
                for character in words:
                    encoded_words.append(self.morse_code_dict[character])

        self.textbox_result.insert(index=0.0, text=" ".join(encoded_words))
        self.textbox_result.configure(state="disabled")

    def decode(self):
        self.textbox_result.configure(state="normal")
        self.textbox_result.delete("1.0", ctk.END)
        decoded_words = []
        for code in self.textbox.get("0.0", "end").split():
            decoded_words += [key for key, value in self.morse_code_dict.items() if code == value]

        self.textbox_result.insert(index=0.0, text="".join(decoded_words).lower())

    def clear(self):
        self.textbox.delete("1.0", ctk.END)


if __name__ == "__main__":
    app = MorseCode()
    app.mainloop()
