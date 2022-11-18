#!/usr/bin/env python
# coding: utf-8

# # Project 10 -- Zeru Zhou

# **TA Help:** NA
# 
# 
#     
# **Collaboration:** NA
#     
# - Get help from dr. ward's videos

# ## Question 1

# In[1]:


class Card:

    _value_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8, "9":9, "10": 10, "j": 11, "q": 12, "k": 13, "a": 14}
    def __init__(self, number, suit):
        if str(number).lower() not in [str(num) for num in range(2, 11)] + list("jqka"):
            raise Exception("Number wasn't 2-10 or J, Q, K, or A.")
        else:
            self.number = str(number).lower()
        if suit.lower() not in ["clubs", "hearts", "diamonds", "spades"]:
            raise Exception("Suit wasn't one of: clubs, hearts, spades, or diamonds.")
        else:
            self.suit = suit.lower()

    def __str__(self):
        return(f'{self.number} of {self.suit.lower()}')

    def __repr__(self):
        return(f'Card(str({self.number}), "{self.suit}")')

    def __eq__(self, other):
        if self.number == other.number:
            return True
        else:
            return False

    def __lt__(self, other):
        if self._value_dict[self.number] < self._value_dict[other.number]:
            return True
        else:
            return False

    def __gt__(self, other):
        if self._value_dict[self.number] > self._value_dict[other.number]:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.number)


# In[2]:


class Deck:
    brand = "Bicycle"
    _suits = ["clubs", "hearts", "diamonds", "spades"]
    _numbers = [str(num) for num in range(2, 11)] + list("jqka")

    def __init__(self):
        self.cards = [Card(number, suit) for suit in self._suits for number in self._numbers]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value


# In[3]:


my_card = Card(5, "clubs")
print(my_card)


# In[4]:


my_card


# In[5]:


my_deck = Deck()
print(my_deck)


# In[10]:


class Deck:
    brand = "Bicycle"
    _suits = ["clubs", "hearts", "diamonds", "spades"]
    _numbers = [str(num) for num in range(2, 11)] + list("jqka")

    def __init__(self):
        self.cards = [Card(number, suit) for suit in self._suits for number in self._numbers]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value
        
    def __str__(self):
        return(f'A {self.brand.lower()} Deck')


# In[7]:


my_deck = Deck()
print(my_deck)


# In[8]:


class Deck:
    brand = "Copag"
    _suits = ["clubs", "hearts", "diamonds", "spades"]
    _numbers = [str(num) for num in range(2, 11)] + list("jqka")

    def __init__(self):
        self.cards = [Card(number, suit) for suit in self._suits for number in self._numbers]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value
        
    def __str__(self):
        return(f'A {self.brand.lower()} Deck')


# In[9]:


my_deck = Deck()
print(my_deck)


# As above, modifications are made.

# ## Question 2

# In[11]:


deck1 = Deck()
deck2 = Deck()
print(deck1)
print(deck2)


# In[12]:


Deck.brand = "Copag"
deck1 = Deck()
deck2 = Deck()
print(deck1)
print(deck2)


# In[13]:


deck1 = Deck()
deck2 = Deck()
deck1.brand = "Aviator"
Deck.brand = "Copag"
print(deck1)
print(deck2)


# The brand of deck1 is specifically modified to "Aviator", and the basic brand for both 2 decks are changed to "Copag".

# ## Question 3

# In[9]:


class Player:

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        
    def __str__(self):
        return(f"""
        {self.name}\n Top Cards:{self.deck[:5]}
        """)
    


# In[5]:


my_deck = Deck()


# In[6]:


player1 = Player("Roger Federer", my_deck)
print(player1)


# In[7]:


import random
random.shuffle(my_deck)
player2 = Player("Eric Zhou", my_deck)
print(player2)


# Class Player is created. The deck is shuffled.

# ## Question 4

# In[3]:


class Player:

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        
    def __str__(self):
        return(f"""
        {self.name}\n Top Cards:{self.deck[:5]}
        """)
    
    def draw(self):
        card = self.deck.cards.pop(0)
        self.hand.append(card)


# In[11]:


fresh_deck = Deck()
player1 = Player("Zeru Zhou", fresh_deck)
random.shuffle(fresh_deck)
player1.draw()
print(player1.hand)


# In[12]:


player1.draw()
print(player1.hand)


# In[13]:


player1.draw()
print(player1.hand)


# Draw method is defined. Hand is also created.

# ## Question 5

# In[7]:


class Player:

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        
    def __str__(self):
        return(f"""
        {self.name}\n Top Cards:{self.deck[:5]}
        """)
    
    def draw(self):
        card = self.deck.cards.pop(0)
        self.hand.append(card)
    
    def has_set(self):
        count_hand = Counter(self.hand)
        for key, value in count_hand.items():
            if value >= 3:
                return True
        return False


# In[4]:


from collections import Counter


# In[8]:


import random
my_deck = Deck()
random.shuffle(my_deck)
player1 = Player("Zeru Zhou", my_deck)
for i in range(10): 
    player1.draw()

player1.has_set()


# In[10]:


print(player1.hand)


# Here, we can see there are 3 "k" making that a set.

# ## Pledge
# 
# By submitting this work I hereby pledge that this is my own, personal work. I've acknowledged in the designated place at the top of this file all sources that I used to complete said work, including but not limited to: online resources, books, and electronic communications. I've noted all collaboration with fellow students and/or TA's. I did not copy or plagiarize another's work.
# 
# > As a Boilermaker pursuing academic excellence, I pledge to be honest and true in all that I do. Accountable together – We are Purdue.
