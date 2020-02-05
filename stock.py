# -*- coding: utf-8 -*-
import sqlite3
import sys
 
con = sqlite3.connect('productos.db')
cursor=con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS productos ('id' INT PRIMARY KEY NOT NULL, 'nombre' TEXT NOT NULL, 'precio' REAL , 'stock' INT, 'categoria' Text)")
cursor.execute("CREATE TABLE IF NOT EXISTS clientes ('id' INT PRIMARY KEY NOT NULL, 'nombre' TEXT NOT NULL, 'apellido' TEXT NOT NULL , 'correo' TEXT NOT NULL, 'direccion' TEXT NOT NULL,'telefono' INT )")

def banner():
    print("==================================================================")
    print("   ______            __             __   _____ __             __  ")
    print("  / ____/___  ____  / /__________  / /  / ___// /_____  _____/ /__")
    print(" / /   / __ \/ __ \/ __/ ___/ __ \/ /   \__ \/ __/ __ \/ ___/ //_/")
    print("/ /___/ /_/ / / / / /_/ /  / /_/ / /   ___/ / /_/ /_/ / /__/ ,<   ")
    print("\____/\____/_/ /_/\__/_/   \____/_/   /____/\__/\____/\___/_/|_|  ")
    print(" v1.0'                                                            ") 
    print("By Solidlucho@gmail.com 2020")
    print("==================================================================")

def menu():
    while True:
        try:
            print("")
            print("MENU")
            print("==================================================================")
            print ("Selecciona una opción")
            print("")
            print ("1  - Ver Listado Stock.          6  - Ver Listado Clientes.")
            print ("2  - Ingresar Producto.          7  - Ingresar Registro de Cliente.") 
            print ("3  - Actualizar Producto.        8  - Actualizar Registro de Clientes.")
            print ("4  - Eliminar Producto.          9  - Eliminar registro de Clientes.")
            print ("5  - Buscar Producto.            10 - Buscar Cliente.")
            print ("")
            print ("0 - Salir.")
            print("==================================================================")
            print("")
            option=int(input("Ingrese una Opcion: "))
            if option == 1:
                listado()
            elif option ==2:
                insertar()
            elif option ==3:
                Actualizar()
            elif option ==4:
                Eliminar()
            elif option ==5:
                buscar()
            elif option ==6:
                listado2()
            elif option ==7:
                insertar2()
            elif option ==8:
                Actualizar2()
            elif option ==9:
                Eliminar2()
            elif option ==10:
                buscar2()
            elif option ==0:
                con.close()
                break
        except:
            print("ingresó un caracter o número no valido.")

#FUNCIONES PRODUCTOS

def listado():
    print("")
    print("LISTA DE PRODUCTOS")
    print("==========================================================================")
    cursor.execute('SELECT * FROM productos ORDER BY id') 
    rows = cursor.fetchall() 
    formatted_row = '{:^4} {:^10} {:^20} {:^20} {:^20} '
    print("")
    print(formatted_row.format("ID", "NOMBRE", "PRECIO", "STOCK", "CATEGORIA"))
    for Row in rows:
        print("-----------------------------------------------------------------------------")
        print(formatted_row.format(*Row))
    print("")
    print("Total de Registros encontrados: ")
    print(len(rows))
    print("")

def insertar():
    while True:
        try:
            idproducto=int(input("Ingrese número de Registro: "))
            break  
        except:
            print("ingresó un caracter no valido.") 
             
    nombre2=input("Ingrese Nombre del Producto: ")

    while True:
        try:
            precio2=float(input("Ingrese el Precio: "))
            break
        except:
                print("ingresó un caracter no valido.")
        
    while True:
        try:
            stock2=int(input("Ingrese la cantidad: "))
            break
        except:
            print("ingresó un caracter no valido.")

    categoria2=input("Ingrese que categoria pertenece: ")
    
    valores=(idproducto, nombre2, precio2, stock2, categoria2)
    cursor.execute("INSERT INTO productos VALUES (?,?,?,?,?)", valores)
    con.commit() 
    print("")
    print("Datos ingresados con exito.")
    print("")
    
def Actualizar():
    print("")
    print("Atención: Verifique antes si el Id está registrado")
    print("")
    cursor.execute('SELECT id FROM productos') 
    
    try:
        idproducto=int(input("Ingrese número de Registro: "))  
    except:
        print("")
        print("ingresó un caracter no valido.")
        print("")
        return
     
             
    nombre2=input("Ingrese Nombre del Producto: ")

    while True:
        try:
            precio2=float(input("Ingrese el Precio: "))
            break
        except:
                print("ingresó un caracter no valido.")
        
    while True:
        try:
            stock2=int(input("Ingrese la cantidad: "))
            break
        except:
            print("ingresó un caracter no valido.")

    categoria2=input("Ingrese que categoria pertenece: ")
    cursor.execute("UPDATE productos SET nombre = ?, precio = ?, stock = ?, categoria = ? WHERE id = ?", [nombre2,precio2,stock2,categoria2,idproducto])
    con.commit()
    print("Datos actualizados.")

def buscar():
    busqueda=input("Ingrese el NOMBRE del producto a buscar: ")
    cursor.execute("select * from productos where nombre like ?", ('%'+busqueda+'%',) )
    rows = cursor.fetchall()
    formatted_row = '{:^4} {:^10} {:^20} {:^20} {:^20} '
    print("")
    print(formatted_row.format("ID", "NOMBRE", "PRECIO", "STOCK", "CATEGORIA"))
    for Row in rows:
        print("-----------------------------------------------------------------------------")
        print(formatted_row.format(*Row))
    print("")
    print("Total de Registros encontrados: ")
    print(len(rows))
    print("")

def Eliminar():
    cursor.execute('SELECT id FROM productos') 
    try:
        idproducto=input("Ingrese número de Registro a Eliminar: ")
    except:
        print("")
        print("ingresó un caracter no valido.")
        print("")
        return
    cursor.execute("DELETE FROM productos WHERE id = ?", [idproducto])
    con.commit()
    print("")
    print("Registro Eliminado.")
    print("")
    
#-------------------------------------------------------------------------------------#
#FUNCIONES CLIENTES

def listado2():
    print("")
    print("LISTA DE CLIENTES")
    print("==========================================================================================")
    cursor.execute('SELECT * FROM CLIENTES ORDER BY id') 
    rows = cursor.fetchall() 
    formatted_row = '{:^4} {:^10} {:^20} {:^20} {:^20} {:^10} '
    print("")
    print(formatted_row.format("ID", "NOMBRE", "APELLIDO", "CORREO", "DIRECCIÓN", "TELEFONO"))
    for Row in rows:
        print("------------------------------------------------------------------------------------------")
        print(formatted_row.format(*Row))
    print("")
    print("Total de Registros encontrados: ")
    print(len(rows))
    print("")

def insertar2():
    while True:
        try:
            idcliente=int(input("Ingrese número de Registro: "))
            break  
        except:
            print("ingresó un caracter no valido.") 
    
    nombre2=input("Ingrese Nombre del Cliente: ")
    apellido2=input("Ingrese Apellido del Cliente: ")
    correo2=input("Ingrese el correo electronico: ")
    direccion2=input("Ingrese la dirección del cliente: ")
    telefono2=input("Ingrese el Telefono del cliente: ")
    valores=(idcliente,nombre2,apellido2,correo2,direccion2,telefono2)
    cursor.execute("INSERT INTO clientes VALUES (?,?,?,?,?,?)", valores)
    con.commit()
    print("")
    print("Datos ingresados con exito.")
    print("")

def Actualizar2():
    print("")
    print("Atención: Verifique antes si el Id está registrado")
    print("")
    cursor.execute('SELECT id FROM clientes') 
    
    try:
        idcliente=int(input("Ingrese número de Registro: "))
 
    except:
        print("")
        print("ingresó un caracter no valido.")
        print("")
        return
    

    nombre2=input("Ingrese Nombre del Cliente: ")
    apellido2=input("Ingrese Apellido del Cliente: ")
    correo2=input("Ingrese el correo electronico: ")
    direccion2=input("Ingrese la dirección del cliente: ")
    telefono2=input("Ingrese el Telefono del cliente: ")
    cursor.execute("UPDATE clientes SET nombre = ?, apellido = ?, correo = ?, direccion = ?, telefono = ? WHERE id = ?", [nombre2,apellido2,correo2,direccion2,telefono2,idcliente])
    con.commit()
    print("")
    print("Datos actualizados.")
    print("")

def buscar2():
    busqueda=input("Ingrese el NOMBRE del Cliente a buscar: ")
    cursor.execute("select * from clientes where nombre like ?", ('%'+busqueda+'%',) )
    print("")
    print("RESULTADO DE BUSQUEDA:")
    print("==================================================================")
    rows = cursor.fetchall()
    formatted_row = '{:^4} {:^10} {:^20} {:^20} {:^20} {:^10} '
    print("")
    print(formatted_row.format("ID", "NOMBRE", "APELLIDO", "CORREO", "DIRECCIÓN", "TELEFONO"))
    for Row in rows:
        print("------------------------------------------------------------------------------------------")
        print(formatted_row.format(*Row))
    print("")
    print("Total de Registros encontrados: ")
    print(len(rows))
    print("")

def Eliminar2():
    cursor.execute('SELECT id FROM clientes') 
    try:
        idcliente=int(input("Ingrese NÚMERO de Registro a Eliminar: "))
    except:
        print("")
        print("ingresó un caracter no valido.")
        print("")
        return
    
    cursor.execute("DELETE FROM clientes WHERE id = ?", [idcliente])
    con.commit()
    print("")
    print("Registro Eliminado.")
    print("")


#-------------------------------------------------------------------------------------#
 
         
if __name__ == "__main__":
    banner()
    menu()
    