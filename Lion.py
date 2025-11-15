########################
#                      #
#    create lions      #
#                      #
########################

from Animal import Animal

class Lion(Animal):

    num_lions = 0

    lion_sound = "ROAR!"

    list_of_lions = []

    with open('animalNames.txt', 'r') as file:
        lines = file.readlines()

        line_number = 1
        for line in lines:
            if line_number == 3:
                list_of_lions.extend(line.strip().split(', '))
                break
            else:
                line_number += 1

    def __init__(self, name='aname', animal_id='aid', birth_date='2099-01-01', color='acolor', sex='asex',
                 weight='aweight', origin='aorigin', date_arival='2099-01-01',animal_sound='lsound'):

        Lion.num_lions += 1

        super().__init__('Lion', name, animal_id, birth_date, color, sex, weight, origin, date_arival,animal_sound)

    def make_sound(self):

        return self.lion_sound
    
    def get_lion_names(self):

        return self.list_of_lions.pop(0)