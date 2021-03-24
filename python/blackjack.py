from abc import *
import random #카드 셔플할 때 필요
class Person(metaclass=ABCMeta):
  def __init__(self, name):
    self.name = name
    self.cards = []
    self.cardsum = sum(self.cards)

  @abstractmethod
  def say_hi(self):
    print(f'Hi, I am {self.name}. I have ${self.money}.')

class Dealer(Person):
  def __init__(self, name):
    Person.__init__(self, name)
    self.money = 10000

  def say_hi(self):
    print(f'Hi, I am {self.name}, a {self.__class__.__name__}. I have {self.money}.')
  def shuffle_cards(self, deck_list):
    random.shuffle(deck_list)
    print('Cards shuffled.'.upper())
  def give_card(self, who_cards, deck_list):
    if len(deck_list)<10:
      self.shuffle_cards(deck_list)
    who_cards.append(deck_list.pop())
    print(f'{self.name} drew card.'.upper())
  def win(self, bet):
    self.money += bet
  def lose(self, bet):
    self.money -= bet

class Player(Person):
  def __init__(self, name, money = 100):
    Person.__init__(self, name)
    self.money = money
    
  def say_hi(self):
    print(f'Hi, I am {self.name}, a {self.__class__.__name__}. I have ${self.money}.')
  def start_game(self):
    print(f'{self.name} starts game.')
    self.bet_money()
  def bet_money(self):
    try:
      self.bet = int(input('How much do you bet? [$10~${}]'.format(self.money)))
    except:
      print('Invalid value. Betting $10.')
      self.bet = 10
    self.money -= self.bet
    print(f'{self.name} bet ${self.bet}. Now you have {self.money} in your wallet.')
  def win(self):
    print(f'{self.name} won ${self.bet}.')
    self.money += self.bet*2
    self.bet = 0
  def lose(self):
    print(f'{self.name} lost ${self.bet}.')
    self.bet = 0


#Deck

deck = [i for i in range(2, 11+1)]
all_deck = deck*4

dealer = Dealer(input("Dealer name: "))
player = Player(input("Player name: "), 100)

player.start_game()

print('Shuffling cards...')
for i in range(3):
  dealer.shuffle_cards(all_deck)
shuffle_more = input('Do you want to shuffle another time? [y/n]')
if shuffle_more == 'y':
  dealer.shuffle_cards(all_deck)
elif shuffle_more =='n':
  print('Continue game without shuffling')
else:
  print('Invalid answer. Continue game without shuffling.')

dealer.give_card(dealer.cards, all_deck)
print(f'{dealer.name} got {dealer.cards}')
dealer.give_card(player.cards, all_deck)
print(f'{player.name} got {player.cards}')

print(f"{player.name}'s turn starts.")
while True:
  dealer.give_card(player.cards, all_deck)
  print(f'{player.name} now has {player.cards}')
  player.cardsum = sum(player.cards)
  if len(player.cards) == 2 and player.cardsum == 21:
    print('Blackjack!')
    break
  elif player.cardsum > 21 and 11 not in player.cards:
    print('Burst!')
    break
  elif 11 in player.cards:
    player.cards.remove(11)
    player.cards.append(1)
    print('Replaced 11 with 1.')
    if input('Draw another card? [y/n] ') =='y':
      continue
    else:
      break
  else:
    pass
  if input('Draw another card? [y/n] ') == 'y':
    continue
  else:
    break
  
print(f"{player.name}'s turn is over. {player.name} has {player.cards}")

print(f"{dealer.name}'s turn now.")
while True:
  dealer.give_card(dealer.cards, all_deck)
  dealer.cardsum = sum(dealer.cards)
  if dealer.cardsum <17:
    continue
  elif dealer.cardsum > 21 and 11 not in dealer.cards:
    print('Burst!')
    break
  elif 11 in dealer.cards:
    dealer.cards.remove(11)
    dealer.cards.append(1)
    continue
  else:
    break
print(f"{dealer.name}'s turn is over. {dealer.name} has {dealer.cards}")

print(f"{player.name}'s cards' sum : {player.cardsum}, {dealer.name}'s cards' sum : {dealer.cardsum}")

if len(player.cards) == 2 and player.cardsum == 21:
  print(f'{player.name} hit blackjack.'.upper())
elif player.cardsum > 21 and dealer.cardsum > 21:
  print('TIE, bet is still ${player.bet}')
elif player.cardsum > 21 or (dealer.cardsum <=21 and dealer.cardsum>player.cardsum):
  print(f'{dealer.name} won.'.upper())
  dealer.win(player.bet)
  player.lose()
else:
  print(f'{player.name} won.'.upper())
  dealer.lose(player.bet)
  player.win()

dealer.say_hi()
player.say_hi()
