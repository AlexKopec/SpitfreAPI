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


class MaterialDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, address_id=None, attachments=None, availability_type=None, company_id=None, components_description=None, conditions_info=None, currency=None, description=None, disposal_method=None, frequency=None, hazardous=None, id=None, location_id=None, marketplace_service_id=None, material_category_id=None, material_category_name=None, material_subcategory_id=None, material_subcategory_name=None, name=None, price=None, quantity=None, quantity_type_id=None, size_description=None, user_id=None):
        """
        MaterialDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'bool',
            'address_id': 'int',
            'attachments': 'list[MaterialAttachmentDTO]',
            'availability_type': 'str',
            'company_id': 'int',
            'components_description': 'str',
            'conditions_info': 'str',
            'currency': 'str',
            'description': 'str',
            'disposal_method': 'str',
            'frequency': 'str',
            'hazardous': 'bool',
            'id': 'int',
            'location_id': 'int',
            'marketplace_service_id': 'int',
            'material_category_id': 'int',
            'material_category_name': 'str',
            'material_subcategory_id': 'int',
            'material_subcategory_name': 'str',
            'name': 'str',
            'price': 'float',
            'quantity': 'int',
            'quantity_type_id': 'int',
            'size_description': 'str',
            'user_id': 'int'
        }

        self.attribute_map = {
            'active': 'active',
            'address_id': 'addressId',
            'attachments': 'attachments',
            'availability_type': 'availabilityType',
            'company_id': 'companyId',
            'components_description': 'componentsDescription',
            'conditions_info': 'conditionsInfo',
            'currency': 'currency',
            'description': 'description',
            'disposal_method': 'disposalMethod',
            'frequency': 'frequency',
            'hazardous': 'hazardous',
            'id': 'id',
            'location_id': 'locationId',
            'marketplace_service_id': 'marketplaceServiceId',
            'material_category_id': 'materialCategoryId',
            'material_category_name': 'materialCategoryName',
            'material_subcategory_id': 'materialSubcategoryId',
            'material_subcategory_name': 'materialSubcategoryName',
            'name': 'name',
            'price': 'price',
            'quantity': 'quantity',
            'quantity_type_id': 'quantityTypeId',
            'size_description': 'sizeDescription',
            'user_id': 'userId'
        }

        self._active = active
        self._address_id = address_id
        self._attachments = attachments
        self._availability_type = availability_type
        self._company_id = company_id
        self._components_description = components_description
        self._conditions_info = conditions_info
        self._currency = currency
        self._description = description
        self._disposal_method = disposal_method
        self._frequency = frequency
        self._hazardous = hazardous
        self._id = id
        self._location_id = location_id
        self._marketplace_service_id = marketplace_service_id
        self._material_category_id = material_category_id
        self._material_category_name = material_category_name
        self._material_subcategory_id = material_subcategory_id
        self._material_subcategory_name = material_subcategory_name
        self._name = name
        self._price = price
        self._quantity = quantity
        self._quantity_type_id = quantity_type_id
        self._size_description = size_description
        self._user_id = user_id


    @property
    def active(self):
        """
        Gets the active of this MaterialDTO.


        :return: The active of this MaterialDTO.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this MaterialDTO.


        :param active: The active of this MaterialDTO.
        :type: bool
        """

        self._active = active

    @property
    def address_id(self):
        """
        Gets the address_id of this MaterialDTO.


        :return: The address_id of this MaterialDTO.
        :rtype: int
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """
        Sets the address_id of this MaterialDTO.


        :param address_id: The address_id of this MaterialDTO.
        :type: int
        """

        self._address_id = address_id

    @property
    def attachments(self):
        """
        Gets the attachments of this MaterialDTO.


        :return: The attachments of this MaterialDTO.
        :rtype: list[MaterialAttachmentDTO]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this MaterialDTO.


        :param attachments: The attachments of this MaterialDTO.
        :type: list[MaterialAttachmentDTO]
        """

        self._attachments = attachments

    @property
    def availability_type(self):
        """
        Gets the availability_type of this MaterialDTO.


        :return: The availability_type of this MaterialDTO.
        :rtype: str
        """
        return self._availability_type

    @availability_type.setter
    def availability_type(self, availability_type):
        """
        Sets the availability_type of this MaterialDTO.


        :param availability_type: The availability_type of this MaterialDTO.
        :type: str
        """
        allowed_values = ["Available", "Wanted"]
        if availability_type not in allowed_values:
            raise ValueError(
                "Invalid value for `availability_type` ({0}), must be one of {1}"
                .format(availability_type, allowed_values)
            )

        self._availability_type = availability_type

    @property
    def company_id(self):
        """
        Gets the company_id of this MaterialDTO.


        :return: The company_id of this MaterialDTO.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """
        Sets the company_id of this MaterialDTO.


        :param company_id: The company_id of this MaterialDTO.
        :type: int
        """

        self._company_id = company_id

    @property
    def components_description(self):
        """
        Gets the components_description of this MaterialDTO.


        :return: The components_description of this MaterialDTO.
        :rtype: str
        """
        return self._components_description

    @components_description.setter
    def components_description(self, components_description):
        """
        Sets the components_description of this MaterialDTO.


        :param components_description: The components_description of this MaterialDTO.
        :type: str
        """

        self._components_description = components_description

    @property
    def conditions_info(self):
        """
        Gets the conditions_info of this MaterialDTO.


        :return: The conditions_info of this MaterialDTO.
        :rtype: str
        """
        return self._conditions_info

    @conditions_info.setter
    def conditions_info(self, conditions_info):
        """
        Sets the conditions_info of this MaterialDTO.


        :param conditions_info: The conditions_info of this MaterialDTO.
        :type: str
        """

        self._conditions_info = conditions_info

    @property
    def currency(self):
        """
        Gets the currency of this MaterialDTO.


        :return: The currency of this MaterialDTO.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this MaterialDTO.


        :param currency: The currency of this MaterialDTO.
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
    def description(self):
        """
        Gets the description of this MaterialDTO.


        :return: The description of this MaterialDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MaterialDTO.


        :param description: The description of this MaterialDTO.
        :type: str
        """

        self._description = description

    @property
    def disposal_method(self):
        """
        Gets the disposal_method of this MaterialDTO.


        :return: The disposal_method of this MaterialDTO.
        :rtype: str
        """
        return self._disposal_method

    @disposal_method.setter
    def disposal_method(self, disposal_method):
        """
        Sets the disposal_method of this MaterialDTO.


        :param disposal_method: The disposal_method of this MaterialDTO.
        :type: str
        """

        self._disposal_method = disposal_method

    @property
    def frequency(self):
        """
        Gets the frequency of this MaterialDTO.


        :return: The frequency of this MaterialDTO.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """
        Sets the frequency of this MaterialDTO.


        :param frequency: The frequency of this MaterialDTO.
        :type: str
        """
        allowed_values = ["Daily", "Weekly", "Monthly", "Yearly"]
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def hazardous(self):
        """
        Gets the hazardous of this MaterialDTO.


        :return: The hazardous of this MaterialDTO.
        :rtype: bool
        """
        return self._hazardous

    @hazardous.setter
    def hazardous(self, hazardous):
        """
        Sets the hazardous of this MaterialDTO.


        :param hazardous: The hazardous of this MaterialDTO.
        :type: bool
        """

        self._hazardous = hazardous

    @property
    def id(self):
        """
        Gets the id of this MaterialDTO.


        :return: The id of this MaterialDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaterialDTO.


        :param id: The id of this MaterialDTO.
        :type: int
        """

        self._id = id

    @property
    def location_id(self):
        """
        Gets the location_id of this MaterialDTO.


        :return: The location_id of this MaterialDTO.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this MaterialDTO.


        :param location_id: The location_id of this MaterialDTO.
        :type: int
        """

        self._location_id = location_id

    @property
    def marketplace_service_id(self):
        """
        Gets the marketplace_service_id of this MaterialDTO.


        :return: The marketplace_service_id of this MaterialDTO.
        :rtype: int
        """
        return self._marketplace_service_id

    @marketplace_service_id.setter
    def marketplace_service_id(self, marketplace_service_id):
        """
        Sets the marketplace_service_id of this MaterialDTO.


        :param marketplace_service_id: The marketplace_service_id of this MaterialDTO.
        :type: int
        """

        self._marketplace_service_id = marketplace_service_id

    @property
    def material_category_id(self):
        """
        Gets the material_category_id of this MaterialDTO.


        :return: The material_category_id of this MaterialDTO.
        :rtype: int
        """
        return self._material_category_id

    @material_category_id.setter
    def material_category_id(self, material_category_id):
        """
        Sets the material_category_id of this MaterialDTO.


        :param material_category_id: The material_category_id of this MaterialDTO.
        :type: int
        """

        self._material_category_id = material_category_id

    @property
    def material_category_name(self):
        """
        Gets the material_category_name of this MaterialDTO.


        :return: The material_category_name of this MaterialDTO.
        :rtype: str
        """
        return self._material_category_name

    @material_category_name.setter
    def material_category_name(self, material_category_name):
        """
        Sets the material_category_name of this MaterialDTO.


        :param material_category_name: The material_category_name of this MaterialDTO.
        :type: str
        """

        self._material_category_name = material_category_name

    @property
    def material_subcategory_id(self):
        """
        Gets the material_subcategory_id of this MaterialDTO.


        :return: The material_subcategory_id of this MaterialDTO.
        :rtype: int
        """
        return self._material_subcategory_id

    @material_subcategory_id.setter
    def material_subcategory_id(self, material_subcategory_id):
        """
        Sets the material_subcategory_id of this MaterialDTO.


        :param material_subcategory_id: The material_subcategory_id of this MaterialDTO.
        :type: int
        """

        self._material_subcategory_id = material_subcategory_id

    @property
    def material_subcategory_name(self):
        """
        Gets the material_subcategory_name of this MaterialDTO.


        :return: The material_subcategory_name of this MaterialDTO.
        :rtype: str
        """
        return self._material_subcategory_name

    @material_subcategory_name.setter
    def material_subcategory_name(self, material_subcategory_name):
        """
        Sets the material_subcategory_name of this MaterialDTO.


        :param material_subcategory_name: The material_subcategory_name of this MaterialDTO.
        :type: str
        """

        self._material_subcategory_name = material_subcategory_name

    @property
    def name(self):
        """
        Gets the name of this MaterialDTO.


        :return: The name of this MaterialDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MaterialDTO.


        :param name: The name of this MaterialDTO.
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """
        Gets the price of this MaterialDTO.


        :return: The price of this MaterialDTO.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this MaterialDTO.


        :param price: The price of this MaterialDTO.
        :type: float
        """

        self._price = price

    @property
    def quantity(self):
        """
        Gets the quantity of this MaterialDTO.


        :return: The quantity of this MaterialDTO.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this MaterialDTO.


        :param quantity: The quantity of this MaterialDTO.
        :type: int
        """

        self._quantity = quantity

    @property
    def quantity_type_id(self):
        """
        Gets the quantity_type_id of this MaterialDTO.


        :return: The quantity_type_id of this MaterialDTO.
        :rtype: int
        """
        return self._quantity_type_id

    @quantity_type_id.setter
    def quantity_type_id(self, quantity_type_id):
        """
        Sets the quantity_type_id of this MaterialDTO.


        :param quantity_type_id: The quantity_type_id of this MaterialDTO.
        :type: int
        """

        self._quantity_type_id = quantity_type_id

    @property
    def size_description(self):
        """
        Gets the size_description of this MaterialDTO.


        :return: The size_description of this MaterialDTO.
        :rtype: str
        """
        return self._size_description

    @size_description.setter
    def size_description(self, size_description):
        """
        Sets the size_description of this MaterialDTO.


        :param size_description: The size_description of this MaterialDTO.
        :type: str
        """

        self._size_description = size_description

    @property
    def user_id(self):
        """
        Gets the user_id of this MaterialDTO.


        :return: The user_id of this MaterialDTO.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this MaterialDTO.


        :param user_id: The user_id of this MaterialDTO.
        :type: int
        """

        self._user_id = user_id

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
