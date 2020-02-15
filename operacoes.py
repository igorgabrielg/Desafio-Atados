import random


def gerar_valores(dias: int) -> list:
    """
    Gera uma List Comprehensions dos valor por dia

    :param dias: int
    :return valores: List Comprehensions
    """

    return [random.randint(1, 10) for _ in range(dias)]


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
    dias = int(input("Digite o total de dias: "))
    array_k = gerar_valores(dias)
    print(f"Input: {array_k}")
    print(f"Output: {melhor_situação(array_k)}")


if __name__ == '__main__':
    run()