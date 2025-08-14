
def wrap(string, max_width):

    lista_string = list(string)

    value_continue = False
    if 0 < len(string) and 1000 > len(string):
        if 0 < max_width and len(string) > max_width:
            value_continue = True
    
    #todos los strings posibles con el max_width indicado
    if value_continue == True:
        for i in range(int(len(string)/max_width)):
            text = []
            for _ in range(max_width):
                text.append(lista_string[0])
                lista_string.pop(0)
            print(text)

    #If the len(string) is add or even, we check that last part 
    if int(len(string)%max_width)!=0:
        print(lista_string)
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap(string, max_width)
