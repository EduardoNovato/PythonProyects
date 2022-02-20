contenedor = []

datosTrabajadore = {
    "Nombre": "",
    "Apellido": "",
    "Sueldo_base": "",
    "AFAP": "",
    "Fecha_de_ingreso": "",
    "Cantidad_de_hijos": ""
}


def ingresarDatos():
    limitador = int(
        input("Ingrese la cantidad de trabajadores que desea agreagar: "))
    for i in range(limitador):
        while True:
            nombre = input("Nombre: ")
            if len(nombre) == 0:
                print("No se pueden ingresar datos vacios, Cabeza e picha")
            else:
                datosTrabajadore["Nombre"] = nombre
                break
        while True:
            apellido = input("Apellido: ")
            if len(apellido) == 0:
                print("No se puden dejar espacios vacios, Cabeza e picha")
            else:
                datosTrabajadore["Apellido"] = apellido
                break
        while True:
            sueldo_base = int(input("Sueldo base: "))
            if sueldo_base < 0:
                print("El numero no puede ser negativo")
            else:
                datosTrabajadore["Sueldo_base"] = sueldo_base
                break
        while True:
            afap = int(input("AFAP: "))
            if afap < 0:
                print("No se pueden dejar camapos vacios")
            else:
                datosTrabajadore["AFAP"] = afap
                break
        while True:
            fecha_ingreso = input("Fecha de ingreso en MM/DD/AA")
            if len(fecha_ingreso) < 6:
                print("Completar fecha de ingreso")
            else:
                datosTrabajadore["Fecha_de_ingreso"] = fecha_ingreso
                break
        while True:
            cant_hijos = int(input("Cantidad de Hijos: "))
            if cant_hijos >= 0:
                datosTrabajadore["Cantidad_de_hijos"] = cant_hijos
                break

        contenedor.append(datosTrabajadore)

    print(contenedor)


ingresarDatos()
