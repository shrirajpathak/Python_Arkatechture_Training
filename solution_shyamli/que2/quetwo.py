import xml.etree.ElementTree as ET
import pandas as pd

myfile = ET.parse('uni_info.xml')
myroot = myfile.getroot()



#Initialise list to store data

course_list = []
name_list = []
age_list = []
gender_list = []
roll_number_list = []


all_items=[]
 
for i in myroot.iter('stream'):
    course = i.find('course').text
    for student in i.iter('student'):
        name = student.find('name').text
        age = student.find('age').text
        gender = student.find('gender').text
        roll_number = student.find('roll_number').text
        
        course_items = [course,name,age,gender,roll_number]
        all_items.append(course_items)
        
coulmn_name = ['course','name','age','gender','roll_number']


df = pd.DataFrame(all_items,columns= coulmn_name)
print(df)

#Filter by name 

def filter_john_Doe(df):
   filter_john_Doe = df[df['name'] == 'John Doe']
    #filter_john_Doe_Count = len(filter_john_Doe)
   # print(f'Jonh Doe present in {filter_john_Doe_Count} course.')
   print(filter_john_Doe)

filter_john_Doe.to_excel('filter_john_Doe.xlsx')

#Filter by age

age_list=df.sort_values(by='age',axis=0,ascending=False)    
print(age_list)
age_list.to_excel('age_list.xlsx')



#count of female

female_count = df[df['gender']=='Female']
print(female_count)   
female_count.to_excel('female_count.xlsx')



 
        
    
