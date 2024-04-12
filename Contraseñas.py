import random
def nueva_contraseña(longitud):
    simbolos = "%+-/*!&#?=@abcdefghijklnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    contraseña = "".join(random.choice(simbolos) for i in range(longitud))
    print("Tu contraseña es: ", contraseña)
    
longitud_contra = int(input("Ingrese la longitud de la contraseña: "))
contraseña_resultante = nueva_contraseña(longitud_contra)
