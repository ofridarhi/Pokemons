class Pokemon:
    def __init__(self, name, pokimonType, level,):
        self.name = name
        self.pokimonType = pokimonType
        self.level = level
        health = 100
        self.health = health * level

    def valid_type(self):
        valid_types = ['water','fire','rock','plant']
        assert self.pokimonType in valid_types, "the pokimon type must be water,fire,rock,electricity"

    def feed(self, food):
        self.health += food

def battle(pokimon1,pokimon2):
    what_type_is_winning = {'water': 'fire', 'rock': 'fire', 'fire': 'plant', 'plant': 'water'}
    if pokimon1.pokimonType in what_type_is_winning.keys() and pokimon2.pokimonType in what_type_is_winning.get(pokimon1.pokimonType):
        pokimon2.health -= 25
    if pokimon2.pokimonType in what_type_is_winning.keys() and pokimon1.pokimonType in what_type_is_winning.get(pokimon2.pokimonType):
        pokimon1.health -= 25
    min_health = min(pokimon1.health, pokimon2.health)
    pokimon1.health -= min_health
    pokimon2.health -= min_health

    if pokimon1.health > pokimon2.health:
        print(f"{pokimon1.name} won ")
    elif pokimon1.health < pokimon2.health:
        print(f"{pokimon2.name} won ")
    else:
        print("its a tie, both of your pokimons has 0 health now")

    print(f"{pokimon1.name}'s health is {pokimon1.health}")
    print(f"{pokimon2.name}'s health is {pokimon2.health}")

poki1 = Pokemon('pikachu', 'plant', 4)

poki2 = Pokemon('charizard', 'water', 3)

battle(poki1,poki2)
