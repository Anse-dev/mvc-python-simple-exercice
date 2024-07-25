from models.Livre import Livre

class LivreController:
    def __init__(self, root):
        self.root = root
        self.livres = []

    def get_livres(self):
        return self.livres

    def add_livre(self, title, author, year,type,id_edition):
        livre = Livre(title, author, year,type,id_edition)
        # self.livres.append(livre)
        Livre.save_livre(livre)
