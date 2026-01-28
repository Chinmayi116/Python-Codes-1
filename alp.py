class MyString:
    def __init__(self, s):
        self.s = s

    def count(self):
        v = c = d = sp = u = 0
        for ch in self.s:
            if ch.lower() in "aeiou":
                v += 1
            elif ch.isalpha():
                c += 1
            elif ch.isdigit():
                d += 1
            elif ch == " ":
                sp += 1
            if ch.isupper():
                u += 1

        print("Vowels:", v)
        print("Consonants:", c)
        print("Digits:", d)
        print("Spaces:", sp)
        print("Uppercase:", u)

s = MyString("Hello World 123")
s.count()
