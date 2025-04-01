
'''
Crie uma classe Jogador21 que permita gerar instâncias de 
jogadores de 21. Os objetos de tal classe deverão ter 
capacidade de armazenar o nome do jogador, armazenar as 
cartas sorteadas, calcular o total de pontos, além de 
perguntar para o usuário se ele deseja continuar ou não o 
sorteio de cartas.
'''

class Jogador21():
    
    def __init__(self):
        self.playerName = " "
        self.hand = 0
        self.hit = False
        self.totalCards = []

    def setName(self, newName):
        self.playerName = newName
    
    def getName(self):
        return self.playerName
    
    def printName(self):
        print(self.playerName)

    def setTotalCards(self, newCard):
        self.totalCards.append(newCard)
    
    def getTotalCards(self):
        return self.totalCards
    
    def printTotalCards(self):
        print(self.totalCards)
    
    def playerHand(self):
        for card in self.totalCards:
            self.hand += card
    
    def printPlayerHand(self):
        print(f"player hand is {self.hand}\n")

    def askPlayer(self):
        print("Do you want to continue the game? (Y/n)\n")
        answer = input().casefold

        if(answer == "y"):
            self.hit = True

        elif(answer == "n"):
            self.hit = False


class Game():

    def __init__(self):
        self.numPlayers = 0
        self.players = []
        self.startGame = False
        self.endGame = False

    def setup(self):
        print("how many players?")
        self.numPlayers = int(input())

        for index in range(self.numPlayers):
            new_player = Jogador21()
            print(f"name of the player {index}\n")
            new_player.setName(input())

            self.players.append(new_player)

    def printAllPlayers(self):
        for player in self.players:
            player.printName()

   # def run(self):
   # main game rotine

# Validation of the class Jogador21
obj = Game()
obj.setup()
obj.printAllPlayers()

