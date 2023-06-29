import os
import xml.etree.ElementTree as ET

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def parse_xml(xml_path):
    print(xml_path)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    uname = root.find('uname').text
    streams = root.findall('stream')

    for index in range(len(streams)):
      students = streams[index].findall('stream/student')
      course = streams[index].find('course').text
      folder_path = os.path.join(uname, course)
      create_folder(folder_path)
      xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
      xml_content += '<students>\n'
      for student in students:
          xml_content += '  <student>\n'
          for child in student:
              xml_content += f'    <{child.tag}>{child.text}</{child.tag}>\n'
          xml_content += '  </student>\n'
      xml_content += '</students>'
  
      xml_file_path = os.path.join(folder_path, f'{course.lower().replace(" ", "_")}.xml')
      create_file(xml_file_path, xml_content)

# Usage
xml_file_path = './uni_info.xml'
parse_xml(xml_file_path)
