import random

class Cliente:

    def __init__(self,dni, nombreCompleto, nroCelular):
        self._dni = dni
        self._nombreCompleto = nombreCompleto
        self._nroCelular = nroCelular

    def getNombre(self):
        return self._nombreCompleto

    def esCliente(self):
        return True




def crearCliente():
    nombres = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Charlotte", "William",
               "Sophia", "James", "Amelia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Harper",
               "Alexander", "Evelyn", "Michael", "Abigail", "Daniel", "Emily", "Matthew"]
    apellidos = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson",
                 "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Clark", "Lewis", "Walker",
                 "Hall", "Young", "King", "Scott", "Green", "Adams", "Baker"]
    v_clientes = []
    i = 0
    for i in range(20):
        nombreCompleto = random.choice(nombres) + " " + random.choice(apellidos)
        dni = random.randint(3000000, 50000000)
        nroCelular = "+54351" + str(random.randint(2000000, 9999999))
        clientes = Cliente(dni, nombreCompleto, nroCelular)
        v_clientes.append(clientes)
    return v_clientes

