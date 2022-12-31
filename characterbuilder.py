import racestats as rs


# print(rs.stat_changes)

def choose_name():
    print('Choose your character\'s name:')
    name = input()

    return name


def choose_race():
    # List of available races and classes
    races = ['Human', 'Elf', 'Dwarf', 'Halfling', 'Gnome', 'Dragonborn', 'Half-Elf', 'Half-Orc', 'Tiefling', 'Aarakocra', 'Genasi', 'Goliath', 'Aasimar', 'Firbolg', 'Kenku', 'Lizardfolk', 'Tabaxi']
    

    # Prompt the user to choose a race
    print('Choose your character\'s race:')
    for i, race in enumerate(races):
        print(f'{i+1}. {race}')
    chosen_race = int(input()) - 1
    race = races[chosen_race]

    return race


def choose_class():
    # List of available races and classes
    classes = ['Fighter', 'Ranger', 'Rogue', 'Wizard', 'Cleric']

    # Prompt the user to choose a class
    print('Choose your character\'s class:')
    for i, cls in enumerate(classes):
        print(f'{i+1}. {cls}')
    chosen_class = int(input()) - 1
    cls = classes[chosen_class]

    return cls



def choose_stats(self):
    #choose all stats
    print('Choose your character\'s strength:')
    self.strength = int(input()) + rs.get_stat_changes(playercharacter.race)['strength']
    print('Choose your character\'s dexterity:')
    self.dexterity = int(input()) + rs.get_stat_changes(playercharacter.race)['dexterity']
    print('Choose your character\'s constitution:')
    self.constitution = int(input()) + rs.get_stat_changes(playercharacter.race)['constitution']
    print('Choose your character\'s intelligence:')
    self.intelligence = int(input()) + rs.get_stat_changes(playercharacter.race)['intelligence']
    print('Choose your character\'s wisdom:')
    self.wisdom = int(input()) + rs.get_stat_changes(playercharacter.race)['wisdom']
    print('Choose your character\'s charisma:')
    self.charisma = int(input()) + rs.get_stat_changes(playercharacter.race)['charisma']

    return 
    



class Character:
    def __init__(self, name, race, cls, level, strength, dexterity, constitution, intelligence, wisdom, charisma, hit_points, armor_class, attacks_and_spells):
        self.name = name
        self.race = race
        self.cls = cls
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.attacks_and_spells = attacks_and_spells



playercharacter = Character(
    name=choose_name(),
    race=choose_race(),
    cls=choose_class(),
    level=1,
    strength=1,
    dexterity=1,
    constitution=1,
    intelligence=1,
    wisdom=1,
    charisma=1,
    hit_points=10,
    armor_class=16,
    attacks_and_spells=[
        ('Short Sword', '1d6 + 2'),
        ('Shortbow', '1d6 + 2'),
        ('Shield Bash', '1d4 + 2')
    ]
    
)


choose_stats(playercharacter)


print(playercharacter.name)
print(playercharacter.race)
print(playercharacter.cls)
print(playercharacter.level)
print(playercharacter.strength)
print(playercharacter.dexterity)
print(playercharacter.constitution)
print(playercharacter.intelligence)
print(playercharacter.wisdom)
print(playercharacter.charisma)
print(playercharacter.hit_points)
print(playercharacter.armor_class)
print(playercharacter.attacks_and_spells)

