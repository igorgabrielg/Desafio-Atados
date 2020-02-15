def melhor_situação(valores: list) -> int:
    """
    Determine o maior lucro dado esse array

    :param valores: list
    :return lucro: int
     """

    lucro = 0

    # Caso Nulo
    if max(valores) is min(valores):
        return 0

    # Melhor caso
    if valores.index(min(valores)) == 0:
        return max(valores)-min(valores)

    cache = []

    for valor_atual in valores:
        if not valor_atual in cache:
            cache.append(valor_atual)
            for valor_comparado in valores[valores.index(valor_atual)+1:]:
                if valor_comparado > valor_atual and lucro < valor_comparado - valor_atual:
                    lucro = valor_comparado - valor_atual

    return lucro


def run():
    print(f"Output: {melhor_situação([7,1,5,3,6,4])}")


if __name__ == '__main__':
    run()