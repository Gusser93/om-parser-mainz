#!/usr/bin/python3.12
import re
from print_xml import print_xml

# Ausgabe 1 Bambus = Hauptspeise 1
# Ausgabe 2 Bambus = Hauptspeise 2
# Y_Eintopf = Eintopf
RENUMS = re.compile(r" \([^\)]*\)")

URL = "https://www.studierendenwerk-mainz.de/speiseplan/Speiseplan.xml"
VERSION = "1.0.0"
VERBRAUCHSORT = "370"
IGNORE = ["Ausgabe intern ZM", "Ausgabe intern ZM vegan"]

CATEGORY = {
	"Ausgabe 1 Bambus": "Hauptspeise",
	"Ausgabe 2 Bambus": "Hauptspeise",
	"Y_Eintopf": "Eintopf",
}

print_xml(VERBRAUCHSORT, CATEGORY, URL, VERSION, RENUMS, IGNORE)