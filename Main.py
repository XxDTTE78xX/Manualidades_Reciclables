import Manualidades_1
import Manualidades_2
import Manualidades_3

print("--- MENU DE MANUALIDADES ECOLOGICAS ---")
print("1. Porta-lapices (Facil)")
print("2. Maceta (Media)")
print("3. Organizador (Dificil)")

opcion = input("Elige una opcion (1-3): ")

if opcion == "1":
    Manualidades_1.ejecutar()
elif opcion == "2":
    Manualidades_2.ejecutar()
elif opcion == "3":
    Manualidades_3.ejecutar()
else:
    print("Opcion no valida.")
