# FILE_MANAGER PROJECT
# proposez a l'utilisateur si il veut crée, supprimer ou editer un fichier
#
import os.path

def file_manager():
    start = False
    while not start:
        print('1: Crée un fichier\n')
        print('2: Supprimer un fichier\n')
        print('3: Consulter un fichier\n')
        print('4: Quitter\n')
        ask = input('Choisir une des options ci-dessus :\n')
        if str(ask) == "1":
            ask_name = input('Donnez un nom a votre fichier : \n')
            file_name = os.path.join('repo', str(ask_name)+".txt")
            if os.path.exists(file_name):
                print('ERREUR: Un fichier posséde deja le même nom\n')
            else:
                file = open(file_name, 'w')
                ask_content = input('Écrire votre texte : \n')
                file.write(str(ask_content))
                file.close()
        elif str(ask) == "2":
            ask_file = input('Quel fichier voulez vous supprimer : \n')
            file_name = os.path.join('repo', str(ask_file)+".txt")
            if not os.path.exists(file_name):
                print("ERREUR: le fichier n'existe pas \n")
            else:
                os.remove(file_name)
        elif str(ask) == "3":
            ask_file = input('Quel fichier voulez vous consulter : \n')
            file_name = os.path.join('repo', str(ask_file)+".txt")
            if not os.path.exists(file_name):
                print("ERREUR: le fichier n'existe pas \n")
            else:
                file = open(file_name, "r")
                print(file.read())
                file.close()
        elif str(ask) == "4":
            print('Aurevoir ! \n')
            start = True
                
file_manager()