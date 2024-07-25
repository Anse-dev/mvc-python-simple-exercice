import json;

class Livre:
  def __init__(self,title, author,annee,type,id_edition):
    self.title= title;
    self.author= author;
    self.annee=annee;
    self.type= type;
    self.id_edition= id_edition;
  
  def load_from_file():
    pass

  def format_to_dictionnaire(self):
      user_dict= {
            "title": self.title,
            "author": self.author,
            "annee": self.annee,
            "type": self.type,
            "id_edition":self. id_edition
      }
      return user_dict;
    
  @staticmethod
  def save_livre(self,nom_du_fichier='./data/livres.json'):
    try:
      with open(nom_du_fichier,'r') as file :
        livres= json.load(file)
    except FileNotFoundError:
      livres=[]

    if not any(livre['title']== self.title and livre['id_edition']== self.id_edition   for livre in livres):
      livres.append(self.format_to_dictionnaire());

    with open(nom_du_fichier,'w') as file :
      json.dump(livres,file, indent=4)
      print('livre enregistrer ')

  
  def update_livre(self,id, nouvelle_annee ,nom_du_fichier='./data/livres.json'):
    try:
      with open(nom_du_fichier,'r') as file :
        livres= json.load(file)
    except FileNotFoundError:
      print("Le fichier n'existe pas.")
      return;
    livre_trouve= False;

    for livre in livres:
      if livre['id_edition'] == id:
        livre['annee']= nouvelle_annee;
        livre_trouve=True;
        break;
    if livre_trouve:
      with open(nom_du_fichier,'w') as file :
          json.dump(livres,file, indent=4)
          print('livre modifieee ')



