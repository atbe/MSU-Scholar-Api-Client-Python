# WSPerson

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**html_renderings** | [**list[WSHtmlRendering]**](WSHtmlRendering.md) |  | [optional] 
**name** | [**WSName**](WSName.md) |  | [optional] 
**genders** | [**list[WSClassification]**](WSClassification.md) | Only available if it is made public | [optional] 
**date_of_birth** | **datetime** | Only available if it is made public | [optional] 
**nationalities** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**name_variants** | [**list[WSClassifiedName]**](WSClassifiedName.md) |  | [optional] 
**titles** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**classified_sources** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**orcid** | **str** |  | [optional] 
**profile_photos** | [**list[WSClassifiedFileRef]**](WSClassifiedFileRef.md) |  | [optional] 
**links** | [**list[WSLink]**](WSLink.md) |  | [optional] 
**start_date_as_researcher** | **datetime** |  | [optional] 
**retirement_date** | **datetime** |  | [optional] 
**profiled** | **bool** | Only available when the Author Profile module is enabled | [optional] [default to False]
**scopus_h_index** | **int** |  | [optional] 
**profile_informations** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**student_organisation_associations** | [**list[WSStudentOrganisationAssociation]**](WSStudentOrganisationAssociation.md) |  | [optional] 
**staff_organisation_associations** | [**list[WSStaffOrganisationAssociation]**](WSStaffOrganisationAssociation.md) |  | [optional] 
**visiting_scholar_organisation_associations** | [**list[WSVisitingScholarOrganisationAssociation]**](WSVisitingScholarOrganisationAssociation.md) |  | [optional] 
**honorary_staff_organisation_associations** | [**list[WSHonoraryStaffOrganisationAssociation]**](WSHonoraryStaffOrganisationAssociation.md) |  | [optional] 
**supervisor_for_relations** | [**list[WSPersonSupervisorAssociation]**](WSPersonSupervisorAssociation.md) |  | [optional] 
**leave_of_absence** | [**WSPersonClassifiedLeaveOfAbsence**](WSPersonClassifiedLeaveOfAbsence.md) | Only available when the proper configuration is enabled | [optional] 
**employee_start_date** | **datetime** |  | [optional] 
**employee_end_date** | **datetime** |  | [optional] 
**fte** | **float** |  | [optional] 
**affiliation_note** | **str** | Only available when the proper configuration is enabled | [optional] 
**external_positions** | [**list[WSPersonExternalPosition]**](WSPersonExternalPosition.md) |  | [optional] 
**educations** | [**list[WSPersonEducation]**](WSPersonEducation.md) |  | [optional] 
**professional_qualifications** | [**list[WSProfessionalQualification]**](WSProfessionalQualification.md) | Only available when the proper configuration is enabled | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**field_of_research_associations** | [**list[WSERA2015FieldOfResearchAssociation]**](WSERA2015FieldOfResearchAssociation.md) | Only available when the ERA module is enabled | [optional] 
**will_take_phd_students** | **bool** | Only available when the proper configuration is enabled | [optional] [default to False]
**phd_research_projects** | **str** | Only available when the proper configuration is enabled | [optional] 
**private_address** | [**WSClassifiedAddress**](WSClassifiedAddress.md) | Only available when the proper configuration is enabled | [optional] 
**visibilities** | [**list[WSVisibility]**](WSVisibility.md) |  | [optional] 
**externalable_info** | [**WSExternalableInformation**](WSExternalableInformation.md) |  | [optional] 
**info** | [**WSContentInformation**](WSContentInformation.md) |  | [optional] 
**expert** | **bool** |  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


