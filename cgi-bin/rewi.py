#!/usr/bin/python3.12
import re
from print_xml import print_xml
# Ausgabe 1 Rewi = Hauptspeise 1
# Ausgabe 2 Rewi = Hauptspeise 2
# Ausgabe 3 Rewi "Bowl"= Bowl
# Rewi Topping 1 = Topping 1
# Rewi Topping 2 = Topping 2
# Beilagen einfach = Beilagen einfach
# Y_Eintopf = Eintopf
RENUMS = re.compile(r" \([^\)]*\)")

URL = "https://www.studierendenwerk-mainz.de/speiseplan/Speiseplan.xml"
VERSION = "1.0.0"
VERBRAUCHSORT = "425"
IGNORE = ["Ausgabe intern ZM", "Ausgabe intern ZM vegan"]

CATEGORY = {
	"Ausgabe 1 Rewi": "Hauptspeise",
	"Ausgabe 2 Rewi": "Hauptspeise",
	"Ausgabe 3 Rewi &quote;Bowl&quote;": "Bowl",
	"Rewi Topping 1": "Bowl",
	"Rewi Topping 2": "Bowl",
	"Beilagen einfach": "Beilagen",
	"Y_Eintopf": "Eintopf",
}

print_xml(VERBRAUCHSORT, CATEGORY, URL, VERSION, RENUMS, IGNORE)