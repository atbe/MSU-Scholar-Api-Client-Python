# WSStaffOrganisationAssociation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**person** | [**WSPersonRef**](WSPersonRef.md) |  | [optional] 
**affiliation_id** | **str** |  | [optional] 
**addresses** | [**list[WSClassifiedAddress]**](WSClassifiedAddress.md) |  | [optional] 
**emails** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**phone_numbers** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**employment_type** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**web_addresses** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**organisational_unit** | [**WSOrganisationRef**](WSOrganisationRef.md) |  | [optional] 
**period** | [**WSDateRange**](WSDateRange.md) |  | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**contract_types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**staff_types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**job_descriptions** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**job_titles** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**fte** | **float** |  | [optional] 
**primary_association** | **bool** |  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


