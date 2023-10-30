import unittest
from employee import Employee  # Assuming 'employee.py' contains the 'Employee' class

class TestEmployee(unittest.TestCase):
    def test_email(self):
        # Create instances of the Employee class with different names and pay
        emp1 = Employee('sai', 'krishnamurugeshan', 1000)
        emp2 = Employee('chaithanyasai', 'murugeshan', 2000)

        # Test the 'email' property for the initial instances
        self.assertEqual(emp1.email, 'saikrishnamurugeshan@sient.tech')
        self.assertEqual(emp2.email, 'chaithanyasaimurugeshan@sient.tech')

        # Modify the 'first' attribute for both instances
        emp1.first = 'rama'
        emp2.first = 'mohansai'

        # Test the 'email' property again after modifying 'first'
        self.assertEqual(emp1.email, 'ramakrishnamurugeshan@sient.tech')
        self.assertEqual(emp2.email, 'mohansaimurugeshan@sient.tech')

    def test_fullName(self):
        # Create instances of the Employee class with different names and pay
        emp1 = Employee('saikrishna', 'murugeshan', 1000)
        emp2 = Employee('chaithanyasai', 'murugeshan', 2000)

        # Test the 'fullName' property for the initial instances
        self.assertEqual(emp1.fullName, 'Saikrishna Murugeshan')
        self.assertEqual(emp2.fullName, 'Chaithanyasai Murugeshan')

        # Modify the 'first' attribute for both instances
        emp1.first = 'ramakrishna'
        emp2.first = 'mohansai'

        # Test the 'fullName' property again after modifying 'first'
        self.assertEqual(emp1.fullName, 'Ramakrishna Murugeshan')
        self.assertEqual(emp2.fullName, 'Mohansai Murugeshan')

    def test_apply_raise(self):
        # Create instances of the Employee class with different names and pay
        emp1 = Employee('saikrishna', 'murugeshan', 1000)
        emp2 = Employee('chaithanyasai', 'murugeshan', 2000)

        # Apply the 'apply_raise' method to increase the pay
        emp1.apply_raise()
        emp2.apply_raise()

        # Test if the pay was increased as expected
        self.assertEqual(emp1.pay, 1050)
        self.assertEqual(emp2.pay, 2100)

if __name__ == '__main__':
    # The code inside this block will only run if this script is the main program.
    # This is important for unit testing, as you typically want to run your tests
    # when executing this script directly but not when it's imported as a module into another script.
    unittest.main()
    # This line runs the test suite and starts the test discovery process. It
    # searches for test cases and test methods in the script and executes them.

