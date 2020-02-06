#2nd Semester Final - Highschool Coding
from random import shuffle
import random
import time

def deck():
  deck = []
  for suit in ['H', 'S', 'D', 'C']:
    for rank in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
      deck.append(suit+rank)
  shuffle(deck)
  return deck

def card_values(player_cards):
  player_Cards = 0
  card_ace = 0
  for a in player_cards:
    #print "Card", a
    if(a[1:] == 'J' or a[1:] == 'Q' or a[1:] == 'K' or a[1:] == '10'):
      player_Cards += 10
    elif(a[1:] != 'A'):
      player_Cards += int(a[1:])
    else:
      card_ace += 1
  if (card_ace == 1 and player_Cards >= 10):
    player_Cards += 11
  elif(card_ace != 0):
    player_Cards += 1
  return player_Cards

def card_playing_hand(player_deck):
  dealer_cards = []
  player_cards = []
  dealer_cards.append(player_deck.pop())
  dealer_cards.append(player_deck.pop())
  player_cards.append(player_deck.pop())
  player_cards.append(player_deck.pop())
  while (card_values (dealer_cards) <= 16):
    dealer_cards.append(player_deck.pop())
  return [dealer_cards, player_cards]

blackjack = 0
wons = 0
losses = 0
player_name = input("Enter your name: ")
cont = "y"
restart = "y"
while(blackjack != "2"):
  print("______________________")
  print("M A I N  M E N U")
  print("")
  print( "Welcome to the basic Blackjack Simulator!", player_name)
  print("")
  print(player_name, "has won", wons, "number of games!")
  print("Dealer has won", losses, "number of games! :(")
  print("")
  print("")
  print("What would you like to do?")
  blackjack = input("1.)Play!\n2.)Quit." )
  print("_____________________")
  if blackjack == "1":
    #restart = "y"
    player_deck = deck()
    hands = card_playing_hand(player_deck)
    dealer = hands[0]
    player = hands[1]
    player_hit = card_playing_hand(player_deck)
   #Cards of the players and the values
    dealer_count = card_values(dealer)
    player_count = card_values(player)
    print("_________________________")
    print("Dealer hand is:", dealer)
    print(dealer_count, "points")
    print("_________________________")
    print(player_name, "hand is:", player)
    print(player_count, "points")
    print("_________________________")
    time.sleep(.5)
    if(player_count == 21):
      print("Blackjack!")
      wons += 1
    elif(player_count > 21):
      print(player_name,"has BuStEd!!! With " + str(player_count) + " points. Dealer Wins! D:")
      losses += 1
    elif(dealer_count == 21):
      print("Dealer claimed blackjack!")
      losses += 1
    elif(dealer_count > 21):
      print("Dealer has Busted! With " + str(dealer_count) + " points. Player Wins! :D")
      wons += 1
    else:
      hit_stay = input("What would you like to do? H: Hit, S: Stay ")
      time.sleep(.5)
      print("_________________________")
      if(hit_stay == 'H' or hit_stay == 'h'):
        player_count += random.randint(1,11)
        dealer_count += random.randint(1,11)
        print(player_name, "now has", player_count, "points")
        print("_______________________")
      else:
        (hit_stay == 'S' or hit_stay == 's')
        #nothing to be placed in here :D
      if player_count > 21:
        print(player_name, "has busted on his second attempt.")
        print("dealer wins!")
        losses += 1
      elif dealer_count > 21:
        print("Dealer has busted!")
        print(player_name, "has claimed a victory!")
        wons += 1
      elif(player_count > dealer_count):
        print(player_name ,"wins with " + str(player_count) + " points!! :D")
        wons += 1
        print("D E A L E R")
        print("Dealer has: " + str(dealer_count) + " points")
      else:
        print("Dealer Wins! D:<")
        losses += 1
        print("_______________________")
        print("Dealer has: " + str(dealer_count) + " points")
        print(player_name, "lost with: " + str(player_count) + " points")
      print("_________________________")
      print("G A M E ... O V E R...")
      print("")
      time.sleep(.5)
      cont = input("Would you like to return to the Main Menu? (y/n)")
      if cont == "n":
        break
