#!/usr/bin/python3.12

import re
from print_xml import print_xml

RENUMS = re.compile(r" \([^\)]*\)")

URL = "https://www.studierendenwerk-mainz.de/speiseplan/Speiseplan.xml"
VERSION = "1.0.0"
VERBRAUCHSORT = "310"
IGNORE = ["Ausgabe intern ZM", "Ausgabe intern ZM vegan"]

CATEGORY = {
	"Ausgabe Menü ZM": "Theke 3",
	"Ausgabe Menü ZM vegan": "Theke 3",
	"Tagessuppe": "Theke 3",
	"Ausgabe Pastatheke v/v ZM": "Theke 2",
	"Ausgabe Pastatheke ZM": "Theke 2",
	"Ausgabe 1.1 ZM": "Theke 1",
	"Ausgabe 1.2 ZM": "Theke 1",
	"Beilagen einfach": "Theke 1",
	"Beilagen frittiert": "Theke 1",
	"Beilagensalat": "Theke 1",
	"Y_Eintopf": "Theke 1",
	"Würstchen Schwein / Rind": "Theke 1",
	"Z_Salatbuffet": "Theke 1",
	"Brötchen Kräuterbaguette": "Theke 1",
}

print_xml(VERBRAUCHSORT, CATEGORY, URL, VERSION, RENUMS, IGNORE)