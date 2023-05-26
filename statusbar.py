# -*- coding: utf-8 -*-
"""
A partir de una cantidad total y una parcial, se muestra una barra de porcentaje equivalente.
Fecha:      07/05/2018
Creador:    Gonzalo Déniz Acosta

"""


def statusbar(tam: int, total: int, correctas: int) -> str:
    """ Devuelve una barra donde se refleja el porcentaje
        de operaciones correctas
        Arg:
        	tam - (int) Tamaño que ocupa la barra en la consola
        	total - (int) Total de elementos. El porcentaje se calculará en base a esta constante.
        	correctas - (int) - Numero que es el porcentaje de la barra con respecto al total que se va a mostrar.
        						Si total y correctas tienen el mismo valor, se muestra una barra del 100%.
        						Si correctas = 0, no se muestra ninguna barra.
    """
    assert (isinstance(tam, int) and 0 < tam < 81), 'Tam debe ser > 0 y <= 80'
    assert (isinstance(total, int) and total > 0), 'Total debe ser > 0'
    assert (isinstance(correctas, int) and 0 <= correctas <= total), 'Correctas debe ser >= 0 o <= total'

    corr_rel = int((correctas * tam) / total)
    corr_por = int((correctas * 100) / total)
    return "[{:<{width}}] {por}% SUCESS".format('=' * corr_rel, width=tam, por=corr_por)


def main():
    tam = 50  # Tamaño de la barra
    total = 10  # Total de elementos. El porcentaje se calculará en base a esta constante

    # Muestra 10 barras para enseñar el comportamiento
    for x in range(total + 1):
        txt = statusbar(tam=tam, total=total, correctas=x)
        print('')
        print(txt)

    print(statusbar(tam=tam, total=total, correctas=5))


main()
