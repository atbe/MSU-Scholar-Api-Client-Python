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


class WSVisitingScholarOrganisationAssociation(object):
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
        'person': 'WSPersonRef',
        'affiliation_id': 'str',
        'addresses': 'list[WSClassifiedAddress]',
        'emails': 'list[WSClassifiedValue]',
        'phone_numbers': 'list[WSClassifiedValue]',
        'employment_types': 'list[WSClassification]',
        'web_addresses': 'list[WSClassifiedLocalizedValue]',
        'organisation': 'WSOrganisationRef',
        'period': 'WSDateRange',
        'keyword_groups': 'list[WSKeywordGroup]',
        'purpose_of_stay': 'str',
        'visitor_from': 'WSExternalOrganisationRef',
        'job_descriptions': 'list[WSLocalizedString]',
        'job_titles': 'list[WSClassification]',
        'primary_association': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'person': 'person',
        'affiliation_id': 'affiliationId',
        'addresses': 'addresses',
        'emails': 'emails',
        'phone_numbers': 'phoneNumbers',
        'employment_types': 'employmentTypes',
        'web_addresses': 'webAddresses',
        'organisation': 'organisation',
        'period': 'period',
        'keyword_groups': 'keywordGroups',
        'purpose_of_stay': 'purposeOfStay',
        'visitor_from': 'visitorFrom',
        'job_descriptions': 'jobDescriptions',
        'job_titles': 'jobTitles',
        'primary_association': 'primaryAssociation'
    }

    def __init__(self, id=None, person=None, affiliation_id=None, addresses=None, emails=None, phone_numbers=None, employment_types=None, web_addresses=None, organisation=None, period=None, keyword_groups=None, purpose_of_stay=None, visitor_from=None, job_descriptions=None, job_titles=None, primary_association=False):
        """
        WSVisitingScholarOrganisationAssociation - a model defined in Swagger
        """

        self._id = None
        self._person = None
        self._affiliation_id = None
        self._addresses = None
        self._emails = None
        self._phone_numbers = None
        self._employment_types = None
        self._web_addresses = None
        self._organisation = None
        self._period = None
        self._keyword_groups = None
        self._purpose_of_stay = None
        self._visitor_from = None
        self._job_descriptions = None
        self._job_titles = None
        self._primary_association = None

        if id is not None:
          self.id = id
        if person is not None:
          self.person = person
        if affiliation_id is not None:
          self.affiliation_id = affiliation_id
        if addresses is not None:
          self.addresses = addresses
        if emails is not None:
          self.emails = emails
        if phone_numbers is not None:
          self.phone_numbers = phone_numbers
        if employment_types is not None:
          self.employment_types = employment_types
        if web_addresses is not None:
          self.web_addresses = web_addresses
        if organisation is not None:
          self.organisation = organisation
        if period is not None:
          self.period = period
        if keyword_groups is not None:
          self.keyword_groups = keyword_groups
        if purpose_of_stay is not None:
          self.purpose_of_stay = purpose_of_stay
        if visitor_from is not None:
          self.visitor_from = visitor_from
        if job_descriptions is not None:
          self.job_descriptions = job_descriptions
        if job_titles is not None:
          self.job_titles = job_titles
        if primary_association is not None:
          self.primary_association = primary_association

    @property
    def id(self):
        """
        Gets the id of this WSVisitingScholarOrganisationAssociation.

        :return: The id of this WSVisitingScholarOrganisationAssociation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WSVisitingScholarOrganisationAssociation.

        :param id: The id of this WSVisitingScholarOrganisationAssociation.
        :type: int
        """

        self._id = id

    @property
    def person(self):
        """
        Gets the person of this WSVisitingScholarOrganisationAssociation.

        :return: The person of this WSVisitingScholarOrganisationAssociation.
        :rtype: WSPersonRef
        """
        return self._person

    @person.setter
    def person(self, person):
        """
        Sets the person of this WSVisitingScholarOrganisationAssociation.

        :param person: The person of this WSVisitingScholarOrganisationAssociation.
        :type: WSPersonRef
        """

        self._person = person

    @property
    def affiliation_id(self):
        """
        Gets the affiliation_id of this WSVisitingScholarOrganisationAssociation.

        :return: The affiliation_id of this WSVisitingScholarOrganisationAssociation.
        :rtype: str
        """
        return self._affiliation_id

    @affiliation_id.setter
    def affiliation_id(self, affiliation_id):
        """
        Sets the affiliation_id of this WSVisitingScholarOrganisationAssociation.

        :param affiliation_id: The affiliation_id of this WSVisitingScholarOrganisationAssociation.
        :type: str
        """

        self._affiliation_id = affiliation_id

    @property
    def addresses(self):
        """
        Gets the addresses of this WSVisitingScholarOrganisationAssociation.

        :return: The addresses of this WSVisitingScholarOrganisationAssociation.
        :rtype: list[WSClassifiedAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this WSVisitingScholarOrganisationAssociation.

        :param addresses: The addresses of this WSVisitingScholarOrganisationAssociation.
        :type: list[WSClassifiedAddress]
        """

        self._addresses = addresses

    @property
    def emails(self):
        """
        Gets the emails of this WSVisitingScholarOrganisationAssociation.

        :return: The emails of this WSVisitingScholarOrganisationAssociation.
        :rtype: list[WSClassifiedValue]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this WSVisitingScholarOrganisationAssociation.

        :param emails: The emails of this WSVisitingScholarOrganisationAssociation.
        :type: list[WSClassifiedValue]
        """

        self._emails = emails

    @property
    def phone_numbers(self):
        """
        Gets the phone_numbers of this WSVisitingScholarOrganisationAssociation.

        :return: The phone_numbers of this WSVisitingScholarOrganisationAssociation.
        :rtype: list[WSClassifiedValue]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """
        Sets the phone_numbers of this WSVisitingScholarOrganisationAssociation.

        :param phone_numbers: The phone_numbers of this WSVisitingScholarOrganisationAssociation.
        :type: list[WSClassifiedValue]
        """

        self._phone_numbers = phone_numbers

    @property
    def employment_types(self):
        """
        Gets the employment_types of this WSVisitingScholarOrganisationAssociation.

        :return: The employment_types of this WSVisitingScholarOrganisationAssociation.
        :rtype: list[WSClassification]
        """
        return self._employment_types

    @employment_types.setter
    def employment_types(self, employment_types):
        """
        Sets the employment_types of this WSVisitingScholarOrganisationAssociation.

        :param employment_types: The employment_types of this WSVisitingScholarOrganisationAssociation.
        :type: list[WSClassification]
        """

        self._employment_types = employment_types

    @property
    def web_addresses(self):
        """
        Gets the web_addresses of this WSVisitingScholarOrganisationAssociation.

        :return: The web_addresses of this WSVisitingScholarOrganisationAssociation.
        :rtype: list[WSClassifiedLocalizedValue]
        """
        return self._web_addresses

    @web_addresses.setter
    def web_addresses(self, web_addresses):
        """
        Sets the web_addresses of this WSVisitingScholarOrganisationAssociation.

        :param web_addresses: The web_addresses of this WSVisitingScholarOrganisationAssociation.
        :type: list[WSClassifiedLocalizedValue]
        """

        self._web_addresses = web_addresses

    @property
    def organisation(self):
        """
        Gets the organisation of this WSVisitingScholarOrganisationAssociation.

        :return: The organisation of this WSVisitingScholarOrganisationAssociation.
        :rtype: WSOrganisationRef
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """
        Sets the organisation of this WSVisitingScholarOrganisationAssociation.

        :param organisation: The organisation of this WSVisitingScholarOrganisationAssociation.
        :type: WSOrganisationRef
        """

        self._organisation = organisation

    @property
    def period(self):
        """
        Gets the period of this WSVisitingScholarOrganisationAssociation.

        :return: The period of this WSVisitingScholarOrganisationAssociation.
        :rtype: WSDateRange
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this WSVisitingScholarOrganisationAssociation.

        :param period: The period of this WSVisitingScholarOrganisationAssociation.
        :type: WSDateRange
        """

        self._period = period

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSVisitingScholarOrganisationAssociation.

        :return: The keyword_groups of this WSVisitingScholarOrganisationAssociation.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSVisitingScholarOrganisationAssociation.

        :param keyword_groups: The keyword_groups of this WSVisitingScholarOrganisationAssociation.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def purpose_of_stay(self):
        """
        Gets the purpose_of_stay of this WSVisitingScholarOrganisationAssociation.

        :return: The purpose_of_stay of this WSVisitingScholarOrganisationAssociation.
        :rtype: str
        """
        return self._purpose_of_stay

    @purpose_of_stay.setter
    def purpose_of_stay(self, purpose_of_stay):
        """
        Sets the purpose_of_stay of this WSVisitingScholarOrganisationAssociation.

        :param purpose_of_stay: The purpose_of_stay of this WSVisitingScholarOrganisationAssociation.
        :type: str
        """

        self._purpose_of_stay = purpose_of_stay

    @property
    def visitor_from(self):
        """
        Gets the visitor_from of this WSVisitingScholarOrganisationAssociation.

        :return: The visitor_from of this WSVisitingScholarOrganisationAssociation.
        :rtype: WSExternalOrganisationRef
        """
        return self._visitor_from

    @visitor_from.setter
    def visitor_from(self, visitor_from):
        """
        Sets the visitor_from of this WSVisitingScholarOrganisationAssociation.

        :param visitor_from: The visitor_from of this WSVisitingScholarOrganisationAssociation.
        :type: WSExternalOrganisationRef
        """

        self._visitor_from = visitor_from

    @property
    def job_descriptions(self):
        """
        Gets the job_descriptions of this WSVisitingScholarOrganisationAssociation.

        :return: The job_descriptions of this WSVisitingScholarOrganisationAssociation.
        :rtype: list[WSLocalizedString]
        """
        return self._job_descriptions

    @job_descriptions.setter
    def job_descriptions(self, job_descriptions):
        """
        Sets the job_descriptions of this WSVisitingScholarOrganisationAssociation.

        :param job_descriptions: The job_descriptions of this WSVisitingScholarOrganisationAssociation.
        :type: list[WSLocalizedString]
        """

        self._job_descriptions = job_descriptions

    @property
    def job_titles(self):
        """
        Gets the job_titles of this WSVisitingScholarOrganisationAssociation.

        :return: The job_titles of this WSVisitingScholarOrganisationAssociation.
        :rtype: list[WSClassification]
        """
        return self._job_titles

    @job_titles.setter
    def job_titles(self, job_titles):
        """
        Sets the job_titles of this WSVisitingScholarOrganisationAssociation.

        :param job_titles: The job_titles of this WSVisitingScholarOrganisationAssociation.
        :type: list[WSClassification]
        """

        self._job_titles = job_titles

    @property
    def primary_association(self):
        """
        Gets the primary_association of this WSVisitingScholarOrganisationAssociation.

        :return: The primary_association of this WSVisitingScholarOrganisationAssociation.
        :rtype: bool
        """
        return self._primary_association

    @primary_association.setter
    def primary_association(self, primary_association):
        """
        Sets the primary_association of this WSVisitingScholarOrganisationAssociation.

        :param primary_association: The primary_association of this WSVisitingScholarOrganisationAssociation.
        :type: bool
        """

        self._primary_association = primary_association

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
        if not isinstance(other, WSVisitingScholarOrganisationAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
