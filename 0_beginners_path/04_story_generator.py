"""
Story Generator 
Our task is to generate a random story every time the user runs the program. 
I will first store the parts of the stories in different lists, 
then the random module can be to select the random parts of the story stored in different lists.
"""
import random
def generador_de_historia():
    when = ['Unos años atras', 'Ayer', 'La última noche', 'Ha muchos años atras', 'El 20 de junio']
    who = ['un conejo', 'un elefante', 'un raton', 'una tortuga', 'un NEKO']
    name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
    residence = ['Isvan', 'Seven', 'Bosco', 'Stella', 'Algún lugar de Fiore']
    went = ['Cine', 'Universidad', 'Seminario', 'escuela', 'lavandería']
    happened = ['hizo muchos amigos', 'comió muchas hamburguezas', 'encontró una llave secreta', 'resolvió un misterio', 'escribió un libro']
    print(random.choice(when)+',', random.choice(name), random.choice(who), 'que vivió en', random.choice(residence)+ ', se fué a la', random.choice(went), 'y', random.choice(happened))
    
def story_generator():
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
    who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
    name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
    residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
    went = ['cinema', 'university','seminar', 'school', 'laundry']
    happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
    print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

generador_de_historia()
story_generator()
