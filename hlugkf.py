day = int(input('write your day:'))
month = int(input('write you month:'))

if (month == 3 and 21 <= day < 31) or (month == 4 and 1 <= day <= 20):
   print('oven')
elif (month == 4 and 21 <= day <= 31) or (month == 5 and 1 <= day <= 21):
   print('telec')
elif (month ==5 and 22 <= day <= 31) or (month == 6 and  1 <= day <= 21):
   print('bliznec')
elif (month ==6 and 22 <= day <= 31) or (month == 7 and  1 <= day <= 22):
   print('rak')
elif (month ==7 and 23 <= day <= 31) or (month == 8 and  1 <= day <= 21):
   print('lev')
elif (month ==8 and 22 <= day <= 31) or (month == 9 and  1 <= day <= 23):
   print('deva')
elif (month ==9 and 24 <= day <= 31) or (month == 10 and  1 <= day <= 23):
   print('vecy')
elif (month ==10 and 24 <= day <= 31) or (month == 11 and 1 <= day <= 22):
   print('scorpion')
elif (month ==11 and 23 <= day <= 31) or (month == 12 and  1 <= day <= 22):
   print('strelec')
elif (month ==12 and 23 <= day <= 31) or (month == 1 and  1 <= day <= 20):
   print('kozerog')
elif (month == 1 and 21 <= day <= 31) or (month == 2 and  1 <= day <= 19):
   print('vodolei')
elif (month == 2 and 20 <= day <= 31) or (month == 3 and 1 <= day <= 21):
   print('ryby')
else:
   print('something went wrong,please ! write correctly')