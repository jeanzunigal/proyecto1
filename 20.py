#Jean Pierre Zuñiga Lara
#2E
invoices = {}
collected = 0
remains = 0
more = ''
while more != 'terminar':
    if more == 'agregar':
        key = input('Introduce el número de la factura: ')
        cost = float(input('Introduce el coste de la factura: '))
        invoices[key] = cost
        remains += cost
    if more == 'pagar':
        key = input('Introduce el número de la factura a pagar: ')
        cost = invoices.pop(key, 0)
        collected += cost
        remains -= cost
    print('Recaudado:', collected)
    print('Pendiente de cobro: ', remains)
    more = input('¿Quieres añadir una nueva factura (agreagr) pagarla (pagar) o terminar (terminar)?:')