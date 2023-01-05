import racestats as rs


# print(rs.stat_changes)

def choose_name():
    print('Choose your character\'s name:')
    name = input()

    return name


def choose_race():
    # List of available races
    races = ['Human', 'Elf', 'Dwarf', 'Halfling', 'Gnome', 'Dragonborn', 'Half-Elf', 'Half-Orc', 'Tiefling', 'Aarakocra', 'Genasi', 'Goliath', 'Aasimar', 'Firbolg', 'Kenku', 'Lizardfolk', 'Tabaxi']
    

    # Prompt the user to choose a race
    print('Choose your character\'s race:')
    for i, race in enumerate(races):
        print(f'{i+1}. {race}')
    chosen_race = int(input()) - 1
    race = races[chosen_race]

    return race


def choose_class():
    # List of available classes
    classes = ['Fighter', 'Ranger', 'Rogue', 'Wizard', 'Cleric']

    # Prompt the user to choose a class
    print('Choose your character\'s class:')
    for i, cls in enumerate(classes):
        print(f'{i+1}. {cls}')
    chosen_class = int(input()) - 1
    cls = classes[chosen_class]

    return cls



#def choose_stats(self):
    #choose all stats
    #print('Choose your character\'s strength:')
    #self.strength = int(input()) + rs.get_stat_changes(self.race)['strength']
    #print('Choose your character\'s dexterity:')
    #self.dexterity = int(input()) + rs.get_stat_changes(self.race)['dexterity']
    #print('Choose your character\'s constitution:')
    #self.constitution = int(input()) + rs.get_stat_changes(self.race)['constitution']
    #print('Choose your character\'s intelligence:')
    #self.intelligence = int(input()) + rs.get_stat_changes(self.race)['intelligence']
    #print('Choose your character\'s wisdom:')
    #self.wisdom = int(input()) + rs.get_stat_changes(self.race)['wisdom']
    #print('Choose your character\'s charisma:')
    #self.charisma = int(input()) + rs.get_stat_changes(self.race)['charisma']
    
def choose_stats(self):
    #choose all stats
    self.strength = int(10) + rs.get_stat_changes(self.race)['strength']
    self.dexterity = int(10) + rs.get_stat_changes(self.race)['dexterity']
    self.constitution = int(10) + rs.get_stat_changes(self.race)['constitution']
    self.intelligence = int(10) + rs.get_stat_changes(self.race)['intelligence']
    self.wisdom = int(10) + rs.get_stat_changes(self.race)['wisdom']
    self.charisma = int(10) + rs.get_stat_changes(self.race)['charisma']


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


#playercharacter = Character(
#        name=choose_name(),
#        race=choose_race(),
#        cls=choose_class(),
#        level=1,
#        strength=1,
#        dexterity=1,
#        constitution=1,
#        intelligence=1,
#        wisdom=1,
#        charisma=1,
#        hit_points=10,
#        armor_class=16,
#        attacks_and_spells=[
#            ('Short Sword', '1d6 + 2'),
#            ('Shortbow', '1d6 + 2'),
#            ('Shield Bash', '1d4 + 2')
#            ]
#    )

def printstats(self):
    print('Name: ',self.name)
    print('Race: ',self.race)
    print('Class: ',self.cls)
    print('Level: ',self.level)
    print('Str: ',self.strength)
    print('Dex: ',self.dexterity)
    print('Con: ',self.constitution)
    print('Int: ',self.intelligence)
    print('Wis: ',self.wisdom)
    print('Cha: ',self.charisma)
    print('HP: ',self.hit_points)
    print('AC: ', self.armor_class)
    print('bajs: ',self.attacks_and_spells)



def PlayerCharacter():
    playerobject = Character(
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
    return playerobject






#print('Name: ',playercharacter.name)
#print('Race: ',playercharacter.race)
#print('Class: ',playercharacter.cls)
#print('Level: ',playercharacter.level)
#print('Str: ',playercharacter.strength)
#print('Dex: ',playercharacter.dexterity)
#print('Con: ',playercharacter.constitution)
#print('Int: ',playercharacter.intelligence)
#print('Wis: ',playercharacter.wisdom)
#print('Cha: ',playercharacter.charisma)
#print('HP: ',playercharacter.hit_points)
#print('AC: ', playercharacter.armor_class)
#print('bajs: ',playercharacter.attacks_and_spells)

