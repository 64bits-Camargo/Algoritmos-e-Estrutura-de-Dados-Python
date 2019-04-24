# -*- coding: utf-8 -*-


class Stack(object):
    """
    Conceito de Pilha
    
    Estrutura de dados baseado no princípio de 'Last in First Out(LIFO)', ou seja,
    "o último que entra é o primeiro a sair" caracterizando empilhamento de dados.
    Pilhas são fundamentalmente compostas por duas operações: push(empilhar) que 
    adiciona elemento no topo da pilha, e pop(desempilhar) que remove o último 
    elemento da pilha.
    """
    
    def __init__(self):
        """
        Método Construtor
        
        Atributos:
        stack       -> lista vazia.
        len_stack   -> carrega o tamanho da lista, otimizando o tempo para consulta de tamanho
        e remoção do último item.
        """
        
        self.stack = []
        self.len_stack = 0
    
    def push(self, e):
        """
        Método push(elemento)
        
        Push recebera um elemento e com o append adicionara esse elemento por último na pilha,
        depois de adicionado é incrementada a variável len_stack.
        """        
        self.stack.append(e)
        self.len_stack += 1
            
    def pop(self):
        """
        Método pop()
        
        Pop removerá o último elemento da pilha, mas antes verificar com o método empty(), se a pilha
        não está vazia, caso esteja nada será feito. O Pop não tornará o valor da variavél len_stack
        negativo.
        """
        
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1
        
    def top(self):
        """
        Método top()
        
        Top busca o último elemento da pilha, caso esteja vazia a pilha não retornara None.
        """
        
        if not self.empty():
            return self.stack[-1]
    
    def empty(self):
        """
        Método empty()
        
        Empty verifica se a pilha está vazia.
        """
        
        if (self.len_stack == 0):
            return True
        return False
    
    def length(self):
        """
        Método length()
        
        Length verifica o tamanho da lista.
        """
        
        return self.len_stack

