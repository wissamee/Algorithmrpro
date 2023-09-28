import xml.etree.ElementTree as ET
def count_domain_extensions(xml_file_path):
    extension_counts = {}
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        for database in root.findall(".//database"):
            for table in database.findall(".//table"):
                for column in table.findall(".//column[@name='domain']"):
                    domain = column.text.lower()
                    parts = domain.split('.')
                    if len(parts) > 1:
                        extension = parts[-1]
                        extension_counts[extension] = extension_counts.get(extension, 0) + 1
        for extension, count in extension_counts.items():
            print(f'{extension}: {count}')

    except ET.ParseError as e:
        print(f'Error parsing the XML file: {e}')

if __name__ == "__main__":
    xml_file_path = r'C:\Users\pcBEN\Desktop\algo pro\domains.xml' 
    count_domain_extensions(xml_file_path)
