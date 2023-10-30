class Employee:

    raise_amount = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    # @property
    # email method is decorated with @property, making it a getter method. When you access e1.email,
    # it doesn't require parentheses, and it behaves like an attribute. 
    # The method returns the email address formatted based on the first and last attributes.
    @property
    def email(self):
        return f'{self.first.lower()}{self.last.lower()}@sient.tech'
    @property
    def fullName(self):
        return f'{self.first.title()} {self.last.title()}'
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Create an instance of the Employee class with the required arguments
e1 = Employee('saikrishna', 'murugeshan', 50000)

# Access the email property
print(e1.email)  # This will print 'sai.krishna@sient.tech'
print(e1.fullName)

# Apply a raise (defined by raise_amount) without passing any arguments
e1.apply_raise()

# Print the updated pay
print(e1.pay)