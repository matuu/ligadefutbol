import csv
import os

from datetime import datetime

from ligafutbol.models import DBSession
from ligafutbol.models import Club, Jugador

CLUB_PATH = os.path.join(os.path.abspath('.'), 'importar', 'clubes.csv')
JUGADOR_PATH = os.path.join(os.path.abspath('.'), 'importar', 'jugadores.csv')


def parse2date(string):
    return datetime.strptime(string, "%d/%m/%Y")

if __name__ == '__main__':
    if not os.path.isfile(CLUB_PATH):
        raise RuntimeError("Por favor, coloque el csv de los clubes en la carpeta importar.")
    if not os.path.isfile(JUGADOR_PATH):
        raise RuntimeError("Por favor, coloque el csv de los jugadores en la carpeta importar.")
    db = DBSession()
    # import clubes
    with open(CLUB_PATH, newline='') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in dataReader:
            if row[0] != 'NRO':
                club = Club(numero=row[0], nombre=row[1])
                db.add(club)
                db.commit()
    db.close()
    db = DBSession()
    i = 0
    with open(JUGADOR_PATH, newline='') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in dataReader:
            if row[0] != 'APE':
                i += 1
                jug = Jugador(apellido=row[0], nombre=row[1])
                jug.fecha_nac = parse2date(row[2])
                jug.lugar_nac = row[3]
                jug.provincia = row[4]
                jug.dni = int(row[5])
                jug.domicilio = row[6]
                jug.club_id = int(row[7])
                jug.fecha_inscripcion = parse2date(row[8])
                jug.division = int(row[12])
                # observaciones -> 9 10 11 13 14
                obsers = (row[9], row[10], row[11], row[13], row[14])
                jug.observaciones = "\n ".join([x for x in obsers if len(x) > 0])
                db.add(jug)
                if i % 500 == 0:
                    db.commit()
    db.commit()
    db.close()
