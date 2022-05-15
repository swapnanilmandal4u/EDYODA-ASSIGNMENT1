# WRITE A PYTHON TO COUNT THE NUMBER OF EVEN AND ODD NUMBERS FROM A SERIES OF NUMBER.


numbers = ( 1,2,3,4,5,6,7,8,9 )
even_num_count =0
odd_num_count =0
for i in numbers:
    if i%2==0:
        even_num_count+=1
    else:
        odd_num_count+=1
print("numbers of even numbers", even_num_count)
print("numbers of odd numbers",odd_num_count)
    

