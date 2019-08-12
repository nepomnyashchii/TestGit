numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Declaring the tuple
odd_number = 0
even_number = 0
for x in numbers:
        if not x % 2:
    	     even_number+=1
        else:
    	     odd_number+=1
print(even_number)
print(odd_number)