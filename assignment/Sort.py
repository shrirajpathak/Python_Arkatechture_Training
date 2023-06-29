import xml.etree.ElementTree as ET
import pandas as pd

# Load the XML file
tree = ET.parse('uni_info.xml')
root = tree.getroot()

data = []

# Iterate over each stream
for stream in root.findall('stream'):
    course = stream.find('course').text

    # Iterate over each student in the stream
    for student in stream.findall('student'):
        name = student.find('name').text
        age = student.find('age').text
        gender = student.find('gender').text
        roll_number = student.find('roll_number').text

        # Append the student data as a list of values
        data.append([course, name, age, gender, roll_number])

# Create a DataFrame using the collected data and column names
df = pd.DataFrame(data, columns=["Stream", "Name", "Age", "Gender", "Roll_No"])

# Print the resulting DataFrame
print(df)
