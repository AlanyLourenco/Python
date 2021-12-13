def jogo(jog=0,gols=0):
    if len(jog)==0:
        jog='<desconhecido>'
    if len(gols)==0:
        gols=0
    print(f'O jogador {jog} fez {gols} gols')
    
jog=str(input('Nome do jogador: '))
gol=str(input(f'Quantos gols o jogador {jog} fez? '))

jogo(jog,gol)

