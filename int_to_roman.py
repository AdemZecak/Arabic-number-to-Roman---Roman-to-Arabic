import re

print("-"*50)
print("Welcome to GATE 21 number converter!")
print("-"*50)



#brojevi predstavljeni kroz "dictionary" koji će se služiti u zadatku

numbers = {

    1000 : "M",
    900 : "CM",
    500 : "D",
    400 : "CD",
    100 : "C",
    90 : "XC",
    50 : "L",
    40 : "XL",
    10 : "X",
    9 : "IX",
    5 : "V",
    4 : "IV",
    1 : "I",
    
}


#funkcija koja pretvara arapske brojeve u rimske 

def arabic(num):

    num_int = int(num)

    roman = ''

    while num_int > 0:
        for j, k in numbers.items():
            while num_int >= j:
                roman += k
                num_int -= j

    print("Equivalent of number", num, "is", roman,".")


#funkcija koja pretvara rimske brojeve u arapske

def roman_to_int(num):


    roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    int_value = 0

    for i in range(len(num)):
        if i > 0 and roman_value[num[i]] > roman_value[num[i - 1]]:
            int_value += roman_value[num[i]] - 2 * roman_value[num[i - 1]]
        else:
            int_value += roman_value[num[i]]

    print("Equivalent of number",num, "is", int_value,".")
  

#kroz jedan input saznajemo da li je broj rimski ili arapski nakon čega nastavljamo sa konvertovanjem u njegov ekvivalent


num = input("Please enter your number: ").upper()

rimski = re.compile(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",re.VERBOSE)


if num.isdigit() in numbers.keys():

    arabic(num)
    

elif re.match(rimski,num):
    roman_to_int(num)
    

else:

    print("Sorry, invalid input, please enter roman or arabic numbers.")