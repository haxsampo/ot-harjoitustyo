# Arkkitehtuurikuvaus

## Rakenne
Ohjelman kansiorakenne ja arkkitehtuuri toimii suurinpiirtein seuraavalla tavalla

![arkkitehtuuri](./td/dokumentaatio/arkkitehtuuri.png)

ui sisältää käyttöliittymään liittyviä elementtejä; services sisältää sovelluslogiikkaa; repositories sisältää sovelluksen tietojen tallentamiseen liittyvää koodia; entities sisältää sovelluksen entiteeteiksi miellettäviä luokkia, jotka eivät ole välttämättä visuaalisia; sprites on pygame.sprite:n periviä entiteettejä; pf sisältää reitinetsintään liittyvän koodin ja luokat

## Käyttöliittymä
Sisältää kaksi erillistä näkymää:

- Päävalikon, jossa pelaaja voi aloittaa uuden pelin, näkee aikaisemmat pisteet ja voi syöttää nimen uutta pelikertaa varetn
- Pelinäkymä

Nämä ovat toteutettu omina luokkinaan menu.py ja level.py. Ulkoinen kirjasto [pygame-text-input](https://github.com/Nearoo/pygame-text-input) hoitaa pelaajan kirjoittaman tekstin vastaanottamisen ja syötteen validoimisen. 

## Sovelluslogiikka
Gameloop määrittää mitä 'skeneä' näytetään ja päivitetään kullakin hetkellä. Kukin skene sisältää omat käyttöliittymäelementtinsä, jotka syötetään rendererille.
Gameloopissa esiin nousevat pelaajan syötteet passataan UserInput luokalle, joka käsittelee ne, palauttaen skenelle relevantin informaation.

## Tietojen pysyväistallennus
Repositories kansion ScoreRepository huolehtii tietojen tallentamisesta. Tieto tallennetaan .csv-tiedostoon. Luokka pyrkii noudattelemaan repository suunnittelumallia.

### Tiedostot
Sovelluksen juureen sijoitettu konfiguraatiotiedosto .env määrittelee tallennustiedoston nimen.
CSV-tiedoston tallennusformaatti on:

```
nimi;pisteet
nimi;pisteet
```

## Päätoiminnallisuudet

Kuvataan toimintalogiikkaa hieman sekvenssikaaviolla:

![sekvenssi](https://github.com/haxsampo/ot-harjoitustyo/blob/master/td/dokumentaatio/arkkitehtuuri.png)


## Ohjelman rakenteeseen jääneet heikkoudet
- Menu ja level olisi luultavasti abstraktoitavissa skeneksi, jolla on omat renderöitävät objektinsa ja kumpikin passaisi user_inputille tapahtuvat eventit.
- index tulisi purkaa 
- pelin päätyttyä olisi ideaalia pystyä palaamaan menuun tai aloittamaan uusi peli
