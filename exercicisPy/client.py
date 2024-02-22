class Client:
    def __init__(self, id, nom, cognom, telefon, correu, ciutat):
        self.id = id
        self.nom = nom
        self.cognom = cognom
        self.telefon = telefon
        self.correu = correu
        self.ciutat = ciutat
        
       
        if not re.match(r'^(\+\d{2}NN-)?\d{6,14}$', telefon):
            raise ValueError("El format del telèfon no és vàlid")
        
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correu):
            raise ValueError("El format del correu no és vàlid")
    
    def __str__(self):
        return f"Client(id={self.id}, nom={self.nom}, cognom={self.cognom}, telefon={self.telefon}, correu={self.correu}, ciutat={self.ciutat})"

