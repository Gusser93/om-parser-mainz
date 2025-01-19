#!/usr/bin/python3.12
import re
from print_xml import print_xml

# Anhänger Döner Falateller = Falafelteller
# Anhänger Dönerteller = Dönerteller
# Anhänger Döner+co Basis = Döner+co
# Anhänger Döner+co veggi = Döner+co vegan/vegetarisch
RENUMS = re.compile(r" \([^\)]*\)")

URL = "https://www.studierendenwerk-mainz.de/speiseplan/Speiseplan.xml"
VERSION = "1.0.0"
VERBRAUCHSORT = "447"
IGNORE = ["Ausgabe intern ZM", "Ausgabe intern ZM vegan"]

CATEGORY = {
	"Anhänger Döner Falateller": "MiniMensa Döner+Co",
	"Anhänger Dönerteller": "MiniMensa Döner+Co",
	"Anhänger Döner+co Basis": "MiniMensa Döner+Co",
	"Anhänger Döner+co veggi": "MiniMensa Döner+Co",
}

print_xml(VERBRAUCHSORT, CATEGORY, URL, VERSION, RENUMS, IGNORE)