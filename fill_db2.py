﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from db_scheme import *

class MainHandler(webapp.RequestHandler):
	def get(self):
		voivodeship = Voivodeship(name=u'mazowieckie')
		voivodeship.put()
		city = City(voivodeship=voivodeship.key(), name=u'Warszawa', people=1720398)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Radom', people=222496)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Płock', people=126061)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Siedlce', people=77392)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Pruszków', people=56929)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ostrołęka', people=53710)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Legionowo', people=52400)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ciechanów', people=44963)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Otwock', people=44487)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Piaseczno', people=42295)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Żyrardów', people=41220)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Mińsk Mazowiecki', people=38697)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sochaczew', people=37585)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wołomin', people=37117)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Mława', people=29652)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ząbki', people=28644)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Grodzisk Mazowiecki', people=28329)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nowy Dwór Mazowiecki', people=27774)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wyszków', people=27126)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Marki', people=26753)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Piastów', people=22922)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ostrów Mazowiecka', people=22536)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Płońsk', people=22486)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Józefów', people=20132)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kobyłka', people=19723)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Pionki', people=19120)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sulejówek', people=19120)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Pułtusk', people=19078)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Gostynin', people=18888)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sokołów Podlaski', people=18481)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sierpc', people=18368)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kozienice', people=17886)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zielonka', people=17464)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Konstancin-Jeziorna', people=16963)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Przasnysz', people=16796)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Garwolin', people=16773)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Łomianki', people=16637)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Milanówek', people=16126)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Grójec', people=15533)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Węgrów', people=12641)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Brwinów', people=12525)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Błonie', people=12344)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Szydłowiec', people=11873)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Warka', people=11435)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Góra Kalwaria', people=11428)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Karczew', people=10271)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Maków Mazowiecki', people=9755)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Radzymin', people=9561)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ożarów Mazowiecki', people=8848)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Żuromin', people=8810)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zwoleń', people=7958)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Tłuszcz', people=7594)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nasielsk', people=7470)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Białobrzegi', people=7294)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Łosice', people=7176)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Łochów', people=6559)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Mszczonów', people=6247)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Przysucha', people=6154)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Lipsko', people=5702)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Iłża', people=5062)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Łaskarzew', people=4884)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Raciąż', people=4642)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Pilawa', people=4370)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Skaryszew', people=4219)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Żelechów', people=4134)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Serock', people=4094)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Gąbin', people=4053)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Tarczyn', people=3919)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nowe Miasto nad Pilicą', people=3862)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Podkowa Leśna', people=3861)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Halinów', people=3619)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zakroczym', people=3321)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Glinojeck', people=3096)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Myszyniec', people=2950)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kałuszyn', people=2921)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Drobin', people=2898)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Chorzele', people=2793)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wyszogród', people=2767)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Różan', people=2630)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Mogielnica', people=2384)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kosów Lacki', people=2086)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Bieżuń', people=1894)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Brok', people=1892)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Mordy', people=1843)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wyśmierzyce', people=873)
		city.put()

		voivodeship = Voivodeship(name=u'małopolskie')
		voivodeship.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kraków', people=756183)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Tarnów', people=114635)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nowy Sącz', people=84537)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Oświęcim', people=39885)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Chrzanów', people=38869)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Olkusz', people=36869)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nowy Targ', people=33485)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Bochnia', people=29800)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Gorlice', people=28135)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zakopane', people=26709)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Skawina', people=23761)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Andrychów', people=21220)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Trzebinia', people=20175)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wieliczka', people=20075)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wadowice', people=19275)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kęty', people=18958)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Myślenice', people=18173)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Libiąż', people=17405)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Brzesko', people=16844)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Limanowa', people=14918)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Rabka-Zdrój', people=13033)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Brzeszcze', people=11555)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Miechów', people=11497)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Dąbrowa Tarnowska', people=11474)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Krynica-Zdrój', people=10758)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Bukowno', people=10565)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Krzeszowice', people=10016)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Niepołomice', people=9698)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sucha Beskidzka', people=9541)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Chełmek', people=9034)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Stary Sącz', people=9003)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wolbrom', people=8942)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Mszana Dolna', people=7605)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Tuchów', people=6607)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sułkowice', people=6434)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Dobczyce', people=6253)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Proszowice', people=6152)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Szczawnica', people=6022)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Grybów', people=5952)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Maków Podhalański', people=5819)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Piwniczna-Zdrój', people=5805)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Jordanów', people=5234)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Muszyna', people=4946)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Biecz', people=4573)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kalwaria Zebrzydowska', people=4493)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Słomniki', people=4365)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Szczucin', people=4247)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Żabno', people=4237)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zator', people=3718)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Skała', people=3691)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wojnicz', people=3473)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Alwernia', people=3379)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Bobowa', people=3086)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ryglice', people=2797)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nowy Wiśnicz', people=2763)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Radłów', people=2721)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ciężkowice', people=2387)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Czchów', people=2307)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Świątniki Górne', people=2204)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nowe Brzesko', people=1644)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zakliczyn', people=1541)
		city.put()

		voivodeship = Voivodeship(name=u'opolskie')
		voivodeship.put()
		city = City(voivodeship=voivodeship.key(), name=u'Opole', people=125710)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kędzierzyn-Koźle', people=64322)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nysa', people=46046)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Brzeg', people=37346)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kluczbork', people=25141)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Prudnik', people=22514)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Strzelce Opolskie', people=19542)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Krapkowice', people=17602)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Namysłów', people=16254)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Głuchołazy', people=14658)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Głubczyce', people=13286)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zdzieszowice', people=12908)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Olesno', people=9964)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ozimek', people=9682)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Grodków', people=8650)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Praszka', people=7987)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Paczków', people=7911)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zawadzkie', people=7880)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Niemodlin', people=6788)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kietrz', people=6260)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Gogolin', people=6147)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Wołczyn', people=6031)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Lewin Brzeski', people=5840)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Głogówek', people=5731)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Otmuchów', people=5052)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Dobrodzień', people=3957)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Byczyna', people=3656)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kolonowskie', people=3345)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Baborów', people=3062)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Leśnica', people=2840)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Prószków', people=2684)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Gorzów Śląski', people=2626)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Biała', people=2538)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Korfantów', people=1856)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ujazd', people=1670)
		city.put()

		voivodeship = Voivodeship(name=u'podkarpackie')
		voivodeship.put()
		city = City(voivodeship=voivodeship.key(), name=u'Rzeszów', people=178227)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Przemyśl', people=66229)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Stalowa Wola', people=63371)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Mielec', people=60743)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Tarnobrzeg', people=49214)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Krosno', people=47471)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Dębica', people=46611)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Jarosław', people=39702)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sanok', people=39106)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Jasło', people=36932)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Łańcut', people=18057)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Przeworsk', people=15733)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nisko', people=15535)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ropczyce', people=15369)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Leżajsk', people=14126)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Lubaczów', people=12374)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nowa Dęba', people=11237)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ustrzyki Dolne', people=9349)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kolbuszowa', people=9156)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Strzyżów', people=8773)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Brzozów', people=7579)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sędziszów Małopolski', people=7149)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Rudnik nad Sanem', people=6753)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Dynów', people=6105)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Nowa Sarzyna', people=6103)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Boguchwała', people=5943)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Lesko', people=5700)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Jedlicze', people=5608)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Głogów Małopolski', people=5568)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Radymno', people=5440)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Zagórz', people=5007)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Pilzno', people=4622)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sokołów Małopolski', people=3968)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Pruchnik', people=3678)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Rymanów', people=3571)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Tyczyn', people=3474)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kańczuga', people=3178)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Radomyśl Wielki', people=3045)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Oleszyce', people=3036)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Brzostek', people=2640)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Sieniawa', people=2133)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Dukla', people=2128)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Błażowa', people=2119)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Narol', people=2069)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Cieszanów', people=1943)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Iwonicz-Zdrój', people=1763)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Przecław', people=1621)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Ulanów', people=1526)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Kołaczyce', people=1453)
		city.put()
		city = City(voivodeship=voivodeship.key(), name=u'Baranów Sandomierski', people=1423)
		city.put()

		self.response.out.write(template.render('fill_db.html', {}))
	
def main():
	application = webapp.WSGIApplication([(r'.*', MainHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()
