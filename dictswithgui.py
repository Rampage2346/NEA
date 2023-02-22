import PySimpleGUI as sg

dict = {0: {'current_tier': ['---'],
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
            'ranking_in_tier': [0],
            'mmr_change': [-13],
            'elo': [1200]},
        2: {'current_tier': ['Platinum 1'],
            'imageS': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/smallicon.png'],
            'imageL': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/largeicon.png'],
            'tri_up': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangledownicon.png'],
            'tri_down': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangleupicon.png'],
            'ranking_in_tier': [10],
            'mmr_change': [18],
            'elo': [1210]},
        3: {'current_tier': ['Gold 3'],
            'imageS': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/14/smallicon.png'],
            'imageL': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/14/largeicon.png'],
            'tri_up': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/14/ranktriangledownicon.png'],
            'tri_down': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/14/ranktriangleupicon.png'],
            'ranking_in_tier': [82],
            'mmr_change': [-18],
            'elo': [1182]},
        4: {'current_tier': ['Platinum 1'],
            'imageS': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/smallicon.png'],
            'imageL': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/largeicon.png'],
            'tri_up': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangledownicon.png'],
            'tri_down': [
                'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/15/ranktriangleupicon.png'],
            'ranking_in_tier': [0],
            'mmr_change': [-8],
            'elo': [1200]}}


def leaderboard_display(dict):
    sg.theme('DarkBlue')
    layout = [
        [sg.Multiline(dict, size=(250, 10))]
    ]
    window = sg.Window("MetaTrak", layout, icon='valorant.ico')
    event = window.read()
    window.close()

    return event


leaderboard_display(dict)
