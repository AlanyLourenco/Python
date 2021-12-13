from random import randint
from operator import itemgetter
dado={'Jogador 1': randint(1,6),'Jogador 2': randint(1,6),'Jogador 3': randint(1,6),'Jogador 4': randint(1,6),}
ranking=[]
ranking=sorted(dado.items(),key= itemgetter(1), reverse= True)
print(ranking)
