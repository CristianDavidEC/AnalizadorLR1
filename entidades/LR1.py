from Gramatica import Gramatica

class LR1:
    
    def __init__(self, gramatica):
        self.gramatica = gramatica


    def analizar(self):
        self.extender()
        self.gramatica.imprimir()


    def extender(self):
        producciones = self.gramatica.getProducciones();
        inicial = self.gramatica.getInicial();
        exten = self.gramatica.getInicial()+"'";

        producciones.insert(0, f'{exten}>{inicial}')

        self.gramatica.setProducciones(producciones);
        self.gramatica.addNoTerminal(exten);

        