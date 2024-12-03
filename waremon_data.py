TRAINER_DATA = {

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