# WSApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**html_renderings** | [**list[WSHtmlRendering]**](WSHtmlRendering.md) |  | [optional] 
**titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**nature_types** | [**list[WSClassification]**](WSClassification.md) |  | [optional] 
**statuses** | [**list[WSApplicationStatus]**](WSApplicationStatus.md) | Not available when the Award Management module is enabled | [optional] 
**short_titles** | [**list[WSLocalizedString]**](WSLocalizedString.md) |  | [optional] 
**acronym** | **str** |  | [optional] 
**descriptions** | [**list[WSClassifiedLocalizedValue]**](WSClassifiedLocalizedValue.md) |  | [optional] 
**classified_sources** | [**list[WSClassifiedValue]**](WSClassifiedValue.md) |  | [optional] 
**funding_opportunity** | [**WSFundingOpportunityRef**](WSFundingOpportunityRef.md) | Not available when the Award Management module is disabled | [optional] 
**applicants** | [**list[WSClassifiedApplicantAssociation]**](WSClassifiedApplicantAssociation.md) |  | [optional] 
**documents** | [**list[WSApplicationDocument]**](WSApplicationDocument.md) |  | [optional] 
**budget_difference** | **float** |  | [optional] 
**organisations** | [**list[WSOrganisationRef]**](WSOrganisationRef.md) |  | [optional] 
**external_organisations** | [**list[WSExternalOrganisationRef]**](WSExternalOrganisationRef.md) |  | [optional] 
**managing_organisational_unit** | [**WSOrganisationRef**](WSOrganisationRef.md) |  | [optional] 
**collaborative** | **bool** |  | [optional] [default to False]
**collaborators** | [**list[WSCollaboratorAssociation]**](WSCollaboratorAssociation.md) |  | [optional] 
**total_academic_ownership_percentage** | **float** |  | [optional] 
**fundings** | [**list[WSApplicationFundingAssociation]**](WSApplicationFundingAssociation.md) |  | [optional] 
**total_applied_amount** | **float** |  | [optional] 
**expected_period** | [**WSDateRange**](WSDateRange.md) |  | [optional] 
**related_project** | [**WSUPMProjectRef**](WSUPMProjectRef.md) |  | [optional] 
**related_applications** | [**list[WSApplicationRef]**](WSApplicationRef.md) |  | [optional] 
**related_awards** | [**list[WSAwardRef]**](WSAwardRef.md) |  | [optional] 
**related_ethical_reviews** | [**list[WSEthicalReviewRef]**](WSEthicalReviewRef.md) | Only available when the Award Management module is enabled | [optional] 
**field_of_research_associations** | [**list[WSERA2015FieldOfResearchAssociation]**](WSERA2015FieldOfResearchAssociation.md) | Only available when the ERA module is enabled | [optional] 
**keyword_groups** | [**list[WSKeywordGroup]**](WSKeywordGroup.md) |  | [optional] 
**visibilities** | [**list[WSVisibility]**](WSVisibility.md) |  | [optional] 
**confidential** | **bool** |  | [optional] [default to False]
**workflows** | [**list[WSWorkflow]**](WSWorkflow.md) |  | [optional] 
**externalable_info** | [**WSExternalableInformation**](WSExternalableInformation.md) |  | [optional] 
**info** | [**WSContentInformation**](WSContentInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


