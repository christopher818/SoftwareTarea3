'''
Created on 11 de may. de 2016

@author: Christopher Flores 10-10824
         Isaac Gonzalez 11-10396
         Kervyn Rivero 11-10874
'''

#clase transaccion
class transaccion(object):
    
    def __init__(self,monto, fecha, idTienda):
        self.monto = monto
        self.fecha = fecha
        self.idTienda = idTienda

class BilleteraElectronica():

    def __init__(self, identificador,nombres,apellidos,ci,pin):

        #Inicializamos los datos personales del dueno
        self.identificador = identificador
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci
        self.pin = pin

        #Inicializamos el historial financiero del dueno
        self.creditos = []
        self.debitos = []
        
    def saldo(self):
        recargas = 0
        consumos = 0

        #Cálculo de recargas
        for i in range(len(self.creditos)):
            recargas = recargas + self.creditos[i].monto

        #Cálculo de consumos
        for i in range(len(self.debitos)):
            consumos = consumos + self.debitos[i].monto

        saldo = recargas - consumos

        return saldo
     
    def recargar(self,monto,fecha,idTienda):

        if  monto<= 0:
            raise Exception("El monto a recargar no puede ser nulo ni negativo")

        else:
            self.creditos.append(transaccion(monto,fecha,idTienda))
    
    def consumir(self,monto,fecha,idTienda,pin):

        if self.pin == pin:
            saldo = self.saldo()
            if monto <= 0:
                raise Exception("El monto  del consumo no puede ser negativo, ERROR")
            elif (saldo - monto) < 0:
                raise Exception("Saldo insuficiente")
            else:
                self.debitos.append(transaccion(monto,fecha,idTienda))

        else:
            raise Exception("Pin incorrecto, ERROR")
