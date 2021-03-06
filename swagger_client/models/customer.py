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


class Customer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, card=None, customer_id=None, email=None, first_name=None, id=None, last_name=None, phone_number=None):
        """
        Customer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'bool',
            'card': 'Card',
            'customer_id': 'str',
            'email': 'str',
            'first_name': 'str',
            'id': 'int',
            'last_name': 'str',
            'phone_number': 'str'
        }

        self.attribute_map = {
            'active': 'active',
            'card': 'card',
            'customer_id': 'customerId',
            'email': 'email',
            'first_name': 'firstName',
            'id': 'id',
            'last_name': 'lastName',
            'phone_number': 'phoneNumber'
        }

        self._active = active
        self._card = card
        self._customer_id = customer_id
        self._email = email
        self._first_name = first_name
        self._id = id
        self._last_name = last_name
        self._phone_number = phone_number


    @property
    def active(self):
        """
        Gets the active of this Customer.


        :return: The active of this Customer.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Customer.


        :param active: The active of this Customer.
        :type: bool
        """

        self._active = active

    @property
    def card(self):
        """
        Gets the card of this Customer.


        :return: The card of this Customer.
        :rtype: Card
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Customer.


        :param card: The card of this Customer.
        :type: Card
        """

        self._card = card

    @property
    def customer_id(self):
        """
        Gets the customer_id of this Customer.


        :return: The customer_id of this Customer.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this Customer.


        :param customer_id: The customer_id of this Customer.
        :type: str
        """

        self._customer_id = customer_id

    @property
    def email(self):
        """
        Gets the email of this Customer.


        :return: The email of this Customer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Customer.


        :param email: The email of this Customer.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this Customer.


        :return: The first_name of this Customer.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Customer.


        :param first_name: The first_name of this Customer.
        :type: str
        """

        self._first_name = first_name

    @property
    def id(self):
        """
        Gets the id of this Customer.


        :return: The id of this Customer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Customer.


        :param id: The id of this Customer.
        :type: int
        """

        self._id = id

    @property
    def last_name(self):
        """
        Gets the last_name of this Customer.


        :return: The last_name of this Customer.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Customer.


        :param last_name: The last_name of this Customer.
        :type: str
        """

        self._last_name = last_name

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Customer.


        :return: The phone_number of this Customer.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Customer.


        :param phone_number: The phone_number of this Customer.
        :type: str
        """

        self._phone_number = phone_number

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
