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
      
      day=str((random.choice(l)))
      m = input("Is your birthday "+month+" "+day+"? (yes/no)")
      while m.lower() == 'no':
        day=str((random.choice(l)))
        m = input("Is your birthday "+month+" " +day+ "?(yes/no)")
        if m.lower() == 'yes':
          return month,day
      return month,day

def main():
  sea = input("Please start by answering this question: Which season is your birthday in?")
  print()
  if sea.lower() == 'winter':
    w = input("Is your birthday in the same month as Christmas, New Years, or Valentine's Day?")
    if w.lower() == 'christmas':
      month='December'
    elif w.lower() =='new years':
      month='January'
    elif w.lower() == "valentine's day":
      month='February'
  elif sea.lower() == 'fall':
    w = input("Is your birthday in the same month as Labor Day, Halloween, or Thanksgiving?")
    if w.lower() == 'labor Day':
      month='September'
    elif w.lower() =='halloween':
      month='October'
    elif w.lower() == 'thanksgiving':
      month='November'
  elif sea.lower() =='spring':
    w = input("Is your birthday in the same month as St. Patricks, Easter, or Mother's day?")
    if w.lower() =='st. patricks':
      month = 'March'
    elif w.lower() =='easter':
      month='April'
    elif w.lower() == "mother's day":
      month='May'
  elif sea.lower() == 'summer':
    w = input("Is your birthday in the same month as Father's day, Fourth of July, or National Watermelon Day?")
    if w.lower() =="father's day":
      month = 'June'
    elif w.lower() =='fourth of july':
      month='July'
    elif w.lower() == "national watermelon day":
      month='August'
  
  d = input("Is your birth date odd or even? (odd/even)")
  if d=='odd':
    t = input("Is your birth date before or after the 16th? (before/after)")
  elif d=='even':
    t = input("Is your birth date before or after the 17th? (before/after)")
  m,day=guess_birthday(month,d,t)
  print("I guessed it! Your Birthday is" + " "+m +" "+ day )
     
main()