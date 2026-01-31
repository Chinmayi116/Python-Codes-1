class Complex:
    def __init__(self,real=0,img=0):
        self.real=real
        self.img=img
    def __add__(self,other):
        real_part=self.real+other.real
        img_part=self.img+other.img
        return Complex(real_part,img_part)
    def display(self):
        print(f"{self.real}+{self.img}i")
c1=Complex(10,90)
c2=Complex(20,38)
c3=c1+c2
c2.display()