import xmltodict
import json


def normalize_number(numb):
    return float(numb.replace(',', '.'))


with open('zad2.xml', encoding="ISO-8859-2") as loaded_xml:
    xml_dict = xmltodict.parse(loaded_xml.read())

high_currencies = list(filter(lambda currency_data: normalize_number(currency_data['kurs_sredni']) >= 1,
                              xml_dict['tabela_kursow']['pozycja']))

xml_dict['tabela_kursow']['pozycja'] = high_currencies
with open('zad2.json', 'w') as output:
    output.write(json.dumps(xml_dict))
