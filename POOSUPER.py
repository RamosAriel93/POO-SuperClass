class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "El Vehiculo es de color {},y posee {} ruedas".format(self.color, self.ruedas)


class Automovil(Vehiculo):  # subclase que define a automoviles de uso particular

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "El Automovil es de color {},tiene una velocidad crucero de {} KM/H, cuenta con {} ruedas," \
               " y un motor de {} CC .".format(self.color, self.velocidad, self.ruedas, self.cilindrada)


class Camioneta(Automovil):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return "La Camioneta es de color {},tiene una velocidad crucero de {} KM/H, cuenta con {} ruedas,  un motor " \
               "de {} CC ,y una capacidad de carga de unos {} KG .".format(self.color, self.velocidad, self.ruedas, self.cilindrada, self.carga)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, estilo):
        super().__init__(color, ruedas)
        self.estilo = estilo

    def __str__(self):
        return "La Bicicleta es de color {},cuenta con {} ruedas, y posse estilo {}".format(self.color,
                                                                                                        self.ruedas,
                                                                                                        self.estilo)


class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, estilo, velocidad, cilindrada):
        super().__init__(color, ruedas, estilo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "La Motocicleta es de color {},tiene una velocidad crucero de {} KM/H, cuenta con {} ruedas, " \
               "y un motor de {} CC, ademas es de estilo {} ."\
            .format(self.color, self.velocidad, self.ruedas, self.cilindrada, self.estilo)


Toyota = Automovil("Rojo", 4, 150, 1400)
print(Toyota)

Suzuki = Motocicleta("Negra", 2, "urbana", 100, 125)
print(Suzuki)

Vairo = Bicicleta("Roja", 2, "Deportiva")
print(Vairo)

Parnet = Camioneta("Blanca", 4, 120, 1600, 250)
print(Parnet)
