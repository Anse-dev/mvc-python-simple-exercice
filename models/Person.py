import json;
#Entity or model
class Person:
  def __init__(self,nom, prenoms,age,id):
    self.nom= nom;
    self.prenoms=prenoms;
    self.age= age;
    self.id= id;

  def to_dict(self):
    return {
      'nom':self.nom,
      'prenoms':self.prenoms
    }

  def se_presenter(self):
    print("Je m'appelle {}".format(self.nom))

  def changer_nom(self,nouveau_nom):
    self.nom=nouveau_nom;


  def enregister_user(self):
    #Ouverture du fichier avec le mode ecriture (W)
    with open('./data/user.json','w')  as fichier:
      user_dict= self.to_dict();
      json.dump(user_dict,fichier,indent=4);
      print('User cree ')



personne_jean=  Person('Jean','Kouakou Martin',14,1)

personne_jean.enregister_user()