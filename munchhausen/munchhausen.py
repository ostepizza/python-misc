import time

#Program settings
zeroIsZero = 1 #this one is broken :D
stopAtFirst = 0
timesToRun = 1000000000

#Program begins
l = 0
k = 0
j = 0
i = 0
h = 0
g = 0
f = 0
e = 0
d = 0 #etc
c = 0 #100s
b = 0 #10s
a = 0 #0s

overflow = 0

found = 0
runs = 0
newRun = 1

number_list = []

def sq(var):
    if var == 0 and zeroIsZero == 1:
        return(0)
    else:
        return(pow(var, var))
    
def addToFile(textInput):
    with open("Output.txt", "a") as text_file:
        if newRun == 1:
            text_file.write("--------------------\n")
            text_file.write(textInput + "\n")
        else:
            text_file.write(textInput + "\n")

startTimer = time.time()
        
while runs <= timesToRun and found != 1: 
    number_string=(str(l)+str(k)+str(j)+str(i)+str(h)+str(g)+str(f)+str(e)+str(d)+str(c)+str(b)+str(a))
    number=int(number_string)
    print(" Input: " + str(number))
    
    l_sq = sq(l)
    k_sq = sq(k)
    j_sq = sq(j)
    i_sq = sq(i)
    h_sq = sq(h)
    g_sq = sq(g)
    f_sq = sq(f)
    e_sq = sq(e)
    d_sq = sq(d)
    c_sq = sq(c)
    b_sq = sq(b)
    a_sq = sq(a)

    result = l_sq + k_sq + j_sq + i_sq + h_sq + g_sq + f_sq + e_sq + d_sq + c_sq + b_sq + a_sq
    result_string = str(result)

    if a == 0:
        a += 1
    elif a == 9:
        a = 0
        b += 1
        if b > 9:
            b = 0
            c += 1
            if c > 9:
                c = 0
                d += 1
                if d > 9:
                    d = 0
                    e += 1
                    if e > 9:
                        e = 0
                        f += 1
                        if f > 9:
                            f = 0
                            g += 1
                            if g > 9:
                                g = 0
                                h += 1
                                if h > 9:
                                    h = 0
                                    i += 1
                                    if i > 9:
                                        i = 0
                                        j += 1
                                        if j > 9:
                                            j = 0
                                            k += 1
                                            if k > 9:
                                                k = 0
                                                l += 1
                                                if l > 9:
                                                    l = 0
                                                    overflow += 1                  
    else:
        a += 1
    
    print("Result: " + str(result))

    if result == number:
        if stopAtFirst == 1:
            found = 1
        else:
            found = 0
            
        number_list.append(result)
        addToFile(str(result))
        newRun = 0
    
    runs += 1
#Loop end

endTimer = time.time()

print("Numbers found: " + str(number_list))
print("Time taken: " + str(int(endTimer-startTimer)) + " seconds")