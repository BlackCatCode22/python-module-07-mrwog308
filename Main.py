###############################
#                             #
# create main to build report #
#                             #
###############################


from Animal import Animal
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear
from datetime import datetime

#create lists of animal types
list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

current_date = datetime.now()
current_year = current_date.year

def calc_birth_date(the_season, the_years):
    year_of_birth = int(current_year) - int(the_years)
    birth_day = ''
    if 'spring' in the_season.lower():
        birth_day = f'{year_of_birth}-03-21'
    elif 'summer' in the_season.lower():
        birth_day = f'{year_of_birth}-06-21'
    elif 'fall' in the_season.lower():
        birth_day = f'{year_of_birth}-09-21'
    elif 'winter' in the_season.lower():
        birth_day = f'{year_of_birth}-12-21'
    else:
        birth_day = f'{year_of_birth}-01-01'
    return birth_day

def process_one_line(line):
    a_species = ''
    a_sex = ''
    age_in_years = 99
    season = ''
    color = ''
    weight = ''
    origin1 = ''
    origin2 = ''

    # print(line)
    groups_of_words = line.strip().split(',')
    # print(groups_of_words)
    single_words = groups_of_words[0].strip().split(' ')
    age_in_years = single_words[0]
    a_sex = single_words[3]
    a_species = single_words[4]
    single_words = groups_of_words[1].strip().split(' ')
    season = single_words[2]
    color = groups_of_words[2].strip()
    weight = groups_of_words[3].strip()
    origin1 = groups_of_words[4].strip()
    origin2 = groups_of_words[5].strip()
    from_zoo = origin1 + ', ' + origin2
    birth_day = calc_birth_date(season, age_in_years)

    if 'hyena' in a_species:
        my_hyena = Hyena('aname', 'aid', birth_day, color, a_sex, weight, from_zoo, current_date,'hsound')
        my_hyena.name = Hyena.get_hyena_names(my_hyena)
        my_hyena.animal_id = 'hy' + str(Hyena.num_hyenas).zfill(2)
        my_hyena.hsound = Hyena.make_sound(my_hyena)
        list_of_hyenas.append(my_hyena)

    if 'lion' in a_species:
        my_lion = Lion('aname', 'aid', birth_day, color, a_sex, weight, from_zoo, current_date,'lsound')
        my_lion.name = Lion.get_lion_names(my_lion)
        my_lion.animal_id = 'li' + str(Lion.num_lions).zfill(2)
        my_lion.lsound = Lion.make_sound(my_lion)
        list_of_lions.append(my_lion)

    if 'tiger' in a_species:
        my_tiger = Tiger('aname', 'aid', birth_day, color, a_sex, weight, from_zoo, current_date,'tsound')
        my_tiger.name = Tiger.get_tiger_names(my_tiger)
        my_tiger.animal_id = 'ti' + str(Tiger.num_tigers).zfill(2)
        my_tiger.tsound = Tiger.make_sound(my_tiger)
        list_of_tigers.append(my_tiger)

    if 'bear' in a_species:
        my_bear = Bear('aname', 'aid', birth_day, color, a_sex, weight, from_zoo, current_date,'bsound')
        my_bear.name = Bear.get_bear_names(my_bear)
        my_bear.animal_id = 'be' + str(Bear.num_bears).zfill(2)
        my_bear.bsound = Bear.make_sound(my_bear)
        list_of_bears.append(my_bear)

with open('arrivingAnimals.txt', 'r') as file:
    for line in file:
        process_one_line(line)

# print(f'\n\nNumber of animals processed: {Animal.num_animals}\n')
# print(f'\n\nNumber of hyenas processed: {Hyena.num_hyenas}\n')
# print(f'\n\nNumber of lions processed: {Lion.num_lions}\n')
# print(f'\n\nNumber of tigers processed: {Tiger.num_tigers}\n')
# print(f'\n\nNumber of bears processed: {Bear.num_bears}\n')

# print()
# print("Zookeeper's Challenge, Zoo Population")
# print()
# print('Hyena Habitat:')

# for hyena in list_of_hyenas:
#     # date_arival = hyena.date_arival.date()
#     print(hyena.animal_id + ', ' + hyena.name + '; Birthdate: ' + str(hyena.birth_date) + '; ' + hyena.color + '; '
#             + hyena.sex + '; ' + hyena.weight + '; From: ' + hyena.origin + '; Arrival Date: ' + str(hyena.date_arival.date()))

# print()
# print('Lion Habitat:')
# for lion in list_of_lions:
#     print(lion.animal_id + ', ' + lion.name + '; Birthdate: ' + str(lion.birth_date) + '; ' + lion.color + '; '
#             + lion.sex + '; ' + lion.weight + '; From: ' + lion.origin + '; Arrival Date: ' + str(lion.date_arival.date()))

# print()
# print('Tiger Habitat:')
# for tiger in list_of_tigers:
#     print(tiger.animal_id + ', ' + tiger.name + '; Birthdate: ' + str(tiger.birth_date) + '; ' + tiger.color + '; '
#             + tiger.sex + '; ' + tiger.weight + '; From: ' + tiger.origin + '; Arrival Date: ' + str(tiger.date_arival.date()))
    
# print()
# print('Bear Habitat:')
# for bear in list_of_bears:
#     print(bear.animal_id + ', ' + bear.name + '; Birthdate: ' + str(bear.birth_date) + '; ' + bear.color + '; '
#             + bear.sex + '; ' + bear.weight + '; From: ' + bear.origin + '; Arrival Date: ' + str(bear.date_arival.date()))

with open(f'zooPopulation_{current_date.strftime("%Y-%m-%d_%H%M")}.txt', 'w') as report_file:
    report_file.write("Zookeeper's Challenge, Zoo Population\n\n")
    report_file.write('Hyena Habitat:\n')
    for hyena in list_of_hyenas:
        report_file.write(hyena.animal_id + ', ' + hyena.name + '; Birthdate: ' + str(hyena.birth_date) + '; ' + hyena.color + '; '
                + hyena.sex + '; ' + hyena.weight + '; Sound: ' + hyena.hsound + '; From: ' + hyena.origin + '; Arrival Date: ' + str(hyena.date_arival.date()) + '\n')
    report_file.write('\nLion Habitat:\n')
    for lion in list_of_lions:
        report_file.write(lion.animal_id + ', ' + lion.name + '; Birthdate: ' + str(lion.birth_date) + '; ' + lion.color + '; '
                +   lion.sex + '; ' + lion.weight + '; Sound: ' + lion.lsound + '; From: ' + lion.origin + '; Arrival Date: ' + str(lion.date_arival.date()) + '\n')
    report_file.write('\nTiger Habitat:\n')
    for tiger in list_of_tigers:
        report_file.write(tiger.animal_id + ', ' + tiger.name + '; Birthdate: ' + str(tiger.birth_date) + '; ' + tiger.color + '; '
                +   tiger.sex + '; ' + tiger.weight + '; Sound: ' + tiger.tsound + '; From: ' + tiger.origin + '; Arrival Date: ' + str(tiger.date_arival.date()) + '\n')
    report_file.write('\nBear Habitat:\n')
    for bear in list_of_bears:
        report_file.write(bear.animal_id + ', ' + bear.name + '; Birthdate: ' + str(bear.birth_date) + '; ' + bear.color + '; '
                +   bear.sex + '; ' + bear.weight + '; Sound: ' + bear.bsound + '; From: ' + bear.origin + '; Arrival Date: ' + str(bear.date_arival.date()) + '\n')
        