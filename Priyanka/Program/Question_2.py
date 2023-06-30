
import os  #to create a folder/directory
import xml.etree.ElementTree as ET
import pandas as pd

#source xml file location stored in a variable
source_file_loc = "D:\\Python training\\Assignment\\Source\\uni_info.xml"

#destination folder stored in a variable.
#this variable will be appeneded with university name and course name folders later
destination = "D:\\Python training\\Assignment\\Destination\\"
directory_name = destination + "DataFrame" + "\\"

#create the direvtory only if it does not exist
if not os.path.exists(directory_name):
    os.makedirs(directory_name, exist_ok=True)

#parse the source XML
tree = ET.parse(source_file_loc)

#get the Root element so that we can traverse the parsed XML tree
root = tree.getroot()

# Define empty list to store data
data = []


# Iterate over each stream using FOR loop
for stream in root.iter('stream'):
    course = stream.find('course').text
    # Iterate over each student in the stream
    for student in stream.findall('student'):
        name = student.find('name').text
        age = int(student.find('age').text)
        gender = student.find('gender').text
        roll_number = student.find('roll_number').text

        # Append student data to the list
        data.append([course, name, age, gender, roll_number])


# Create a DataFrame
columns = ['Stream', 'Name', 'Age', 'Gender', 'Roll Number']
df = pd.DataFrame(data, columns=columns)

# Print the DataFrame
print(df)

print("------------------------------")

file_name = directory_name + "XML_to_DF" + '.csv'
df.to_csv(file_name)

#print/store only JOHN DOE DATA
john_data = df.query("Name == 'John Doe'")
file_name =directory_name + "John_Doe" + '.csv'
john_data.to_csv(file_name)
#print(john_data)

#print/store sorted data by Age column
print("####################")
file_name =directory_name + "Age_wise_sorting" + '.csv'
sort_data = df.sort_values(by=['Age'])      #add 'ascending = False' as a second parameter for sorting in descending order
sort_data.to_csv(file_name)
print(sort_data)


#finding Female students and their count
female_cnt=(df['Gender'].value_counts()['Female'])
print("Total no. of female students =",female_cnt)


