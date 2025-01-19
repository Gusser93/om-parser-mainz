#!/usr/bin/python3.12
import re
from print_xml import print_xml
# Ausgabe 1 Bingen = Hauptspeise 1
# Ausgabe 2 Bingen = Hauptspeise 2
# Beilagen einfach = Beilage einfach
# Beilagen frittiert = Beilage frittiert
# Beilagensalat = Beilagensalat
# Y_Eintopf = Eintopf
# Würstchen Schwein / Rind = Wurst
RENUMS = re.compile(r" \([^\)]*\)")

URL = "https://www.studierendenwerk-mainz.de/speiseplan/Speiseplan.xml"
VERSION = "1.0.0"
VERBRAUCHSORT = "360"
IGNORE = ["Ausgabe intern ZM", "Ausgabe intern ZM vegan"]

CATEGORY = {
	"Ausgabe 1 Bingen": "Hauptspeise",
	"Ausgabe 2 Bingen": "Hauptspeise",
	"Beilagen einfach": "Beilage",
	"Beilagen frittiert": "Beilage",
	"Beilagensalat": "Salat",
	"Y_Eintopf": "Eintopf",
	"Würstchen Schwein / Rind": "Wurst",
}

print_xml(VERBRAUCHSORT, CATEGORY, URL, VERSION, RENUMS, IGNORE)