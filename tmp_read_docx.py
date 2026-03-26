import zipfile
import xml.etree.ElementTree as ET

def read_docx(path):
    z = zipfile.ZipFile(path)
    xml_content = z.read('word/document.xml')
    root = ET.fromstring(xml_content)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    for p in root.findall('.//w:p', ns):
        texts = []
        for t in p.findall('.//w:t', ns):
            if t.text:
                texts.append(t.text)
        if texts:
            print(''.join(texts))

read_docx(r'd:\Projects\week-5\Day-25\Week 05 · Day 25.docx')
