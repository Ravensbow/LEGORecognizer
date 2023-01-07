from PIL import Image, ImageChops
import os

IMAGE_FILE_DIR = 'C:\\Users\\walko\\OneDrive\\Dokumenty\\LEGORecognizer\\images'
DATA_CLASSES_DIR = 'C:\\Users\\walko\\OneDrive\\Dokumenty\\LEGORecognizer\\Data_classes.txt'
FRAME_COUNT = 40

def getBox(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    return diff.getbbox()

def readLabel_ids():
    labelFile = open(DATA_CLASSES_DIR, "r")
    labels = labelFile.read().splitlines()
    return labels

def getImages():
    fileNames = [fileName for fileName in os.listdir(IMAGE_FILE_DIR) if fileName.endswith(".png")]
    fileNames.sort()
    return fileNames

def constructTrainingFile():
    data_train = open("data_train.txt", "w")
    tempCount = 0
    imageFiles = getImages()
    print(imageFiles)
    labels = readLabel_ids()

    for image in imageFiles:
        im = Image.open(IMAGE_FILE_DIR + "/" + image)
        line = IMAGE_FILE_DIR + '/' + image + ' ' + ','.join(map(str, getBox(im))) + ',' + str(tempCount//FRAME_COUNT)
        data_train.write(line)
        data_train.write('\n')
        tempCount = tempCount + 1
    data_train.close() 

constructTrainingFile()