class Usuario:
    def __init__(self, codigo, tipo, dinero, nivel, puntaje):
        self.codigo = codigo
        self.tipo = tipo.strip()
        self.dinero = int(dinero)
        self.nivel = int(nivel)
        self.puntaje = int(puntaje)

def leer_jugadores(archivo):
    jugadores = []
    with open(archivo, 'r') as file:
        for linea in file:
            datos = linea.strip().split(',')
            if len(datos) == 5:
                jugador = Usuario(*datos)
                jugadores.append(jugador)
    return jugadores

def agrupar_por_tipo(jugadores):
    grupos = {}
    for jugador in jugadores:
        tipo = jugador.tipo
        if tipo in grupos:
            grupos[tipo].append(jugador)
        else:
            grupos[tipo] = [jugador]
    return grupos

def ordenar_por_nivel(grupos):
    for tipo in grupos:
        jugadores = grupos[tipo]
        for i in range(len(jugadores)):
            for j in range(i + 1, len(jugadores)):
                if jugadores[i].nivel < jugadores[j].nivel:
                    jugadores[i], jugadores[j] = jugadores[j], jugadores[i]

def guardar_en_archivos(grupos):
    for tipo, jugadores in grupos.items():
        with open(f"{tipo}.csv", 'w') as archivo:
            archivo.write("Codigo,Tipo,Dinero,Nivel,Puntaje\n")
            for jugador in jugadores:
                archivo.write(f"{jugador.codigo},{jugador.tipo},{jugador.dinero},{jugador.nivel},{jugador.puntaje}\n")

def main():
    jugadores = leer_jugadores('datosusuario.csv')
    grupos = agrupar_por_tipo(jugadores)
    ordenar_por_nivel(grupos)
    guardar_en_archivos(grupos)

if __name__ == "__main__":
    main()
