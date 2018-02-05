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


class WSPersonSupervisorAssociation(object):
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
        'id': 'int',
        'supervisor': 'WSPersonRef',
        'external_supervisor': 'WSExternalPersonRef',
        'supervision_percentage': 'int',
        'period': 'WSDateRange',
        'supervisor_roles': 'list[WSClassification]',
        'student': 'WSPersonOrganisationAssociation'
    }

    attribute_map = {
        'id': 'id',
        'supervisor': 'supervisor',
        'external_supervisor': 'externalSupervisor',
        'supervision_percentage': 'supervisionPercentage',
        'period': 'period',
        'supervisor_roles': 'supervisorRoles',
        'student': 'student'
    }

    def __init__(self, id=None, supervisor=None, external_supervisor=None, supervision_percentage=None, period=None, supervisor_roles=None, student=None):
        """
        WSPersonSupervisorAssociation - a model defined in Swagger
        """

        self._id = None
        self._supervisor = None
        self._external_supervisor = None
        self._supervision_percentage = None
        self._period = None
        self._supervisor_roles = None
        self._student = None

        if id is not None:
          self.id = id
        if supervisor is not None:
          self.supervisor = supervisor
        if external_supervisor is not None:
          self.external_supervisor = external_supervisor
        if supervision_percentage is not None:
          self.supervision_percentage = supervision_percentage
        if period is not None:
          self.period = period
        if supervisor_roles is not None:
          self.supervisor_roles = supervisor_roles
        if student is not None:
          self.student = student

    @property
    def id(self):
        """
        Gets the id of this WSPersonSupervisorAssociation.

        :return: The id of this WSPersonSupervisorAssociation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WSPersonSupervisorAssociation.

        :param id: The id of this WSPersonSupervisorAssociation.
        :type: int
        """

        self._id = id

    @property
    def supervisor(self):
        """
        Gets the supervisor of this WSPersonSupervisorAssociation.

        :return: The supervisor of this WSPersonSupervisorAssociation.
        :rtype: WSPersonRef
        """
        return self._supervisor

    @supervisor.setter
    def supervisor(self, supervisor):
        """
        Sets the supervisor of this WSPersonSupervisorAssociation.

        :param supervisor: The supervisor of this WSPersonSupervisorAssociation.
        :type: WSPersonRef
        """

        self._supervisor = supervisor

    @property
    def external_supervisor(self):
        """
        Gets the external_supervisor of this WSPersonSupervisorAssociation.

        :return: The external_supervisor of this WSPersonSupervisorAssociation.
        :rtype: WSExternalPersonRef
        """
        return self._external_supervisor

    @external_supervisor.setter
    def external_supervisor(self, external_supervisor):
        """
        Sets the external_supervisor of this WSPersonSupervisorAssociation.

        :param external_supervisor: The external_supervisor of this WSPersonSupervisorAssociation.
        :type: WSExternalPersonRef
        """

        self._external_supervisor = external_supervisor

    @property
    def supervision_percentage(self):
        """
        Gets the supervision_percentage of this WSPersonSupervisorAssociation.

        :return: The supervision_percentage of this WSPersonSupervisorAssociation.
        :rtype: int
        """
        return self._supervision_percentage

    @supervision_percentage.setter
    def supervision_percentage(self, supervision_percentage):
        """
        Sets the supervision_percentage of this WSPersonSupervisorAssociation.

        :param supervision_percentage: The supervision_percentage of this WSPersonSupervisorAssociation.
        :type: int
        """

        self._supervision_percentage = supervision_percentage

    @property
    def period(self):
        """
        Gets the period of this WSPersonSupervisorAssociation.

        :return: The period of this WSPersonSupervisorAssociation.
        :rtype: WSDateRange
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this WSPersonSupervisorAssociation.

        :param period: The period of this WSPersonSupervisorAssociation.
        :type: WSDateRange
        """

        self._period = period

    @property
    def supervisor_roles(self):
        """
        Gets the supervisor_roles of this WSPersonSupervisorAssociation.

        :return: The supervisor_roles of this WSPersonSupervisorAssociation.
        :rtype: list[WSClassification]
        """
        return self._supervisor_roles

    @supervisor_roles.setter
    def supervisor_roles(self, supervisor_roles):
        """
        Sets the supervisor_roles of this WSPersonSupervisorAssociation.

        :param supervisor_roles: The supervisor_roles of this WSPersonSupervisorAssociation.
        :type: list[WSClassification]
        """

        self._supervisor_roles = supervisor_roles

    @property
    def student(self):
        """
        Gets the student of this WSPersonSupervisorAssociation.

        :return: The student of this WSPersonSupervisorAssociation.
        :rtype: WSPersonOrganisationAssociation
        """
        return self._student

    @student.setter
    def student(self, student):
        """
        Sets the student of this WSPersonSupervisorAssociation.

        :param student: The student of this WSPersonSupervisorAssociation.
        :type: WSPersonOrganisationAssociation
        """

        self._student = student

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
        if not isinstance(other, WSPersonSupervisorAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
