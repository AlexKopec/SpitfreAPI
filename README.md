# swagger_client
spitfire API documentation

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.AccountresourceApi()
key = 'key_example' # str | key

try:
    # activateAccount
    api_response = api_instance.activate_account_using_get(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountresourceApi->activate_account_using_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://127.0.0.1:8000/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountresourceApi* | [**activate_account_using_get**](docs/AccountresourceApi.md#activate_account_using_get) | **GET** /api/activate | activateAccount
*AccountresourceApi* | [**change_password_using_post**](docs/AccountresourceApi.md#change_password_using_post) | **POST** /api/account/change_password | changePassword
*AccountresourceApi* | [**finish_password_reset_using_post**](docs/AccountresourceApi.md#finish_password_reset_using_post) | **POST** /api/account/reset_password/finish | finishPasswordReset
*AccountresourceApi* | [**get_account_using_get**](docs/AccountresourceApi.md#get_account_using_get) | **GET** /api/account | getAccount
*AccountresourceApi* | [**is_authenticated_using_get**](docs/AccountresourceApi.md#is_authenticated_using_get) | **GET** /api/authenticate | isAuthenticated
*AccountresourceApi* | [**register_account_using_post**](docs/AccountresourceApi.md#register_account_using_post) | **POST** /api/register | registerAccount
*AccountresourceApi* | [**request_password_reset_using_post**](docs/AccountresourceApi.md#request_password_reset_using_post) | **POST** /api/account/reset_password/init | requestPasswordReset
*AccountresourceApi* | [**save_account_using_post**](docs/AccountresourceApi.md#save_account_using_post) | **POST** /api/account | saveAccount
*ActivitymessageresourceApi* | [**create_activity_message_using_post**](docs/ActivitymessageresourceApi.md#create_activity_message_using_post) | **POST** /api/activity-messages | createActivityMessage
*ActivitymessageresourceApi* | [**delete_activity_message_using_delete**](docs/ActivitymessageresourceApi.md#delete_activity_message_using_delete) | **DELETE** /api/activity-messages/{id} | deleteActivityMessage
*ActivitymessageresourceApi* | [**get_activity_message_using_get**](docs/ActivitymessageresourceApi.md#get_activity_message_using_get) | **GET** /api/activity-messages/{id} | getActivityMessage
*ActivitymessageresourceApi* | [**get_all_activity_messages_using_get**](docs/ActivitymessageresourceApi.md#get_all_activity_messages_using_get) | **GET** /api/activity-messages | getAllActivityMessages
*ActivitymessageresourceApi* | [**search_activity_messages_using_get**](docs/ActivitymessageresourceApi.md#search_activity_messages_using_get) | **GET** /api/_search/activity-messages | searchActivityMessages
*ActivitymessageresourceApi* | [**update_activity_message_using_put**](docs/ActivitymessageresourceApi.md#update_activity_message_using_put) | **PUT** /api/activity-messages | updateActivityMessage
*ActivityparticipantresourceApi* | [**create_activity_participant_using_post**](docs/ActivityparticipantresourceApi.md#create_activity_participant_using_post) | **POST** /api/activity-participants | createActivityParticipant
*ActivityparticipantresourceApi* | [**delete_activity_participant_using_delete**](docs/ActivityparticipantresourceApi.md#delete_activity_participant_using_delete) | **DELETE** /api/activity-participants/{id} | deleteActivityParticipant
*ActivityparticipantresourceApi* | [**get_activity_participant_using_get**](docs/ActivityparticipantresourceApi.md#get_activity_participant_using_get) | **GET** /api/activity-participants/{id} | getActivityParticipant
*ActivityparticipantresourceApi* | [**get_all_activity_participants_using_get**](docs/ActivityparticipantresourceApi.md#get_all_activity_participants_using_get) | **GET** /api/activity-participants | getAllActivityParticipants
*ActivityparticipantresourceApi* | [**search_activity_participants_using_get**](docs/ActivityparticipantresourceApi.md#search_activity_participants_using_get) | **GET** /api/_search/activity-participants | searchActivityParticipants
*ActivityparticipantresourceApi* | [**update_activity_participant_using_put**](docs/ActivityparticipantresourceApi.md#update_activity_participant_using_put) | **PUT** /api/activity-participants | updateActivityParticipant
*ActivityresourceApi* | [**create_activity_using_post**](docs/ActivityresourceApi.md#create_activity_using_post) | **POST** /api/activities | createActivity
*ActivityresourceApi* | [**delete_activity_using_delete**](docs/ActivityresourceApi.md#delete_activity_using_delete) | **DELETE** /api/activities/{id} | deleteActivity
*ActivityresourceApi* | [**get_activity_using_get**](docs/ActivityresourceApi.md#get_activity_using_get) | **GET** /api/activities/{id} | getActivity
*ActivityresourceApi* | [**get_all_activities_using_get**](docs/ActivityresourceApi.md#get_all_activities_using_get) | **GET** /api/activities | getAllActivities
*ActivityresourceApi* | [**search_activities_using_get**](docs/ActivityresourceApi.md#search_activities_using_get) | **GET** /api/_search/activities | searchActivities
*ActivityresourceApi* | [**update_activity_using_put**](docs/ActivityresourceApi.md#update_activity_using_put) | **PUT** /api/activities | updateActivity
*AddressresourceApi* | [**create_address_using_post**](docs/AddressresourceApi.md#create_address_using_post) | **POST** /api/addresses | createAddress
*AddressresourceApi* | [**delete_address_using_delete**](docs/AddressresourceApi.md#delete_address_using_delete) | **DELETE** /api/addresses/{id} | deleteAddress
*AddressresourceApi* | [**get_address_using_get**](docs/AddressresourceApi.md#get_address_using_get) | **GET** /api/addresses/{id} | getAddress
*AddressresourceApi* | [**get_all_addresses_using_get**](docs/AddressresourceApi.md#get_all_addresses_using_get) | **GET** /api/addresses | getAllAddresses
*AddressresourceApi* | [**update_address_using_put**](docs/AddressresourceApi.md#update_address_using_put) | **PUT** /api/addresses | updateAddress
*CardresourceApi* | [**create_card_using_post**](docs/CardresourceApi.md#create_card_using_post) | **POST** /api/cards | createCard
*CardresourceApi* | [**delete_card_using_delete**](docs/CardresourceApi.md#delete_card_using_delete) | **DELETE** /api/cards/{id} | deleteCard
*CardresourceApi* | [**get_all_cards_using_get**](docs/CardresourceApi.md#get_all_cards_using_get) | **GET** /api/cards | getAllCards
*CardresourceApi* | [**get_card_using_get**](docs/CardresourceApi.md#get_card_using_get) | **GET** /api/cards/{id} | getCard
*CardresourceApi* | [**update_card_using_put**](docs/CardresourceApi.md#update_card_using_put) | **PUT** /api/cards | updateCard
*CompanyresourceApi* | [**create_company_using_post**](docs/CompanyresourceApi.md#create_company_using_post) | **POST** /api/companies | createCompany
*CompanyresourceApi* | [**delete_company_using_delete**](docs/CompanyresourceApi.md#delete_company_using_delete) | **DELETE** /api/companies/{id} | deleteCompany
*CompanyresourceApi* | [**get_all_companies_using_get**](docs/CompanyresourceApi.md#get_all_companies_using_get) | **GET** /api/companies | getAllCompanies
*CompanyresourceApi* | [**get_company_using_get**](docs/CompanyresourceApi.md#get_company_using_get) | **GET** /api/companies/{id} | getCompany
*CompanyresourceApi* | [**search_companies_using_get**](docs/CompanyresourceApi.md#search_companies_using_get) | **GET** /api/_search/companies | searchCompanies
*CompanyresourceApi* | [**update_company_using_put**](docs/CompanyresourceApi.md#update_company_using_put) | **PUT** /api/companies | updateCompany
*ContactinforesourceApi* | [**create_contact_info_using_post**](docs/ContactinforesourceApi.md#create_contact_info_using_post) | **POST** /api/contact-infos | createContactInfo
*ContactinforesourceApi* | [**delete_contact_info_using_delete**](docs/ContactinforesourceApi.md#delete_contact_info_using_delete) | **DELETE** /api/contact-infos/{id} | deleteContactInfo
*ContactinforesourceApi* | [**get_all_contact_infos_using_get**](docs/ContactinforesourceApi.md#get_all_contact_infos_using_get) | **GET** /api/contact-infos | getAllContactInfos
*ContactinforesourceApi* | [**get_contact_info_using_get**](docs/ContactinforesourceApi.md#get_contact_info_using_get) | **GET** /api/contact-infos/{id} | getContactInfo
*ContactinforesourceApi* | [**update_contact_info_using_put**](docs/ContactinforesourceApi.md#update_contact_info_using_put) | **PUT** /api/contact-infos | updateContactInfo
*CustomerresourceApi* | [**create_customer_using_post**](docs/CustomerresourceApi.md#create_customer_using_post) | **POST** /api/customers | createCustomer
*CustomerresourceApi* | [**delete_customer_using_delete**](docs/CustomerresourceApi.md#delete_customer_using_delete) | **DELETE** /api/customers/{id} | deleteCustomer
*CustomerresourceApi* | [**get_all_customers_using_get**](docs/CustomerresourceApi.md#get_all_customers_using_get) | **GET** /api/customers | getAllCustomers
*CustomerresourceApi* | [**get_customer_using_get**](docs/CustomerresourceApi.md#get_customer_using_get) | **GET** /api/customers/{id} | getCustomer
*CustomerresourceApi* | [**update_customer_using_put**](docs/CustomerresourceApi.md#update_customer_using_put) | **PUT** /api/customers | updateCustomer
*FileuploadresourceApi* | [**upload_attached_file_using_post**](docs/FileuploadresourceApi.md#upload_attached_file_using_post) | **POST** /api/attachment/upload | uploadAttachedFile
*FileuploadresourceApi* | [**upload_materials_using_post**](docs/FileuploadresourceApi.md#upload_materials_using_post) | **POST** /api/materials/upload | uploadMaterials
*FileuploadresourceApi* | [**upload_profile_image_using_post**](docs/FileuploadresourceApi.md#upload_profile_image_using_post) | **POST** /api/profileimage/upload | uploadProfileImage
*IndustryresourceApi* | [**create_industry_using_post**](docs/IndustryresourceApi.md#create_industry_using_post) | **POST** /api/industries | createIndustry
*IndustryresourceApi* | [**delete_industry_using_delete**](docs/IndustryresourceApi.md#delete_industry_using_delete) | **DELETE** /api/industries/{id} | deleteIndustry
*IndustryresourceApi* | [**get_all_industries_using_get**](docs/IndustryresourceApi.md#get_all_industries_using_get) | **GET** /api/industries | getAllIndustries
*IndustryresourceApi* | [**get_industry_using_get**](docs/IndustryresourceApi.md#get_industry_using_get) | **GET** /api/industries/{id} | getIndustry
*IndustryresourceApi* | [**update_industry_using_put**](docs/IndustryresourceApi.md#update_industry_using_put) | **PUT** /api/industries | updateIndustry
*LocationresourceApi* | [**create_location_using_post**](docs/LocationresourceApi.md#create_location_using_post) | **POST** /api/locations | createLocation
*LocationresourceApi* | [**delete_location_using_delete**](docs/LocationresourceApi.md#delete_location_using_delete) | **DELETE** /api/locations/{id} | deleteLocation
*LocationresourceApi* | [**get_all_locations_using_get**](docs/LocationresourceApi.md#get_all_locations_using_get) | **GET** /api/locations | getAllLocations
*LocationresourceApi* | [**get_location_using_get**](docs/LocationresourceApi.md#get_location_using_get) | **GET** /api/locations/{id} | getLocation
*LocationresourceApi* | [**update_location_using_put**](docs/LocationresourceApi.md#update_location_using_put) | **PUT** /api/locations | updateLocation
*MarketplaceserviceresourceApi* | [**create_marketplace_service_using_post**](docs/MarketplaceserviceresourceApi.md#create_marketplace_service_using_post) | **POST** /api/marketplace-services | createMarketplaceService
*MarketplaceserviceresourceApi* | [**delete_marketplace_service_using_delete**](docs/MarketplaceserviceresourceApi.md#delete_marketplace_service_using_delete) | **DELETE** /api/marketplace-services/{id} | deleteMarketplaceService
*MarketplaceserviceresourceApi* | [**get_all_marketplace_services_using_get**](docs/MarketplaceserviceresourceApi.md#get_all_marketplace_services_using_get) | **GET** /api/marketplace-services | getAllMarketplaceServices
*MarketplaceserviceresourceApi* | [**get_marketplace_service_using_get**](docs/MarketplaceserviceresourceApi.md#get_marketplace_service_using_get) | **GET** /api/marketplace-services/{id} | getMarketplaceService
*MarketplaceserviceresourceApi* | [**update_marketplace_service_using_put**](docs/MarketplaceserviceresourceApi.md#update_marketplace_service_using_put) | **PUT** /api/marketplace-services | updateMarketplaceService
*MarketplaceuserresourceApi* | [**create_marketplace_user_using_post**](docs/MarketplaceuserresourceApi.md#create_marketplace_user_using_post) | **POST** /api/marketplace-users | createMarketplaceUser
*MarketplaceuserresourceApi* | [**delete_marketplace_user_using_delete**](docs/MarketplaceuserresourceApi.md#delete_marketplace_user_using_delete) | **DELETE** /api/marketplace-users/{id} | deleteMarketplaceUser
*MarketplaceuserresourceApi* | [**get_all_marketplace_users_using_get**](docs/MarketplaceuserresourceApi.md#get_all_marketplace_users_using_get) | **GET** /api/marketplace-users | getAllMarketplaceUsers
*MarketplaceuserresourceApi* | [**get_marketplace_user_using_get**](docs/MarketplaceuserresourceApi.md#get_marketplace_user_using_get) | **GET** /api/marketplace-users/{id} | getMarketplaceUser
*MarketplaceuserresourceApi* | [**update_marketplace_user_using_put**](docs/MarketplaceuserresourceApi.md#update_marketplace_user_using_put) | **PUT** /api/marketplace-users | updateMarketplaceUser
*MaterialattachmentresourceApi* | [**create_material_attachment_using_post**](docs/MaterialattachmentresourceApi.md#create_material_attachment_using_post) | **POST** /api/material-attachments | createMaterialAttachment
*MaterialattachmentresourceApi* | [**delete_material_attachment_using_delete**](docs/MaterialattachmentresourceApi.md#delete_material_attachment_using_delete) | **DELETE** /api/material-attachments/{id} | deleteMaterialAttachment
*MaterialattachmentresourceApi* | [**get_all_material_attachments_using_get**](docs/MaterialattachmentresourceApi.md#get_all_material_attachments_using_get) | **GET** /api/material-attachments | getAllMaterialAttachments
*MaterialattachmentresourceApi* | [**get_material_attachment_using_get**](docs/MaterialattachmentresourceApi.md#get_material_attachment_using_get) | **GET** /api/material-attachments/{id} | getMaterialAttachment
*MaterialattachmentresourceApi* | [**search_material_attachments_using_get**](docs/MaterialattachmentresourceApi.md#search_material_attachments_using_get) | **GET** /api/_search/material-attachments | searchMaterialAttachments
*MaterialattachmentresourceApi* | [**update_material_attachment_using_put**](docs/MaterialattachmentresourceApi.md#update_material_attachment_using_put) | **PUT** /api/material-attachments | updateMaterialAttachment
*MaterialcategoryresourceApi* | [**create_material_category_using_post**](docs/MaterialcategoryresourceApi.md#create_material_category_using_post) | **POST** /api/material-categories | createMaterialCategory
*MaterialcategoryresourceApi* | [**delete_material_category_using_delete**](docs/MaterialcategoryresourceApi.md#delete_material_category_using_delete) | **DELETE** /api/material-categories/{id} | deleteMaterialCategory
*MaterialcategoryresourceApi* | [**get_all_material_categories_using_get**](docs/MaterialcategoryresourceApi.md#get_all_material_categories_using_get) | **GET** /api/material-categories | getAllMaterialCategories
*MaterialcategoryresourceApi* | [**get_material_category_using_get**](docs/MaterialcategoryresourceApi.md#get_material_category_using_get) | **GET** /api/material-categories/{id} | getMaterialCategory
*MaterialcategoryresourceApi* | [**update_material_category_using_put**](docs/MaterialcategoryresourceApi.md#update_material_category_using_put) | **PUT** /api/material-categories | updateMaterialCategory
*MaterialresourceApi* | [**create_material_using_post**](docs/MaterialresourceApi.md#create_material_using_post) | **POST** /api/materials | createMaterial
*MaterialresourceApi* | [**delete_material_using_delete**](docs/MaterialresourceApi.md#delete_material_using_delete) | **DELETE** /api/materials/{id} | deleteMaterial
*MaterialresourceApi* | [**get_all_materials_using_get**](docs/MaterialresourceApi.md#get_all_materials_using_get) | **GET** /api/materials | getAllMaterials
*MaterialresourceApi* | [**get_material_using_get**](docs/MaterialresourceApi.md#get_material_using_get) | **GET** /api/materials/{id} | getMaterial
*MaterialresourceApi* | [**search_materials_using_get**](docs/MaterialresourceApi.md#search_materials_using_get) | **GET** /api/_search/materials | searchMaterials
*MaterialresourceApi* | [**update_material_using_put**](docs/MaterialresourceApi.md#update_material_using_put) | **PUT** /api/materials | updateMaterial
*MaterialsubcategoryresourceApi* | [**create_material_subcategory_using_post**](docs/MaterialsubcategoryresourceApi.md#create_material_subcategory_using_post) | **POST** /api/material-subcategories | createMaterialSubcategory
*MaterialsubcategoryresourceApi* | [**delete_material_subcategory_using_delete**](docs/MaterialsubcategoryresourceApi.md#delete_material_subcategory_using_delete) | **DELETE** /api/material-subcategories/{id} | deleteMaterialSubcategory
*MaterialsubcategoryresourceApi* | [**get_all_material_subcategories_using_get**](docs/MaterialsubcategoryresourceApi.md#get_all_material_subcategories_using_get) | **GET** /api/material-subcategories | getAllMaterialSubcategories
*MaterialsubcategoryresourceApi* | [**get_material_subcategory_using_get**](docs/MaterialsubcategoryresourceApi.md#get_material_subcategory_using_get) | **GET** /api/material-subcategories/{id} | getMaterialSubcategory
*MaterialsubcategoryresourceApi* | [**update_material_subcategory_using_put**](docs/MaterialsubcategoryresourceApi.md#update_material_subcategory_using_put) | **PUT** /api/material-subcategories | updateMaterialSubcategory
*PaymentresourceApi* | [**create_payment_using_post**](docs/PaymentresourceApi.md#create_payment_using_post) | **POST** /api/payments | createPayment
*PaymentresourceApi* | [**delete_payment_using_delete**](docs/PaymentresourceApi.md#delete_payment_using_delete) | **DELETE** /api/payments/{id} | deletePayment
*PaymentresourceApi* | [**get_all_payments_using_get**](docs/PaymentresourceApi.md#get_all_payments_using_get) | **GET** /api/payments | getAllPayments
*PaymentresourceApi* | [**get_payment_using_get**](docs/PaymentresourceApi.md#get_payment_using_get) | **GET** /api/payments/{id} | getPayment
*PaymentresourceApi* | [**handle_notification_using_post**](docs/PaymentresourceApi.md#handle_notification_using_post) | **POST** /api/notify | handleNotification
*PaymentresourceApi* | [**update_payment_using_put**](docs/PaymentresourceApi.md#update_payment_using_put) | **PUT** /api/payments | updatePayment
*PlanresourceApi* | [**create_plan_using_post**](docs/PlanresourceApi.md#create_plan_using_post) | **POST** /api/plans | createPlan
*PlanresourceApi* | [**delete_plan_using_delete**](docs/PlanresourceApi.md#delete_plan_using_delete) | **DELETE** /api/plans/{id} | deletePlan
*PlanresourceApi* | [**get_all_plans_using_get**](docs/PlanresourceApi.md#get_all_plans_using_get) | **GET** /api/plans | getAllPlans
*PlanresourceApi* | [**get_plan_using_get**](docs/PlanresourceApi.md#get_plan_using_get) | **GET** /api/plans/{id} | getPlan
*PlanresourceApi* | [**update_plan_using_put**](docs/PlanresourceApi.md#update_plan_using_put) | **PUT** /api/plans | updatePlan
*ProfileinforesourceApi* | [**get_active_profiles_using_get**](docs/ProfileinforesourceApi.md#get_active_profiles_using_get) | **GET** /api/profile-info | getActiveProfiles
*QuantitytyperesourceApi* | [**create_quantity_type_using_post**](docs/QuantitytyperesourceApi.md#create_quantity_type_using_post) | **POST** /api/quantity-types | createQuantityType
*QuantitytyperesourceApi* | [**delete_quantity_type_using_delete**](docs/QuantitytyperesourceApi.md#delete_quantity_type_using_delete) | **DELETE** /api/quantity-types/{id} | deleteQuantityType
*QuantitytyperesourceApi* | [**get_all_quantity_types_using_get**](docs/QuantitytyperesourceApi.md#get_all_quantity_types_using_get) | **GET** /api/quantity-types | getAllQuantityTypes
*QuantitytyperesourceApi* | [**get_quantity_type_using_get**](docs/QuantitytyperesourceApi.md#get_quantity_type_using_get) | **GET** /api/quantity-types/{id} | getQuantityType
*QuantitytyperesourceApi* | [**update_quantity_type_using_put**](docs/QuantitytyperesourceApi.md#update_quantity_type_using_put) | **PUT** /api/quantity-types | updateQuantityType
*SubscriptionresourceApi* | [**create_subscription_using_post**](docs/SubscriptionresourceApi.md#create_subscription_using_post) | **POST** /api/subscriptions | createSubscription
*SubscriptionresourceApi* | [**delete_subscription_using_delete**](docs/SubscriptionresourceApi.md#delete_subscription_using_delete) | **DELETE** /api/subscriptions/{id} | deleteSubscription
*SubscriptionresourceApi* | [**get_all_subscriptions_using_get**](docs/SubscriptionresourceApi.md#get_all_subscriptions_using_get) | **GET** /api/subscriptions | getAllSubscriptions
*SubscriptionresourceApi* | [**get_subscription_using_get**](docs/SubscriptionresourceApi.md#get_subscription_using_get) | **GET** /api/subscriptions/{id} | getSubscription
*SubscriptionresourceApi* | [**update_subscription_using_put**](docs/SubscriptionresourceApi.md#update_subscription_using_put) | **PUT** /api/subscriptions | updateSubscription
*UserjwtcontrollerApi* | [**authorize_using_post**](docs/UserjwtcontrollerApi.md#authorize_using_post) | **POST** /api/authenticate | authorize
*UserresourceApi* | [**create_user_using_post**](docs/UserresourceApi.md#create_user_using_post) | **POST** /api/users | createUser
*UserresourceApi* | [**delete_user_using_delete**](docs/UserresourceApi.md#delete_user_using_delete) | **DELETE** /api/users/{login} | deleteUser
*UserresourceApi* | [**get_all_users_using_get**](docs/UserresourceApi.md#get_all_users_using_get) | **GET** /api/users | getAllUsers
*UserresourceApi* | [**get_user_using_get**](docs/UserresourceApi.md#get_user_using_get) | **GET** /api/users/{login} | getUser
*UserresourceApi* | [**search_using_get**](docs/UserresourceApi.md#search_using_get) | **GET** /api/_search/users/{query} | search
*UserresourceApi* | [**update_user_using_put**](docs/UserresourceApi.md#update_user_using_put) | **PUT** /api/users | updateUser


## Documentation For Models

 - [ActivityDTO](docs/ActivityDTO.md)
 - [ActivityMessageDTO](docs/ActivityMessageDTO.md)
 - [ActivityParticipantDTO](docs/ActivityParticipantDTO.md)
 - [AddressDTO](docs/AddressDTO.md)
 - [Card](docs/Card.md)
 - [CardDTO](docs/CardDTO.md)
 - [CompanyDTO](docs/CompanyDTO.md)
 - [ContactInfoDTO](docs/ContactInfoDTO.md)
 - [Customer](docs/Customer.md)
 - [IndustryDTO](docs/IndustryDTO.md)
 - [KeyAndPasswordDTO](docs/KeyAndPasswordDTO.md)
 - [LocationDTO](docs/LocationDTO.md)
 - [LoginDTO](docs/LoginDTO.md)
 - [ManagedUserDTO](docs/ManagedUserDTO.md)
 - [MarketplaceServiceDTO](docs/MarketplaceServiceDTO.md)
 - [MarketplaceUserDTO](docs/MarketplaceUserDTO.md)
 - [MaterialAttachmentDTO](docs/MaterialAttachmentDTO.md)
 - [MaterialCategoryDTO](docs/MaterialCategoryDTO.md)
 - [MaterialDTO](docs/MaterialDTO.md)
 - [MaterialSubcategoryDTO](docs/MaterialSubcategoryDTO.md)
 - [Payment](docs/Payment.md)
 - [Plan](docs/Plan.md)
 - [ProfileInfoResponse](docs/ProfileInfoResponse.md)
 - [QuantityTypeDTO](docs/QuantityTypeDTO.md)
 - [ResponseEntity](docs/ResponseEntity.md)
 - [Subscription](docs/Subscription.md)
 - [User](docs/User.md)
 - [UserDTO](docs/UserDTO.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author
