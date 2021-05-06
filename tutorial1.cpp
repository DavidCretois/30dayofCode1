#include <iostream> // Permet de compiler l'entrée et la sortie (aussi library)
#include <string> // Pour installer la variable "String"
using namespace std; // Permet d'ajouter des variables, des types connus dans <iostream>

// 5 les plus importants variables : "int", "float", "bool", "string", "char"
/*
int : abréviation de "integer", est un type de variable fondamental intégré au compilateur et utilisé 
pour définir des variables numériques contenant des nombres entiers.

float : est un terme abrégé pour "virgule flottante". Par définition, il s'agit d'un type de données 
fondamental intégré au compilateur qui est 
utilisé pour définir des valeurs numériques avec des décimales flottantes.

bool true, false : Les variables de ce type ne peuvent prendre que deux valeurs : -1 et 0. En C++, ces valeurs correspondent 
à true et false et peuvent être utilisées de manière interchangeable.

string "7.0 " : type 

char 'x' '0' 'ss': Les variables de ce type ne peuvent prendre que deux valeurs : -1 et 0. En C++, ces valeurs correspondent 
à true et false et peuvent être utilisées de manière interchangeable.

cin is an objects of class iostream. it is used to accept the input from the standart input device i.e. keyboard
*/

int main() {
	cout << "Hello World";
}

// Résultat : Hello World


int main() {
	int x = 2.9;
	string y = "David";
	cout << y;
}
// Resultat 2 for x and y for David GO GO


int main() {
	int x, y;
	x = 7;
	y = 4;
	cout << x << y;
}


int main() {
	int n;
	cin >> n;
}