##TEST
with open("fruits.txt","a") as myFile:
    myFile.write("\npeaches")
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##Exercise 1
with open("name list.txt") as myFile:
    box1=myFile.read()
box1 = box1.split("\n")
box2 = [i.title() for i in box1]
box2 = "\n".join(box2)
with open("name list.txt","w") as myFile:
    myFile.write(box2)
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##Exercise 2
#Homework
