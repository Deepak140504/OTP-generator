import random
import string

class OTPGenerator:
    """
    A class to generate One-Time Passwords (OTPs).
    Supports numeric and alphabetic OTPs.
    """

    def __init__(self, length=6):
        """
        Initializes the OTP generator with the desired OTP length.
        :param length: Length of the OTP to generate.
        """
        self.length = length

    def generate_numeric_otp(self):
        """
        Generates a numeric OTP consisting only of digits.
        :return: A string representing the numeric OTP.
        """
        otp = ''.join([str(random.randint(0, 9)) for _ in range(self.length)])
        return otp

    def generate_alphabetic_otp(self):
        """
        Generates an alphabetic OTP consisting of uppercase and lowercase letters.
        :return: A string representing the alphabetic OTP.
        """
        characters = string.ascii_letters  # Includes a-z and A-Z
        otp = ''.join(random.choice(characters) for _ in range(self.length))
        return otp

    def generate_alphanumeric_otp(self):
        """
        Generates an alphanumeric OTP with digits and letters.
        :return: A string representing the alphanumeric OTP.
        """
        characters = string.ascii_letters + string.digits
        otp = ''.join(random.choice(characters) for _ in range(self.length))
        return otp


if __name__ == "__main__":
    otp_length = 8

    # Create an OTPGenerator object
    otp_generator = OTPGenerator(length=otp_length)

    # Generate different types of OTPs
    numeric_otp = otp_generator.generate_numeric_otp()
    alphabetic_otp = otp_generator.generate_alphabetic_otp()
    alphanumeric_otp = otp_generator.generate_alphanumeric_otp()

    # Display the results
    print("Generated OTPs:")
    print("------------------")
    print("Numeric OTP      :", numeric_otp)
    print("Alphabetic OTP   :", alphabetic_otp)
    print("Alphanumeric OTP :", alphanumeric_otp)
