'''
Created on 11 de may. de 2016

@author: Christopher Flores
'''
import unittest
from BilleteraElectronica import *
from datetime import datetime 
import sys

class Test(unittest.TestCase):

    # Caso TDD para probrar que se crea una Billetera Electronica 
    def testClaseBE(self):
        BE = BilleteraElectronica(1,"Christopher","Flores",21534848,2970)
    
 
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
    
    #Caso Frontera donde monto de recarga sea negativo
    def testRecargaNegativa(self):
        BE = BilleteraElectronica(11,"Christopher","Flores",21534848,8912)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        self.assertRaises(Exception, BE.recargar,-100,fechaRecarga,"Restaurante13")
        
    #Caso Frontera donde monto del consumo es mayor al saldo disponible
    def testConsumirSinSaldo(self):
        BE = BilleteraElectronica(12,"Christopher","Flores",21534848,9123)
        fechaConsumo = datetime(2016,5, 11, 6, 15)
        self.assertRaises(Exception, BE.consumir,150,fechaConsumo,"Restaurante14",7891)
    
    #Caso Frontera donde el monto del consumo es negativo
    def testConsumirNegativo(self):
        BE = BilleteraElectronica(13,"Christopher","Flores",21534848,1234)
        fechaConsumo = datetime(2016,5, 11, 6, 15)
        self.assertRaises(Exception, BE.consumir,-150,fechaConsumo,"Restaurante13",7891)
    
    #Caso Frontera donde el monto de la recarga es CERO    
    def testRecargaCero(self):
        BE = BilleteraElectronica(11,"Christopher","Flores",21534848,8912)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        self.assertRaises(Exception, BE.recargar,0,fechaRecarga,"Restaurante13")
    
    #Caso Frontera donde el monto del consumo es CERO
    def testConsumoCero(self):
        BE = BilleteraElectronica(13,"Christopher","Flores",21534848,1234)
        fechaConsumo = datetime(2016,5, 11, 6, 15)
        self.assertRaises(Exception, BE.consumir,0,fechaConsumo,"Restaurante13",7891)
    
    #Caso Esquina para la recarga minima
    def testMinRecargaSaldo(self):
        BE = BilleteraElectronica(15,"Christopher", "Flores", 21534848, 4321)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        BE.recargar(0.000001, fechaRecarga, "id")
        self.assertEqual(BE.saldo(), 0.000001 , "El saldo no es el correcto")
    
    #Caso Esquina para la recarga con un numero muy grande
    def testMaxRecargaSaldo(self):
        BE = BilleteraElectronica(15,"Christopher", "Flores", 21534848, 4321)
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        numerogrande = sys.float_info.max
        BE.recargar(numerogrande, fechaRecarga, "id")
        self.assertEqual(BE.saldo(), numerogrande , "El saldo no es el correcto")
    
    #Caso Esquina para la recarga de un numero muy grande cuando el saldo ya es muy grande
    def testRecargaConSaldo(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 0321)
        BE.monto= sys.float_info.max # colocamos un saldo al usuario muy grande
        numerogrande = sys.float_info.max
        saldoInfinito = BE.monto+numerogrande
        fechaRecarga = datetime(2016,5, 11, 6, 15)
        BE.recargar(numerogrande, fechaRecarga, "id")
        self.assertEqual(BE.saldo(), (saldoInfinito), 'El saldo es infinito')
        
    #Caso Mali1cia para probar que la Billetera acepta caracteres especiales
    '''def test1ClaseBeEspeciales(self):
        
    En python no reconoce estos caracteres especiales '''
        
    #Caso para un entero empezando en 0 (Malicioso)
    def testEnteroEmpezando0(self):
        BE = BilleteraElectronica(5,"Antonio", "Perez", 12345678, 0321)
        
        '''En python los enteros no pueden empezar en 0, dando un error detectado
    a nivel de lexer'''

                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()