import cv2
image = cv2.imread("img.jpg")

def forceLengthTo8(string):
    if len(string) ==7:
        return string
    return  "0"+string



class image:
    def __init__(self):
        imgSource = cv2.imread("img.jpg")
        height,width,channel = imgSource.shape




class message:
    messageInput=str()
    stringBin=list()

    def binaryString(self):
        self.stringBin = list(map(lambda x: forceLengthTo8(bin(ord(x))[2:]), self.messageInput))

    def printBinary(self):
        for i in self.stringBin:
            print (i)

    def __init__(self):
        self.messageInput = input("Enter the code to encrypt")
        self.binaryString()
        self.printBinary()


mainMsg = message()
