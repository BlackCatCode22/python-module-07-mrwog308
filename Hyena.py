########################
#                      #
#    create hyenas     #
#                      #
########################

from Animal import Animal

class Hyena(Animal):

    num_hyenas = 0

    hyena_sound = "Laugh"

    list_of_hyenas = []

    with open('animalNames.txt', 'r') as file:
        lines = file.readlines()

        line_number = 1
        for line in lines:
            if line_number == 3:
                list_of_hyenas.extend(line.strip().split(', '))
                break
            else:
                line_number += 1

    def __init__(self, name='aname', animal_id='aid', birth_date='2099-01-01', color='acolor', sex='asex',
                 weight='aweight', origin='aorigin', date_arival='2099-01-01',animal_sound='hsound'):

        Hyena.num_hyenas += 1
        # Hyena.make_sound  = self.hyena_sound

        super().__init__('Hyena', name, animal_id, birth_date, color, sex, weight, origin, date_arival,animal_sound)

    def make_sound(self):

        self.hyena_sound

        return self.hyena_sound
    
    def get_hyena_names(self):

        return self.list_of_hyenas.pop(0)