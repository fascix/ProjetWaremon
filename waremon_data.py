TRAINER_DATA = {
    'blond': {
                'dialog': { 'default': ['Salut!' , ' Enfin une nouvelle tête!' , ' Ca te dit un combat?'],
                            'vaincu': ['Tu es plus fort que je le pensais!', 'Bien joué ']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'Boss': {
                'dialog': {'default': ['Je t attendais! ', ' Battons nous!'],
                           'vaincu': ['ARGH!', 'Je te retrouv....']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'Daronne': {
                'dialog':{'default': ['Bonjour, tu veux etre mon ami ?', 'Pardon... Je voulais dire ennemie!'],
                          'vaincu': ['Bon courage pour la suite!']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'Dresseur': {
                'dialog': {'default': ['J adore les nouveaux defis!', 'COMBATTONS!!!'],
                            'vaincu': ['Bien joué...', 'Va voir le boss, tu vas souffrir!']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'fire_boss': {
                'dialog': {'deafult': ['J adore jouer avec le feu!', 'JOUONS!!'],
                           'vaincu': ['Bonne chance...']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'grass_boss': {
                'dialog': {'default': ['Tu oses fouler ma terre ?!', 'Montre moi ce que tu vaut !'],
                           'vaincu': ['#@*%&']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'hat_girl': {
                'dialog': {'default':['Salut toi!','J ai un petit jeu...'],
                           'vaincu':['On peut plus jouer entres amis...']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'purple_girl': {
                'dialog': {'default': ['Les tenebres vont s abattre sur toi!!'],
                           'vaincu': ['Les tenebres sont immortels....']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'straw': {
                'dialog': {'default': ['Salut toi!','Je m ennuis...', 'Ca te dit un combat?'],
                           'vaincu': ['Bien joué', 'A bientot.']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'water_boss': {
                'dialog': {'default': ['Je vais te massacrer!!'],
                           'vaincu': ['ARGH..','Je reviendr....']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'young_girl': {
                'dialog': {'default': ['Un petit combat ca te dit?'],
                           'vaincu': ['Tu as triché!', 'Je te battrai!!']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    },
    'young_guy': {
                'dialog': {'default': ['Hey!', 'Tu as deja gouté a la defaite?', 'Non? Tu vas voir!!'],
                           'vaincu': ['Très mauvais goût la defaite...']},
                'directions': ['down'],
                'look_around': True,
                'vaincu': False,
    }

}

WAREMON_DATA = {
    'CryptoLocker' : {
        'statistiques': {'element': 'Ransomware', 'max_hp': '150', 'attaque': '20', 'defense' : '150', 'vitesse': '20' },
        'capacités' : {},
    },
    'ExPtr': {
        'statistiques': {'element': 'Ransomware', 'max_hp': '70', 'attaque': '100', 'defense' : '50', 'vitesse': '70' },
        'capacités' : {},
    },
    'GandCrab': {
        'statistiques': {'element': 'Ransomware', 'max_hp': '70', 'attaque': '60', 'defense' : '70', 'vitesse': '100' },
        'capacités' : {},
    },
    'Locky': {
        'statistiques': {'element': 'Ransomware', 'max_hp': '150', 'attaque': '40', 'defense' : '70', 'vitesse': '30' },
        'capacités' : {},
    },
    'Pinchy': {
        'statistiques': {'element': 'Ransomware', 'max_hp': '100', 'attaque': '40', 'defense' : '70', 'vitesse': '40' },
        'capacités' : {},
    },

    'DarkHotel' : {
        'statistiques': {'element': 'Spyware', 'max_hp': '50', 'attaque': '150', 'defense' : '70', 'vitesse': '100' },
        'capacités' : {},
    },
    'FinFisher': {
        'statistiques': {'element': 'Spyware', 'max_hp': '150', 'attaque': '100', 'defense' : '40', 'vitesse': '50' },
        'capacités' : {},
    },
    'Havex': {
        'statistiques': {'element': 'Spyware', 'max_hp': '150', 'attaque': '50', 'defense' : '150', 'vitesse': '20' },
        'capacités' : {},
    },
    'Pegasus': {
        'statistiques': {'element': 'Spyware', 'max_hp': '70', 'attaque': '70', 'defense' : '50', 'vitesse': '150' },
        'capacités' : {},
    },
    'Regin': {
        'statistiques': {'element': 'Spyware', 'max_hp': '50', 'attaque': '70', 'defense' : '150', 'vitesse': '150' },
        'capacités' : {},
    },

    'Dropper' : {
        'statistiques': {'element': 'Trojan', 'max_hp': '50', 'attaque': '150', 'defense' : '70', 'vitesse': '50' },
        'capacités' : {},
    },
    'PC-Cyborg': {
        'statistiques': {'element': 'Trojan', 'max_hp': '150', 'attaque': '70', 'defense' : '70', 'vitesse': '70' },
        'capacités' : {},
    },
    'SharkBot': {
        'statistiques': {'element': 'Trojan', 'max_hp': '100', 'attaque': '150', 'defense' : '70', 'vitesse': '50' },
        'capacités' : {},
    },
    'Stuxnet': {
        'statistiques': {'element': 'Trojan', 'max_hp': '150', 'attaque': '40', 'defense' : '150', 'vitesse': '20' },
        'capacités' : {},
    },
    'Zeus': {
        'statistiques': {'element': 'Trojan', 'max_hp': '100', 'attaque': '100', 'defense' : '40', 'vitesse': '20' },
        'capacités' : {},
    },
}

CAPACITES_DATA = {
    'brûlure_virale': {'cible': 'adversaire', 'quantité': 2, 'multiplicateur': 15, 'élément': 'Trojan', 'animation': 'flamme'},
    'onde_de_choc': {'cible': 'adversaire', 'quantité': 3, 'multiplicateur': 20, 'élément': 'Trojan', 'animation': 'éclair'},
    'barrage_de_paquets': {'cible': 'adversaire', 'quantité': 1, 'multiplicateur': 10, 'élément': 'Trojan', 'animation': 'onde'},
    'survoltage': {'cible': 'soi-même', 'quantité': 2, 'multiplicateur': 12, 'élément': 'Trojan', 'animation': 'étincelle'},
    'parasite_logique': {'cible': 'adversaire', 'quantité': 3, 'multiplicateur': 18, 'élément': 'Spyware', 'animation': 'ver_informatique'},
    'effacement_critique': {'cible': 'adversaire', 'quantité': 5, 'multiplicateur': 25, 'élément': 'Ransomware', 'animation': 'erreur_fatale'},
    'patch_défensif': {'cible': 'soi-même', 'quantité': 3, 'multiplicateur': 15, 'élément': 'Spyware', 'animation': 'barrière'},
    'injection_SQL': {'cible': 'adversaire', 'quantité': 4, 'multiplicateur': 22, 'élément': 'Spyware', 'animation': 'texte_codé'},
    'chiffrement': {'cible': 'soi-même', 'quantité': 2, 'multiplicateur': 20, 'élément': 'Ransomware', 'animation': 'bouclier'},
    'Rançon': {'cible': 'adversaire', 'quantité': 3, 'multiplicateur': 17, 'élément': 'Ransomware', 'animation': 'billet'},
    'zero_day': {'cible': 'adversaire', 'quantité': 5, 'multiplicateur': 30, 'élément': 'Trojan', 'animation': 'explosion_codée'},
    'dévoration_CPU': {'cible': 'adversaire', 'quantité': 3, 'multiplicateur': 12, 'élément': 'Trojan', 'animation': 'spirale_énergie'},
    'Espionnage': {'cible': 'adversaire', 'quantité': 2, 'multiplicateur': 10, 'élément': 'Spyware', 'animation': 'Lunette espion'},
    'écran_bleu': {'cible': 'adversaire', 'quantité': 4, 'multiplicateur': 20, 'élément': 'Ransomware', 'animation': 'glitch'},
    'charge_électromagnétique': {'cible': 'adversaire', 'quantité': 3, 'multiplicateur': 15, 'élément': 'Trojan', 'animation': 'onde_électromagnétique'}
}