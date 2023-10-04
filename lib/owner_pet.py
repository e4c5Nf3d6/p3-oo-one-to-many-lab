class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def get_pet_type(self):
        return self._pet_type
    
    def set_pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("Not a valid pet type.")

    pet_type = property(get_pet_type, set_pet_type)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class.")
        
        pet.owner = self

    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key=lambda pet: pet.name)
