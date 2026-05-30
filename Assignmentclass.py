class multipleFunctions():
    def subfields():
        subfield_list = ["Machine Learning","Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in subfield_list:
            print(field)
    def oddEven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("Even number")
            msg="even number"
        else:
            print("Odd number")
            msg="Odd number"
        return msg

    def marriageAge():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if (age<=18) or (age>18 and age<=21 and gender=="male"):
            print("NOT ELIGIBLE")
        elif (age>18 and gender=="female") or (age>21):
            print("ELIGIBLE")

    def percentage(markslist):
        total=0
        for marks in markslist:
            total+=marks
        length= len(markslist)
        percent= total/length
        print("Total: ", total)
        print("Percentage:",f"{percent:.13f}")

    def triangle_area(height, breadth):
        area=(height*breadth)/2
        print("Area of triangle: ", area)

    def triangle_perimeter(height1, height2, breadth):
        perimeter= height1+height2+breadth
        print("Perimeter of triangle: ", perimeter)