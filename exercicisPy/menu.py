from empresa import Empresa

class Menu:
    def __init__(self):
        self.empresa = Empresa()

    def run(self):
        while True:
            option = self.mostra_menu_principal()
            if option == '1':
                self.afegir_client()
            elif option == '2':
                self.eliminar_client()
            elif option == '3':
                self.consultar_client()
            elif option == '4':
                self.modificar_client()
            elif option == '5':
                print("Sortint del programa...")
                break
            else:
                print("Opció no vàlida. Si us plau, tria una opció vàlida.")

    def mostra_menu_principal(self):
        print("\nMENU PRINCIPAL")
        print("=======================================")
        print("1. Afegir client")
        print("2. Eliminar client")
        print("3. Consultar client")
        print("4. Modificar client")
        print("5. Sortir")
        option = input("Escull una opció: ")
        return option

    def mostra_menu_consulta(self):
        print("\nMENU CONSULTA")
        print("=======================================")
        print("1. Cerca per ID")
        print("2. Cerca per Nom")
        print("3. Cerca per Cognom")
        print("4. Tornar al menú principal")
        option = input("Escull una opció: ")
        return option

    def afegir_client(self):
        print("\nAfegir Client:")
        nom = input("Nom: ")
        cognom = input("Cognom: ")
        telefon = input("Telèfon: ")
        correu = input("Correu electrònic: ")
        ciutat = input("Ciutat: ")
        try:
            self.empresa.afegir_client(nom, cognom, telefon, correu, ciutat)
            print("Client afegit amb èxit!")
        except ValueError as e:
            print(e)

    def eliminar_client(self):
        print("\nEliminar Client:")
        id_client = input("ID del client a eliminar: ")
        self.empresa.eliminar_client(id_client)

    def consultar_client(self):
        while True:
            option = self.mostra_menu_consulta()
            if option == '1':
                id_client = input("ID del client a cercar: ")
                client = self.empresa.cercar_per_id(id_client)
                if client:
                    print(client)
            elif option == '2':
                nom = input("Nom del client a cercar: ")
                clients = self.empresa.cercar_per_nom(nom)
                if clients:
                    for client in clients:
                        print(client)
            elif option == '3':
                cognom = input("Cognom del client a cercar: ")
                clients = self.empresa.cercar_per_cognom(cognom)
                if clients:
                    for client in clients:
                        print(client)
            elif option == '4':
                break
            else:
                print("Opció no vàlida. Si us plau, tria una opció vàlida.")

    def modificar_client(self):
        print("\nModificar Client:")
        id_client = input("ID del client a modificar: ")
        nom = input("Nou nom (deixa en blanc si no vols modificar): ")
        cognom = input("Nou cognom (deixa en blanc si no vols modificar): ")
        telefon = input("Nou telèfon (deixa en blanc si no vols modificar): ")
        correu = input("Nou correu electrònic (deixa en blanc si no vols modificar): ")
        ciutat = input("Nova ciutat (deixa en blanc si no vols modificar): ")
        self.empresa.modificar_client(id_client, nom, cognom, telefon, correu, ciutat)


if __name__ == "__main__":
    menu = Menu()
    menu.run()
