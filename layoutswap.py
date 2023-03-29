blue5_tab = [
    [sg.Text("Level: " + blue_players['blue5_level'])],
    [sg.Text("Character: " + blue_players['blue5_character'])],
    [sg.Text("C Casts: " + blue_players['blue5_c_casts'])],
    [sg.Text("E Casts: " + blue_players['blue5_e_cast'])],
    [sg.Text("Q Casts: " + blue_players['blue5_q_casts'])],
    [sg.Text("ACS: " + blue_players['blue5_score'])],
    [sg.Text("Kills: " + blue_players['blue5_kills'])],
    [sg.Text("Deaths: " + blue_players['blue5_deaths'])],
    [sg.Text("Assist: " + blue_players['blue5_assists'])],
    [sg.Text("H/S %: " + ((blue_players['blue5_headshots']) / (blue_players['blue5_headshots']
                                                             + blue_players['blue5_bodyshots'] + blue_players[
                                                                 'blue5_legshots'])) * 500)],
    [sg.Text("Damage Dealt: " + blue_players['blue5_damage_made'])],
    [sg.Text("Damage Received: " + blue_players['blue5_damage_received'])]
]