def line():
    C_A = float(input ("Ingrese el coeficiente A: "))
    C_B = float(input ("Ingrese el coeficiente B: "))
    C_X1 = float(input ("Ingrese el coeficiente X1: "))
    C_X2 = float(input ("Ingrese el coeficiente X2: "))
    C_Y1 = (C_A * C_X1 + C_B) 
    C_Y2 = (C_A*C_X2+C_B)
    
    import math
    
    p = [C_X1, C_Y1]
    q = [C_X2, C_Y2]
    P1_str = (f"P1 ({C_X1}, {C_Y1})")
    P2_str = (f"P2 ({C_X2}, {C_Y2})")

    #print (C_A)
    #print (C_B)
    #print (C_X1)
    #print (C_X2)
    print (f"El coeficiente A de su ecuación de la recta es: {C_A}")
    print (f"El coeficiente B de su ecuación de la recta es: {C_B}")
    print (f"El coeficiente X1 de su ecuación de la recta es: {C_X1}")
    print (f"El coeficiente X2 de su ecuación de la recta es: {C_X2}")
    print ("")
    print("Para la siguiente ecuación:")
    print (f"\tY = {C_A}X + {C_B}")
    print ("")
    print ("Dados los siguientes puntos:")
    print (f"\t{P1_str}")
    print (f"\t{P2_str}")
    print ("")
    Distancia = (math.dist(p, q))
    print (f"La distancia entre ellos es: {Distancia}")
line()
