from abc import ABC, abstractmethod

class IAnimal(ABC):
    
    @abstractmethod
    def falar(self):
        """Defina na classe filha."""
    
    @abstractmethod
    def andar(self):
        """Defina na classe filha."""
        
        
class Cachorro(IAnimal):
    
    def falar(self):
        print("Au au au.")
    
    def andar(self):
        print("Anda com 4 patas.")
        
        
class Pessoa():
    
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
        self.__humano = True
    
    def fala_pessoa(self):
        print("Falando...")
        
    def mostra_nome_e_idade(self):
        print(f"Nome: {self._nome} e Idade: {self.idade}")
        
        
pingo = Cachorro()
pingo.falar()
pingo.andar()

humano = Pessoa("Fulano", 35)
humano.fala_pessoa()
humano.mostra_nome_e_idade()