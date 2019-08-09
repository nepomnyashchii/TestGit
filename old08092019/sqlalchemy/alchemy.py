from alchemy_models import Person, Address, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

anakin = Person(name="Anakin Skywalker", age=32)
obi1 = Person(name='Obi_Wan Kenobi', age=40)


obi1.addresses = [
    Address(email='obi1@example.com'),
    Address(email='wanwan@example.com'),
]

anakin.addresses.append(Address(email='ani@example.com'))
anakin.addresses.append(Address(email='evil.dart@example.com'))
anakin.addresses.append(Address(email='vader@example.com'))

session.add(anakin)
session.add(obi1)
session.commit()

obi = session.query (Person).filter
Person.name.like('Obi%').first()
print (anakin, anakin.addresses)

anakin_id = anakin.ud
del anakin


def display_info ():
    addresses = session.query(Address).all()
    for address in addresses:
        print(f'{address.person.name}<{address.email}>')
#     print('people : {}, addresses: {}'.format(session.query(Person).count(), session.query(Address).count())

# display_info()

# anakin = session_query(Person).get(anakin_id)
# session.delete(anakin)

session.commit()

display_info ()



