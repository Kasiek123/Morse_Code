import customtkinter as ctk
from morse_dict import morse_code_dict
from functools import partial


class MorseAlphabet(ctk.CTkToplevel):
    """
        This class creates a new window with buttons for each letter
    in the Morse code dictionary.

        When button is pressed, the corresponding Morse code is
    inserted into the textbox.
    """
    def __init__(self, textbox):
        super().__init__()

        self.geometry("260x250")
        self.resizable(False, False)

        self.morse_code_dict = morse_code_dict  # Morse code dictionary
        self.textbox = textbox  # Textbox for user input

        # Framge to hold the buttons
        self.buttons_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.buttons_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        row = 0
        column = 0
        # Create a button for each letter in the Morse code dictionary
        for key in self.morse_code_dict:
            ctk.CTkButton(master=self.buttons_frame, text=key, width=30, border_spacing=5,
                          command=partial(self.write_letter, letter=key)).grid(row=row, column=column)

            column += 1
            # Move to the next row after every 8th button
            if column == 8:
                row += 1
                column = 0

    def write_letter(self, letter):
        """
            This method is the command for each button. It inserts
        the Morse code for the selected letter into the textbox.
        """
        self.textbox.insert(index=ctk.END, text=(self.morse_code_dict[letter] + " "))