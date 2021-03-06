# coding: utf-8

"""
    spitfire API

    spitfire API documentation

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Plan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, currency=None, id=None, name=None, period=None, plan_id=None, price=None):
        """
        Plan - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'bool',
            'currency': 'str',
            'id': 'int',
            'name': 'str',
            'period': 'str',
            'plan_id': 'str',
            'price': 'float'
        }

        self.attribute_map = {
            'active': 'active',
            'currency': 'currency',
            'id': 'id',
            'name': 'name',
            'period': 'period',
            'plan_id': 'planId',
            'price': 'price'
        }

        self._active = active
        self._currency = currency
        self._id = id
        self._name = name
        self._period = period
        self._plan_id = plan_id
        self._price = price


    @property
    def active(self):
        """
        Gets the active of this Plan.


        :return: The active of this Plan.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Plan.


        :param active: The active of this Plan.
        :type: bool
        """

        self._active = active

    @property
    def currency(self):
        """
        Gets the currency of this Plan.


        :return: The currency of this Plan.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Plan.


        :param currency: The currency of this Plan.
        :type: str
        """
        allowed_values = ["USD", "EUR"]
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def id(self):
        """
        Gets the id of this Plan.


        :return: The id of this Plan.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Plan.


        :param id: The id of this Plan.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Plan.


        :return: The name of this Plan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Plan.


        :param name: The name of this Plan.
        :type: str
        """

        self._name = name

    @property
    def period(self):
        """
        Gets the period of this Plan.


        :return: The period of this Plan.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this Plan.


        :param period: The period of this Plan.
        :type: str
        """
        allowed_values = ["day", "week", "month", "year"]
        if period not in allowed_values:
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}"
                .format(period, allowed_values)
            )

        self._period = period

    @property
    def plan_id(self):
        """
        Gets the plan_id of this Plan.


        :return: The plan_id of this Plan.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this Plan.


        :param plan_id: The plan_id of this Plan.
        :type: str
        """

        self._plan_id = plan_id

    @property
    def price(self):
        """
        Gets the price of this Plan.


        :return: The price of this Plan.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this Plan.


        :param price: The price of this Plan.
        :type: float
        """

        self._price = price

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
