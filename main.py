'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    nr=0
    for i in range(1,n+1):
        if n%i==0:
            nr=nr+1
    if nr==2:
        return True
    else:
        return False

  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    produs=1
    for ele in range(0, len(lst)):
        produs = produs * lst[ele]
    return produs
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    while x != y:
        if x > y: x -= y
        else: y -= x
    return x

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    while y!=0:
        r=x%y
        x=y
        y=r
    return x
  
def main():
    a = int(input("primul numar este:"))
    b = int(input("al doilea numar este:"))
    print(get_cmmdc_v1(a,b))
    print(get_cmmdc_v2(a,b))
if __name__ == '__main__':
  main()