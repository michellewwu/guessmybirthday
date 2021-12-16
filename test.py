import math
import random

def guess_birthday(month,d,t):
      l=[]
      if month=="December" or month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="October": 
        if(d=='odd' and t=='after'): l=[17, 19, 21, 23, 25, 27, 29, 31]
      elif  month=="June" or month=="September" or month=="February" or month=="April" or month=="November":
        if(d=='odd' and t=='after'): l=[17, 19, 21, 23, 25, 27, 29]
      
      if(d=='odd' and t=='before'): l=[1, 3, 5, 7, 9, 11, 13, 15]
      elif(d=='even' and t=='after'): l=[18, 20, 22, 24, 26, 28, 30]
      elif(d=='even' and t=='before'): l=[2, 4, 6, 8, 10, 12, 14, 16]
      
      o = (print("Is your birthday "+month+" ", (random.choice(l)), "?"))
      while input(o.lower()) != "Yes":
          print("Is your birthday "+month+" ", (random.choice(l)), "?")

print ("Hello! Welcome to the 'Guess My Birthday' game!")
sea = input("Please start by answering this question: Which season is your birthday in? ")

if sea.lower() == 'fall':
  f = input("Is your birthday in the same month as Labor Day, Halloween, or Thanksgiving? ")
  if f.lower() == 'labor day':
    d = input("Is your birth date odd or even? ")
    if d.lower() == 'odd':
      w = input("Is your birth date before or after the 16th? ")
      if w.lower() == 'after the 16th' or w.lower() == 'after':
        o = (print("Is your birthday September ", (random.choice(odda16)), "?"))
        while input(o.lower()) != "Yes":
          print("Is your birthday September ", (random.choice(odda16)), "?")
  elif f.lower()=="":
    pass
  else:
    pass

elif sea.lower() == 'spring':
    sp = input("Is your birthday in the same month as St.Patrick's Day, Easter, or Mother's Day?")

elif sea.lower() == 'summer':
    su = input("Is your birthday in the same month as Father's Day, Fourth of July, or National Watermelon Day?")

elif sea.lower()=='winter':
    w = input("Is your birthday in the same month as Christmas, New Years, or Valentine's Day?")
    if w.lower() == 'christmas':
      d = input("Is your birth date odd or even? ")
      if d.lower() == 'odd':
        w = input("Is your birth date before or after the 16th? ")
        if w.lower() == 'after the 16th' or w.lower() == 'after':
          o = (print("Is your birthday Decmeber ", (random.choice(odda16)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday December ", (random.choice(odda16)), "?")
        elif w.lower() == 'after the 16th' or w.lower() == 'before':
          o = (print("Is your birthday Decmeber ", (random.choice(oddb16)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday December ", (random.choice(oddb16)), "?")
      elif d.lower() == 'even':
        w = input("Is your birth date before or after the 17th? ")
        if w.lower() == 'after the 17th' or w.lower() == 'after':
          o = (print("Is your birthday December ", (random.choice(evena17)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday December ", (random.choice(evena17)), "?")
        elif w.lower() == 'after the 17th' or w.lower() == 'before':
          o = (print("Is your birthday Decmeber ", (random.choice(evenb17)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday December ", (random.choice(evenb17)), "?")
    elif w.lower() == 'new years':
      d = input("Is your birth date odd or even? ")
      if d.lower() == 'odd':
        w = input("Is your birth date before or after the 16th? ")
        if w.lower() == 'after the 16th' or w.lower() == 'after':
          o = (print("Is your birthday January ", (random.choice(odda16)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday January ", (random.choice(odda16)), "?")
        elif w.lower() == 'after the 16th' or w.lower() == 'before':
          o = (print("Is your birthday January ", (random.choice(oddb16)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday January ", (random.choice(oddb16)), "?")
      elif d.lower() == 'even':
        w = input("Is your birth date before or after the 17th? ")
        if w.lower() == 'after the 17th' or w.lower() == 'after':
          o = (print("Is your birthday January ", (random.choice(evena17)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday January ", (random.choice(evena17)), "?")
        elif w.lower() == 'after the 17th' or w.lower() == 'before':
          o = (print("Is your birthday January ", (random.choice(evenb17)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday January ", (random.choice(evenb17)), "?")
    elif w.lower() == 'valentine':
      d = input("Is your birth date odd or even? ")
      if d.lower() == 'odd':
        w = input("Is your birth date before or after the 16th? ")
        if w.lower() == 'after the 16th' or w.lower() == 'after':
          o = (print("Is your birthday February ", (random.choice(odda16)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday February ", (random.choice(odda16)), "?")
        elif w.lower() == 'after the 16th' or w.lower() == 'before':
          o = (print("Is your birthday February ", (random.choice(oddb16)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday February ", (random.choice(oddb16)), "?")
      elif d.lower() == 'even':
        w = input("Is your birth date before or after the 17th? ")
        if w.lower() == 'after the 17th' or w.lower() == 'after':
          o = (print("Is your birthday February ", (random.choice(evena17)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday February ", (random.choice(evena17)), "?")
        elif w.lower() == 'after the 17th' or w.lower() == 'before':
          o = (print("Is your birthday February ", (random.choice(evenb17)), "?"))
          while input(o.lower()) != "Yes":
            print("Is your birthday February ", (random.choice(evenb17)), "?")



