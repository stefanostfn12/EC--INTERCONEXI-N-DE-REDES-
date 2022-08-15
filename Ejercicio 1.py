#Variables del ejercicio:
Horas_Trabajadas = 600
codigo = "B987436"
#Código del ejercicio
Nombre = input("Ingrese su nombre: ")
print("Bienvenido", Nombre, "al sitio de consultas")
ID_profesor = input("Ingrese su código: ")
if ID_profesor == codigo:
    print("Horas trabajadas:", Horas_Trabajadas)
    sueldo = Horas_Trabajadas * 30
    AFP=(sueldo*10)/100
    Quinta=(sueldo*8)/100
    Sa = input("Ingresar el tipo de seguro de salud: ")
    if Sa == "ESSALUD":
        Sa_D=(sueldo*11)/100
    elif Sa == "EPS":
        Sa_D=(sueldo*15)/100
    else: 
        print("Ingreso un valor incorrecto")
        breakpoint
    sueldo_b= sueldo - AFP - Quinta - Sa_D
    print(
        """
    --------------------------------------
    - Boleta Idat                          -
    --------------------------------------
    | Ingresos: """, sueldo,"""
    | Descueto del AFP:""",AFP,"""
    | Descuento de su seguro de salud:""",Sa_D,"""
    | Renta de quinta:""",Quinta,"""
    | --------------------------------------
    | Sueldo neto:""",sueldo_b,"""
    --------------------------------------
    """)
else: 
    print("Código equivocado, vuelvalo a intentar ingresar su codigo")
