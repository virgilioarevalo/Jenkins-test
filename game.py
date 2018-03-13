def game(P1, P2):
    """
    Enter values that represent the player choice
    Return p1 id player 1 wins otherway p2
    """
    if P1 == 'Piedra' and P2 == 'Piedra':
            return 'Empate'
    elif P1 == 'Piedra' and P2 == 'Papel':
            return 'Gana P2'
    elif P1 == 'Piedra' and P2 == 'Tijeras':
            return 'Gana P1'	
    elif P1 == 'Tijeras' and P2 == 'Tijeras':
            return 'Empate'
    elif P1 == 'Tijeras' and P2 == 'Papel':
            return 'Gana P1'	
    elif P1 == 'Tijeras' and P2 == 'Piedra':
            return 'Gana P2'
    elif P1 == 'Papel' and P2 == 'Papel':
           return 'Empate'	
    elif P1 == 'Papel' and P2 == 'Tijeras':
            return 'Gana P2'	
    elif P1 == 'Papel' and P2 == 'Piedra':
            return 'Gana P1'
    else:
            return 'Error 404'
