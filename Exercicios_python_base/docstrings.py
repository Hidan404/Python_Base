from pathlib import Path

class View:
    """Classe de exemplo para demonstrar docstrings."""
    
    def display(self):
        """Exibe uma mensagem de exemplo."""
        print("Esta é uma mensagem de exemplo.")

print(dir(View))
print(View.__doc__)
#print(View.__file__)
print(View.__name__)