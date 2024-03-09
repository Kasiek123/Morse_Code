import customtkinter as ctk
from morse_dict import morse_code_dict
from morse_alphabet import MorseAlphabet

ctk.set_appearance_mode("dark")


class MorseCode(ctk.CTk):
    """
        A Morse Code Translator application.

        This application provides functionality to encode or decode
    text to/from Morse code.
    """

    def __init__(self):
        super().__init__()

        self.title("Morse Code Translator")
        self.geometry("900x500")
        self.resizable(False, False)

        # Initialize variables
        self.morse_code_dict = morse_code_dict  # Dictionary storing letters as keys and corresponding Morse codes as values (used in encode and decode methods)
        self.radio_var = ctk.IntVar()   # Variable storing the value of the selected option (encode/decode) in the user interface (used in translate method)

        # create and configure widgets
        self.radiobutton_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.radiobutton_frame.grid(row=0, column=1, columnspan=3)

        self.button_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.button_frame.grid(row=0, column=0, rowspan=3)

        self.textbox_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.textbox_frame.grid(row=1, column=1, columnspan=2, rowspan=2)

        self.radiobutton_encode = ctk.CTkRadioButton(master=self.radiobutton_frame, text="Encode",
                                                     border_width_checked=3, variable=self.radio_var, value=0)
        self.radiobutton_encode.pack(side="left", padx=10, pady=10)

        self.radiobutton_decode = ctk.CTkRadioButton(master=self.radiobutton_frame, text="Decode",
                                                     border_width_checked=3, variable=self.radio_var, value=1)
        self.radiobutton_decode.pack(side="left", padx=10, pady=10)

        self.textbox = ctk.CTkTextbox(master=self.textbox_frame, width=700, height=200, font=("Arial", 13, "bold"))
        self.textbox.pack(padx=10, pady=10)

        self.textbox_result = ctk.CTkTextbox(master=self.textbox_frame, width=700, height=200, font=("Arial", 27))
        self.textbox_result.pack(padx=10, pady=10)

        self.translate_button = ctk.CTkButton(master=self.button_frame, text="Translate", font=("Arial", 15, "bold"),
                                              command=self.translate)
        self.translate_button.pack(padx=10, pady=10)

        self.button_clear = ctk.CTkButton(master=self.button_frame, text="Clear", font=("Arial", 15, "bold"),
                                          command=self.clear)
        self.button_clear.pack(padx=10, pady=10)

        self.alphabet_button = ctk.CTkButton(master=self.button_frame, text="Alphabet", font=("Arial", 15, "bold"),
                                             command=self.alphabet_window)
        self.alphabet_button.pack(padx=10, pady=10)

    def translate(self):
        """ Translates user input based on the selected option (encode/decode). """
        selected_option = self.radio_var.get()

        if selected_option == 0:
            self.encode()   # Encode if 'Encode' option is selected
        else:
            self.decode()   # Decode if 'Decode' option is selected

    def encode(self):
        """ Encodes the text entered by the user. """
        self.textbox_result.configure(state="normal")
        self.textbox_result.delete("1.0", ctk.END)

        # Check if the textbox is empty
        if not self.textbox.get("0.0", "end").upper().split():
            self.textbox_result.insert(index=0.0, text="Nothing to translate")
        else:
            # Encode each character in the textbox
            encoded_words = [
                '/' if word == '\n' else self.morse_code_dict[character]
                for word in self.textbox.get("0.0", "end").upper().strip()
                for character in word
            ]

            self.textbox_result.insert(index=0.0, text=" ".join(encoded_words))
        self.textbox_result.configure(state="disabled")

    def decode(self):
        """ Decodes the text entered by the user. """
        self.textbox_result.configure(state="normal")
        self.textbox_result.delete("1.0", ctk.END)

        # Check if the textbox contains only valid Morse code symbols
        if not all(i in self.morse_code_dict.values() for i in self.textbox.get("0.0", "end").upper().split()):
            self.textbox_result.insert(index=0.0,
                                       text='The text to be translated should contain only "." or "_" or "/"."')
        else:
            # Decode each Morse code symbol in the textbox
            decoded_words = [
                key for code in self.textbox.get("0.0", "end").split()
                for key, value in self.morse_code_dict.items() if code == value
            ]

            self.textbox_result.insert(index=0.0, text="".join(decoded_words).lower())

        self.textbox_result.configure(state="disabled")

    def clear(self):
        """ Clears the textbox. """
        self.textbox.delete("1.0", ctk.END)

    def alphabet_window(self):
        """ Displays the Morse Alphabet keyboard window. """
        MorseAlphabet(self.textbox)


if __name__ == "__main__":
    app = MorseCode()
    app.mainloop()
