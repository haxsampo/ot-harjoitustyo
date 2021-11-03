import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_uusi_kassa_alustus(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_liian_vahan_rahaa_kateinen(self):
        alussa_rahaa = self.kassa.kassassa_rahaa

        palautus = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(palautus, 200)
        self.assertEqual(alussa_rahaa, self.kassa.kassassa_rahaa)

        palautus2 = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(palautus2, 200)
        self.assertEqual(alussa_rahaa, self.kassa.kassassa_rahaa)

        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisostot_onnistuu(self):
        alussa_rahaa = self.kassa.kassassa_rahaa

        palautus = self.kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(palautus, 10)
        self.assertEqual(alussa_rahaa+240, self.kassa.kassassa_rahaa)

        palautus2 = self.kassa.syo_maukkaasti_kateisella(450)
        self.assertEqual(palautus2, 50)
        self.assertEqual(alussa_rahaa+400+240, self.kassa.kassassa_rahaa)

        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_korttiostot_toimii(self):
        alussa_rahaa = self.kassa.kassassa_rahaa
        
        palautusEdullinen = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(True, palautusEdullinen)
        self.assertEqual("saldo: 7.6", str(self.maksukortti))
        
        palautusMaukas = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(True, palautusMaukas)
        self.assertEqual("saldo: 3.6", str(self.maksukortti))

        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(alussa_rahaa, self.kassa.kassassa_rahaa)

    def test_korttiostot_liian_vahan_rahaa_kortilla(self):
        self.maksukortti = Maksukortti(10)

        palautusEdullinen = self.kassa.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(False, palautusEdullinen)
        self.assertEqual("saldo: 0.1", str(self.maksukortti))

        palautusMaukas = self.kassa.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(False, palautusMaukas)
        self.assertEqual("saldo: 0.1", str(self.maksukortti))

        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortin_lataus(self):
        self.assertEqual("saldo: 10.0", str(self.maksukortti))
        self.kassa.lataa_rahaa_kortille(self.maksukortti, 3)
        self.assertEqual("saldo: 10.03", str(self.maksukortti))
        self.kassa.lataa_rahaa_kortille(self.maksukortti, -3)
        self.assertEqual("saldo: 10.03", str(self.maksukortti))





