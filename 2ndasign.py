import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('uni_info.xml')
root = tree.getroot()

data = []

for stream in root.findall('stream'):
    course = stream.find('course').text

    for student in stream.findall('student'):
        name = student.find('name').text
        age = student.find('age').text
        gender = student.find('gender').text
        roll_number = student.find('roll_number').text

        data.append([course, name, age, gender, roll_number])


df = pd.DataFrame(data, columns=["Stream", "Name", "Age", "Gender", "Roll_No"])

print(df)