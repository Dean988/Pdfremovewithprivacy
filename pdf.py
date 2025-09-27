import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image, ImageTk

class PDFPageRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Page Remover")
        self.root.geometry("500x300") # Increased window size to accommodate images

        self.pdf_path = tk.StringVar()
        self.page_number = tk.StringVar()

        self.load_images()

        # File selection frame
        file_frame = tk.LabelFrame(root, text="Seleziona File PDF")
        file_frame.pack(pady=10, padx=10, fill="x")

        self.file_entry = tk.Entry(file_frame, textvariable=self.pdf_path, width=40)
        self.file_entry.pack(side="left", padx=5, pady=5, expand=True, fill="x")
        self.browse_button = tk.Button(file_frame, text="Sfoglia", command=self.browse_pdf)
        self.browse_button.pack(side="right", padx=5, pady=5)

        # Page number frame
        page_frame = tk.LabelFrame(root, text="Numero Pagina da Rimuovere")
        page_frame.pack(pady=5, padx=10, fill="x")

        self.page_label = tk.Label(page_frame, text="Pagina (1-based):")
        self.page_label.pack(side="left", padx=5, pady=5)
        self.page_entry = tk.Entry(page_frame, textvariable=self.page_number, width=10)
        self.page_entry.pack(side="left", padx=5, pady=5)

        # Action buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.remove_button = tk.Button(button_frame, text="Rimuovi Pagina", image=self.delete_icon, compound=tk.LEFT, command=self.remove_page)
        self.remove_button.pack(side="left", padx=10)

        self.exit_button = tk.Button(button_frame, text="Esci", image=self.exit_icon, compound=tk.LEFT, command=root.quit)
        self.exit_button.pack(side="left", padx=10)

    def load_images(self):
        import os
        images_dir = "images"
        if not os.path.exists(images_dir):
            os.makedirs(images_dir, exist_ok=True)

        try:
            self.delete_image_raw = Image.open(os.path.join(images_dir, "delete_icon.png"))
            self.delete_icon = ImageTk.PhotoImage(self.delete_image_raw.resize((24, 24), Image.Resampling.LANCZOS))

            self.exit_image_raw = Image.open(os.path.join(images_dir, "exit_icon.png"))
            self.exit_icon = ImageTk.PhotoImage(self.exit_image_raw.resize((24, 24), Image.Resampling.LANCZOS))
        except FileNotFoundError:
            messagebox.showwarning("Avviso Immagini", "Impossibile trovare le icone (delete_icon.png, exit_icon.png) nella cartella 'images'. L'interfaccia userà solo il testo.")
            self.delete_icon = None
            self.exit_icon = None
        except Exception as e:
            messagebox.showwarning("Avviso Immagini", f"Errore nel caricamento delle immagini: {e}. L'interfaccia userà solo il testo.")
            self.delete_icon = None
            self.exit_icon = None

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.pdf_path.set(file_path)

    def remove_page(self):
        pdf_file_path = self.pdf_path.get()
        page_to_remove_str = self.page_number.get()

        if not pdf_file_path:
            messagebox.showerror("Errore", "Seleziona un file PDF.")
            return

        if not page_to_remove_str:
            messagebox.showerror("Errore", "Inserisci il numero di pagina da rimuovere.")
            return

        try:
            page_to_remove = int(page_to_remove_str)
            if page_to_remove <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Errore", "Il numero di pagina deve essere un intero positivo.")
            return

        try:
            reader = PdfReader(pdf_file_path)
            writer = PdfWriter()

            num_pages = len(reader.pages)

            if page_to_remove > num_pages:
                messagebox.showerror("Errore", f"La pagina {page_to_remove} non esiste. Il PDF ha {num_pages} pagine.")
                return

            for i in range(num_pages):
                if i != page_to_remove - 1:
                    writer.add_page(reader.pages[i])

            output_pdf_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
                title="Salva il PDF modificato come"
            )

            if output_pdf_path:
                with open(output_pdf_path, "wb") as output_pdf_file:
                    writer.write(output_pdf_file)
                messagebox.showinfo("Successo", f"Pagina {page_to_remove} rimossa con successo. Salvato come {output_pdf_path}")
            else:
                messagebox.showinfo("Annullato", "Operazione di salvataggio annullata.")

        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFPageRemoverApp(root)
    root.mainloop()
