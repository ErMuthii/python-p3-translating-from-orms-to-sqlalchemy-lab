from models import Dog


def create_table(base):
    if __name__ == '__main__':
        engine = create_engine('sqlite:///:memory:')
        base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    dogs = session.query(Dog).all()
    print (dogs)

def find_by_name(session, name):
    dog = session.query(Dog).filter(Dog.name == name).first()
    print(dog)
  

def find_by_id(session, id):
    dog = session.query(Dog).filter(Dog.id == id).first()
    print(dog)

  

def find_by_name_and_breed(session, name, breed):
     dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
     print(dog)

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()