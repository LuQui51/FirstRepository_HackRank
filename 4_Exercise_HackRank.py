def print_rangoli(size):
    alf = ["a","b","c","d","e","f","g","h","i","j",
           "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alf_use = alf[0:size]
    alf_use_r = alf_use[::-1]

    #Mayor
    alf_use_r1 = alf_use_r
    alf_use_r2 = alf_use_r

    n = 1
    for _ in range(len(alf_use_r)):

        text1 = ""
        text2 = ""
        g = 1
        h = 1

        for i in alf_use_r1[:n]:
            if g==1:
                text1 = i
            else:
                text1 = text1 + "-" + i
            g = 0


        if n != 1:
            for m in alf_use_r2[:n-1]:
                if h == 1:
                    text2 = m
                else:
                    text2 = m + "-" + text2
                h = 0

        text2 = "-" + text2[:(2*size-2)]
        text1 = text1[0:] 

        n += 1

        if len(alf_use_r) == 1:
            print(text1)
        else:
            print(text1.rjust((2*size)-1,"-") + text2.ljust((2* size - 2),"-"))


    #Menor
    alf_use2 = alf_use[1:size]
    alf_use3 = alf_use[2:size] + [""]
    for _ in range(len(alf_use2)):

        text3 = ""
        text4 = ""

        for k in alf_use2:
           text3 = k + "-" + text3

        for j in alf_use3:
            text4 = text4 + "-" + j

        text4 = text4[1:]

        alf_use2.pop(0)
        alf_use3.pop(0)

        print(text3.rjust((2*size),"-")+text4.ljust(2*size - 3,"-"))


n = int(input("Num: "))
print_rangoli(n)