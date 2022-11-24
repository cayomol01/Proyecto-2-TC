# Fuente de consulta: https://en.wikipedia.org/wiki/Church_encoding

cero    = lambda f: lambda x: (x)
uno     = lambda f: lambda x: (f)(x)
dos     = lambda f: lambda x: (f)((f)(x))
tres    = lambda f: lambda x: (f)((f)((f)(x)))
cuatro  = lambda f: lambda x: (f)((f)((f)((f)(x))))
cinco   = lambda f: lambda x: (f)((f)((f)((f)((f)(x)))))
seis    = lambda f: lambda x: (f)((f)((f)((f)((f)((f)(x))))))
siete   = lambda f: lambda x: (f)((f)((f)((f)((f)((f)((f)(x)))))))
ocho    = lambda f: lambda x: (f)((f)((f)((f)((f)((f)((f)((f)(x))))))))
nueve   = lambda f: lambda x: (f)((f)((f)((f)((f)((f)((f)((f)((f)(x)))))))))
diez    = lambda f: lambda x: (f)((f)((f)((f)((f)((f)((f)((f)((f)((f)(x))))))))))

# cero -> uno
sucesor = lambda f: lambda x: lambda y: x((f)(x)(y))

# x + y
suma = lambda x: lambda y: lambda f: lambda g: (x)(f)((y)(f)(g))

# x * y
multiplicacion = lambda x: lambda y: lambda f: lambda g: (x)((y)(f))(g)

# x ^ y
potencia = lambda x: lambda y: lambda f: lambda g: ((y)(x))(f)(g)

alpha = lambda x: suma(x)(uno)
beta = lambda x: multiplicacion(dos)(x)

def print_lambda(x):
    conv = lambda n: n(lambda x: x + 1)(0)

    print(x.replace("conv", ""), '=', eval("conv(" + x + ")"))

print("========Numeros========")
print_lambda("cero")
print_lambda("uno")
print_lambda("dos")
print_lambda("tres")
print_lambda("nueve")

print("========Operaciones========")
print_lambda("sucesor(sucesor(cuatro))")
print_lambda("suma(dos)(tres)")
print_lambda("multiplicacion(seis)(cuatro)")
print_lambda("potencia(cuatro)(tres)")

print("========Alpha y beta raras========")
print_lambda("alpha(uno)(dos)")
print_lambda("beta(tres)(dos)")
