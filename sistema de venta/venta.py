from cliente import Cliente
from venta_detalle import VentaDetalle
class Venta:
    #crea la clase venta
    def __init__(self, numero, cliente:Cliente, detalle:VentaDetalle=[], total=0) -> None:
        self.serie='F005'
        self.numero=numero
        self.cliente:Cliente=cliente
        self.detalle:VentaDetalle=detalle
        self.base_imponible=total/1.18
        self.igv=total-(total/1.18)
        self.total=total
        pass
    def contertir_a_texto(self):
        return "|{}|{}|{}|{}|{}|{}|".format(self.serie,self.numero,self.cliente.razon_social,self.base_imponible,self.igv,self.total)