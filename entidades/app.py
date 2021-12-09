from FuncionesGenerales import FuncionesGenerales as fncGen
from Gramatica import Gramatica

from LR1

ruta = 'archivos\gramatica1.json'

gram = Gramatica()
gram = fncGen.leerJson(ruta)

gram.imprimir()