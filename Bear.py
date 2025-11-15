########################
#                      #
#    create bears      #
#                      #
########################

from Animal import Animal 

class Bear(Animal):

    num_bears = 0

    bear_sound = "Yawn!"

    list_of_bears = []

    with open('animalNames.txt', 'r') as file:
        lines = file.readlines()

        line_number = 1
        for line in lines:
            if line_number == 3:
                list_of_bears.extend(line.strip().split(', '))
                break
            else:
                line_number += 1

    def __init__(self, name='aname', animal_id='aid', birth_date='2099-01-01', color='acolor', sex='asex',
                 weight='aweight', origin='aorigin', date_arival='2099-01-01',animal_sound='bsound'):

        Bear.num_bears += 1

        super().__init__('Bear', name, animal_id, birth_date, color, sex, weight, origin, date_arival,animal_sound)

    def make_sound(self):

        return self.bear_sound
    
    def get_bear_names(self):

        return self.list_of_bears.pop(0)