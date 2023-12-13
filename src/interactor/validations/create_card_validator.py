from typing import Dict
from datetime import datetime
import calendar
import re
from src.interactor.validations.base_input_validator import BaseInputValidator
from src.interactor.errors.error_classes import ValidationError
from creditcard.card import BRAND_REGEX, CreditCard


class ValidatedCreditCard(CreditCard):
    def __init__(self, *args, **kwargs):
        """Initialize the credit card."""
        return super().__init__(*args, **kwargs)

    # Check the card number against known brand regex patterns and return the brand name
    # override method from CreditCard from python-creditcard MAISTODOS
    def get_brand(self):
        """Get the brand of the credit card."""
        for brand, regex in BRAND_REGEX.items():
            if re.match(regex, self.number):
                return brand
        # return none because original method return Exception
        raise ValidationError({"brand": 'Brand not Found"'})


class CreateCardInputDtoValidator(BaseInputValidator):
    """Validates the create card input data.
    :param input_data: The input data to be validated.
    """

    def __init__(self, input_data: Dict) -> None:
        super().__init__(input_data)
        self.input_data = input_data
        self.__schema = {
            "number": {
                "type": "string",
                "minlength": 16,
                "maxlength": 16,
                "required": True,
                "empty": False,
            },
            "holder": {
                "type": "string",
                "minlength": 2,
                "maxlength": 255,
                "required": True,
                "empty": False,
            },
            "expiration_date": {"type": "date", "required": True, "empty": False},
            "cvv": {"type": "string", "required": False, "empty": True},
        }

    def is_exp_date_valid(self, exp_date):
        exp = self._format_date(exp_date)
        now = datetime.utcnow()
        return exp > now

    def _format_date(self, date):
        """Sets the last day of a month in a datetime object from given month / year"""
        lastday = calendar.monthrange(date.year, date.month)
        return datetime(date.year, date.month, lastday[1])

    def validate(self) -> None:
        """Validates the input data"""
        # Verify the input data using BaseInputValidator method
        super().verify(self.__schema)
        is_exp_date_valid = self.is_exp_date_valid(self.input_data["expiration_date"])
        if not is_exp_date_valid:
            raise ValidationError("Data Inválida")
        self.input_data["expiration_date"] = self._format_date(
            self.input_data["expiration_date"]
        )
        is_valid_card = ValidatedCreditCard(self.input_data["number"]).is_valid()
        if is_valid_card:
            brand = ValidatedCreditCard(self.input_data["number"]).get_brand()
            self.input_data["brand"] = brand
