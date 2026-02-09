def serieFibonacci(size):
    if size == 1:
        return [0]
    elif size == 2:
        return [0,1]
    else:
        a,b = 0,1
        def numSig(a,b):
            return a+b
        lista = []
        lista.append(a)
        lista.append(b)
        while len(lista) < size:
            lista.append(numSig(a,b))
            a, b = b,numSig(a,b)
        return lista

print(serieFibonacci(1))
print(serieFibonacci(2))
print(serieFibonacci(3))
print(serieFibonacci(10))

            
            
