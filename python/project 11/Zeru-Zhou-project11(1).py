#!/usr/bin/env python
# coding: utf-8

# # Project11 -- Zeru Zhou

# **TA Help:** NA
# 
# 
#     
# **Collaboration:** NA
#     
# - Get help from dr. Ward's videos
# - Get help from this link https://stackoverflow.com/questions/2361945/detecting-consecutive-integers-in-a-list

# ## Question 1

# In[2]:


from collections import Counter

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []

    def __str__(self):
        return(f"""
        {self.name}\n
        Top 5 cards: {self.deck[:5]}
        """)

    def draw(self):
        card = self.deck.cards.pop(0)
        self.hand.append(card)

    def has_set(self):
        summarizedhand = Counter(self.hand)
        for key, value in summarizedhand.items():
            if value >= 3:
                return True
        return False
    
    def get_sets(self):
        summarizedhand = Counter(self.hand)
        my_set = []
        for key, value in summarizedhand.items():
            if value >= 3:
                my_set.append([card for card in self.hand if card == key])
        return my_set
                


# In[3]:


class Card:
    _value_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8, "9":9, "10": 10, "j": 11, "q": 12, "k": 13, "a": 1}
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


# In[4]:


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
        return f"A {self.brand.lower()} deck."


# In[5]:


import random
deck = Deck()
player1 = Player("Eric", deck)
random.shuffle(deck)
for i in range(20):
    player1.draw()
sets = player1.get_sets()
sets


# As above, get_sets method is added.

# ## Question 2

# In[6]:


from collections import Counter

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []

    def __str__(self):
        return(f"""
        {self.name}\n
        Top 5 cards: {self.deck[:5]}
        """)

    def draw(self):
        card = self.deck.cards.pop(0)
        self.hand.append(card)

    def has_set(self):
        summarizedhand = Counter(self.hand)
        for key, value in summarizedhand.items():
            if value >= 3:
                return True
        return False
    
    def get_sets(self):
        summarizedhand = Counter(self.hand)
        my_set = []
        for key, value in summarizedhand.items():
            if value >= 3:
                my_set.append([card for card in self.hand if card == key])
        return my_set
    
    def hand_as_df(self):
        my_df = {'suit': [], 'numeric_value': [], 'card': []}
        for card in self.hand:
            my_df['suit'].append(card.suit)
            my_df['numeric_value'].append(card._value_dict[card.number])
            my_df['card'].append(card)
        return my_df


# In[7]:


import random
import pandas as pd
deck = Deck()
player1 = Player("Eric", deck)
random.shuffle(deck)
for i in range(20):
    player1.draw()

sets = pd.DataFrame(data = player1.hand_as_df())
sets


# Data frame is created.

# ## Question 3

# In[29]:


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []

    def __str__(self):
        return(f"""
        {self.name}\n
        Top 5 cards: {self.deck[:5]}
        """)

    def draw(self):
        card = self.deck.cards.pop(0)
        self.hand.append(card)

    def has_set(self):
        summarizedhand = Counter(self.hand)
        for key, value in summarizedhand.items():
            if value >= 3:
                return True
        return False
    
    def get_sets(self):
        summarizedhand = Counter(self.hand)
        my_set = []
        for key, value in summarizedhand.items():
            if value >= 3:
                my_set.append([card for card in self.hand if card == key])
        return my_set
    
    def hand_as_df(self):
        my_df = {'suit': [], 'numeric_value': [], 'card': []}
        for card in self.hand:
            my_df['suit'].append(card.suit)
            my_df['numeric_value'].append(card._value_dict[card.number])
            my_df['card'].append(card)
        return my_df
    
    def get_runs(self):
        outcome = []
        consecutive = []
        consecutive1 = []
        final=[]
        for idx, group in df.groupby("suit"):
            group = group.sort_values(by = ['numeric_value'])
            outcome.append(group['numeric_value'].tolist())
        from itertools import groupby
        from operator import itemgetter
        for i in outcome:
            for a, b in groupby(enumerate(i), lambda ix : ix[0]-ix[1]):
                consecutive.append(list(map(itemgetter(1), b)))
        for i in consecutive:
            if len(i) >= 3:
                consecutive1.append(i)
        for lists in consecutive1:
            for idx, group in df.groupby("suit"):
                if all(item in group['numeric_value'].tolist() for item in lists):
                    for element in lists:
                        for i in group['numeric_value']:
                            if element==i:
                                final.append(group.loc[group['numeric_value']==i,'card'])
        return final
                
            
            


# In[24]:


import random
import pandas as pd
deck = Deck()
player1 = Player("Alice", deck)
random.shuffle(deck)
for _ in range(20):
    player1.draw()

df = player1.hand_as_df()
df = pd.DataFrame(df)
df


# In[30]:


import random

deck = Deck()
player1 = Player("Alice", deck)
random.shuffle(deck)
for _ in range(20):
    player1.draw()

runs = player1.get_runs()
runs


# As above, get_runs is created.

# ## Pledge
# 
# By submitting this work I hereby pledge that this is my own, personal work. I've acknowledged in the designated place at the top of this file all sources that I used to complete said work, including but not limited to: online resources, books, and electronic communications. I've noted all collaboration with fellow students and/or TA's. I did not copy or plagiarize another's work.
# 
# > As a Boilermaker pursuing academic excellence, I pledge to be honest and true in all that I do. Accountable together – We are Purdue.
