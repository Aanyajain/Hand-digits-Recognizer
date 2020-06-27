from PIL import Image
img=Image.open("C:/Users/om/Desktop/Hand-digits-Recognizer/two.png")

data=list(img.getdata())
for i in range(len(data)):
    data[i]=255-data[i]
print(data)