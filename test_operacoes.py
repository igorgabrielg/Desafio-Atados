from operacoes import gerar_valores, melhor_situação
import unittest


class MyTestCase(unittest.TestCase):
    def test_gerar_valores(self):
        valores = (10, 7, 3)
        for valor in valores:
            self.assertEqual(len(gerar_valores(valor)), valor)
            self.assertIs(type(gerar_valores(valor)), list)

    def test_melhor_situação(self):
        testes = (
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([1, 1, 1, 1], 0)
        )

        for teste, expectativa in testes:
            self.assertEqual(melhor_situação(teste), expectativa)
            self.assertIs(type(melhor_situação(teste)), int)


if __name__ == '__main__':
    unittest.main()
