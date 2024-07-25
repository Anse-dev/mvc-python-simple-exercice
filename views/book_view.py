import tkinter as tk
from tkinter import ttk

class BookView:
  def __init__(self, root,controller) :
    self.root = root
    self.controller = controller
    self.frame = ttk.Frame(root)
    self.frame.grid(row=0,column=0)
    self.root.configure(bg='#f0f0f0')
    # Title
    self.title_label = ttk.Label(self.frame, text="Gestion des Livres",)
    self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # champ titre
    self.title_label = ttk.Label(self.frame, text="Titre")
    self.title_label.grid(row=2, column=0)
    self.title_entry = ttk.Entry(self.frame, width=30)
    self.title_entry.grid(row=2, column=1, padx=10, pady=5)

    # champ auteur
    self.author_label = ttk.Label(self.frame, text="Auteur")
    self.author_label.grid(row=3, column=0)
    self.author_entry = ttk.Entry(self.frame, width=30)
    self.author_entry.grid(row=3, column=1)

    #champ annee
    self.year_label = ttk.Label(self.frame, text="Année")
    self.year_label.grid(row=4, column=0,)
    self.year_entry = ttk.Entry(self.frame, width=30)
    self.year_entry.grid(row=4, column=1)
    #champ Type
    self.type_label = ttk.Label(self.frame, text="Type")
    self.type_label.grid(row=5, column=0,)
    self.type_entry = ttk.Entry(self.frame, width=30)
    self.type_entry.grid(row=5, column=1)
    #champ Id edition
    self.id_edition_label = ttk.Label(self.frame, text="id_edition")
    self.id_edition_label.grid(row=6, column=0,)
    self.id_edition_entry = ttk.Entry(self.frame, width=30)
    self.id_edition_entry.grid(row=6, column=1)

    self.add_button = ttk.Button(self.frame, text="Ajouter Livre", command=self.add_book, style="TButton")
    self.add_button.grid(row=7, column=0, columnspan=2, pady=20)

  def add_book(self):
      title = self.title_entry.get()
      author = self.author_entry.get()
      year = self.year_entry.get()
      type= self.type_entry.get();
      id_edi= self.id_edition_entry.get()

      if title and author and year:
        try:
          self.controller.add_livre(title,author, year,type, id_edi)
          self.root.destroy()
        except :
          pass # vider les champ

   