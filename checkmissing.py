import glob
import pandas as pd
import os

def main():
    image_path = r'F:\keras-default\images'
    for xml_file in glob.glob(image_path + '/*.xml'):
        filenametree = xml_file.split('\\')
        filename = filenametree[len(filenametree) - 1].split('.')[0]+'.jpg'
        filename2 = filenametree[len(filenametree) - 1].split('.')[0]+'.xml'
        if os.path.isfile(r'F:\keras-default\images' + filename2 ) and os.path.isfile(r'F:\keras-default\images' + filename ) :
            continue
        else :
            print (filename2)
            os.remove(r'F:/keras-default/images/'+filename2)


main()