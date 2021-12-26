# TOWER DEFENCE OT2021

Pelissä on tarkoitus suojata rahkapihaa hyökkääviltä velhoilta.

## Harjoitustyö

Harjoitustyön aiheena on tower defence -tyyppinen peli.

- [Tuntikirjanpito](./td/dokumentaatio/tuntikirjanpito.md)
- [Käyttöliittymäluonnos](./td/dokumentaatio/kayttoliittymaluonnos.png)
- [Alustava vaatimusmäärittely](./td/dokumentaatio/vaatimusmaarittely.md)
- [Käyttöohje](./td/dokumentaatio/kayttoohje.md)
- [Arkkitehtuuri](./td/dokumentaatio/arkkitehtuurikuvaus.md)

### Doku-mentaatio

1. Asenna riippuvuudet

```bash
poetry install
```

3. Käynnistä sovellus

```bash
poetry run invoke start
```

### Testaus

Testit

```bash
poetry run invoke test
```

Testikattavuus

```bash
poetry run invoke coverage-report
```

-> _htmlcov_

###

Tiedoston [.pylintrc](./.pylintrc) määrittelemien sääntöjen kattavuus:

```bash
poetry run invoke lint
```
