from operacoes import gerar_valores, melhor_situação
import unittest


class MyTestCase(unittest.TestCase):
    def test_gerar_valores(self):
        valores = (10, 7, 3)
        for valor in valores:
            self.assertEqual(len(gerar_valores(valor)), valor)
            self.assertIs(type(gerar_valores(valor)), list)


if __name__ == '__main__':
    unittest.main()
