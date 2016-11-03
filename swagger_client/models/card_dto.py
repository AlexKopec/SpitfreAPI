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


class CardDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, cvc=None, exp_month=None, exp_year=None, id=None, number=None, token=None):
        """
        CardDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'bool',
            'cvc': 'str',
            'exp_month': 'int',
            'exp_year': 'int',
            'id': 'int',
            'number': 'str',
            'token': 'str'
        }

        self.attribute_map = {
            'active': 'active',
            'cvc': 'cvc',
            'exp_month': 'exp_month',
            'exp_year': 'exp_year',
            'id': 'id',
            'number': 'number',
            'token': 'token'
        }

        self._active = active
        self._cvc = cvc
        self._exp_month = exp_month
        self._exp_year = exp_year
        self._id = id
        self._number = number
        self._token = token


    @property
    def active(self):
        """
        Gets the active of this CardDTO.


        :return: The active of this CardDTO.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CardDTO.


        :param active: The active of this CardDTO.
        :type: bool
        """

        self._active = active

    @property
    def cvc(self):
        """
        Gets the cvc of this CardDTO.


        :return: The cvc of this CardDTO.
        :rtype: str
        """
        return self._cvc

    @cvc.setter
    def cvc(self, cvc):
        """
        Sets the cvc of this CardDTO.


        :param cvc: The cvc of this CardDTO.
        :type: str
        """

        self._cvc = cvc

    @property
    def exp_month(self):
        """
        Gets the exp_month of this CardDTO.


        :return: The exp_month of this CardDTO.
        :rtype: int
        """
        return self._exp_month

    @exp_month.setter
    def exp_month(self, exp_month):
        """
        Sets the exp_month of this CardDTO.


        :param exp_month: The exp_month of this CardDTO.
        :type: int
        """

        self._exp_month = exp_month

    @property
    def exp_year(self):
        """
        Gets the exp_year of this CardDTO.


        :return: The exp_year of this CardDTO.
        :rtype: int
        """
        return self._exp_year

    @exp_year.setter
    def exp_year(self, exp_year):
        """
        Sets the exp_year of this CardDTO.


        :param exp_year: The exp_year of this CardDTO.
        :type: int
        """

        self._exp_year = exp_year

    @property
    def id(self):
        """
        Gets the id of this CardDTO.


        :return: The id of this CardDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CardDTO.


        :param id: The id of this CardDTO.
        :type: int
        """

        self._id = id

    @property
    def number(self):
        """
        Gets the number of this CardDTO.


        :return: The number of this CardDTO.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this CardDTO.


        :param number: The number of this CardDTO.
        :type: str
        """

        self._number = number

    @property
    def token(self):
        """
        Gets the token of this CardDTO.


        :return: The token of this CardDTO.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this CardDTO.


        :param token: The token of this CardDTO.
        :type: str
        """

        self._token = token

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