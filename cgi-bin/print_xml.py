import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
import requests
from datetime import date
from sys import exit

def print_xml(verbrauchsort, category_dict, url, version, renums, ignore_list=[]):
	r = requests.get(url)

	if r.status_code != 200:
		print("ERROR")
		exit()

	root_element = Element("openmensa", {"version":"2.1", "xmlns":"http://openmensa.org/open-mensa-v2", "xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance", "xsi:schemaLocation": "http://openmensa.org/open-mensa-v2 http://openmensa.org/open-mensa-v2.xsd"})
	version_element = SubElement(root_element, "version")
	version_element.text = version
	canteen_element = SubElement(root_element, "canteen")

	data = ET.fromstring(r.text)

	date_elements = dict()

	for result in data.findall(f"./ROWDATA/ROW[@VERBRAUCHSORT='{verbrauchsort}']"):
		if result.get("SPEISE") in ignore_list:
			continue
		_date = result.get("DATUM").split(".")
		_date = date(int(_date[2]), int(_date[1]), int(_date[0]))
		_date = _date.isoformat()

		if not _date in date_elements:
			date_element = SubElement(canteen_element, "day", date=_date)
			for category_name in category_dict.values():
				SubElement(date_element, "category", name=category_name)
				SubElement(date_element, "category", name=category_name)
				SubElement(date_element, "category", name=category_name)
			SubElement(date_element, "category", name="Sonstiges")
			date_elements[_date] = date_element
		date_element = date_elements[_date]

		category = "Sonstiges"
		if result.get("SPEISE") in category_dict:
			category = category_dict[result.get("SPEISE").strip()]
		category_element = date_element.find(f"./category[@name='{category}']")
		name = result.get("AUSGABETEXT")
		if len(name) > 250:
			name = renums.sub("", name)
		if len(name) > 250:
			name = name[:250]
		note = result.get("MENUEKENNZTEXT").strip() + " Allergene: " + result.get("ZSNUMMERN").strip()
		students = result.get("STUDIERENDE").strip()
		employee = result.get("BEDIENSTETE").strip()
		meal = SubElement(category_element, "meal")
		meal_name = SubElement(meal, "name")
		meal_name.text = name
		note_element = SubElement(meal, "note")
		note_element.text = note
		price_stud = SubElement(meal, "price", role="student")
		price_stud.text = students
		price_empl = SubElement(meal, "price", role="employee")
		price_empl.text = employee

	for day in canteen_element.findall("day"):
		for result in day.findall("category"):
			if len(result) == 0:
				day.remove(result)

	print("Content-Type: application/xml\n\n")
	#print('<?xml version="1.0" encoding="UTF-8"?>')
	print(ET.tostring(root_element, encoding="unicode", method="xml", xml_declaration=True))