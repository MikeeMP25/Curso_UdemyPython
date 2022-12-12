import unittest
def doblar(a): return a*2

#Es una estructura de pruebas inicio /proceso /final 
class PruebaTestFixture(unittest.TestCase):

    def setup(self):
        print("preparados el contexto")
        self.numeros=[1,2,3,4,5]
    def test(self):
        print("Realizando una prueba")
        r=[doblar(n)for n in self.numeros]
        self.assertEqual(r,[2,4,6,8,10])
    def tearDown(self):
        print("Destruyendo el contexto")
        return (self.numeros)

if __name__=="__main__":
    unittest.main()