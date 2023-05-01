def affiche_menu():
	print("""*************
[M] Menu principal
[LG] Liste des Genres
[LL] Liste des Livres
[NG] Nouveau Genre
[NL] Nouveau Livre
[SG] Suppresion d'un Genre
[SL] Suppresion d'un Livre
[Q] Quitter le programme et sauvgarder la base de donnée
*************""") 

def nouveau_genre(obj_bibli:object):
	genre = input("Donnez un nouveau genre: ")
	try: 
		obj_bibli.ajoute_genre(genre)
	except ValueError:
		print("Le genre '{}' existe déjà !".format(genre))

def nouveau_livre(obj_biblio:object): 
	titre = input("Titre :") 
	annee = input("Année :") 
	genre = input("Genre :") 
	
	if not obj_biblio.genre_existe(genre): 
		print("Le genre n'existe pas")
		choix = input("Voulez vous ajouter ce genre à la bibliothèque ? ")
		if choix.lower() in ["oui", "o",  "y", "yes"]: 
			obj_biblio.ajoute_genre(genre)
		else:
			print("Le livre ne va donc pas être ajouté a la bibliothèque.")

	obj_biblio.ajoute_livre(titre, annee, genre)

def affiche_genre(obj_biblio:object):
	print("Tout les genres de livres dans la biblioothèque ({}):{}".format(len(obj_biblio.genre),obj_biblio.affiche_genre()))

def supp_genre(obj_biblio:object): 
	genre = input("Quel genre voulez vous supprimer: ")
	try: 
		obj_biblio.supp_genre(genre)
		print("Le genre '{}' a bien été supprimé.".format(genre))
	except ValueError: 
		print("Le genre n'est pas dans la bibliothèque.")
	

def supp_livre(obj_biblio:object): 
	livre = input("Quel livre voulez vous supprimer: ")
	if obj_biblio.supp_livre(livre) != None: 
		print("Le livre '{}' a bien été supprimé.".format(livre))
	else: print("Le livre n'est pas dans la bibliothèque.") 
	

def save(obj_biblio:object):
	obj_biblio.save() 
