"""
Description: A class used to test the Mortgage class.
Author: {Mason Josefchuk}
Date: {Nov-08-2024}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):

    def test_init_raises_ValueError_when_invalid_loan_amount_inputted(self):
        #Arrange
        loan_Amount = -200000
        rate = "FIXED_3"
        frequency = "MONTHLY"
        amortization = 20
        expected = "Loan Amount must be positive."

        #Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_Amount, rate, frequency, amortization)
        
        self.assertEqual(expected, str(context.exception))


    def test_init_rasies_ValueError_when_invalid_rate_percent_inputted(self):
        #Arrange
        loan_Amount = 200000
        rate = "FIXED_4"
        frequency = "MONTHLY"
        amortization = 20
        expected = "Rate provided is invalid."

        #Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_Amount, rate, frequency, amortization)
        
        self.assertEqual(expected, str(context.exception))


    def test_init_raises_ValueError_when_invalid_frequency_inputted(self):
        #Arrange
        loan_Amount = 200000
        rate = "FIXED_3"
        frequency = "YEARLY"
        amortization = 20
        expected = "Frequency provided is invalid."

        #Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_Amount, rate, frequency, amortization)
        
        self.assertEqual(expected, str(context.exception))


    def test_init_raises_ValueError_when_invalid_amortization_inputted(self):
        #Arrange
        loan_Amount = 200000
        rate = "FIXED_3"
        frequency = "MONTHLY"
        amortization = 365
        expected = "Amortization provided is invalid."

        #Act and Assert
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_Amount, rate, frequency, amortization)
        
        self.assertEqual(expected, str(context.exception))


    def test_init_sets_attributes_for_valid_inputs(self):
        #Arrange
        loan_Amount = 200000
        rate = "FIXED_1"
        frequency = "MONTHLY"
        amortization = 20
        
        #Act
        mortgages = Mortgage(loan_Amount, rate, frequency, amortization)

        #Arrange
        self.assertEqual(loan_Amount, mortgages.loan_Amount)
        self.assertEqual(MortgageRate.FIXED_1, (mortgages.rate))
        self.assertEqual(PaymentFrequency.MONTHLY, mortgages.frequency)
        self.assertEqual(amortization, mortgages.amortization)
