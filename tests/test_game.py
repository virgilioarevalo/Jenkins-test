from game import game

def test_game_01():
    assert game('Piedra', 'Tijeras') == 'Gana P1', 'debe ganar el Jugador 1'
    assert game('Tijeras', 'Piedra') == 'Gana P2', 'debe ganar el Jugador 2'
    assert game('Tijeras', 'Papel') == 'Gana P1', 'debe ganar el jugador 1' 

