# Jälkiruokareseptit

## Sovelluksen toiminnot 

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään reseptejä ja muokkaamaan ja poistamaan niitä.
* Käyttäjä pystyy lisäämään kuvia reseptiin.
* Reseptissä lukee tarvittavat ainekset ja valmistusohje. 
* Käyttäjä näkee sovellukseen lisätyt reseptit. 
* Käyttäjä pystyy etsimään reseptejä hakusanalla.
* Käyttäjäsivu näyttää, montako reseptiä käyttäjä on lisännyt ja listan käyttäjän lisäämistä resepteistä.
* Käyttäjä pystyy valitsemaan reseptille luokittelun (esim. maku ja vaikeustaso). 
* Käyttäjä pystyy antamaan reseptille kommentin. 

## Sovelluksen asennus 
Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```

