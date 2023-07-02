import datetime

def obtener_fecha_hora_actual():
    fecha_hora_actual = datetime.datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
    return fecha_hora_formateada

# Llamar a la función y obtener la fecha y hora actual
fecha_hora = obtener_fecha_hora_actual()

# Imprimir la fecha y hora actual
print(fecha_hora)
