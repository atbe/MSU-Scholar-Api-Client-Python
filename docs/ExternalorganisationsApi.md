# msu_scholars_api.ExternalorganisationsApi

All URIs are relative to *https://localhosthttps://scholars.opb.msu.edu/ws/api/510/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_orderings**](ExternalorganisationsApi.md#get_available_orderings) | **GET** /external-organisations-meta/orderings | Lists available orderings
[**get_available_renderings**](ExternalorganisationsApi.md#get_available_renderings) | **GET** /external-organisations-meta/renderings | Lists available renderings
[**get_external_organisation**](ExternalorganisationsApi.md#get_external_organisation) | **GET** /external-organisations/{id} | Get external organisation
[**list_external_organisations**](ExternalorganisationsApi.md#list_external_organisations) | **GET** /external-organisations | Lists all external organisations
[**list_external_organisations_0**](ExternalorganisationsApi.md#list_external_organisations_0) | **POST** /external-organisations | Complex operation for external organisations


# **get_available_orderings**
> WSOrderingsList get_available_orderings()

Lists available orderings

Lists all orderings available to the external organisation endpoint. These values can be used by the order parameter

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.ExternalorganisationsApi()

try: 
    # Lists available orderings
    api_response = api_instance.get_available_orderings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalorganisationsApi->get_available_orderings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WSOrderingsList**](WSOrderingsList.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_renderings**
> WSRenderingsList get_available_renderings()

Lists available renderings

Lists all renderings available to the external organisation endpoint. These values can be used by the rendering parameter

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.ExternalorganisationsApi()

try: 
    # Lists available renderings
    api_response = api_instance.get_available_renderings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalorganisationsApi->get_available_renderings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WSRenderingsList**](WSRenderingsList.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_organisation**
> WSExternalOrganisation get_external_organisation(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)

Get external organisation

Get external organisation with specific ID (path parameter).

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.ExternalorganisationsApi()
id = 'id_example' # str | Id of the desired external organisation
id_classification = 'id_classification_example' # str | Specifies an optional classification used to specify which type of ID should be used in the match. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)

try: 
    # Get external organisation
    api_response = api_instance.get_external_organisation(id, id_classification=id_classification, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, return_used_content=return_used_content, navigation_link=navigation_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalorganisationsApi->get_external_organisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the desired external organisation | 
 **id_classification** | **str**| Specifies an optional classification used to specify which type of ID should be used in the match. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#idclassification_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSExternalOrganisation**](WSExternalOrganisation.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_organisations**
> WSExternalOrganisationListResult list_external_organisations(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)

Lists all external organisations

Lists all external organisations in the PURE installation. If filtering of the returned external organisations is required, see the POST version which supports additional filtering.

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.ExternalorganisationsApi()
q = 'q_example' # str | Free text search string using Lucene query syntax. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#q_param\">Read more</a> (optional)
order = ['order_example'] # list[str] | Specify the ordering of content in the result. Default: ID ascending. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#order_param\">Read more</a> (optional)
fields = ['fields_example'] # list[str] | Limit the fields included in the response. E.g. 'nameVariants.nameVariant' will only return the name variants. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\">Read more</a> (optional)
locale = ['locale_example'] # list[str] | Enter the desired locale. E.g. 'en_GB' will only return the English text strings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\">Read more</a> (optional)
fallback_locale = ['fallback_locale_example'] # list[str] | Fallback locale string. Syntax is 'Locale1=>Locale2' to map Locale1 to Locale2. Example: 'da_DK=>en_GB'. Locale1 must be equal to locale provided in the locale string. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\">Read more</a> (optional)
rendering = ['rendering_example'] # list[str] | HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\">Read more</a> (optional)
linking_strategy = 'linking_strategy_example' # str | Specifies the linking strategy to use used when creating HTML renderings. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\">Read more</a> (optional)
return_used_content = true # bool | If 'true', the id's of the content used to create HTML renderings are returned as part of the result. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\">Read more</a> (optional)
navigation_link = true # bool | Include navigation links for paging and content. Default: true. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\">Read more</a> (optional)
size = 56 # int | Enter the number of results per window. Default: 10. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
offset = 56 # int | Enter the offset into the total result set where items should be returned from. Default: 0. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\">Read more</a> (optional)
page = 56 # int | Enter the desired page number. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)
page_size = 56 # int | Enter the desired number of results per page. <a href=\"documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\">Read more</a> (optional)

try: 
    # Lists all external organisations
    api_response = api_instance.list_external_organisations(q=q, order=order, fields=fields, locale=locale, fallback_locale=fallback_locale, rendering=rendering, linking_strategy=linking_strategy, return_used_content=return_used_content, navigation_link=navigation_link, size=size, offset=offset, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalorganisationsApi->list_external_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free text search string using Lucene query syntax. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#q_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **order** | [**list[str]**](str.md)| Specify the ordering of content in the result. Default: ID ascending. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#order_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fields** | [**list[str]**](str.md)| Limit the fields included in the response. E.g. &#39;nameVariants.nameVariant&#39; will only return the name variants. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fields_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **locale** | [**list[str]**](str.md)| Enter the desired locale. E.g. &#39;en_GB&#39; will only return the English text strings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#locale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **fallback_locale** | [**list[str]**](str.md)| Fallback locale string. Syntax is &#39;Locale1&#x3D;&gt;Locale2&#39; to map Locale1 to Locale2. Example: &#39;da_DK&#x3D;&gt;en_GB&#39;. Locale1 must be equal to locale provided in the locale string. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#fallbackLocale_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **rendering** | [**list[str]**](str.md)| HTML rendering formats. If rendering formats are specified, the content will be returned in these formats instead of XML. If XML is also wanted, it can be included using the fields parameter. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#rendering_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **linking_strategy** | **str**| Specifies the linking strategy to use used when creating HTML renderings. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#linkingStrategy_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **return_used_content** | **bool**| If &#39;true&#39;, the id&#39;s of the content used to create HTML renderings are returned as part of the result. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#usedContent_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **navigation_link** | **bool**| Include navigation links for paging and content. Default: true. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#navLink_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **size** | **int**| Enter the number of results per window. Default: 10. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **offset** | **int**| Enter the offset into the total result set where items should be returned from. Default: 0. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#size_offset_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page** | **int**| Enter the desired page number. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 
 **page_size** | **int**| Enter the desired number of results per page. &lt;a href&#x3D;\&quot;documentation/Content/Topics/Parameter_Descriptions.htm#page_size_param\&quot;&gt;Read more&lt;/a&gt; | [optional] 

### Return type

[**WSExternalOrganisationListResult**](WSExternalOrganisationListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_external_organisations_0**
> WSExternalOrganisationListResult list_external_organisations_0(body=body)

Complex operation for external organisations

Lists external organisations in the PURE installation, similar to the GET version, instead of using parameters to alter the response, an XML document is posted with the request. The XML document contains fields for all the parameters available for the GET version, but also additional filtering options. For documentation of the XML format see <a href=\"documentation/Content/Topics/CT_ExternalOrganisation.htm#post_xml\">External Organisation documentation</a>

### Example 
```python
from __future__ import print_function
import time
import msu_scholars_api
from msu_scholars_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
msu_scholars_api.configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: apiKey
msu_scholars_api.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# msu_scholars_api.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = msu_scholars_api.ExternalorganisationsApi()
body = msu_scholars_api.WSExternalOrganisationsQuery() # WSExternalOrganisationsQuery |  (optional)

try: 
    # Complex operation for external organisations
    api_response = api_instance.list_external_organisations_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalorganisationsApi->list_external_organisations_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WSExternalOrganisationsQuery**](WSExternalOrganisationsQuery.md)|  | [optional] 

### Return type

[**WSExternalOrganisationListResult**](WSExternalOrganisationListResult.md)

### Authorization

[api-key](../README.md#api-key), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

