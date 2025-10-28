class Employee:
    def __init__(self):
        self.empno=int(input("Empno:"))
        self.name=input("Name:")
        self.depname=input("Depname:")
        self.designation=input("Designation:")
        self.age=int(input("Age:"))
        self.salary=int(input("Salary:"))
    def search(self,eid):
        return self.empno==eid
    def display(self):
        print(f"\n Empno:{self.empno}")
        print(f"Name:{self.name}")
        print(f"Depname:{self.depname}")
        print(f"Age:{self.age}")
        print(f"Salary:{self.salary}")
lst=[]
while True:
    print("\n 1.Accept details of n employees")
    print("2.Search given employee using empno")
    print("3.Display employee details in neat format")
    print("4.Exit")
    print()
    ch=input("your choice:")
    if ch=="1":
        n=int(input("Enter the total number of employees:"))
        for i in range(n):
            emp=Employee()
            lst.append(emp)
            print()
    elif ch=="2":
        eid=int(input("Enter employee no to search:"))
        found=False
        for emp in lst:
            if emp.search(eid):
                print("Employee found")
                emp.display()
                found=True
                break
        if not found:
            print("Employee not found")
    elif ch=="3":
        print("Empyoee details:")
        for emp in lst:
            emp.display()
    elif ch=="4":
        print("Exiting...")
        break
    else:
        print("Invalid choice,try again!")
        
        
