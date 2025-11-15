##########################
#                        #
# ZooKeepersChallenge.py #
#                        #
##########################

class ZooKeepersChallenge:

    def __init__(self):
        pass

    def find_animal_names(self, anames):
        #make animal_list like if type = hyena then [{'type': 'hyena01', 'name': 'Shenzi'}, {'type': 'hyena02', 'name': 'Banzai'}, etc.] if type = lion then [{'type': 'lion01', 'name': 'Mufasa'}, etc.]
        animal_list = []
        current_type = None
        with open(anames, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    if 'Names' in line:
                        current_type = line.replace(' Names', '').lower()
                    else:
                        entry = {'type': current_type, 'name': line}
                        animal_list.append(entry)

        #remake a new animal_list with type and name as keys in dictionary like if type = hyena then [{'type': 'hyena01', 'name': 'Shenzi'}, {'type': 'hyena02', 'name': 'Banzai'}, etc.] if type = lion then [{'type': 'lion01', 'name': 'Mufasa'}, etc.]
        




        return animal_list

    
        # animal_list = []
        # with open(anames, 'r') as file:
        #     for line in file:
        #         line = line.strip()
        #         if line:
        #             if 'Names' in line:
        #                 line = line.replace(' Names', '')
        #                 entry = {'type': line.lower()}
        #             else:
        #                 entry = {'name': line}
        #             animal_list.append(entry)
        # return animal_list

    
    def find_new_arrivals(self, arrivals, animal_list):


        new_arrivals = []
        existing_names = set()
        for animal in self.find_animal_names('animalNames.txt'):
            if 'name' in animal:
                existing_names.add(animal['name'])
        with open(arrivals, 'r') as file:
            for line in file:
                line = line.strip()
                if line and line not in existing_names:
                    entry = {'stats': line}
                    new_arrivals.append(entry)
        return new_arrivals
    
    #create a list of dictionaries of Hyena01, Hyena02, Hyena03, etc. and assign them characteriestics from the new_arrivals list
    def assign_characteristics(self, animal_list, new_arrivals):
        characteristics = []
        for i in range(min(len(animal_list), len(new_arrivals))):
            animal = animal_list[i]
            arrival = new_arrivals[i]
            name = animal.get('name', f'Animal{i+1}')
            type_ = animal.get('type', 'unknown')
            characteristics.append({
                'name': name,
                'type': type_,
                'stats': arrival['stats']
            })
        return characteristics
    # def assign_characteristics(self, animal_list, new_arrivals):
    #     characteristics = []
    #     for i, animal in enumerate(animal_list):
    #         if i < len(new_arrivals):
    #             characteristics.append({
    #                 'name': animal.get('name', f'Animal{i+1}'),
    #                 'type': animal.get('type', 'unknown'),
    #                 'stats': new_arrivals[i]['stats']
    #             })
    #     return characteristics
    
anames = 'animalNames.txt'
arrivals = 'arrivingAnimals.txt'

zkc = ZooKeepersChallenge()
animal_list = zkc.find_animal_names(anames)
new_arrivals = zkc.find_new_arrivals(arrivals, animal_list)
characteristics = zkc.assign_characteristics(animal_list, new_arrivals)

# print("Animal Names Dictionary Entries:")
# print(animals)

print(animal_list)
# print(new_arrivals)
# print(characteristics)
# for animal in animal_list:
#     print(animal)

# for arrival in new_arrivals:
#     print(arrival)