#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    costPrice = distance * 7
    sellingPrice = no_of_passengers * 80

    if(sellingPrice > costPrice):
        return sellingPrice - costPrice
    else:
        return -1
    #Remove pass and write your logic here

#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
