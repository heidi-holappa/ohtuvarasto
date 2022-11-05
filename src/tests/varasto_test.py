import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_asettaa_tilavuudeksi_nolla(self):
        self.uusi_varasto = Varasto(-10)
        self.assertAlmostEqual(self.uusi_varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_asettaa_alkusaldoksi_nolla(self):
        self.uusi_varasto = Varasto(10, -3)
        self.assertAlmostEqual(self.uusi_varasto.saldo, 0)

    def test_negatiivisen_maaran_lisays_ei_kasvata_saldoa(self):
        self.varasto.lisaa_varastoon(2)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_saldo_voi_olla_enimmillaan_tilavuuden_verran(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivisen_maaran_ottaminen_palauttaa_nolla(self):
        result = self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(result, 0)

    def test_saldoa_suuremman_maaran_ottaminen_palauttaa_koko_saldon(self):
        self.varasto.lisaa_varastoon(8)
        result = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(result, 8)

    def test_saldoa_suuremman_maaran_ottaminen_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_on_halutussa_muodossa(self):
        syote = self.varasto
        tulisi_olla = "saldo = 0.0, vielä tilaa 10.0"
        self.assertEqual(str(syote), tulisi_olla)
