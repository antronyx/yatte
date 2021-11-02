# YATTE
# Yet Another Truth Table Elaborator

import readline

n=int(input("Insert number of variables\n"))
readline.read_history_file('.yatte_history')
stringin=input("Insert Expression\n")
readline.append_history_file(1,'.yatte_history')
#Convert +, * to and, or
stringin=stringin.replace('+',' or ')
stringin=stringin.replace('*', ' and ')

max_num=2**n
lst = ["{:0{}b}".format(x, n) for x in range(2**n)]
i=0
minterms=[]



print()
print ("N\tBinary\tValue")


while(i<max_num):
    try:
        num=lst[i]
        a=bool(int(num[0]))
        b=bool(int(num[1]))
        c=bool(int(num[2]))
        d=bool(int(num[3]))
        e=bool(int(num[4]))
        f=bool(int(num[5]))
        g=bool(int(num[6]))
        h=bool(int(num[7]))
        i=bool(int(num[8]))
        l=bool(int(num[9]))
        m=bool(int(num[10]))
        n=bool(int(num[11]))
        o=bool(int(num[12]))
        p=bool(int(num[13]))
        q=bool(int(num[14]))
        r=bool(int(num[15]))
        
    except:
        pass
    fun_out=eval(stringin)
    
    if(fun_out):
        minterms.append(i)
    print("------------------------")
    print("|%s\t|%s\t|%s\t|" %(i, lst[i], fun_out))
    i=i+1
print("------------------------")
print()
print("Those are the function's minterms [f=Σ m(...)]:")
print(minterms)

