import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    counter=1
    invalid = []
    for xml_file in glob.glob(path + '/*.xml'):
        filenametree = xml_file.split('\\')
        filename = filenametree[len(filenametree) - 1].split('.')[0] + '.jpg'
        filename2 = filenametree[len(filenametree) - 1].split('.')[0] + '.xml'
        filename = './images/' + filename
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('space'):
            noclass = False
            xmin = min([int(member[1][0].attrib['x']),int(member[1][1].attrib['x']),int(member[1][2].attrib['x']),
                        int(member[1][3].attrib['x'])])
            xmax = max([int(member[1][0].attrib['x']),int(member[1][1].attrib['x']),int(member[1][2].attrib['x']),
                        int(member[1][3].attrib['x'])])
            ymin = min([int(member[1][0].attrib['y']), int(member[1][1].attrib['y']), int(member[1][2].attrib['y']),
                        int(member[1][3].attrib['y'])])
            ymax = max([int(member[1][0].attrib['y']), int(member[1][1].attrib['y']), int(member[1][2].attrib['y']),
                        int(member[1][3].attrib['y'])])
            #height = ymax - ymin
            #widht = xmax - xmin
            if('occupied' in member.attrib):
                if (member.attrib['occupied']=='1'):
                    status = "taken"
                else :
                    status = "vacant"
            else :
                noclass = True
            value = (filename,
                     status,
                     xmin,
                     ymin,
                     xmax,
                     ymax
                     )
            if noclass == False:
                xml_list.append(value)





    column_name = ['filename', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
        image_path = r'.\images'
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(r'.\images\train.csv', index=None)
        print('Successfully converted xml to csv.')

main()