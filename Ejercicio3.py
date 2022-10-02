peso = float( input ("Introduzca su peso en kilogramos\n"))
altura = float (input ("Introduzca su estatura en metros\n"))

print ('\nEl peso es de {0} KG y la estatura es de {1} metros'.format(peso, altura))
print ('La altura es de {1} metros y el peso es de {0} KG\n'.format(peso, altura))
#Otra forma
print ('El peso es de {} KG y la estatura es de {} metros'.format(peso, altura))
print ('La altura es de {} metros y el peso es de {} KG\n'.format(altura, peso))
#Otra manera
print (f'El peso es de {peso} KG y la estatura es de {altura} metros')
print (f'La altura es de {altura} metros y el peso es de {peso} KG')
