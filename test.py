import unittest
import time
from pyHM310T import PowerSupply

class TestPowerSupply(unittest.TestCase):
    def setUp(self):
        self.ps = PowerSupply(port='/dev/ttyUSB0')  # Replace with the actual port

    def tearDown(self):
        self.ps.close()

    def test_enable_and_check_output(self):
        #DANGER! Make sure you don't have any load or a safe load connected

        self.ps.set_current(1)

        self.ps.enable_output(True)
        self.assertTrue(self.ps.is_output_enabled())

        self.ps.enable_output(False)
        self.assertFalse(self.ps.is_output_enabled())

    def test_set_and_get_voltage(self):
        self.ps.set_voltage(12)
        self.assertEqual(self.ps.get_voltage(), 12)

        self.ps.set_voltage(30)
        self.assertEqual(self.ps.get_voltage(), 30)

        # Test voltage limit
        self.ps.set_voltage(31)
        self.assertEqual(self.ps.get_voltage(), 30)

        self.ps.set_voltage(3.3)
        self.assertEqual(self.ps.get_voltage(), 3.3)

        self.ps.set_voltage(3.33)
        self.assertEqual(self.ps.get_voltage(), 3.33)

    def test_set_and_get_current(self):
        self.ps.set_current(5)
        self.assertEqual(self.ps.get_current(), 5)

        self.ps.set_current(10)
        self.assertEqual(self.ps.get_current(), 10)

        # Test current limit
        self.ps.set_current(11)
        self.assertEqual(self.ps.get_current(), 10)
        
        self.ps.set_current(1)
        self.assertEqual(self.ps.get_current(), 1)

    def test_get_display_values(self):
        #requires test under load. Recommend LED/220Ohm resister combo.
        self.ps.enable_output(True)
        self.ps.set_voltage(5)
        time.sleep(1)
        # These tests depend on the current state of the power supply
        print(f"Voltage display: {self.ps.get_voltage_display()}")
        self.assertEqual(self.ps.get_voltage_display(),5)
        print(f"Current display: {self.ps.get_current_display()}")
        self.assertGreater(self.ps.get_current_display(),0)
        print(f"Power display: {self.ps.get_power_display()}")
        self.assertGreater(self.ps.get_power_display(),0)
        self.ps.enable_output(False)

    def test_get_comm_address(self):
        # This test depends on the current communication address of the power supply
        print(f"Communication address: {self.ps.get_comm_address()}")

    def test_set_and_get_ovp(self):
        self.ps.set_ovp(12)
        self.assertEqual(self.ps.get_ovp(), 12)

        self.ps.set_ovp(30)
        self.assertEqual(self.ps.get_ovp(), 30)

        # Test OVP limit
        self.ps.set_ovp(31)
        self.assertEqual(self.ps.get_ovp(), 30)
       
        self.ps.set_ovp(5.2)
        self.assertEqual(self.ps.get_ovp(), 5.2)

    def test_set_and_get_ocp(self):
        self.ps.set_ocp(5)
        self.assertEqual(self.ps.get_ocp(), 5)

        self.ps.set_ocp(10)
        self.assertEqual(self.ps.get_ocp(), 10)

        # Test OCP limit
        self.ps.set_ocp(11)
        self.assertEqual(self.ps.get_ocp(), 10)

        self.ps.set_ocp(2.22)
        self.assertEqual(self.ps.get_ocp(), 2.22)

    def test_set_and_get_opp(self):
        self.ps.set_opp(100)
        self.assertEqual(self.ps.get_opp(), 100)

        self.ps.set_opp(300)
        self.assertEqual(self.ps.get_opp(), 300)

        # Test OPP limit
        self.ps.set_opp(301)
        self.assertEqual(self.ps.get_opp(), 300)

        self.ps.set_opp(12.34)
        self.assertEqual(self.ps.get_opp(), 12.34)

    def test_get_protection_status(self):
        status = self.ps.get_protection_status()
        self.assertIsInstance(status, dict)
        self.assertIn('isOVP', status)
        self.assertIn('isOCP', status)
        self.assertIn('isOPP', status)
        self.assertIn('isOTP', status)
        self.assertIn('isSCP', status)

    # Add more tests as needed...

if __name__ == '__main__':
    unittest.main()

