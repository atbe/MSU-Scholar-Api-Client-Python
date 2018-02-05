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


class WSLocalizedString(object):
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
        'locale': 'str',
        'formatted': 'bool',
        'value': 'str'
    }

    attribute_map = {
        'locale': 'locale',
        'formatted': 'formatted',
        'value': 'value'
    }

    def __init__(self, locale=None, formatted=False, value=None):
        """
        WSLocalizedString - a model defined in Swagger
        """

        self._locale = None
        self._formatted = None
        self._value = None

        if locale is not None:
          self.locale = locale
        if formatted is not None:
          self.formatted = formatted
        if value is not None:
          self.value = value

    @property
    def locale(self):
        """
        Gets the locale of this WSLocalizedString.

        :return: The locale of this WSLocalizedString.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this WSLocalizedString.

        :param locale: The locale of this WSLocalizedString.
        :type: str
        """

        self._locale = locale

    @property
    def formatted(self):
        """
        Gets the formatted of this WSLocalizedString.

        :return: The formatted of this WSLocalizedString.
        :rtype: bool
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted):
        """
        Sets the formatted of this WSLocalizedString.

        :param formatted: The formatted of this WSLocalizedString.
        :type: bool
        """

        self._formatted = formatted

    @property
    def value(self):
        """
        Gets the value of this WSLocalizedString.

        :return: The value of this WSLocalizedString.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this WSLocalizedString.

        :param value: The value of this WSLocalizedString.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, WSLocalizedString):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
