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


class WSPrizeListResult(object):
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
        'count': 'int',
        'navigation_links': 'list[WSNavigationLink]',
        'items': 'list[WSPrize]'
    }

    attribute_map = {
        'count': 'count',
        'navigation_links': 'navigationLinks',
        'items': 'items'
    }

    def __init__(self, count=None, navigation_links=None, items=None):
        """
        WSPrizeListResult - a model defined in Swagger
        """

        self._count = None
        self._navigation_links = None
        self._items = None

        if count is not None:
          self.count = count
        if navigation_links is not None:
          self.navigation_links = navigation_links
        if items is not None:
          self.items = items

    @property
    def count(self):
        """
        Gets the count of this WSPrizeListResult.

        :return: The count of this WSPrizeListResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this WSPrizeListResult.

        :param count: The count of this WSPrizeListResult.
        :type: int
        """

        self._count = count

    @property
    def navigation_links(self):
        """
        Gets the navigation_links of this WSPrizeListResult.

        :return: The navigation_links of this WSPrizeListResult.
        :rtype: list[WSNavigationLink]
        """
        return self._navigation_links

    @navigation_links.setter
    def navigation_links(self, navigation_links):
        """
        Sets the navigation_links of this WSPrizeListResult.

        :param navigation_links: The navigation_links of this WSPrizeListResult.
        :type: list[WSNavigationLink]
        """

        self._navigation_links = navigation_links

    @property
    def items(self):
        """
        Gets the items of this WSPrizeListResult.

        :return: The items of this WSPrizeListResult.
        :rtype: list[WSPrize]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this WSPrizeListResult.

        :param items: The items of this WSPrizeListResult.
        :type: list[WSPrize]
        """

        self._items = items

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
        if not isinstance(other, WSPrizeListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
