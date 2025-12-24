class Plant:
    def __init__(name, height, age):
        name = ""
        height = 0
        age = 0
    
    def display(this):
        print(f"Name : {this.name}")
        print(f"Name : {this.height}cm")
        print(f"Age : {this.age}")

test = Plant("Bonjour", 50, 3)
test.display()