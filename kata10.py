#  7x^1 - 2x^2 + 1x^3 + 2x^4 =  3
#  2x^1 + 8x^2 + 3x^3 + 1x^4 = -2
# -1x^1 + 0x^2 + 5x^3 + 2x^4 =  5
#  0x^1 + 2x^2 - 1x^3 + 4x^4 =  4

def getX1(x2,x3,x4):
    return (3+2*x2-x3-2*x4)/7

def getX2(x1,x3,x4):
    return (-2-2*x1-3*x3-x4)/8

def getX3(x1,x2,x4):
    return (5+x1-2*x4)/5

def getX4(x1,x2,x3):
    return (4-2*x2+x3)/4


x1=0
x2=0
x3=0
x4=0

#error=0.00001

x1a = 0.00001
x2a = 0.00001
x3a = 0.00001
x4a = 0.00001
for i in range(5):
    x1 = getX1(x2,x3, x4)
    x2 = getX2(x1,x3, x4)
    x3 = getX3(x1,x2, x4)
    x4 = getX4(x1,x2, x3)
    #print("VALUES {0}{1}{2}{3}".format(x1,x2,x3,x4))
    ex1 = abs((x1a-x1)/x1a)
    ex2 = abs((x2a-x2)/x2a)
    ex3 = abs((x3a-x3)/x3a)
    ex4 = abs((x4a-x4)/x4a)
    #if ex1 < error and ex2 < error and ex3 < error:
        #break
    x1a = x1
    x2a = x2
    x3a = x3
    x4a = x4

print("FINAL: {0}\t{1}\t{2}\t{3}".format(x1,x2,x3,x4))
print("Errores: {0}\t{1}\t{2}\t{3}".format(ex1,ex2,ex3,ex4))
