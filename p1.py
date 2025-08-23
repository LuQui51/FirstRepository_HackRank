def print_formatted(num):
    for j in range(1,num+1):
        #Decimal
        decimal = j

        #Octal 
        i = j
        octal = 0
        dec = 1
        while(i!=0):
            octal += i%8 * dec    
            i = int(i/8)
            dec *= 10


        #Hexa
        hexa = (str(hex(j)[2:])).capitalize()


        #Binary
        i = j
        binary = 0
        dec = 1
        while(i!=0):
            binary += i%2 * dec    
            i = int(i/2)
            dec *= 10
        
        espacio = len(bin(num)[2:])
        espacio1 = str(decimal).rjust(espacio," ")
        espacio2 = str(octal).rjust(espacio + 1," ")
        espacio3 = str(hexa).upper().rjust(espacio + 1," ")
        espacio4 = str(binary).rjust(espacio + 1," ")

        print(espacio1 + espacio2 + espacio3 + espacio4 )


n = int(input())
print_formatted(n)
63