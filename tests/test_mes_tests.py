from dames import Partie


def test_sauvegarder_et_reprendre():
    partie = Partie()

    partie.jouer("d4", "e5")

    partie.sauvegarder("partie_test.json")

    reprise = Partie.charger("partie_test.json")

    assert reprise.trait == "noir"
    assert len(reprise.plateau) == 40
    assert reprise.plateau["e5"].couleur == "blanc"
    assert reprise.plateau["d4"] is None