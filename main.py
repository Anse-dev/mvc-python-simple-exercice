from tkinter import *;
from views.book_view import BookView;
from controllers.book_controller import LivreController
class MainApplicatin :
  def __init__(self,root) -> None:
    self.root= root;
    self.root.title('Gestion de Bibliotheque')
    self.root.geometry("700x600")
    self.controller= LivreController(self.root)
    BookView(self.root,self.controller)


if __name__ == '__main__':
    root= Tk();
    app= MainApplicatin(root);
    root.mainloop();