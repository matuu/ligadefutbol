import base64
import os
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, func, Text
from sqlalchemy.orm import relationship, sessionmaker, backref, scoped_session
from sqlalchemy import create_engine


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __mapper_args__ = {'always_refresh': True}

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())

Base = declarative_base(cls=Base)

DATABASE_PATH = 'ligadefutbol.db'
DATABASE_CONNECTION_INFO = 'sqlite:///' + DATABASE_PATH
db_engine = create_engine(DATABASE_CONNECTION_INFO, echo=False)
DBSession = scoped_session(sessionmaker(autoflush=True, autocommit=False, bind=db_engine))


class Club(Base):
    """
    Un club deportivo
    """
    numero = Column(Integer, nullable=False)
    nombre = Column(String(255))

    def verify(self):
        errors = []
        if not self.numero:
            errors.append("El campo número es obligatorio.")
        if not self.nombre:
            errors.append("El campo nombre es obligatorio.")
        return errors

    def __repr__(self):
        return "{} - {}".format(self.numero, self.nombre)


class Jugador(Base):
    """
    Una persona inscripta en la liga como jugador de algún club.
    """
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    # Nacimiento
    fecha_nac = Column(DateTime)
    lugar_nac = Column(String(255))
    provincia = Column(String(64))
    # Actual
    dni = Column(Integer)
    domicilio = Column(String(255))
    fecha_inscripcion = Column(DateTime)
    fecha_renovacion = Column(DateTime)
    fecha_impresion = Column(DateTime)
    observaciones = Column(Text)
    division = Column(Integer)

    foto = Column(String(255))

    # relationships
    club_id = Column(Integer, ForeignKey('club.id'))
    club = relationship(Club)

    def __repr__(self):
        return "{} {}".format(self.nombre, self.apellido)

    @property
    def avatar(self):
        if self.foto:
            return os.path.join(os.path.abspath('.'), 'media', self.foto)
        return self.get_default_avatar()

    @property
    def vigencia(self):
        if self.fecha_renovacion:
            return datetime(day=31, month=12, year=self.fecha_renovacion.year)
        elif self.fecha_inscripcion:
            return datetime(day=31, month=12, year=self.fecha_inscripcion.year)
        else:
            return None

    @classmethod
    def get_default_avatar(cls):
        return os.path.join(os.path.abspath('.'), 'ligafutbol', 'asserts', 'default-user.png')

    def verify(self):
        errors = []
        if not all((self.nombre, self.apellido)):
            errors.append("Nombre y Apellido son obligatorios (ambos).")
        if not self.fecha_nac:
            errors.append("Especifique la fecha de nacimiento.")
        try:
            self.dni = int(self.dni)
            if self.dni <= 0:
                errors.append("El DNI es obligatorio")
        except ValueError:
            errors.append("El DNI deben ser sólo números.")
        return errors

    def dict_to_render(self):
        img_path = self.avatar
        if not os.path.exists(img_path):
            img_path = self.get_default_avatar()
        with open(img_path, 'rb') as f:
            img_b64 = base64.b64encode(f.read()).decode()

        return {
            'club': self.club.nombre if self.club else '',
            'imagen': 'data:image/jpeg;base64,{}'.format(img_b64),
            'apellido': self.apellido,
            'nombre': self.nombre,
            'dni': self.dni,
            'lugar': self.lugar_nac,
            'provincia': self.provincia,
            'fecha_nac': self.fecha_nac.strftime("%d/%m/%Y"),
            'año': self.vigencia.year,
            'fecha_vigencia': self.vigencia.strftime("%d/%m/%Y")
        }

# Conservar al final
Base.metadata.bind = db_engine
Base.metadata.create_all(db_engine)
