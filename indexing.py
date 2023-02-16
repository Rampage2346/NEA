import pprint

mmr = {0: {'current_tier': ['---'],
           'imageS': ['---'],
           'imageL': ['---'],
           'tri_up': ['---'],
           'tri_down': ['---'],
           'ranking_in_tier': ['---'],
           'mmr_change': ['---'],
           'elo': ['---']},
       1: {'current_tier': ['Platinum 1'],
           'imageS': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/smallicon.png'],
           'imageL': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/largeicon.png'],
           'tri_up': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangledownicon.png'],
           'tri_down': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangleupicon.png'],
           'ranking_in_tier': [76],
           'mmr_change': [30],
           'elo': [1276]},
       2: {'current_tier': ['Platinum 1'],
           'imageS': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/smallicon.png'],
           'imageL': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/largeicon.png'],
           'tri_up': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangledownicon.png'],
           'tri_down': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangleupicon.png'],
           'ranking_in_tier': [46],
           'mmr_change': [19],
           'elo': [1246]},
       3: {'current_tier': ['Platinum 1'],
           'imageS': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/smallicon.png'],
           'imageL': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/largeicon.png'],
           'tri_up': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangledownicon.png'],
           'tri_down': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangleupicon.png'],
           'ranking_in_tier': [27],
           'mmr_change': [-18],
           'elo': [1227]},
       4: {'current_tier': ['Platinum 1'],
           'imageS': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/smallicon.png'],
           'imageL': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/largeicon.png'],
           'tri_up': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangledownicon.png'],
           'tri_down': [
               'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangleupicon.png'],
           'ranking_in_tier': [45],
           'mmr_change': [35],
           'elo': [1245]}}

pprint.pp(mmr)
a = mmr[1]["current_tier"][0]
pprint.pp(a)
b = [*a]
pprint.pp(b)
c = "".join(b)
pprint.pp(c)
print(type(c))