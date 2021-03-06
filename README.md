# TOWER DEFENCE OT2021

Pelissä on tarkoitus suojata rahkapihaa hyökkääviltä velhoilta.

### Python versiosta & käyttöjärjestelmistä
Peli testattu windows 10:llä ja cubbli linuxilla. Kummallakin Pythonin versio on ollut +3.8

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

2. Käynnistä sovellus

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

Kattavuusraportit ja muut löytyy _htmlcov_ kansiosta

###

Tiedoston [.pylintrc](./.pylintrc) määrittelemien sääntöjen kattavuus:

```bash
poetry run invoke lint
```
