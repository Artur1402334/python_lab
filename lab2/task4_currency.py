import xml.dom.minidom as minidom

FILE_NAME = 'currency.xml'


def write_dictionary():
    with open(FILE_NAME, encoding='cp1251') as xml_file:
        xml_data = xml_file.read()

    dom = minidom.parseString(xml_data)
    currency_dict = {}

    for valute in dom.getElementsByTagName('Valute'):
        num_code = valute.getElementsByTagName('NumCode')[0].firstChild.data
        char_code = valute.getElementsByTagName('CharCode')[0].firstChild.data
        currency_dict[num_code] = char_code

    print(currency_dict)
    print(f'Валют в словаре: {len(currency_dict)}')


write_dictionary()