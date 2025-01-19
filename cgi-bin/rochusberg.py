#!/usr/bin/python3.12

import re
from print_xml import print_xml

# Ausgabe Rochusberg = Hauptspeise
# Y_Eintopf = Eintopf
RENUMS = re.compile(r" \([^\)]*\)")

URL = "https://www.studierendenwerk-mainz.de/speiseplan/Speiseplan.xml"
VERSION = "1.0.0"
VERBRAUCHSORT = "431"
IGNORE = ["Ausgabe intern ZM", "Ausgabe intern ZM vegan"]

CATEGORY = {
	"Ausgabe Rochusberg": "Hauptspeise",
	"Y_Eintopf": "Eintopf",
}

print_xml(VERBRAUCHSORT, CATEGORY, URL, VERSION, RENUMS, IGNORE)