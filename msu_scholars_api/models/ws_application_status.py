# coding: utf-8

"""
    PURE API 510

    This is the Pure Web Service. Listed below are all available endpoints, along with a short description.<br/>In order to use the Pure Web Service, you must enter an API key. These are generated in the Administrator tab of Pure, and issues with a given set of available endpoints.<br/>To enter your API key and begin your use, press the Authorize button to at the top of the page. You are then presented with two options for entering the API key: the first option is to use the API key in query format, and the second option is to use the API key in a header.<br/> For further documentation, see <a href=\"documentation/Default.htm\">API Documentation</a>.<br/>A new version of the API is released with each major version of Pure, and remains available for one year. This version is no longer available in Pure 5.14<br/>The old web service is deprecated, but still available <a href=\"../../../doc/\">here</a>, and it will no longer be available in Pure 5.13

    OpenAPI spec version: 510
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WSApplicationStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'statuses': 'list[WSClassification]',
        'date': 'datetime',
        'documents': 'list[WSDocument]'
    }

    attribute_map = {
        'statuses': 'statuses',
        'date': 'date',
        'documents': 'documents'
    }

    def __init__(self, statuses=None, date=None, documents=None):
        """
        WSApplicationStatus - a model defined in Swagger
        """

        self._statuses = None
        self._date = None
        self._documents = None

        if statuses is not None:
          self.statuses = statuses
        if date is not None:
          self.date = date
        if documents is not None:
          self.documents = documents

    @property
    def statuses(self):
        """
        Gets the statuses of this WSApplicationStatus.

        :return: The statuses of this WSApplicationStatus.
        :rtype: list[WSClassification]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """
        Sets the statuses of this WSApplicationStatus.

        :param statuses: The statuses of this WSApplicationStatus.
        :type: list[WSClassification]
        """

        self._statuses = statuses

    @property
    def date(self):
        """
        Gets the date of this WSApplicationStatus.

        :return: The date of this WSApplicationStatus.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this WSApplicationStatus.

        :param date: The date of this WSApplicationStatus.
        :type: datetime
        """

        self._date = date

    @property
    def documents(self):
        """
        Gets the documents of this WSApplicationStatus.

        :return: The documents of this WSApplicationStatus.
        :rtype: list[WSDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this WSApplicationStatus.

        :param documents: The documents of this WSApplicationStatus.
        :type: list[WSDocument]
        """

        self._documents = documents

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
        if not isinstance(other, WSApplicationStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
