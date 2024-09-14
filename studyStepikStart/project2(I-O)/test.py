#a=[[]] * 3
#a[1].append(1)
#print(a)

class A:
    def test(self):
        print("A")
class B(A):
    def test(self):
        print("B")
class C(A):
    def test(self):
        print("C")
class D(B,C):
    def new_test(self):
        print("D")
obj = D()
obj.test()



def foo(a=[]):
    a.append(1)
    print(a)

foo()
foo()
foo()