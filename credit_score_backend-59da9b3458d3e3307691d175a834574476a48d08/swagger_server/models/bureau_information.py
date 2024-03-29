# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BureauInformation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, amt_annuity: float=None, credit_active: str=None, credit_type: str=None, days_credit: int=None, days_credit_enddate: int=None, amt_credit_sum: float=None, amt_credit_sum_debt: float=None, amt_credit_sum_limit: float=None, amt_credit_sum_overdue: float=None, days_enddate_fact: int=None, sk_bureau_id: int=None, sk_id_curr: int=None):  # noqa: E501
        """BureauInformation - a model defined in Swagger

        :param amt_annuity: The amt_annuity of this BureauInformation.  # noqa: E501
        :type amt_annuity: float
        :param credit_active: The credit_active of this BureauInformation.  # noqa: E501
        :type credit_active: str
        :param credit_type: The credit_type of this BureauInformation.  # noqa: E501
        :type credit_type: str
        :param days_credit: The days_credit of this BureauInformation.  # noqa: E501
        :type days_credit: int
        :param days_credit_enddate: The days_credit_enddate of this BureauInformation.  # noqa: E501
        :type days_credit_enddate: int
        :param amt_credit_sum: The amt_credit_sum of this BureauInformation.  # noqa: E501
        :type amt_credit_sum: float
        :param amt_credit_sum_debt: The amt_credit_sum_debt of this BureauInformation.  # noqa: E501
        :type amt_credit_sum_debt: float
        :param amt_credit_sum_limit: The amt_credit_sum_limit of this BureauInformation.  # noqa: E501
        :type amt_credit_sum_limit: float
        :param amt_credit_sum_overdue: The amt_credit_sum_overdue of this BureauInformation.  # noqa: E501
        :type amt_credit_sum_overdue: float
        :param days_enddate_fact: The days_enddate_fact of this BureauInformation.  # noqa: E501
        :type days_enddate_fact: int
        :param sk_bureau_id: The sk_bureau_id of this BureauInformation.  # noqa: E501
        :type sk_bureau_id: int
        :param sk_id_curr: The sk_id_curr of this BureauInformation.  # noqa: E501
        :type sk_id_curr: int
        """
        self.swagger_types = {
            'amt_annuity': float,
            'credit_active': str,
            'credit_type': str,
            'days_credit': int,
            'days_credit_enddate': int,
            'amt_credit_sum': float,
            'amt_credit_sum_debt': float,
            'amt_credit_sum_limit': float,
            'amt_credit_sum_overdue': float,
            'days_enddate_fact': int,
            'sk_bureau_id': int,
            'sk_id_curr': int
        }

        self.attribute_map = {
            'amt_annuity': 'AMT_ANNUITY',
            'credit_active': 'CREDIT_ACTIVE',
            'credit_type': 'CREDIT_TYPE',
            'days_credit': 'DAYS_CREDIT',
            'days_credit_enddate': 'DAYS_CREDIT_ENDDATE',
            'amt_credit_sum': 'AMT_CREDIT_SUM',
            'amt_credit_sum_debt': 'AMT_CREDIT_SUM_DEBT',
            'amt_credit_sum_limit': 'AMT_CREDIT_SUM_LIMIT',
            'amt_credit_sum_overdue': 'AMT_CREDIT_SUM_OVERDUE',
            'days_enddate_fact': 'DAYS_ENDDATE_FACT',
            'sk_bureau_id': 'SK_BUREAU_ID',
            'sk_id_curr': 'SK_ID_CURR'
        }
        self._amt_annuity = amt_annuity
        self._credit_active = credit_active
        self._credit_type = credit_type
        self._days_credit = days_credit
        self._days_credit_enddate = days_credit_enddate
        self._amt_credit_sum = amt_credit_sum
        self._amt_credit_sum_debt = amt_credit_sum_debt
        self._amt_credit_sum_limit = amt_credit_sum_limit
        self._amt_credit_sum_overdue = amt_credit_sum_overdue
        self._days_enddate_fact = days_enddate_fact
        self._sk_bureau_id = sk_bureau_id
        self._sk_id_curr = sk_id_curr

    @classmethod
    def from_dict(cls, dikt) -> 'BureauInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BureauInformation of this BureauInformation.  # noqa: E501
        :rtype: BureauInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amt_annuity(self) -> float:
        """Gets the amt_annuity of this BureauInformation.

        Annuity of the Credit Bureau credit  # noqa: E501

        :return: The amt_annuity of this BureauInformation.
        :rtype: float
        """
        return self._amt_annuity

    @amt_annuity.setter
    def amt_annuity(self, amt_annuity: float):
        """Sets the amt_annuity of this BureauInformation.

        Annuity of the Credit Bureau credit  # noqa: E501

        :param amt_annuity: The amt_annuity of this BureauInformation.
        :type amt_annuity: float
        """

        self._amt_annuity = amt_annuity

    @property
    def credit_active(self) -> str:
        """Gets the credit_active of this BureauInformation.

        Status of the Credit Bureau (CB) reported credits  # noqa: E501

        :return: The credit_active of this BureauInformation.
        :rtype: str
        """
        return self._credit_active

    @credit_active.setter
    def credit_active(self, credit_active: str):
        """Sets the credit_active of this BureauInformation.

        Status of the Credit Bureau (CB) reported credits  # noqa: E501

        :param credit_active: The credit_active of this BureauInformation.
        :type credit_active: str
        """
        allowed_values = ["Closed", "Active", "Sold", "Bad debt"]  # noqa: E501
        if credit_active not in allowed_values:
            raise ValueError(
                "Invalid value for `credit_active` ({0}), must be one of {1}"
                .format(credit_active, allowed_values)
            )

        self._credit_active = credit_active

    @property
    def credit_type(self) -> str:
        """Gets the credit_type of this BureauInformation.

        Type of Credit Bureau credit (Car, cash,...)  # noqa: E501

        :return: The credit_type of this BureauInformation.
        :rtype: str
        """
        return self._credit_type

    @credit_type.setter
    def credit_type(self, credit_type: str):
        """Sets the credit_type of this BureauInformation.

        Type of Credit Bureau credit (Car, cash,...)  # noqa: E501

        :param credit_type: The credit_type of this BureauInformation.
        :type credit_type: str
        """
        allowed_values = ["Consumer credit", "Credit card", "Mortgage", "Car loan", "Microloan", "Loan for working capital replenishment", "Loan for business development", "Real estate loan", "Unknown type of loan", "Another type of loan", "Cash loan (non-earmarked)", "Loan for the purchase of equipment", "Mobile operator loan", "Interbank credit", "Loan for purchase of shares (margin lending)"]  # noqa: E501
        if credit_type not in allowed_values:
            raise ValueError(
                "Invalid value for `credit_type` ({0}), must be one of {1}"
                .format(credit_type, allowed_values)
            )

        self._credit_type = credit_type

    @property
    def days_credit(self) -> int:
        """Gets the days_credit of this BureauInformation.

        How many days before current application did client apply for Credit Bureau credit  # noqa: E501

        :return: The days_credit of this BureauInformation.
        :rtype: int
        """
        return self._days_credit

    @days_credit.setter
    def days_credit(self, days_credit: int):
        """Sets the days_credit of this BureauInformation.

        How many days before current application did client apply for Credit Bureau credit  # noqa: E501

        :param days_credit: The days_credit of this BureauInformation.
        :type days_credit: int
        """

        self._days_credit = days_credit

    @property
    def days_credit_enddate(self) -> int:
        """Gets the days_credit_enddate of this BureauInformation.

        Remaining duration of CB credit (in days) at the time of application in Home Credit  # noqa: E501

        :return: The days_credit_enddate of this BureauInformation.
        :rtype: int
        """
        return self._days_credit_enddate

    @days_credit_enddate.setter
    def days_credit_enddate(self, days_credit_enddate: int):
        """Sets the days_credit_enddate of this BureauInformation.

        Remaining duration of CB credit (in days) at the time of application in Home Credit  # noqa: E501

        :param days_credit_enddate: The days_credit_enddate of this BureauInformation.
        :type days_credit_enddate: int
        """

        self._days_credit_enddate = days_credit_enddate

    @property
    def amt_credit_sum(self) -> float:
        """Gets the amt_credit_sum of this BureauInformation.

        Current credit amount for the Credit Bureau credit  # noqa: E501

        :return: The amt_credit_sum of this BureauInformation.
        :rtype: float
        """
        return self._amt_credit_sum

    @amt_credit_sum.setter
    def amt_credit_sum(self, amt_credit_sum: float):
        """Sets the amt_credit_sum of this BureauInformation.

        Current credit amount for the Credit Bureau credit  # noqa: E501

        :param amt_credit_sum: The amt_credit_sum of this BureauInformation.
        :type amt_credit_sum: float
        """

        self._amt_credit_sum = amt_credit_sum

    @property
    def amt_credit_sum_debt(self) -> float:
        """Gets the amt_credit_sum_debt of this BureauInformation.

        Current debt on Credit Bureau credit  # noqa: E501

        :return: The amt_credit_sum_debt of this BureauInformation.
        :rtype: float
        """
        return self._amt_credit_sum_debt

    @amt_credit_sum_debt.setter
    def amt_credit_sum_debt(self, amt_credit_sum_debt: float):
        """Sets the amt_credit_sum_debt of this BureauInformation.

        Current debt on Credit Bureau credit  # noqa: E501

        :param amt_credit_sum_debt: The amt_credit_sum_debt of this BureauInformation.
        :type amt_credit_sum_debt: float
        """

        self._amt_credit_sum_debt = amt_credit_sum_debt

    @property
    def amt_credit_sum_limit(self) -> float:
        """Gets the amt_credit_sum_limit of this BureauInformation.

        Current credit limit of credit card reported in Credit Bureau  # noqa: E501

        :return: The amt_credit_sum_limit of this BureauInformation.
        :rtype: float
        """
        return self._amt_credit_sum_limit

    @amt_credit_sum_limit.setter
    def amt_credit_sum_limit(self, amt_credit_sum_limit: float):
        """Sets the amt_credit_sum_limit of this BureauInformation.

        Current credit limit of credit card reported in Credit Bureau  # noqa: E501

        :param amt_credit_sum_limit: The amt_credit_sum_limit of this BureauInformation.
        :type amt_credit_sum_limit: float
        """

        self._amt_credit_sum_limit = amt_credit_sum_limit

    @property
    def amt_credit_sum_overdue(self) -> float:
        """Gets the amt_credit_sum_overdue of this BureauInformation.

        Current amount overdue on Credit Bureau credit  # noqa: E501

        :return: The amt_credit_sum_overdue of this BureauInformation.
        :rtype: float
        """
        return self._amt_credit_sum_overdue

    @amt_credit_sum_overdue.setter
    def amt_credit_sum_overdue(self, amt_credit_sum_overdue: float):
        """Sets the amt_credit_sum_overdue of this BureauInformation.

        Current amount overdue on Credit Bureau credit  # noqa: E501

        :param amt_credit_sum_overdue: The amt_credit_sum_overdue of this BureauInformation.
        :type amt_credit_sum_overdue: float
        """

        self._amt_credit_sum_overdue = amt_credit_sum_overdue

    @property
    def days_enddate_fact(self) -> int:
        """Gets the days_enddate_fact of this BureauInformation.

        Days since CB credit ended at the time of application in Home Credit (only for closed credit)  # noqa: E501

        :return: The days_enddate_fact of this BureauInformation.
        :rtype: int
        """
        return self._days_enddate_fact

    @days_enddate_fact.setter
    def days_enddate_fact(self, days_enddate_fact: int):
        """Sets the days_enddate_fact of this BureauInformation.

        Days since CB credit ended at the time of application in Home Credit (only for closed credit)  # noqa: E501

        :param days_enddate_fact: The days_enddate_fact of this BureauInformation.
        :type days_enddate_fact: int
        """

        self._days_enddate_fact = days_enddate_fact

    @property
    def sk_bureau_id(self) -> int:
        """Gets the sk_bureau_id of this BureauInformation.

        Recoded ID of previous Credit Bureau credit related to our loan (unique coding for each loan application)  # noqa: E501

        :return: The sk_bureau_id of this BureauInformation.
        :rtype: int
        """
        return self._sk_bureau_id

    @sk_bureau_id.setter
    def sk_bureau_id(self, sk_bureau_id: int):
        """Sets the sk_bureau_id of this BureauInformation.

        Recoded ID of previous Credit Bureau credit related to our loan (unique coding for each loan application)  # noqa: E501

        :param sk_bureau_id: The sk_bureau_id of this BureauInformation.
        :type sk_bureau_id: int
        """

        self._sk_bureau_id = sk_bureau_id

    @property
    def sk_id_curr(self) -> int:
        """Gets the sk_id_curr of this BureauInformation.

        ID of loan in our sample - one loan in our sample can have 0,1,2 or more related previous credits in credit bureau  # noqa: E501

        :return: The sk_id_curr of this BureauInformation.
        :rtype: int
        """
        return self._sk_id_curr

    @sk_id_curr.setter
    def sk_id_curr(self, sk_id_curr: int):
        """Sets the sk_id_curr of this BureauInformation.

        ID of loan in our sample - one loan in our sample can have 0,1,2 or more related previous credits in credit bureau  # noqa: E501

        :param sk_id_curr: The sk_id_curr of this BureauInformation.
        :type sk_id_curr: int
        """

        self._sk_id_curr = sk_id_curr
