from cliente import Cliente
from producto import Producto
from venta_detalle import VentaDetalle
from venta import Venta
# CRUD CLIENTE
data_clientes:list=[{"numero_documento":"10472596972",
                     "razon_social":"Noe Wilber Tipo Mamani",
                     "direccion":"Jr. Tupac yupanqui 590",
                     "telefono":"997120432"},
                     {"numero_documento":"47259697",
                     "razon_social":"Noe Wilber",
                     "direccion":"Jr. Tupac yupanqui 590",
                     "telefono":"997120432"},
                     {"numero_documento":"78524122",
                     "razon_social":"JUan Carlos tumpi",
                     "direccion":"Jr. Tupac yupanqui 790",
                     "telefono":"997120440"}]

clientes:Cliente = []
def cargar_datos_clientes():
    for data in data_clientes:
        clientes.append(Cliente(data["numero_documento"],
                                data["razon_social"],
                                data["direccion"],
                                data["telefono"]))
    return clientes

def insertar_cliente():
    numero_documento:str=input("Ingrese el numero de docuemto del cliente: ")
    razon_social:str=input("Ingrese la razon social del cliente: ")
    direccion:str=input("Ingrese la direccion del cliente: ")
    telefono:str=input("Ingrese telefono del cliente: ")
    clientes.append(Cliente(numero_documento,razon_social,direccion,telefono))
    return clientes

def listar_clientes():
    for cliente in clientes:
        print(cliente.convertir_a_texto())
    return clientes

def buscar_cliente():
    numero_documento:str=input("Ingrese el numero de documento para buscar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento==numero_documento:
            print(cliente.convertir_a_texto())
            return cliente

def editar_cliente():
    listar_clientes()
    numero_documento:str=input("Ingrese el numero de documento para editar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento==numero_documento:
            print(cliente.convertir_a_texto())
            cliente.razon_social=input("Ingrese nueva razon social del cliente: ")
            cliente.direccion=input("Ingrese nueva direcion del cliente: ")
            cliente.telefono=input("Ingrese nuevo telefono del cliente: ")
    listar_clientes()
    return clientes

def eliminar_cliente():
    listar_clientes()
    numero_documento:str=input("Ingrese el numero de documento del cliente para eliminar: ")
    for indice, cliente in enumerate(clientes):
        if cliente.numero_documento==numero_documento:
            clientes.pop(indice)
    listar_clientes()
    return clientes

# CRUD PRODUCTO

data_productos:list=[{"codigo":"001",
                     "nombre":"salteña",
                     "precio":2.00},
                     {"codigo":"002",
                     "nombre":"agua",
                     "precio":1.50},
                     {"codigo":"003",
                     "nombre":"gaseosa de 2 litros",
                     "precio":8.00}]

productos:Producto = []
def cargar_datos_productos():
    for data in data_productos:
        productos.append(Producto(data["codigo"],
                                data["nombre"],
                                data["precio"]))
    return productos

def insertar_producto():
    codigo:str=input("Ingrese codigo del producto: ")
    nombre:str=input("Ingrese nombre del producto: ")
    precio:str=input("Ingrese precio del producto: ")
    productos.append(Producto(codigo,nombre,precio))
    return productos

def listar_productos():
    for producto in productos:
        print(producto.convertir_a_texto())
    return productos

def buscar_producto():
    codigo:str=input("Ingrese codigo del producto para buscar producto: ")
    for producto in productos:
        if producto.codigo==codigo:
            print(producto.convertir_a_texto())
            return producto

def editar_producto():
    listar_productos()
    codigo:str=input("Ingrese codigo del producto para editar producto: ")
    for producto in productos:
        if producto.codigo==codigo:
            print(producto.convertir_a_texto())
            producto.nombre=input("Ingrese nuevo nombre del producto: ")
            producto.precio=float(input("Ingrese nuevo precio del producto: "))
           
    listar_productos()
    return productos

def eliminar_producto():
    listar_productos()
    codigo:str=input("Ingrese codigo del producto para eliminar producto: ")
    for indice, producto in enumerate(productos):
        if producto.codigo==codigo:
            productos.pop(indice)
    listar_productos()
    return productos

# CRUD VENTA
ventas:Venta=[]
venta_detalles:VentaDetalle=[]
def agregar_productos():
    producto:Producto=buscar_producto()
    cantidad:float=float(input("Ingrese la cantidad del producto: "))
    venta_detalles.append(VentaDetalle(len(venta_detalles)+1,
                                       producto.codigo,
                                       producto.nombre,
                                       cantidad,
                                       producto.precio))
    return venta_detalles


def insertar_venta():
    cliente:Cliente=buscar_cliente()
    continuar_venta:bool=True
    while continuar_venta:
        opcion:str=input("1: para agregar producto, 2 para guargar venta: ")
        match opcion:
            case "1":
                agregar_productos()
            case "2":
                continuar_venta=False
    total:float=0
    for venta_detalle in venta_detalles:
        total=total+venta_detalle.total
    ventas.append(Venta(len(ventas)+1,cliente,venta_detalles,total))
    return ventas
def listar_ventas():
    for venta in ventas:
        print(venta.convertir_a_texto())
    return ventas
        
def buscar_venta():
    numero:int=int(input("Ingrese el numero de la venta para bucar: "))
    for venta in ventas:
        if venta.numero==numero:
            print(venta.convertir_a_texto())
            print("================================")
            for venta_detalle in venta.detalle:
                print(venta_detalle.convertir_a_texto())
            return venta 




def menu_texto():
    print("===============MENU===========")
    print("=========CRUD CLIENTE========")
    print("1: para Insertar Cliente")
    print("2: para listar Cliente")
    print("3: para Buscar Cliente")
    print("4: para Editar Cliente")
    print("5: para Elimiar Cliente")
    print("=========CRUD PRODUCTO========")
    print("6: para Insertar Producto")
    print("7: para listar Producto")
    print("8: para Buscar Producto")
    print("9: para Editar Producto")
    print("10: para Elimiar Producto")

    print("=========CRUD VENTA========")
    print("11: para Insertar Venta")
    print("12: para Listar Venta")
    print("13: para buscar Venta")
    
    print("30: para terminar")

def menu():
    continuar:bool=True
    while continuar:
        menu_texto()
        opcion:str=input("Ingrese la opcion: ")
        match opcion:
            case "1":
                insertar_cliente()
            case "2":
                listar_clientes()
            case "3":
                buscar_cliente() 
            case "4":
                editar_cliente()   
            case "5":
                eliminar_cliente() 
            
            case "6":
                insertar_producto()
            case "7":
                listar_productos()
            case "8":
                buscar_producto() 
            case "9":
                editar_producto()   
            case "10":
                eliminar_producto()
            case "11":
                insertar_venta()
            case "12":
                listar_ventas()
            case "13":
                buscar_venta() 
            case "30":
                continuar=False    


def main():
    cargar_datos_clientes()
    cargar_datos_productos()
    menu()
    print("iniciando programna")
    return True
if __name__=='__main__':
    main()