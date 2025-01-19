#!/usr/bin/python3.12

import re
from print_xml import print_xml

# Ausgabe 1 Mensaria = Hauptspeise 1
# Ausgabe 2 Mensaria = Hauptspeise 2
# 32.318 && Pommes frites = kleine Pommes
# 32.319 && Pommes frites = große Pommes
# Y_Eintopf = Eintopf
# Z_Salatbuffet = Salatbuffet pro Kilogramm


RENUMS = re.compile(r" \([^\)]*\)")

URL = "https://www.studierendenwerk-mainz.de/speiseplan/Speiseplan.xml"
VERSION = "1.0.0"
VERBRAUCHSORT = "312"
IGNORE = ["Ausgabe intern ZM", "Ausgabe intern ZM vegan"]

CATEGORY = {
	"Ausgabe 1 Mensaria": "Hauptspeise",
	"Ausgabe 2 Mensaria": "Hauptspeise",
	"Pommes frites": "Pommes",
	"Y_Eintopf": "Eintopf",
	"Z_Salatbuffet": "Salat",
}

print_xml(VERBRAUCHSORT, CATEGORY, URL, VERSION, RENUMS, IGNORE)