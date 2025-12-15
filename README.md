**Notes Python** 

ide recommandé 
vscode 
pycharm 
mecanisme a acceder 
outil essentiels  : 
pip gestionnaire de paquent
venv  : environnemnt virtuel 
black : formatiage de code 
pytest : test unitaire 

porté des variable : 
# L - Local
def fonction():
x = "local"
print(x)

# E - Enclosing
def externe():
x = "enclosing"
def interne():
print(x) # Accède à enclosing
interne()

Global
x = "global"
def fonction():
print(x) # Accède à global

# B - Built-in
print(len([1,2,3])) # len est built-in
Fonctions et Module
Définition de Fonctions

# Fonction simple
def saluer(nom):
return f"Bonjour {nom}"
# Paramètres par défaut
def saluer(nom, titre="M."):
return f"Bonjour {titre} {nom}"
# Arguments nommés
resultat = saluer(nom="Dupont", titre="Dr.")
# Plusieurs retours
def divmod_custom(a, b):
quotient = a // b
reste = a % b
return quotient, reste
q, r = divmod_custom(17, 5)

importer des modules 
" exemples import" 

