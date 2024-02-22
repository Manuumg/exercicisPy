class Empresa:
    def __init__(self):
        self.llista_clients = []
        self.id_client_proper = 1

    def get_llista_clients(self):
        for client in self.llista_clients:
            print(client)

    def afegir_client(self, nom, cognom, telefon, correu, ciutat):
        id_client = self.id_client_proper
        self.id_client_proper += 1
        client_nou = Client(id_client, nom, cognom, telefon, correu, ciutat)
        self.llista_clients.append(client_nou)

    def eliminar_client(self, id_client):
        for client in self.llista_clients:
            if client.id == id_client:
                self.llista_clients.remove(client)
                break
        else:
            print("No s'ha trobat cap client amb aquest identificador")

    def cercar_per_id(self, id_client):
        for client in self.llista_clients:
            if client.id == id_client:
                return client
        print("No s'ha trobat cap client amb aquest identificador")
        return None

    def cercar_per_nom(self, nom):
        clients_trobats = []
        for client in self.llista_clients:
            if client.nom == nom:
                clients_trobats.append(client)
        return clients_trobats

    def cercar_per_cognom(self, cognom):
        clients_trobats = []
        for client in self.llista_clients:
            if client.cognom == cognom:
                clients_trobats.append(client)
        return clients_trobats

    def modificar_client(self, id_client, nom=None, cognom=None, telefon=None, correu=None, ciutat=None):
        client = self.cercar_per_id(id_client)
        if client:
            if nom:
                client.nom = nom
            if cognom:
                client.cognom = cognom
            if telefon:
                client.telefon = telefon
            if correu:
                client.correu = correu
            if ciutat:
                client.ciutat = ciutat
            print("Client modificat amb èxit")
