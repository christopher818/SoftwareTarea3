'''
Created on 11 de may. de 2016

@author: Christopher Flores
'''
import unittest
from BilleteraElectronica import *
from datetime import datetime 


class Test(unittest.TestCase):

    # Caso TDD para probrar que se crea una Billetera Electronica 
    def testClaseBE(self):
        BE = BilleteraElectronica(1,"Christopher","Flores",21534848,2970)
    
    #Caso TDD para probar que la Billetera acepta caracteres especiales
    def testClaseBeEspeciales(self):
        pass
    
    #Caso TDD para probrar que existe el metodo saldo
    def testSaldo(self):
        BE = BilleteraElectronica(3,"Christopher","Flores",21534848,1234)
        BE.saldo()
        
    #Caso TDD para probrar que existe el metodo recargar
    def testRecargar(self):
        BE = BilleteraElectronica(4,"Christopher","Flores",21534848,2345)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        BE.recargar(10,fechaRecarga,"Restaurante10")
    
    #Caso TDD para probar que el metodo esta realmente recargando
    def testRecargarTrue(self):
        BE = BilleteraElectronica(5,"Christopher","Flores",21534848,3456)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        BE.recargar(100,fechaRecarga,"Restaurante11")
        self.assertEqual(BE.saldo(), 100, "El saldo no es el correcto")
        
    #Caso TDD para probar que existe el metodo consumir
    def testConsumir(self):
        BE = BilleteraElectronica(6,"Christopher","Flores",21534848,4567)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        BE.recargar(100,fechaRecarga,"Restaurante12")
        fechaConsumo = datetime(2016,5, 11, 6, 15)
        BE.consumir(11,fechaConsumo,"Restaurante12",4567)
        
    #Caso TDD para probar que el metodo esta realmente consumiendo
    def testConsumirTrue(self):
        BE = BilleteraElectronica(7,"Christopher","Flores",21534848,5678)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        BE.recargar(100,fechaRecarga,"Restaurante12")
        fechaConsumo = datetime(2016,5, 11, 6, 15)
        BE.consumir(12,fechaConsumo,"Restaurante12",5678)
        self.assertEqual(BE.saldo(), 88, "No esta consumiendo correctamente y el saldo no es el correcto")
    
    #Caso TDD para probar que al consumir el pin sea el mismo que el del dueno de la billetera
    def testConsumirPinTrue(self):
        BE = BilleteraElectronica(8,"Christopher","Flores",21534848,6789)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        BE.recargar(100,fechaRecarga,"Restaurante12")
        fechaConsumo = datetime(2016,5, 11, 6, 15)
        BE.consumir(13,fechaConsumo,"Restaurante12",6789)
        self.assertEqual(BE.pin, 6789, "No esta consumiendo correctamente y el saldo no es el correcto")
    
    #Caso TDD para probar que al consumir el pin sea distinto al del dueno de la billetera
    def testComusirPinFalse(self):
        BE = BilleteraElectronica(9,"Christopher","Flores",21534848,7890)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        BE.recargar(100,fechaRecarga,"Restaurante12")
        fechaConsumo = datetime(2016,5, 11, 6, 15)
        self.assertRaises(Exception, BE.consumir,13,fechaConsumo,"Restaurante12",7891)
    
    #Caso TDD para consumir sin saldo suficiente a pesar de tener saldo
    def testConsumirSinSaldo(self):
        BE = BilleteraElectronica(10,"Christopher","Flores",21534848,7891)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        fechaConsumo = datetime(2016,5, 11, 6, 15)
        BE.recargar(100,fechaRecarga,"Restaurante12")
        self.assertRaises(Exception, BE.consumir,150,fechaConsumo,"Restaurante13",7891)
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()