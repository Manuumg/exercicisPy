
class menu :

  def run(self):
        option = self.mostra_menu_principal()
        while option != '3':
            if option == '1':
                self.mostra_menu_consulta()
            elif option == '2':
                print("Executant alguna altra funcionalitat...")
            else:
                print("Opció invàlida. Torna a intentar-ho.")
            option = self.mostra_menu_principal()
        print("Programa finalitzat.")

  def mostra_menu_principal(self):
        print("MENU PRINCIPAL")
        print("=======================================")
        print("Seleccioni una opció i premi intro")
        print("=======================================")
        print("1. Afegir client")
        print("2. Elimianr client")
        print("3. Consultar client ")
        print("4. Modificar un camp d'un client")
        print("5. Sortir")
        option = input("Escull una opció: ")
        return option
  
  def mostra_menu_consulta(self):
      print("MENU CONSULTA")
      print("====================================")
      print("Seleccioni una opció i premi intro")
      print("===================================")
      print("1. Cercar client per Identificador ")
      print("2. Cercar client per Nom")
      print("3. Cercar client per Identificador ")
      print("4. Cercar client per Identificador ")
      print("5. Cercar client per Identificador ")



       
    



