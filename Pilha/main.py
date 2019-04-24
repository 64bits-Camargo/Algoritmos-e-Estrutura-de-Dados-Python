# -*- coding: utf-8 -*-


from stack import Stack


s = Stack()

s.push(2*2)
s.push('*%&*')
s.push('a'+'b')
s.push(1 == 2)

print("Último elemento: {}".format(s.top()))
print("Tamanho da pilha: {}".format(s.length()))

