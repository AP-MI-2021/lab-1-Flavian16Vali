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
  print("ana are mere")
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  print("ana are mere")


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  print("ana are mere")
  
  
def main():
    n = int(input("n este:"))
    if is_prime(n):
        print("a")
    else:
        print("b")

if __name__ == '__main__':
  main()