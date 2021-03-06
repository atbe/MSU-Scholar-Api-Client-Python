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


class WSStudentOrganisationAssociation(object):
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
        'fte': 'float',
        'start_year': 'str',
        'student_type_descriptions': 'list[WSClassification]',
        'programme': 'str',
        'expected_study_duration': 'int',
        'min_study_duration': 'int',
        'max_study_duration': 'int',
        'programme_year': 'str',
        'initial_submissions_date': 'datetime',
        'expected_end_date': 'datetime',
        'nationalities': 'list[WSClassification]',
        'student_residency_flags': 'list[WSResidencyFlag]',
        'country_of_domiciles': 'list[WSClassification]',
        'award_gained': 'str',
        'project_titles': 'list[WSLocalizedString]',
        'award_date': 'datetime',
        'statuses': 'list[WSClassification]',
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
        'fte': 'fte',
        'start_year': 'startYear',
        'student_type_descriptions': 'studentTypeDescriptions',
        'programme': 'programme',
        'expected_study_duration': 'expectedStudyDuration',
        'min_study_duration': 'minStudyDuration',
        'max_study_duration': 'maxStudyDuration',
        'programme_year': 'programmeYear',
        'initial_submissions_date': 'initialSubmissionsDate',
        'expected_end_date': 'expectedEndDate',
        'nationalities': 'nationalities',
        'student_residency_flags': 'studentResidencyFlags',
        'country_of_domiciles': 'countryOfDomiciles',
        'award_gained': 'awardGained',
        'project_titles': 'projectTitles',
        'award_date': 'awardDate',
        'statuses': 'statuses',
        'primary_association': 'primaryAssociation'
    }

    def __init__(self, id=None, person=None, affiliation_id=None, addresses=None, emails=None, phone_numbers=None, employment_types=None, web_addresses=None, organisation=None, period=None, keyword_groups=None, fte=None, start_year=None, student_type_descriptions=None, programme=None, expected_study_duration=None, min_study_duration=None, max_study_duration=None, programme_year=None, initial_submissions_date=None, expected_end_date=None, nationalities=None, student_residency_flags=None, country_of_domiciles=None, award_gained=None, project_titles=None, award_date=None, statuses=None, primary_association=False):
        """
        WSStudentOrganisationAssociation - a model defined in Swagger
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
        self._fte = None
        self._start_year = None
        self._student_type_descriptions = None
        self._programme = None
        self._expected_study_duration = None
        self._min_study_duration = None
        self._max_study_duration = None
        self._programme_year = None
        self._initial_submissions_date = None
        self._expected_end_date = None
        self._nationalities = None
        self._student_residency_flags = None
        self._country_of_domiciles = None
        self._award_gained = None
        self._project_titles = None
        self._award_date = None
        self._statuses = None
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
        if fte is not None:
          self.fte = fte
        if start_year is not None:
          self.start_year = start_year
        if student_type_descriptions is not None:
          self.student_type_descriptions = student_type_descriptions
        if programme is not None:
          self.programme = programme
        if expected_study_duration is not None:
          self.expected_study_duration = expected_study_duration
        if min_study_duration is not None:
          self.min_study_duration = min_study_duration
        if max_study_duration is not None:
          self.max_study_duration = max_study_duration
        if programme_year is not None:
          self.programme_year = programme_year
        if initial_submissions_date is not None:
          self.initial_submissions_date = initial_submissions_date
        if expected_end_date is not None:
          self.expected_end_date = expected_end_date
        if nationalities is not None:
          self.nationalities = nationalities
        if student_residency_flags is not None:
          self.student_residency_flags = student_residency_flags
        if country_of_domiciles is not None:
          self.country_of_domiciles = country_of_domiciles
        if award_gained is not None:
          self.award_gained = award_gained
        if project_titles is not None:
          self.project_titles = project_titles
        if award_date is not None:
          self.award_date = award_date
        if statuses is not None:
          self.statuses = statuses
        if primary_association is not None:
          self.primary_association = primary_association

    @property
    def id(self):
        """
        Gets the id of this WSStudentOrganisationAssociation.

        :return: The id of this WSStudentOrganisationAssociation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WSStudentOrganisationAssociation.

        :param id: The id of this WSStudentOrganisationAssociation.
        :type: int
        """

        self._id = id

    @property
    def person(self):
        """
        Gets the person of this WSStudentOrganisationAssociation.

        :return: The person of this WSStudentOrganisationAssociation.
        :rtype: WSPersonRef
        """
        return self._person

    @person.setter
    def person(self, person):
        """
        Sets the person of this WSStudentOrganisationAssociation.

        :param person: The person of this WSStudentOrganisationAssociation.
        :type: WSPersonRef
        """

        self._person = person

    @property
    def affiliation_id(self):
        """
        Gets the affiliation_id of this WSStudentOrganisationAssociation.

        :return: The affiliation_id of this WSStudentOrganisationAssociation.
        :rtype: str
        """
        return self._affiliation_id

    @affiliation_id.setter
    def affiliation_id(self, affiliation_id):
        """
        Sets the affiliation_id of this WSStudentOrganisationAssociation.

        :param affiliation_id: The affiliation_id of this WSStudentOrganisationAssociation.
        :type: str
        """

        self._affiliation_id = affiliation_id

    @property
    def addresses(self):
        """
        Gets the addresses of this WSStudentOrganisationAssociation.

        :return: The addresses of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassifiedAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this WSStudentOrganisationAssociation.

        :param addresses: The addresses of this WSStudentOrganisationAssociation.
        :type: list[WSClassifiedAddress]
        """

        self._addresses = addresses

    @property
    def emails(self):
        """
        Gets the emails of this WSStudentOrganisationAssociation.

        :return: The emails of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassifiedValue]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this WSStudentOrganisationAssociation.

        :param emails: The emails of this WSStudentOrganisationAssociation.
        :type: list[WSClassifiedValue]
        """

        self._emails = emails

    @property
    def phone_numbers(self):
        """
        Gets the phone_numbers of this WSStudentOrganisationAssociation.

        :return: The phone_numbers of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassifiedValue]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """
        Sets the phone_numbers of this WSStudentOrganisationAssociation.

        :param phone_numbers: The phone_numbers of this WSStudentOrganisationAssociation.
        :type: list[WSClassifiedValue]
        """

        self._phone_numbers = phone_numbers

    @property
    def employment_types(self):
        """
        Gets the employment_types of this WSStudentOrganisationAssociation.

        :return: The employment_types of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassification]
        """
        return self._employment_types

    @employment_types.setter
    def employment_types(self, employment_types):
        """
        Sets the employment_types of this WSStudentOrganisationAssociation.

        :param employment_types: The employment_types of this WSStudentOrganisationAssociation.
        :type: list[WSClassification]
        """

        self._employment_types = employment_types

    @property
    def web_addresses(self):
        """
        Gets the web_addresses of this WSStudentOrganisationAssociation.

        :return: The web_addresses of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassifiedLocalizedValue]
        """
        return self._web_addresses

    @web_addresses.setter
    def web_addresses(self, web_addresses):
        """
        Sets the web_addresses of this WSStudentOrganisationAssociation.

        :param web_addresses: The web_addresses of this WSStudentOrganisationAssociation.
        :type: list[WSClassifiedLocalizedValue]
        """

        self._web_addresses = web_addresses

    @property
    def organisation(self):
        """
        Gets the organisation of this WSStudentOrganisationAssociation.

        :return: The organisation of this WSStudentOrganisationAssociation.
        :rtype: WSOrganisationRef
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """
        Sets the organisation of this WSStudentOrganisationAssociation.

        :param organisation: The organisation of this WSStudentOrganisationAssociation.
        :type: WSOrganisationRef
        """

        self._organisation = organisation

    @property
    def period(self):
        """
        Gets the period of this WSStudentOrganisationAssociation.

        :return: The period of this WSStudentOrganisationAssociation.
        :rtype: WSDateRange
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this WSStudentOrganisationAssociation.

        :param period: The period of this WSStudentOrganisationAssociation.
        :type: WSDateRange
        """

        self._period = period

    @property
    def keyword_groups(self):
        """
        Gets the keyword_groups of this WSStudentOrganisationAssociation.

        :return: The keyword_groups of this WSStudentOrganisationAssociation.
        :rtype: list[WSKeywordGroup]
        """
        return self._keyword_groups

    @keyword_groups.setter
    def keyword_groups(self, keyword_groups):
        """
        Sets the keyword_groups of this WSStudentOrganisationAssociation.

        :param keyword_groups: The keyword_groups of this WSStudentOrganisationAssociation.
        :type: list[WSKeywordGroup]
        """

        self._keyword_groups = keyword_groups

    @property
    def fte(self):
        """
        Gets the fte of this WSStudentOrganisationAssociation.

        :return: The fte of this WSStudentOrganisationAssociation.
        :rtype: float
        """
        return self._fte

    @fte.setter
    def fte(self, fte):
        """
        Sets the fte of this WSStudentOrganisationAssociation.

        :param fte: The fte of this WSStudentOrganisationAssociation.
        :type: float
        """

        self._fte = fte

    @property
    def start_year(self):
        """
        Gets the start_year of this WSStudentOrganisationAssociation.

        :return: The start_year of this WSStudentOrganisationAssociation.
        :rtype: str
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """
        Sets the start_year of this WSStudentOrganisationAssociation.

        :param start_year: The start_year of this WSStudentOrganisationAssociation.
        :type: str
        """

        self._start_year = start_year

    @property
    def student_type_descriptions(self):
        """
        Gets the student_type_descriptions of this WSStudentOrganisationAssociation.

        :return: The student_type_descriptions of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassification]
        """
        return self._student_type_descriptions

    @student_type_descriptions.setter
    def student_type_descriptions(self, student_type_descriptions):
        """
        Sets the student_type_descriptions of this WSStudentOrganisationAssociation.

        :param student_type_descriptions: The student_type_descriptions of this WSStudentOrganisationAssociation.
        :type: list[WSClassification]
        """

        self._student_type_descriptions = student_type_descriptions

    @property
    def programme(self):
        """
        Gets the programme of this WSStudentOrganisationAssociation.

        :return: The programme of this WSStudentOrganisationAssociation.
        :rtype: str
        """
        return self._programme

    @programme.setter
    def programme(self, programme):
        """
        Sets the programme of this WSStudentOrganisationAssociation.

        :param programme: The programme of this WSStudentOrganisationAssociation.
        :type: str
        """

        self._programme = programme

    @property
    def expected_study_duration(self):
        """
        Gets the expected_study_duration of this WSStudentOrganisationAssociation.

        :return: The expected_study_duration of this WSStudentOrganisationAssociation.
        :rtype: int
        """
        return self._expected_study_duration

    @expected_study_duration.setter
    def expected_study_duration(self, expected_study_duration):
        """
        Sets the expected_study_duration of this WSStudentOrganisationAssociation.

        :param expected_study_duration: The expected_study_duration of this WSStudentOrganisationAssociation.
        :type: int
        """

        self._expected_study_duration = expected_study_duration

    @property
    def min_study_duration(self):
        """
        Gets the min_study_duration of this WSStudentOrganisationAssociation.

        :return: The min_study_duration of this WSStudentOrganisationAssociation.
        :rtype: int
        """
        return self._min_study_duration

    @min_study_duration.setter
    def min_study_duration(self, min_study_duration):
        """
        Sets the min_study_duration of this WSStudentOrganisationAssociation.

        :param min_study_duration: The min_study_duration of this WSStudentOrganisationAssociation.
        :type: int
        """

        self._min_study_duration = min_study_duration

    @property
    def max_study_duration(self):
        """
        Gets the max_study_duration of this WSStudentOrganisationAssociation.

        :return: The max_study_duration of this WSStudentOrganisationAssociation.
        :rtype: int
        """
        return self._max_study_duration

    @max_study_duration.setter
    def max_study_duration(self, max_study_duration):
        """
        Sets the max_study_duration of this WSStudentOrganisationAssociation.

        :param max_study_duration: The max_study_duration of this WSStudentOrganisationAssociation.
        :type: int
        """

        self._max_study_duration = max_study_duration

    @property
    def programme_year(self):
        """
        Gets the programme_year of this WSStudentOrganisationAssociation.

        :return: The programme_year of this WSStudentOrganisationAssociation.
        :rtype: str
        """
        return self._programme_year

    @programme_year.setter
    def programme_year(self, programme_year):
        """
        Sets the programme_year of this WSStudentOrganisationAssociation.

        :param programme_year: The programme_year of this WSStudentOrganisationAssociation.
        :type: str
        """

        self._programme_year = programme_year

    @property
    def initial_submissions_date(self):
        """
        Gets the initial_submissions_date of this WSStudentOrganisationAssociation.

        :return: The initial_submissions_date of this WSStudentOrganisationAssociation.
        :rtype: datetime
        """
        return self._initial_submissions_date

    @initial_submissions_date.setter
    def initial_submissions_date(self, initial_submissions_date):
        """
        Sets the initial_submissions_date of this WSStudentOrganisationAssociation.

        :param initial_submissions_date: The initial_submissions_date of this WSStudentOrganisationAssociation.
        :type: datetime
        """

        self._initial_submissions_date = initial_submissions_date

    @property
    def expected_end_date(self):
        """
        Gets the expected_end_date of this WSStudentOrganisationAssociation.

        :return: The expected_end_date of this WSStudentOrganisationAssociation.
        :rtype: datetime
        """
        return self._expected_end_date

    @expected_end_date.setter
    def expected_end_date(self, expected_end_date):
        """
        Sets the expected_end_date of this WSStudentOrganisationAssociation.

        :param expected_end_date: The expected_end_date of this WSStudentOrganisationAssociation.
        :type: datetime
        """

        self._expected_end_date = expected_end_date

    @property
    def nationalities(self):
        """
        Gets the nationalities of this WSStudentOrganisationAssociation.

        :return: The nationalities of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassification]
        """
        return self._nationalities

    @nationalities.setter
    def nationalities(self, nationalities):
        """
        Sets the nationalities of this WSStudentOrganisationAssociation.

        :param nationalities: The nationalities of this WSStudentOrganisationAssociation.
        :type: list[WSClassification]
        """

        self._nationalities = nationalities

    @property
    def student_residency_flags(self):
        """
        Gets the student_residency_flags of this WSStudentOrganisationAssociation.

        :return: The student_residency_flags of this WSStudentOrganisationAssociation.
        :rtype: list[WSResidencyFlag]
        """
        return self._student_residency_flags

    @student_residency_flags.setter
    def student_residency_flags(self, student_residency_flags):
        """
        Sets the student_residency_flags of this WSStudentOrganisationAssociation.

        :param student_residency_flags: The student_residency_flags of this WSStudentOrganisationAssociation.
        :type: list[WSResidencyFlag]
        """

        self._student_residency_flags = student_residency_flags

    @property
    def country_of_domiciles(self):
        """
        Gets the country_of_domiciles of this WSStudentOrganisationAssociation.

        :return: The country_of_domiciles of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassification]
        """
        return self._country_of_domiciles

    @country_of_domiciles.setter
    def country_of_domiciles(self, country_of_domiciles):
        """
        Sets the country_of_domiciles of this WSStudentOrganisationAssociation.

        :param country_of_domiciles: The country_of_domiciles of this WSStudentOrganisationAssociation.
        :type: list[WSClassification]
        """

        self._country_of_domiciles = country_of_domiciles

    @property
    def award_gained(self):
        """
        Gets the award_gained of this WSStudentOrganisationAssociation.

        :return: The award_gained of this WSStudentOrganisationAssociation.
        :rtype: str
        """
        return self._award_gained

    @award_gained.setter
    def award_gained(self, award_gained):
        """
        Sets the award_gained of this WSStudentOrganisationAssociation.

        :param award_gained: The award_gained of this WSStudentOrganisationAssociation.
        :type: str
        """

        self._award_gained = award_gained

    @property
    def project_titles(self):
        """
        Gets the project_titles of this WSStudentOrganisationAssociation.

        :return: The project_titles of this WSStudentOrganisationAssociation.
        :rtype: list[WSLocalizedString]
        """
        return self._project_titles

    @project_titles.setter
    def project_titles(self, project_titles):
        """
        Sets the project_titles of this WSStudentOrganisationAssociation.

        :param project_titles: The project_titles of this WSStudentOrganisationAssociation.
        :type: list[WSLocalizedString]
        """

        self._project_titles = project_titles

    @property
    def award_date(self):
        """
        Gets the award_date of this WSStudentOrganisationAssociation.

        :return: The award_date of this WSStudentOrganisationAssociation.
        :rtype: datetime
        """
        return self._award_date

    @award_date.setter
    def award_date(self, award_date):
        """
        Sets the award_date of this WSStudentOrganisationAssociation.

        :param award_date: The award_date of this WSStudentOrganisationAssociation.
        :type: datetime
        """

        self._award_date = award_date

    @property
    def statuses(self):
        """
        Gets the statuses of this WSStudentOrganisationAssociation.

        :return: The statuses of this WSStudentOrganisationAssociation.
        :rtype: list[WSClassification]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """
        Sets the statuses of this WSStudentOrganisationAssociation.

        :param statuses: The statuses of this WSStudentOrganisationAssociation.
        :type: list[WSClassification]
        """

        self._statuses = statuses

    @property
    def primary_association(self):
        """
        Gets the primary_association of this WSStudentOrganisationAssociation.

        :return: The primary_association of this WSStudentOrganisationAssociation.
        :rtype: bool
        """
        return self._primary_association

    @primary_association.setter
    def primary_association(self, primary_association):
        """
        Sets the primary_association of this WSStudentOrganisationAssociation.

        :param primary_association: The primary_association of this WSStudentOrganisationAssociation.
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
        if not isinstance(other, WSStudentOrganisationAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
