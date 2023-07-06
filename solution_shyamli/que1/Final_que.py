import xml.etree.ElementTree as ET
import os


myfile =ET.iterparse('uni_info.xml',events = ('end',))
for events, uni in myfile:
    if uni.tag == 'university':
        uni_title = uni.find('uname').text
        uni_filename = format(uni_title +".xml")
        #filename = "/"+title+"/"+title+".xml"
        # Parent Directory path
        parent_dir = uni_title
        # Path
        path = os.path.join(parent_dir, uni_filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path,'wb') as f:
            #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write(ET.tostring(uni))

    if uni.tag == 'stream':
        stream_title = uni.find('course').text     

        filename = format(stream_title +".xml")
        #filename = "/"+title+"/"+title+".xml"
        # Parent Directory path
        parent_dir = 'Mumbai University'
        sub_dir = stream_title
        # Path
        path = os.path.join(parent_dir,stream_title, filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path,'wb') as f:
            #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write(ET.tostring(uni))