import tkinter as tk
from googletrans import Translator  # Assuming you have googletrans library installed

class LanguageTranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Language Translator")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Enter text to translate:")
        self.label.pack(pady=10)

        self.input_text = tk.Entry(self)
        self.input_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.translate_button = tk.Button(self, text="Translate", command=self.translate)
        self.translate_button.pack(pady=5)

        self.output_label = tk.Label(self, text="")
        self.output_label.pack(pady=10)

    def translate(self):
        user_input = self.input_text.get()
        translated_text = self.perform_translation(user_input)
        self.output_label.config(text=f"Translated Text: {translated_text}")

    def perform_translation(self, text):
        translator = Translator()
        translated = translator.translate(text, src='en', dest='es')  # Translate from English to Spanish
        return translated.text

if __name__ == "__main__":
    app = LanguageTranslatorApp()
    app.mainloop()
