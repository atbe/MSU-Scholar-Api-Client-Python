# WSStudentOrganisationAssociation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**person** | [**WSPersonRef**](WSPersonRef.md) |  | [optional] 
**affiliation_id** | **str** |  | [optional] 
**addresses** | [**list[WSClassifiedAddress]**](WSClassifiedAddress.md) |  | [optional] 
**emails** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**phone_numbers** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**employment_types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**web_addresses** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**organisation** | [**WSOrganisationRef**](WSOrganisationRef.md) |  | [optional] 
**period** | [**WSDateRange**](WSDateRange.md) |  | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**fte** | **float** |  | [optional] 
**start_year** | **str** |  | [optional] 
**student_type_descriptions** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**programme** | **str** |  | [optional] 
**expected_study_duration** | **int** |  | [optional] 
**min_study_duration** | **int** |  | [optional] 
**max_study_duration** | **int** |  | [optional] 
**programme_year** | **str** |  | [optional] 
**initial_submissions_date** | **datetime** |  | [optional] 
**expected_end_date** | **datetime** |  | [optional] 
**nationalities** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**student_residency_flags** | [**list[WSResidencyFlag]**](WSResidencyFlag.md) |  | [optional] 
**country_of_domiciles** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**award_gained** | **str** |  | [optional] 
**project_titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**award_date** | **datetime** |  | [optional] 
**statuses** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**primary_association** | **bool** |  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


