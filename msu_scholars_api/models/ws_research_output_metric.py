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


class WSResearchOutputMetric(object):
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
        'value': 'int',
        'year': 'int'
    }

    attribute_map = {
        'value': 'value',
        'year': 'year'
    }

    def __init__(self, value=None, year=None):
        """
        WSResearchOutputMetric - a model defined in Swagger
        """

        self._value = None
        self._year = None

        if value is not None:
          self.value = value
        if year is not None:
          self.year = year

    @property
    def value(self):
        """
        Gets the value of this WSResearchOutputMetric.

        :return: The value of this WSResearchOutputMetric.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this WSResearchOutputMetric.

        :param value: The value of this WSResearchOutputMetric.
        :type: int
        """

        self._value = value

    @property
    def year(self):
        """
        Gets the year of this WSResearchOutputMetric.

        :return: The year of this WSResearchOutputMetric.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Sets the year of this WSResearchOutputMetric.

        :param year: The year of this WSResearchOutputMetric.
        :type: int
        """

        self._year = year

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
        if not isinstance(other, WSResearchOutputMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
