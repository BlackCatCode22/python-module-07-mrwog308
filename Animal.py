########################
#                      #
# create animal object #
#                      #
########################

class Animal:
    num_animals = 0
    def __init__(self, species, name, animal_id, birth_date, color, sex, weight, origin, date_arival,animal_sound):

        self.name = species
        self.type = name
        self.animal_id = animal_id
        self.birth_date = birth_date
        self.color = color
        self.sex = sex
        self.weight = weight
        self.origin = origin
        self.date_arival = date_arival
        self.animal_sound = animal_sound

        Animal.num_animals += 1