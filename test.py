'''
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

def main():
  sea = input("Please start by answering this question: Which season is your birthday in?")
  month = ''
  d = ''
  t = ''
  if sea.lower() == 'winter':
    w = input("Is your birthday in the same month as Christmas, New Years, or Valentine's Day?")
    d = input("Is your birth date odd or even? ")
    if d=='odd':
      t = input("Is your birth date before or after the 16th? ")
    elif d=='even':
      t = input("Is your birth date before or after the 17th? ")
    if w.lower() == 'christmas':
      month='December'
    elif  =='new years':
      month='January'
    elif == 'valentine':
      month='February'
  elif:
    w = input("Is your birthday in the same month as Christmas, New Years, or Valentine's Day?")
    d = input("Is your birth date odd or even? ")
    t = input("Is your birth date before or after the 16th? ")
    if w.lower() == 'christmas':
      month=''
    elif  =='new years':
      month='January'
    elif == 'valentine':
      month='February'
  elif sea.lower() =='spring':
    w = input("Is your birthday in the same month as a, b, or c?")
    d = input("is your birth date odd or even?")
    if d=='odd':
      t = input("Is your birth date before or after the 16th? ")
    elif d=='even':
      t = input("Is your birth date before or after the 17th? ")
    if w.lower()='a':
      month = 'March'
    elif  =='b':
      month='April'
    elif == 'c':
      month='May'
  elif:
    pass

  guess_birthday(month,d,t)
     

 main()
 '''
 import math
import random

oddb16 = [1, 3, 5, 7, 9, 11, 13, 15]
odda16 = [17, 19, 21, 23, 25, 27, 29, 31]
evenb15 = [2, 4, 6, 8, 10, 12, 14]
evena15 = [16, 18, 20, 22, 24, 26, 28, 30]

print ("Hello! Welcome to the 'Guess My Birthday' game!")

sea = input("Please start by answering this question: Which season is your birthday in? ")

#FALL

if sea.lower() == 'fall':
    f = input("Is your birthday in the same month as Labor Day, Halloween, or Thanksgiving? ")
    if f.lower() == 'labor day':  #laborday
        d = input("Is your birth date odd or even? ")
        if d.lower() == 'odd':     #odd
            w = input("Is your birth date before or after the 16th? ")  
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday September", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday September", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before':
                o = (print("Is your birthday September", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday September", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':   #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday September", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday September", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before':
                o = (print("Is your birthday September", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday September", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;
                    
    elif f.lower() == 'halloween':  #halloween
        d = input("Is your birth date odd or even? ")
        if d.lower() == 'odd':        #odd
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday October", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday October", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before': #before
                o = (print("Is your birthday October", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday October", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':    #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday October", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday October", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before': #before
                o = (print("Is your birthday October", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday October", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;
    else:                            #thanksgiving
        d = input("Is your birth date odd or even? ")   
        if d.lower() == 'odd':
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday November", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday November", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before':
                o = (print("Is your birthday November", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday November", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':    #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday November", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday November", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before':
                o = (print("Is your birthday November", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday November", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;

#SPRING

if sea.lower() == 'spring':
    f = input("Is your birthday in the same month as St.Patricks Day, Easter, or Mother's Day? ")
    if f.lower() == "st.patrick's day" or f.lower() == "st.patricks day":  #stpatricks day
        d = input("Is your birth date odd or even? ")
        if d.lower() == 'odd':     #odd
            w = input("Is your birth date before or after the 16th? ")  
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday March", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday March", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before':
                o = (print("Is your birthday March", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday March", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':   #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday March", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday March", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before':
                o = (print("Is your birthday March", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday March", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;
                    
    elif f.lower() == 'easter':  #easter
        d = input("Is your birth date odd or even? ")
        if d.lower() == 'odd':        #odd
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday April", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday April", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before': #before
                o = (print("Is your birthday April", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday April", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':    #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday April", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday April", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before': #before
                o = (print("Is your birthday April", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday April", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;
    else:                            #mother's day
        d = input("Is your birth date odd or even? ")   
        if d.lower() == 'odd':
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday May", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday May", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before':
                o = (print("Is your birthday May", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday May", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':    #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday May", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday May", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before':
                o = (print("Is your birthday May", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday May", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;

#SUMMER
                    
elif sea.lower() == 'summer':
    f = input("Is your birthday in the same month as Father's Day, Fourth of July, or National Watermelon Day? ")
    if f.lower() == "fathers day" or f.lower() == "father's day":  #fathersday
        d = input("Is your birth date odd or even? ")
        if d.lower() == 'odd':     #odd
            w = input("Is your birth date before or after the 16th? ")  
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday June", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday June", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before':
                o = (print("Is your birthday June", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday June", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':   #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday June", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday June", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before':
                o = (print("Is your birthday June", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday June", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;
                    
    elif f.lower() == 'fourth of july':  #fourthofjuly
        d = input("Is your birth date odd or even? ")
        if d.lower() == 'odd':        #odd
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday July", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday July", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before': #before
                o = (print("Is your birthday July", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday July", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':    #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday July", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday July", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before': #before
                o = (print("Is your birthday July", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday July", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;
    else:                            #national watermelon day
        d = input("Is your birth date odd or even? ")   
        if d.lower() == 'odd':
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 16th' or w.lower() == 'after':
                o = (print("Is your birthday August", (random.choice(odda16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday August", (random.choice(odda16)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 16th' or w.lower() == 'before':
                o = (print("Is your birthday August", (random.choice(oddb16)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday August", (random.choice(oddb16)), "?")
                    if n.lower() == 'yes':
                        break;
        elif d.lower() == 'even':    #even
            w = input("Is your birth date before or after the 16th? ")
            if w.lower() == 'after the 15th' or w.lower() == 'after':
                o = (print("Is your birthday August", (random.choice(evena15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday August", (random.choice(evena15)), "?")
                    if n.lower() == 'yes':
                        break;
            elif w.lower() == 'before the 15th' or w.lower() == 'before':
                o = (print("Is your birthday August", (random.choice(evenb15)), "?"))
                m = input(o)
                while m == 'no':
                    n = print("Is your birthday August", (random.choice(evenb15)), "?")
                    if n.lower() == 'yes':
                        break;
else:
    w = input("Is your birthday in the same month as Christmas, New Years, or Valentine's Day?")
