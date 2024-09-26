#Course: ITI 1120
#Assignment 4 Part 1 Question 3
#Malek, James
#300352042

# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.



import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''

    random.shuffle(deck)

#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
    dealer=[]
    other=[]
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for i in range(0, len(deck)//2):
        dealer.append(deck[i])
    for j in range(len(deck)//2, len(deck)):
        other.append(deck[j])

    return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    
    no_pairs=[]
    new_l=[]

    for i in l:
        type_attribution=str(i)
        new_l.append(type_attribution)
    #l=[str(item) for item in l]
    new_l.sort()
    n=len(new_l)
    i=0
    while i<n-1:
        first_card=new_l[i][0]
        second_card=new_l[i+1][0]
        if first_card==second_card: 
            i+=1 
        else:
            no_pairs.append(new_l[i])
        i=i+1
    if i==n-1: 
        no_pairs.append(new_l[i])

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    human=deck
    for i in deck:
        print(i, end=" ")
    print()

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     print("\nI have ", n, " cards. If 1 stands for my first card and")
     print(n, " for my last card, which of my cards would you like?")
     position=int(input("Give me an integer between 1 and "+str(n)+": ").strip())
     
     while not(position>=1 and position <=n):
          position=int(input("Invalid number. Please enter integer between 1 and "+str(n)+": ").strip())
     return position

def random_pick(human):
    '''
     (lst of str)->str
     Returns a string which represents the card that the robot picked from the human.
     '''
    r_position=random.randint(1,len(human))
    suffixes=["st","nd","rd","th"]

    if 1<=r_position<=3:
        index_position=suffixes[r_position-1]  
    else:
        index_position=suffixes[-1]
    print("I took your " +str(r_position)+index_position+" card.")

    
    card=human.pop(r_position-1)

    return card

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print()
     print_deck(human)
     print("\nDo not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     suffixes=["st","nd","rd","th"]

     turn=0

     while len(dealer)>0 and len(human)>0:
          
          if turn==0: 
               print("\n***********************************************************")
               print("Your turn.\n")
               print("Your current deck of cards is:\n")
               
               print_deck(human)
               
               n=len(dealer)
               position=get_valid_input(n)
               card = dealer[position-1]
               dealer.remove(card)

               

               if 1<=position<=3:
                   index_position=suffixes[position-1]  
               else:
                   index_position=suffixes[-1]
               print("You asked for my " +str(position)+index_position+" card.")
               print("Here it is. It is ", card)
    
               human.append(card)
               print("With ", card, " added, your current deck of cards is:\n ")
               print_deck(human)
               print("\nAnd after discarding pairs and shuffling, your deck is:\n ")
               human=remove_pairs(human)
               print_deck(human)
               wait_for_player()


               turn=1
          else:

                print("\n***********************************************************")
                print("My turn.\n")
                card=random_pick(human)
                dealer.append(card)
                dealer=remove_pairs(dealer)
                n=len(dealer)
                
                wait_for_player()

                turn=0

     if len(dealer)==0:
        print("Ups. I do not have any more cards.")
        print("You lost! I, Robot, win.")
     else:
        print("********************************************************")
        print("Ups. You do not have any more cards")
        print("Congratulations! You, Human, win")
           
        

# main
play_game()



