#!/usr/bin/python3.12
import re
from print_xml import print_xml

# Ausgabe 1 Mensablitz = Mensablitz 1
# Ausgabe 2 Mensablitz = Mensablitz 2
# Food Truck Aktion I = Food Truck 1
# Food Truck Aktion II = Food Truck 2
# Food Truck vegan/veggetar = Food Truck vegan/vegetarisch
# 32.318 && Pommes frites = kleine Pommes
# 32.319 && Pommes frites = große Pommes
RENUMS = re.compile(r" \([^\)]*\)")
URL = "https://www.studierendenwerk-mainz.de/speiseplan/Speiseplan.xml"
VERSION = "1.0.0"
VERBRAUCHSORT = "446"
IGNORE = ["Ausgabe intern ZM", "Ausgabe intern ZM vegan"]

CATEGORY = {
	"Ausgabe 1 Mensablitz": "Mensablitz",
	"Ausgabe 2 Mensablitz": "Mensablitz",
	"Food Truck Aktion I": "Food Truck",
	"Food Truck Aktion II": "Food Truck",
	"Food Truck vegan/veggetar": "Food Truck",
	"Pommes frites": "Food Truck",
}

print_xml(VERBRAUCHSORT, CATEGORY, URL, VERSION, RENUMS, IGNORE)