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


class ActivityMessageDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, activity_id=None, activity_participant_id=None, id=None, message_date_time=None, message_text=None):
        """
        ActivityMessageDTO - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_id': 'int',
            'activity_participant_id': 'int',
            'id': 'int',
            'message_date_time': 'datetime',
            'message_text': 'str'
        }

        self.attribute_map = {
            'activity_id': 'activityId',
            'activity_participant_id': 'activityParticipantId',
            'id': 'id',
            'message_date_time': 'messageDateTime',
            'message_text': 'messageText'
        }

        self._activity_id = activity_id
        self._activity_participant_id = activity_participant_id
        self._id = id
        self._message_date_time = message_date_time
        self._message_text = message_text


    @property
    def activity_id(self):
        """
        Gets the activity_id of this ActivityMessageDTO.


        :return: The activity_id of this ActivityMessageDTO.
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """
        Sets the activity_id of this ActivityMessageDTO.


        :param activity_id: The activity_id of this ActivityMessageDTO.
        :type: int
        """

        self._activity_id = activity_id

    @property
    def activity_participant_id(self):
        """
        Gets the activity_participant_id of this ActivityMessageDTO.


        :return: The activity_participant_id of this ActivityMessageDTO.
        :rtype: int
        """
        return self._activity_participant_id

    @activity_participant_id.setter
    def activity_participant_id(self, activity_participant_id):
        """
        Sets the activity_participant_id of this ActivityMessageDTO.


        :param activity_participant_id: The activity_participant_id of this ActivityMessageDTO.
        :type: int
        """

        self._activity_participant_id = activity_participant_id

    @property
    def id(self):
        """
        Gets the id of this ActivityMessageDTO.


        :return: The id of this ActivityMessageDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ActivityMessageDTO.


        :param id: The id of this ActivityMessageDTO.
        :type: int
        """

        self._id = id

    @property
    def message_date_time(self):
        """
        Gets the message_date_time of this ActivityMessageDTO.


        :return: The message_date_time of this ActivityMessageDTO.
        :rtype: datetime
        """
        return self._message_date_time

    @message_date_time.setter
    def message_date_time(self, message_date_time):
        """
        Sets the message_date_time of this ActivityMessageDTO.


        :param message_date_time: The message_date_time of this ActivityMessageDTO.
        :type: datetime
        """

        self._message_date_time = message_date_time

    @property
    def message_text(self):
        """
        Gets the message_text of this ActivityMessageDTO.


        :return: The message_text of this ActivityMessageDTO.
        :rtype: str
        """
        return self._message_text

    @message_text.setter
    def message_text(self, message_text):
        """
        Sets the message_text of this ActivityMessageDTO.


        :param message_text: The message_text of this ActivityMessageDTO.
        :type: str
        """

        self._message_text = message_text

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
