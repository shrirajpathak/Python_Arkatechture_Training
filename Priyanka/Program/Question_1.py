import os  #to create a folder/directory
import xml.etree.ElementTree as ET

#source xml file location stored in a variable
source_file_loc = "D:\\Python training\\Assignment\\Source\\uni_info.xml"

#destination folder stored in a variable.
#this variable will be appeneded with university name and course name folders later
destination = "D:\\Python training\\Assignment\\Destination\\"


def parse_xml_files(source_file_loc,destination):
    #parsing the source XML file
    xmldoc = ET.parse(source_file_loc)

    #get   the root element
    xmlroot = xmldoc.getroot()

    #below line will fetch UnitversityName from the root element
    uni_name = xmlroot.find('uname').text


    #below line will find all chunks(i.e xml belonging to each) of 'stream' and store them in stream_elements array
    stream_elements  = xmlroot.findall('stream')

    #we need to iterate through this stream_elements for accessing the content of each 'stream' and store separately
    #this is done using FOR loop
    for stream_element in stream_elements:
        stream_tree = ET.ElementTree(stream_element)  #ElementTree returns all elements in the tree
        course_name = stream_element.find('course').text

        directory_name = destination + uni_name + "\\" + course_name + "\\"
        if not os.path.exists(directory_name):
            os.makedirs(directory_name,exist_ok=True)
        file_name = directory_name + course_name + '.xml'

        stream_tree.write(file_name, encoding='utf-8', xml_declaration=True)


parse_xml_files(source_file_loc,destination)