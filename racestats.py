def get_stat_changes(race):
    stat_changes = {
        'Human': {
            'strength': 1,
            'dexterity': 1,
            'constitution': 1,
            'intelligence': 1,
            'wisdom': 1,
            'charisma': 1
        },
        'Elf': {
            'strength': 0,
            'dexterity': 2,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        },
        'Dwarf': {
            'strength': 0,
            'dexterity': 0,
            'constitution': 2,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        },
        'Halfling': {
            'strength': 0,
            'dexterity': 2,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        },
        'Gnome': {
            'strength': 0,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 2,
            'wisdom': 0,
            'charisma': 0
        },
        'Dragonborn': {
            'strength': 2,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 1
        },
        'Half-Elf': {
            'strength': 0,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 2
        },
        'Half-Orc': {
            'strength': 2,
            'dexterity': 0,
            'constitution': 1,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        },
        'Tiefling': {
            'strength': 0,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 2
        },
        'Aarakocra': {
            'strength': 0,
            'dexterity': 2,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 1,
            'charisma': 0
        },
        'Genasi': {
            'strength': 0,
            'dexterity': 0,
            'constitution': 2,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        },
        'Goliath': {
            'strength': 2,
            'dexterity': 0,
            'constitution': 1,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        },
        'Aasimar': {
            'strength': 0,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 2
        },
        'Firbolg': {
            'strength': 1,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 1,
            'charisma': 0
        },
        'Kenku': {
            'strength': 0,
            'dexterity': 2,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        },
        'Lizardfolk': {
            'strength': 0,
            'dexterity': 0,
            'constitution': 1,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        },
        'Tabaxi': {
            'strength': 0,
            'dexterity': 2,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 1
        }
    }
    return stat_changes[race]