# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BureauBalanceInformation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, months_balance: int=None, sk_bureau_id: int=None, status: str=None):  # noqa: E501
        """BureauBalanceInformation - a model defined in Swagger

        :param months_balance: The months_balance of this BureauBalanceInformation.  # noqa: E501
        :type months_balance: int
        :param sk_bureau_id: The sk_bureau_id of this BureauBalanceInformation.  # noqa: E501
        :type sk_bureau_id: int
        :param status: The status of this BureauBalanceInformation.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'months_balance': int,
            'sk_bureau_id': int,
            'status': str
        }

        self.attribute_map = {
            'months_balance': 'MONTHS_BALANCE',
            'sk_bureau_id': 'SK_BUREAU_ID',
            'status': 'STATUS'
        }
        self._months_balance = months_balance
        self._sk_bureau_id = sk_bureau_id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'BureauBalanceInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BureauBalanceInformation of this BureauBalanceInformation.  # noqa: E501
        :rtype: BureauBalanceInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def months_balance(self) -> int:
        """Gets the months_balance of this BureauBalanceInformation.

        Month of balance relative to application date (-1 means the freshest balance date)  # noqa: E501

        :return: The months_balance of this BureauBalanceInformation.
        :rtype: int
        """
        return self._months_balance

    @months_balance.setter
    def months_balance(self, months_balance: int):
        """Sets the months_balance of this BureauBalanceInformation.

        Month of balance relative to application date (-1 means the freshest balance date)  # noqa: E501

        :param months_balance: The months_balance of this BureauBalanceInformation.
        :type months_balance: int
        """

        self._months_balance = months_balance

    @property
    def sk_bureau_id(self) -> int:
        """Gets the sk_bureau_id of this BureauBalanceInformation.

        Recoded ID of Credit Bureau credit (unique coding for each application) - use this to join to CREDIT_BUREAU table  # noqa: E501

        :return: The sk_bureau_id of this BureauBalanceInformation.
        :rtype: int
        """
        return self._sk_bureau_id

    @sk_bureau_id.setter
    def sk_bureau_id(self, sk_bureau_id: int):
        """Sets the sk_bureau_id of this BureauBalanceInformation.

        Recoded ID of Credit Bureau credit (unique coding for each application) - use this to join to CREDIT_BUREAU table  # noqa: E501

        :param sk_bureau_id: The sk_bureau_id of this BureauBalanceInformation.
        :type sk_bureau_id: int
        """

        self._sk_bureau_id = sk_bureau_id

    @property
    def status(self) -> str:
        """Gets the status of this BureauBalanceInformation.

        Status of Credit Bureau loan during the month (active, closed, DPD0-30,… [C means closed, X means status unknown, 0 means no DPD, 1 means maximal did during month between 1-30, 2 means DPD 31-60,… 5 means DPD 120+ or sold or written off ] )  # noqa: E501

        :return: The status of this BureauBalanceInformation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this BureauBalanceInformation.

        Status of Credit Bureau loan during the month (active, closed, DPD0-30,… [C means closed, X means status unknown, 0 means no DPD, 1 means maximal did during month between 1-30, 2 means DPD 31-60,… 5 means DPD 120+ or sold or written off ] )  # noqa: E501

        :param status: The status of this BureauBalanceInformation.
        :type status: str
        """
        allowed_values = ["C", "0", "X", "1", "2", "3", "5", "4"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
