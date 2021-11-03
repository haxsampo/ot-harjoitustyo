import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alussa_oikein(self):
        print(str(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "saldo: 0.1",)
    
    def test_lataus(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2",)

    def test_rahan_ottaminen(self):
        eka = self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05",)
        toka = self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05",)
        self.assertEqual(eka, True)
        self.assertEqual(toka,False)