def A():
    print("Hello")
def B():
    print("How are you")
def C():
    print("Hi")

x = input("Pick a capital letter from A to C: ")
if x == "A":
    A()
elif x == "B":
    B()
elif x == "C":
    C()
elif x != "A" and x != "B" and x != "C":
    print("That is not a capital letter from A to C")