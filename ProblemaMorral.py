

def morral(tamano_morral, pesos, valores, n):
    
    if n == 0 or tamano_morral == 0:
        return 0
    
    if pesos[n - 1] > tamano_morral:
        print(f'1. Tamano morral {tamano_morral}')
        return morral(tamano_morral, pesos, valores, n - 1)

    print(f'2. Tamano morral {tamano_morral}')
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1), 
    morral(tamano_morral, pesos, valores, n - 1))
    


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 40

    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)