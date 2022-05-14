from basic import db,Puppy

# CREATES ALL THE TABLES (i.e.) Transforming your Models into Tables
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

#NONE OF THE BELOW WORKS
print(sam.id)
print(frank.id)

###############################

db.session.add_all([sam,frank])

db.session.commit() #Save changes to db

print(sam.id)
print(frank.id)

