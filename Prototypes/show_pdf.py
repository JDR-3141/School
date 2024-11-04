
import tkinter as tk
from tkinterPdfViewer import tkinterPdfViewer as pdf
from os import getcwd
root = tk.Tk()
root.geometry("700x780")
d = pdf.ShowPdf().pdf_view(root, pdf_location=getcwd()+"\\Project\\Assets\\Test-Test1-Take2.pdf", width=100, height=100)
d.pack()
root.mainloop()