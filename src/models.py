import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(50),)
    apellido = Column(String(50))
    correo = Column(String(50))
    contraseña = Column(String(50))

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer,primary_key=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id"))    
    descripcion = Column(String(250))
    fecha = Column(DateTime)
    relacion_usuario = relationship("Usuario")
     

class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer,primary_key=True)
    usuario_post = Column(Integer,ForeignKey("post.id")) 
    usuario_id = Column(Integer,ForeignKey("usuario.id"))   
    relacion_usuario = relationship("Usuario") 
    relacion_post = relationship("Post")


class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer,primary_key=True)
    usuario_post = Column(Integer,ForeignKey("post.id")) 
    usuario_id = Column(Integer,ForeignKey("usuario.id")) 
    comentario = Column(String(250))
    relacion_usuario = relationship("Usuario")
    relacion_post = relationship("Post")


"""
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
"""
  
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
