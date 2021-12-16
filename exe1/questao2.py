#!/usr/bin/python

def read_pol(g, n):
    p = [0] * (g+1)

    for i in range(g+1):
         p[i] = int( input(f"p[{i}]: ") )%n

    return p


def multiply(a, b, n):
    c = [0] * (len(a)+len(b)-1)
    
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] = (c[i+j] + a[i]*b[j]) % n

    print("c(x) = ", end="")
    for i in range(len(c)):
        if c[i] != 0:
            print(f"{c[i]}x^{i} + ", end="")
        
    print()
    

def main():
    n = int( input("N: ") )
    ga = int( input("Grau do polinômio a: ") )
    print("Preencha o polinômio a: ")
    a = read_pol(ga, n)
    gb = int( input("Grau do polinômio b: ") )
    print("Preencha o polinômio b: ")
    b = read_pol(gb, n)

    multiply(a, b, n)

main()
