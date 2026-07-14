prendas={
'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon',
True],
'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester',
True],
'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon',
True],
'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon',
False]} 
#precio, unidades
bodega={
'S001': [7990, 12],
'S002': [19990, 0],
'S003': [29990, 3],
'S004': [24990, 6],
'S005': [17990, 8],
'S006': [14990, 2]}



def leer_opcion():
    while True:
        try:
            print('''
            ========== MENÚ PRINCIPAL ==========
            1. Unidades por categoría
            2. Búsqueda de prendas por rango de precio
            3. Actualizar precio de prenda
            4. Agregar prenda
            5. Eliminar prenda
            6. Salir
            =====================================''')      
            opcion=int(input("por favor ingrese una opcion: "))
            opcion=int(opcion)
            if opcion<1 or opcion>6:
                print("Debe seleccionar una opción válida")
                return 0
            return opcion
        except ValueError:
            print("Debe seleccionar una opción válida")


def unidades_categoria(categoria):
    total=0
    for codigo in prendas:
        if prendas[codigo][1].lower()== categoria.lower():
            total+=bodega[codigo][1]
    print(f"La cantidad de unidades desponibles es: ",total)       

def busqueda_precio(precio_min,precio_max):
    prendas_en_rango=[]
    for codigo in bodega:
        precio=bodega[codigo][0]
        unidades=bodega[codigo][1]
        if precio>=precio_min and precio<=precio_max and unidades>0:
            nombre=prendas[codigo][0]
            prendas_en_rango.append(nombre + "-" + codigo)
    prendas_en_rango.sort()
    if len(prendas_en_rango)==0:
        print("No hay prendas en ese rango de precios")
    else:
        for elemento in prendas_en_rango:
            print (elemento)
     
def buscar_codigo(codigo):
    codigo=codigo.lower()
    for cod in prendas:
        if cod.lower()== codigo:
            return True
        return False
      
def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        for cod in bodega:
            if cod.lower()==codigo.lower():
                bodega[cod][0]=nuevo_precio
                return True
            return False
def agregar_prenda(codigo, nombre,categoría, talla, color, material, unisex, precio, unidades):
    if buscar_codigo(codigo):
        return False
    else:
        prendas[codigo]=[nombre,categoría, talla, color, material, unisex]
        bodega[codigo]=[precio,unidades]
        return True
def eliminar_prenda(codigo):
    if buscar_codigo(codigo):
        codigo_existe=""
        for cod in prendas:
            if cod.lower()==codigo.lower():
                codigo_existe=cod
            del prendas[codigo_existe]
            del bodega[codigo_existe] 
            return True       
    return False

def validar_texto(texto):
    return texto.strip() != ""
def validar_codigo(codigo):
    return codigo.strip() != ""
def validar_precio(precio):
    return precio>0
def validar_unidades(unidades):
    return unidades>0

while True:
    opcion=leer_opcion()
    if opcion==1:
        categoria=input("Ingrese su categoría a consultar: ")
        unidades_categoria(categoria)
    elif opcion==2:
        while True:
            try:
                precio_min=int(input("Ingrese su precio minimo: "))
                precio_max=int(input("Ingrese su precio maximo: "))
                if precio_min>=0 and precio_max>=0 and precio_min<=precio_max:
                    break
                else:
                    print("Debe ingresar valores enteros")
            except ValueError:
                print ("Debe ingresar valores enteros")
        busqueda_precio(precio_min,precio_max) 

    elif opcion==3:
        repetir_opc="s"
        while repetir_opc.lower()=="s":
            codigo=input ("ingrese el codigo: ")
            try:
                nuevo_precio=input("ingrese nuevo precio: ")
                if actualizar_precio(codigo,nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("El codigo no existe")    
            except ValueError:
                print("Datos invalidos")
            repetir_opc=input("desea actualizar otro precio? s/n: ") 
    elif opcion==4:
        codigo=input("Ingrese codigo de la prenda: ")
        nombre=input("ingrese nombre de la prenda: ")
        categoria=input("ingrese categoria: ") 
        talla=input("ingrese talla: ")        
        color=input("Ingrese color: ")
        material=input("ingrese material: ")
        unisex=input("Es unisex? s/n: ").lower()
        try:
            precio=int(input("Ingrese precio: "))
            unidades=int(input("Ingrese unidades: "))
            if not validar_codigo(codigo):
                print("codigo invalido")
            elif not validar_texto(nombre):
                print("nombre invalido") 
            elif not validar_texto(categoria):
                print("categoria invalida")
            elif not validar_texto(talla):
                print("talla invalida")
            elif not validar_texto  (color):
                print("color invalido")
            elif not validar_texto(material):
                print("material invalido")
            elif not validar_precio(precio):
                print("precio invalido")
            elif not validar_unidades(unidades):
                print("unidades invalidas")
            else:
                if agregar_prenda(codigo, nombre,categoria, talla, color, material, unisex, precio, unidades):
                    print("Prenda agregada con exito")    
        except ValueError:
            print("Precio o unidades invalidas")
    elif opcion==5:
        codigo=input("Ingrese codigo que desea eliminar: ") 
        if eliminar_prenda(codigo):
            print("prenda eliminada")
        else:
            print("El codigo no existe")           
    elif opcion==6:
        print("Finalizando el programa...")
        break










