'''
Created on 11 de may. de 2016

@author: Christopher Flores 10-10824
'''

class BilleteraElectronica:

    def __init__(self, identificador,nombre,apellido,ci,pin):
     self.identificador = identificador
     self.nombre = nombre
     self.apellido = apellido
     self.ci = ci
     self.pin = pin
     self.creditos = []
     self.monto = 0
     self.debitos = []
     
    def saldo(self):
         return self.monto
     
    def recargar(self,monto,fecha,idEstablecimiento):
        if monto <= 0:
            raise Exception("El monto para la recarga no puede ser negativo")
        self.monto = self.monto + monto
        self.creditos.append((monto,fecha,idEstablecimiento))
    
    def consumir(self,monto,fecha,idEstablecimiento,pin):
        if self.pin != pin:
            raise Exception("El pin es incorrecto")
        elif self.monto - monto < 0:
            raise Exception("No hay saldo suficiente para la realizacion del consumo")
        if monto <= 0:
            raise Exception("El monto para la recarga no puede ser negativo")
        self.monto = self.monto - monto
        self.debitos.append((monto,fecha,idEstablecimiento))