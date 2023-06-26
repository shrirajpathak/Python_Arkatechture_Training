
import xml.etree.ElementTree as ET   #helps structure in tree format
import xml.dom.minidom
import os 
mytree = ET.parse('uni_info.xml') #parse fn takes XML file format to parse it. my tree is variable parse xml learn in one time 
myroot = mytree.getroot()
university = myroot.find('uname').text
abc_uni=university.replace(' ','_')
root_path=r'/Users/saurabhp/Desktop/Python'
def parse_xml_files(mytree,root_path):
    os.makedirs(os.path.join(root_path,abc_uni))
    for x in myroot.findall('stream'):
        course=x.find('course').text
        print(course.replace(' ','_'))
        course_uni=course.replace(' ','_')
        os.makedirs(os.path.join(root_path,abc_uni,course_uni))


    context = ET.iterparse('uni_info.xml', events=('end', ))   #iterparse - run in loop 
    for event, elem in context:
        if elem.tag == 'stream':
            course = elem.find('course').text
            course_uni=course.replace(' ','_')
       # os.makedirs(os.path.join(root_path,abc_uni,course_uni))
            filename = os.path.join(root_path,abc_uni,course_uni,f"{course_uni}.xml")
            with open(filename, 'wb') as f:
                f.write(ET.tostring(elem))

parse_xml_files(mytree,root_path)