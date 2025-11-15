########################
#                      #
#    create tigers     #
#                      #
########################

from Animal import Animal

class Tiger(Animal):

    num_tigers = 0

    tiger_sound = "Rawr?"

    list_of_tigers = []

    with open('animalNames.txt', 'r') as file:
        lines = file.readlines()

        line_number = 1
        for line in lines:
            if line_number == 3:
                list_of_tigers.extend(line.strip().split(', '))
                break
            else:
                line_number += 1

    def __init__(self, name='aname', animal_id='aid', birth_date='2099-01-01', color='acolor', sex='asex',
                 weight='aweight', origin='aorigin', date_arival='2099-01-01',animal_sound='tsound'):

        Tiger.num_tigers += 1

        super().__init__('Tiger', name, animal_id, birth_date, color, sex, weight, origin, date_arival,animal_sound)

    def make_sound(self):

        return self.tiger_sound
    
    def get_tiger_names(self):

        return self.list_of_tigers.pop(0)