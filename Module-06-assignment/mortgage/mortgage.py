"""
Description: A class meant to manage Mortgage options.
Author: {Mason Josefchuk}
Date: {Nov-08-2024}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    """
    A class that maintains Mortgages.
    
    Attributes:
        __Loan_Amount (float): The amount of the loan.
        __Rate (string): The Interest Rate that is applied.
        __Frequency (string): The amount of times you have to pay in a given time frame.
        __Amortization (integer): The amount of years of you have pay off the loan.
    """

    def __init__(self, loan_Amount: float, rate: str, frequency: str, amortization: int):
        """
        Initializes a new Mortgage calculation with the loan amount,
        interest rate, frequency, and the amortization.
        
        Args:
            Loan_Amount (float): The amount of the loan.
            Rate (string): The Interest Rate that is applied.
            Frequency (string): The amount of times you have to pay in a given time frame.
            Amortization (integer): The amount of years you have to pay off the loan.
        Returns: 
            None
        Raises:
        ValueError: Loan Amount must be positive
        ValueError: Rate provided is invalid
        ValueError: Frequency provided is invalid
        ValueError: Amortization provided is invalid
        """

        if loan_Amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        else:
            self.__loan_Amount = loan_Amount
        
        try:
            self.__rate = MortgageRate[rate]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        try:
            self.__frequency = PaymentFrequency[frequency]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")

        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        else:
            self.__amortization = amortization

    #Accessors
    @property
    def loan_Amount(self):
        """
        Accessor for the _loan_Amount attribute
        """
        return self.__loan_Amount

    @property
    def rate(self):
        """
        Accessor for the _rate attribute
        """
        return self.__rate
    
    @property
    def frequency(self):
        """
        Accessor for the _frequency attribute
        """
        return self.__frequency
    
    @property
    def amortization(self):
        """
        Accessor for the _amortization attribute
        """
        return self.__amortization
    
    #Mutators
    @loan_Amount.setter
    def loan_Amount(self, value: float):
        """
        Validates the Arguments that loan amount is a float
        and is not zero or below.
        Args:
            value(float): The loan amount
        Raises:
            ValueError: Loan Amount must be positive.
        """
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        
        self.__loan_Amount = value
        
    @rate.setter
    def rate(self, value: MortgageRate):
        """
        Converts the argument string rate value to it's
        corresponding enumeration.
        Args:
            value(str): The type of rate percentage
        Raises:
            ValueError: Rate provided is invalid.
        """
        try:
            if value.upper() in MortgageRate.__members__:
                self.__rate = MortgageRate[value.upper()]
        except:
            raise ValueError("Rate provided is invalid.")
        
        self.__rate = value
        
    @frequency.setter
    def frequency(self, value: PaymentFrequency):
        """
        Converts the argument string rate value to it's
        corresponding enumeration.
        Args:
            value(str): The type of frequent payments
        Raises:
            ValueError: Frequency provided is invalid.
        """
        try:
            if value.upper() in PaymentFrequency.__members__:
                self.__frequency = PaymentFrequency[value.upper()]
        except:
            raise ValueError("Frequency provided is invalid.")
        
        self.__frequency = value
        
    @amortization.setter
    def amortization(self, value: int):
        """
        Validates the argument that valid amortization is
        found in the VALID_AMORTIZAATION list
        Args:
            value(int): The type of amortization 
        Raises:
            ValueError: Amortization provided is invalid.
        """
        if  value not in VALID_AMORTIZATION:
            raise Exception("Amortization provided is invalid.")
        
        self.__amortization = value

    def calculate_payment(self) -> float:
        """
        Returns the Mortgage calculation with the loan amount,
        interest rate, frequency, and amortization calculated
        and returns the amount you will be paying.
        
        Args:
            Loan_Amount: Holds the amount of the loan.
            Rate: Holds the interest rate of the mortgage.
            Frequency: The amount of times you have to pay within the amortization frame.
            Amortization: The amount of years you have to pay off the loan.
            Total_Payments: Holds the multiplied solution of frequency and amortization.
        Returns: 
            Mortgage Payments: Returns the value of the Mortgage in the determined portions.
        Raises:
            None:
        """
        loan_Amount = self.__loan_Amount
        rate = self.__rate
        frequency = self.__frequency
        amortization = self.__frequency

        total_Payments = self.__amortization * self.__frequency
        
        
        mortgage_Payment = loan_Amount* (rate * (1 + rate)**total_Payments) / ((1 + rate)**total_Payments - 1)

        self.__mortgage_Payment = mortgage_Payment
        return(f"Loan Amount: ${loan_Amount:,.2f}\nInterest Rate: {rate * 100 * 12:.2f}% {rate}\nFrequency: {frequency}\nAmortization : {amortization} (years)\nPayment = {mortgage_Payment:.2f}")


    def __str__(self):
        """
        Returns a string representation of the class.
        
        Returns:
            str:  A string representation of a bank account 
        """
        return (f"Mortgage Amount: ${self.__loan_Amount:,.2f}\nRate: {self.__rate * 100 * 12}%\nAmortizaion: {self.__amortization}\nFrequency: {self.__frequency.title()} -- Calculated Payment: ${self.__mortgage_Payment:,.2f}")
    

    def __repr__(self):
        """
        Provides a representation of an Account object.
        Returns:
            str: A representation of a Mortgage Calculation.
                format: loan_Amount | interest rate | frequency | amortization
                example: [400000 | 00.0599 | 12 | 25]
        """
        return (f"Mortgage({self.loan_Amount}, {self.__rate}, "
                + f"{self.__frequency}, {self.__amortization})")