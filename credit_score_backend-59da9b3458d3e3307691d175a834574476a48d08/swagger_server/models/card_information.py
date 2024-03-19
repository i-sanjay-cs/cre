# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CardInformation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, amt_balance: float=None, amt_credit_limit_actual: float=None, amt_drawings_atm_current: float=None, amt_drawings_current: float=None, amt_drawings_pos_current: float=None, amt_payment_current: float=None, cnt_drawings_atm_current: int=None, cnt_drawings_current: int=None, cnt_drawings_pos_current: int=None, cnt_instalment_mature_cum: int=None, months_balance: int=None, name_contract_status: str=None, sk_dpd_def: int=None, sk_id_curr: int=None, sk_id_prev: int=None):  # noqa: E501
        """CardInformation - a model defined in Swagger

        :param amt_balance: The amt_balance of this CardInformation.  # noqa: E501
        :type amt_balance: float
        :param amt_credit_limit_actual: The amt_credit_limit_actual of this CardInformation.  # noqa: E501
        :type amt_credit_limit_actual: float
        :param amt_drawings_atm_current: The amt_drawings_atm_current of this CardInformation.  # noqa: E501
        :type amt_drawings_atm_current: float
        :param amt_drawings_current: The amt_drawings_current of this CardInformation.  # noqa: E501
        :type amt_drawings_current: float
        :param amt_drawings_pos_current: The amt_drawings_pos_current of this CardInformation.  # noqa: E501
        :type amt_drawings_pos_current: float
        :param amt_payment_current: The amt_payment_current of this CardInformation.  # noqa: E501
        :type amt_payment_current: float
        :param cnt_drawings_atm_current: The cnt_drawings_atm_current of this CardInformation.  # noqa: E501
        :type cnt_drawings_atm_current: int
        :param cnt_drawings_current: The cnt_drawings_current of this CardInformation.  # noqa: E501
        :type cnt_drawings_current: int
        :param cnt_drawings_pos_current: The cnt_drawings_pos_current of this CardInformation.  # noqa: E501
        :type cnt_drawings_pos_current: int
        :param cnt_instalment_mature_cum: The cnt_instalment_mature_cum of this CardInformation.  # noqa: E501
        :type cnt_instalment_mature_cum: int
        :param months_balance: The months_balance of this CardInformation.  # noqa: E501
        :type months_balance: int
        :param name_contract_status: The name_contract_status of this CardInformation.  # noqa: E501
        :type name_contract_status: str
        :param sk_dpd_def: The sk_dpd_def of this CardInformation.  # noqa: E501
        :type sk_dpd_def: int
        :param sk_id_curr: The sk_id_curr of this CardInformation.  # noqa: E501
        :type sk_id_curr: int
        :param sk_id_prev: The sk_id_prev of this CardInformation.  # noqa: E501
        :type sk_id_prev: int
        """
        self.swagger_types = {
            'amt_balance': float,
            'amt_credit_limit_actual': float,
            'amt_drawings_atm_current': float,
            'amt_drawings_current': float,
            'amt_drawings_pos_current': float,
            'amt_payment_current': float,
            'cnt_drawings_atm_current': int,
            'cnt_drawings_current': int,
            'cnt_drawings_pos_current': int,
            'cnt_instalment_mature_cum': int,
            'months_balance': int,
            'name_contract_status': str,
            'sk_dpd_def': int,
            'sk_id_curr': int,
            'sk_id_prev': int
        }

        self.attribute_map = {
            'amt_balance': 'AMT_BALANCE',
            'amt_credit_limit_actual': 'AMT_CREDIT_LIMIT_ACTUAL',
            'amt_drawings_atm_current': 'AMT_DRAWINGS_ATM_CURRENT',
            'amt_drawings_current': 'AMT_DRAWINGS_CURRENT',
            'amt_drawings_pos_current': 'AMT_DRAWINGS_POS_CURRENT',
            'amt_payment_current': 'AMT_PAYMENT_CURRENT',
            'cnt_drawings_atm_current': 'CNT_DRAWINGS_ATM_CURRENT',
            'cnt_drawings_current': 'CNT_DRAWINGS_CURRENT',
            'cnt_drawings_pos_current': 'CNT_DRAWINGS_POS_CURRENT',
            'cnt_instalment_mature_cum': 'CNT_INSTALMENT_MATURE_CUM',
            'months_balance': 'MONTHS_BALANCE',
            'name_contract_status': 'NAME_CONTRACT_STATUS',
            'sk_dpd_def': 'SK_DPD_DEF',
            'sk_id_curr': 'SK_ID_CURR',
            'sk_id_prev': 'SK_ID_PREV'
        }
        self._amt_balance = amt_balance
        self._amt_credit_limit_actual = amt_credit_limit_actual
        self._amt_drawings_atm_current = amt_drawings_atm_current
        self._amt_drawings_current = amt_drawings_current
        self._amt_drawings_pos_current = amt_drawings_pos_current
        self._amt_payment_current = amt_payment_current
        self._cnt_drawings_atm_current = cnt_drawings_atm_current
        self._cnt_drawings_current = cnt_drawings_current
        self._cnt_drawings_pos_current = cnt_drawings_pos_current
        self._cnt_instalment_mature_cum = cnt_instalment_mature_cum
        self._months_balance = months_balance
        self._name_contract_status = name_contract_status
        self._sk_dpd_def = sk_dpd_def
        self._sk_id_curr = sk_id_curr
        self._sk_id_prev = sk_id_prev

    @classmethod
    def from_dict(cls, dikt) -> 'CardInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CardInformation of this CardInformation.  # noqa: E501
        :rtype: CardInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amt_balance(self) -> float:
        """Gets the amt_balance of this CardInformation.

        Balance during the month of previous credit  # noqa: E501

        :return: The amt_balance of this CardInformation.
        :rtype: float
        """
        return self._amt_balance

    @amt_balance.setter
    def amt_balance(self, amt_balance: float):
        """Sets the amt_balance of this CardInformation.

        Balance during the month of previous credit  # noqa: E501

        :param amt_balance: The amt_balance of this CardInformation.
        :type amt_balance: float
        """

        self._amt_balance = amt_balance

    @property
    def amt_credit_limit_actual(self) -> float:
        """Gets the amt_credit_limit_actual of this CardInformation.

        Credit card limit during the month of the previous credit  # noqa: E501

        :return: The amt_credit_limit_actual of this CardInformation.
        :rtype: float
        """
        return self._amt_credit_limit_actual

    @amt_credit_limit_actual.setter
    def amt_credit_limit_actual(self, amt_credit_limit_actual: float):
        """Sets the amt_credit_limit_actual of this CardInformation.

        Credit card limit during the month of the previous credit  # noqa: E501

        :param amt_credit_limit_actual: The amt_credit_limit_actual of this CardInformation.
        :type amt_credit_limit_actual: float
        """

        self._amt_credit_limit_actual = amt_credit_limit_actual

    @property
    def amt_drawings_atm_current(self) -> float:
        """Gets the amt_drawings_atm_current of this CardInformation.

        Amount drawing at ATM during the month of the previous credit  # noqa: E501

        :return: The amt_drawings_atm_current of this CardInformation.
        :rtype: float
        """
        return self._amt_drawings_atm_current

    @amt_drawings_atm_current.setter
    def amt_drawings_atm_current(self, amt_drawings_atm_current: float):
        """Sets the amt_drawings_atm_current of this CardInformation.

        Amount drawing at ATM during the month of the previous credit  # noqa: E501

        :param amt_drawings_atm_current: The amt_drawings_atm_current of this CardInformation.
        :type amt_drawings_atm_current: float
        """

        self._amt_drawings_atm_current = amt_drawings_atm_current

    @property
    def amt_drawings_current(self) -> float:
        """Gets the amt_drawings_current of this CardInformation.

        Amount drawing during the month of the previous credit  # noqa: E501

        :return: The amt_drawings_current of this CardInformation.
        :rtype: float
        """
        return self._amt_drawings_current

    @amt_drawings_current.setter
    def amt_drawings_current(self, amt_drawings_current: float):
        """Sets the amt_drawings_current of this CardInformation.

        Amount drawing during the month of the previous credit  # noqa: E501

        :param amt_drawings_current: The amt_drawings_current of this CardInformation.
        :type amt_drawings_current: float
        """

        self._amt_drawings_current = amt_drawings_current

    @property
    def amt_drawings_pos_current(self) -> float:
        """Gets the amt_drawings_pos_current of this CardInformation.

        Amount drawing or buying goods during the month of the previous credit  # noqa: E501

        :return: The amt_drawings_pos_current of this CardInformation.
        :rtype: float
        """
        return self._amt_drawings_pos_current

    @amt_drawings_pos_current.setter
    def amt_drawings_pos_current(self, amt_drawings_pos_current: float):
        """Sets the amt_drawings_pos_current of this CardInformation.

        Amount drawing or buying goods during the month of the previous credit  # noqa: E501

        :param amt_drawings_pos_current: The amt_drawings_pos_current of this CardInformation.
        :type amt_drawings_pos_current: float
        """

        self._amt_drawings_pos_current = amt_drawings_pos_current

    @property
    def amt_payment_current(self) -> float:
        """Gets the amt_payment_current of this CardInformation.

        How much did the client pay during the month on the previous credit  # noqa: E501

        :return: The amt_payment_current of this CardInformation.
        :rtype: float
        """
        return self._amt_payment_current

    @amt_payment_current.setter
    def amt_payment_current(self, amt_payment_current: float):
        """Sets the amt_payment_current of this CardInformation.

        How much did the client pay during the month on the previous credit  # noqa: E501

        :param amt_payment_current: The amt_payment_current of this CardInformation.
        :type amt_payment_current: float
        """

        self._amt_payment_current = amt_payment_current

    @property
    def cnt_drawings_atm_current(self) -> int:
        """Gets the cnt_drawings_atm_current of this CardInformation.

        Number of drawings at ATM during this month on the previous credit  # noqa: E501

        :return: The cnt_drawings_atm_current of this CardInformation.
        :rtype: int
        """
        return self._cnt_drawings_atm_current

    @cnt_drawings_atm_current.setter
    def cnt_drawings_atm_current(self, cnt_drawings_atm_current: int):
        """Sets the cnt_drawings_atm_current of this CardInformation.

        Number of drawings at ATM during this month on the previous credit  # noqa: E501

        :param cnt_drawings_atm_current: The cnt_drawings_atm_current of this CardInformation.
        :type cnt_drawings_atm_current: int
        """

        self._cnt_drawings_atm_current = cnt_drawings_atm_current

    @property
    def cnt_drawings_current(self) -> int:
        """Gets the cnt_drawings_current of this CardInformation.

        Number of drawings during this month on the previous credit  # noqa: E501

        :return: The cnt_drawings_current of this CardInformation.
        :rtype: int
        """
        return self._cnt_drawings_current

    @cnt_drawings_current.setter
    def cnt_drawings_current(self, cnt_drawings_current: int):
        """Sets the cnt_drawings_current of this CardInformation.

        Number of drawings during this month on the previous credit  # noqa: E501

        :param cnt_drawings_current: The cnt_drawings_current of this CardInformation.
        :type cnt_drawings_current: int
        """

        self._cnt_drawings_current = cnt_drawings_current

    @property
    def cnt_drawings_pos_current(self) -> int:
        """Gets the cnt_drawings_pos_current of this CardInformation.

        Number of drawings for goods during this month on the previous credit  # noqa: E501

        :return: The cnt_drawings_pos_current of this CardInformation.
        :rtype: int
        """
        return self._cnt_drawings_pos_current

    @cnt_drawings_pos_current.setter
    def cnt_drawings_pos_current(self, cnt_drawings_pos_current: int):
        """Sets the cnt_drawings_pos_current of this CardInformation.

        Number of drawings for goods during this month on the previous credit  # noqa: E501

        :param cnt_drawings_pos_current: The cnt_drawings_pos_current of this CardInformation.
        :type cnt_drawings_pos_current: int
        """

        self._cnt_drawings_pos_current = cnt_drawings_pos_current

    @property
    def cnt_instalment_mature_cum(self) -> int:
        """Gets the cnt_instalment_mature_cum of this CardInformation.

        Number of paid installments on the previous credit  # noqa: E501

        :return: The cnt_instalment_mature_cum of this CardInformation.
        :rtype: int
        """
        return self._cnt_instalment_mature_cum

    @cnt_instalment_mature_cum.setter
    def cnt_instalment_mature_cum(self, cnt_instalment_mature_cum: int):
        """Sets the cnt_instalment_mature_cum of this CardInformation.

        Number of paid installments on the previous credit  # noqa: E501

        :param cnt_instalment_mature_cum: The cnt_instalment_mature_cum of this CardInformation.
        :type cnt_instalment_mature_cum: int
        """

        self._cnt_instalment_mature_cum = cnt_instalment_mature_cum

    @property
    def months_balance(self) -> int:
        """Gets the months_balance of this CardInformation.

        Month of balance relative to application date (-1 means the freshest balance date)  # noqa: E501

        :return: The months_balance of this CardInformation.
        :rtype: int
        """
        return self._months_balance

    @months_balance.setter
    def months_balance(self, months_balance: int):
        """Sets the months_balance of this CardInformation.

        Month of balance relative to application date (-1 means the freshest balance date)  # noqa: E501

        :param months_balance: The months_balance of this CardInformation.
        :type months_balance: int
        """

        self._months_balance = months_balance

    @property
    def name_contract_status(self) -> str:
        """Gets the name_contract_status of this CardInformation.

        Contract status (active signed,...) on the previous credit  # noqa: E501

        :return: The name_contract_status of this CardInformation.
        :rtype: str
        """
        return self._name_contract_status

    @name_contract_status.setter
    def name_contract_status(self, name_contract_status: str):
        """Sets the name_contract_status of this CardInformation.

        Contract status (active signed,...) on the previous credit  # noqa: E501

        :param name_contract_status: The name_contract_status of this CardInformation.
        :type name_contract_status: str
        """
        allowed_values = ["Active", "Completed", "Demand", "Signed", "Sent proposal", "Refused", "Approved"]  # noqa: E501
        if name_contract_status not in allowed_values:
            raise ValueError(
                "Invalid value for `name_contract_status` ({0}), must be one of {1}"
                .format(name_contract_status, allowed_values)
            )

        self._name_contract_status = name_contract_status

    @property
    def sk_dpd_def(self) -> int:
        """Gets the sk_dpd_def of this CardInformation.

        DPD (Days past due) during the month with tolerance (debts with low loan amounts are ignored) of the previous credit  # noqa: E501

        :return: The sk_dpd_def of this CardInformation.
        :rtype: int
        """
        return self._sk_dpd_def

    @sk_dpd_def.setter
    def sk_dpd_def(self, sk_dpd_def: int):
        """Sets the sk_dpd_def of this CardInformation.

        DPD (Days past due) during the month with tolerance (debts with low loan amounts are ignored) of the previous credit  # noqa: E501

        :param sk_dpd_def: The sk_dpd_def of this CardInformation.
        :type sk_dpd_def: int
        """

        self._sk_dpd_def = sk_dpd_def

    @property
    def sk_id_curr(self) -> int:
        """Gets the sk_id_curr of this CardInformation.

        ID of loan in our sample  # noqa: E501

        :return: The sk_id_curr of this CardInformation.
        :rtype: int
        """
        return self._sk_id_curr

    @sk_id_curr.setter
    def sk_id_curr(self, sk_id_curr: int):
        """Sets the sk_id_curr of this CardInformation.

        ID of loan in our sample  # noqa: E501

        :param sk_id_curr: The sk_id_curr of this CardInformation.
        :type sk_id_curr: int
        """

        self._sk_id_curr = sk_id_curr

    @property
    def sk_id_prev(self) -> int:
        """Gets the sk_id_prev of this CardInformation.

        ID of previous credit in Home credit related to loan in our sample. (One loan in our sample can have 0,1,2 or more previous loans in Home Credit)  # noqa: E501

        :return: The sk_id_prev of this CardInformation.
        :rtype: int
        """
        return self._sk_id_prev

    @sk_id_prev.setter
    def sk_id_prev(self, sk_id_prev: int):
        """Sets the sk_id_prev of this CardInformation.

        ID of previous credit in Home credit related to loan in our sample. (One loan in our sample can have 0,1,2 or more previous loans in Home Credit)  # noqa: E501

        :param sk_id_prev: The sk_id_prev of this CardInformation.
        :type sk_id_prev: int
        """

        self._sk_id_prev = sk_id_prev