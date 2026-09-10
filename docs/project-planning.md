# Project 4 Planning

## Project Title

**Almac & Sons Mobile Fitting Services**

---

## Project Overview

Almac & Sons Mobile Fitting Services is planned as a full-stack Django application for managing mobile vehicle assistance, recovery, fitting and collection/delivery services.

The application will support both private customers and commercial/fleet customers.

Private customers may use the service for:

- Breakdown assistance
- Vehicle recovery
- Mobile tyre fitting
- Battery replacement
- Jump starts
- Minor roadside repairs
- Vehicle collection for workshop work or MOT
- Vehicle delivery following completed work

Commercial and fleet customers may use the service for:

- Car and van breakdown assistance
- HGV/commercial vehicle support
- Trailer tyre or roadside assistance
- Agricultural vehicle/equipment assistance
- Scheduled mobile fitting
- Fleet vehicle collection/delivery
- Recovery and roadside support

The application is intended to model a realistic mobile-service workflow rather than operate purely as a booking website.

---

# Requirement 1 — Full-Stack Django Application and Relational Database

## Academic Requirement

The project must be a full-stack Django application using a relational database.

Users must be able to store and manipulate application-specific data.

The completed project must demonstrate full CRUD functionality.

---

## Planned Business Implementation

The application will allow customers to request and manage mobile vehicle services.

Authorised staff and technicians will manage service requests through the operational lifecycle:

1. Customer identifies the vehicle or asset requiring assistance.
2. Customer selects the required service.
3. Customer provides the service location.
4. A service request is created.
5. Staff review and manage the request.
6. A technician is assigned.
7. The technician attends the job.
8. Job progress is recorded.
9. Work is completed.
10. An invoice is produced.
11. Payment is made using Stripe test mode.
12. The job is closed.

---

## Planned User Roles

### Customer

The Customer role will support both:

- Private customers
- Commercial/fleet customers

Customers will be able to interact only with data that they are authorised to access.

Planned customer functionality includes:

- Registering and logging into an account
- Managing vehicles/assets
- Requesting assistance
- Providing service-location information
- Viewing their own requests
- Updating eligible requests
- Cancelling eligible requests
- Viewing completed jobs
- Viewing invoices
- Making payments

---

### Technician

Technicians will manage work that has been assigned to them.

Planned technician functionality includes:

- Viewing assigned jobs
- Accepting jobs
- Updating job status
- Recording arrival
- Recording work undertaken
- Marking work as completed

Possible job statuses include:

- Assigned
- Accepted
- En route
- On site
- Work in progress
- Completed

---

### Dispatcher / Staff

Dispatcher or staff users will manage day-to-day service operations.

Planned functionality includes:

- Reviewing incoming service requests
- Managing customer and vehicle information where authorised
- Assigning technicians
- Updating job information
- Monitoring active jobs
- Managing scheduled and emergency work

---

### Manager / Administrator

Managers or administrators will have broader operational permissions.

Planned responsibilities include:

- Managing users and permissions
- Managing operational records
- Managing technicians
- Reviewing jobs
- Managing invoices and payment-related records
- Performing administrative functions

---

## Customer Types

The system will be designed to accommodate both private and commercial customers.

A private customer may have one or more vehicles.

A business customer may have multiple vehicles or assets, including:

- Cars
- Vans
- HGVs
- Trailers
- Agricultural vehicles or equipment

The database design must therefore avoid assumptions such as:

> One customer = one vehicle

Commercial/fleet functionality may be expanded as development progresses, but the underlying design should allow the system to support multiple vehicles/assets per customer.

---

## Service Request Types

The application is expected to support both immediate and scheduled services.

### Immediate / Roadside Services

Examples include:

- Breakdown assistance
- Vehicle recovery
- Tyre failure
- Battery failure
- Jump start
- Minor roadside repair

These requests should use a short, safety-conscious workflow focused on:

- Vehicle
- Problem
- Location
- Contact details
- Assistance request

---

### Scheduled Services

Examples include:

- Mobile tyre fitting
- Battery replacement
- Vehicle collection
- Vehicle delivery
- Workshop collection
- MOT collection/delivery

These requests may include:

- Preferred date
- Preferred time
- Address
- Additional instructions

---

## CRUD Planning

CRUD operations must represent genuine application functionality rather than exist only to satisfy assessment requirements.

Examples include:

### Create

Customers create service requests.

### Read

Customers view their own service requests.

### Update

Customers may update requests where the request status permits editing.

### Delete / Cancel

Customers may cancel eligible requests.

Staff users may have broader CRUD permissions according to their role.

---

## Permission Testing

Permissions will be tested using both successful and unsuccessful access attempts.

Examples:

```text
Customer A creates Request A       → Allowed
Customer A views Request A         → Allowed
Customer A views Request B         → Denied
Customer A edits Request B         → Denied
Customer edits completed request   → Denied
Staff manages authorised request   → Allowed
Technician updates assigned job    → Allowed
Technician accesses unauthorised job → Denied

# Requirement 2 — Brand-New Django Project and Multiple Reusable Apps

## Academic Requirement

Project 4 must be created as a brand-new Django project.

The application must contain multiple Django apps with sensible reusable responsibilities.

The architecture must demonstrate separation of concerns rather than creating artificial apps purely to satisfy the requirement.

---

## Planned Project Architecture

Working project name:

`almac_mobile`

Planned Django apps:

- `core`
- `accounts`
- `assistance`
- `payments`

The exact architecture may change during design if further analysis identifies better domain boundaries.

---

## `core`

Planned responsibilities:

- Homepage
- Public/static pages
- Shared application functionality
- General site-level functionality that does not naturally belong to another app

---

## `accounts`

Planned responsibilities:

- Customer accounts
- Authentication
- User profiles
- Private/commercial account information
- Account-related permissions

The app should be designed so that account-related functionality could potentially be reused elsewhere.

---

## `assistance`

Planned responsibilities:

- Vehicles/assets
- Service requests
- Service locations
- Jobs
- Technicians
- Operational workflow
- Service status

These components are initially grouped because they form the core mobile-assistance business domain.

This boundary will be reviewed during ERD design.

---

## `payments`

Planned responsibilities:

- Invoices
- Stripe integration
- Payment records
- Payment status
- Payment confirmation

Payment functionality will remain separated from core operational job-management logic.

---

## Architecture Principles

The app structure should follow genuine business boundaries.

Apps will not be created simply to increase the number of Django apps.

Possible future app separation may include:

- Technician/workforce management
- Fleet management

These will only be separated if the domain becomes complex enough to justify doing so.

---

## Planned Evidence

Evidence for this requirement will include:

- Project structure
- `INSTALLED_APPS`
- URL configuration
- Models
- App responsibilities documented in README
- Git history showing apps created incrementally
- Explanation of separation of concerns

**Status: PLANNED**

# Requirement 3 — Original Custom Data Models

## Academic Requirement

The application must contain at least two original custom Django models beyond models provided by Django or reproduced from course examples.

The models must represent genuine application-specific data and form meaningful relationships within the relational database.

---

## Planned Domain Models

The current proposed domain model includes:

- PrivateCustomerProfile
- BusinessAccount
- Asset
- ServiceRequest
- ServiceLocation
- Job
- Technician
- Invoice
- Payment

Additional relationship models may be introduced where required by the final ERD.

The final model structure will be determined during database design rather than creating models purely to satisfy the assessment requirement.

---

## Authentication and Customer Accounts

Django's authentication system will provide the underlying user authentication.

Private and commercial customers will use different profile/account structures because the information required from each type of customer is significantly different.

### Private Customer

A private customer account may contain:

- Name
- Email
- Telephone
- Address
- Vehicles/assets associated with the customer

The private registration process should remain short and should not request commercial information that is irrelevant to the customer.

### Business / Fleet Account

A business account may contain:

- Business name
- Primary contact
- Email
- Telephone
- Business/operating address
- Billing information
- Fleet/assets

Commercial functionality may later support multiple authorised contacts or users, but this will only be implemented if justified by the final project scope.

Separate private and commercial registration/profile workflows will prevent users from being presented with unnecessary fields.

---

## Asset Model

The term `Asset` is currently preferred internally to `Vehicle` because the service may support:

- Cars
- Vans
- HGVs
- Trailers
- Agricultural vehicles
- Agricultural equipment

Not every supported asset will necessarily have the same identifying information.

The public user interface may use more familiar terminology such as "Vehicle / Equipment" while the internal data model uses `Asset`.

The database must not assume that one customer has only one asset.

---

## Asset Ownership / Responsibility

The relationship between customers and assets requires further design during the ERD stage.

The application should avoid permanently attaching the historical record of an asset to one customer.

Where ownership or responsibility for an asset changes, the system should preserve appropriate asset/service history without exposing a previous customer's personal information to a new customer.

A relationship model may therefore be required between customer accounts and assets.

---

## Service Request

A `ServiceRequest` will represent what the customer is asking Almac & Sons Mobile Fitting Services to provide.

Requests may include immediate/roadside assistance or scheduled services.

The service request should remain separate from the operational `Job` created to fulfil that request.

---

## Service Location

Service location and service type will be treated as separate concepts.

Initial location types are:

- Workshop
- Customer premises
- Roadside

Location information required from the customer will depend on the selected location type.

### Workshop

The workshop location is already known by the business and should not require the customer to enter unnecessary address information.

### Customer Premises

May require:

- Address
- Postcode
- Access instructions
- Additional location notes

### Roadside

May require:

- Current/GPS location
- Road or motorway
- Direction of travel
- Motorway marker/reference where applicable
- Nearest junction
- Map location
- Additional safety/location notes

The final implementation will be determined after investigation of suitable mapping/location services.

---

## Location Purpose

A service may involve more than one operational location.

Planned location purposes include:

- Service
- Collection
- Delivery

This allows the data model to represent workflows such as:

Customer premises (collection)
→ Workshop (service)
→ Customer premises (delivery)

without treating collection/delivery as an unrelated system.

---

## Collection and Delivery

Private customers may request collection and/or delivery for workshop-based services such as:

- MOT
- Servicing
- Repairs
- Other workshop work

The underlying architecture should not prevent collection/delivery being offered to commercial customers.

Commercial vehicle collection, however, introduces additional operational requirements.

---

## Commercial Vehicle Collection and Driver Eligibility

A commercial vehicle must only be assigned for collection to a technician/driver who is suitably authorised and holds the appropriate driving licence entitlement for that vehicle.

The application should therefore be capable of matching the requirements of an asset/job against technician eligibility.

This should be implemented as a business rule rather than relying solely on staff remembering the restriction.

A commercial collection assignment should be rejected where the selected technician does not meet the required eligibility criteria.

---

## Technician

A technician/workforce profile may need to record information such as:

- Associated authenticated user
- Availability
- Service capabilities
- Driving licence entitlements
- Vehicle collection authorisation
- Relevant equipment/capabilities

The exact structure will be determined during ERD design.

Technician suitability provides an opportunity for original Python business logic by allowing the application to determine which technicians are eligible for a particular job.

---

## Job

A `Job` will represent the operational work required to fulfil a service request.

Potential job states include:

- Assigned
- Accepted
- En route
- On site
- Work in progress
- Completed

The final workflow and permitted status transitions will be defined during detailed design.

---

## Invoice and Payment

Completed work may result in an `Invoice`.

Payment records will be maintained separately from invoices so that the application can record payment state and integrate Stripe test-mode payments without combining financial and operational responsibilities into a single model.

The exact payment workflow will be designed separately as part of the Stripe requirement.

---

## Initial Conceptual Relationships

```text
Django User
├── PrivateCustomerProfile
└── BusinessAccount

PrivateCustomerProfile
└── Asset Relationship
      └── Asset

BusinessAccount
└── Asset Relationship
      └── Asset

Asset
└── ServiceRequest
      └── ServiceLocation
      └── Job
            └── Technician
            └── Invoice
                  └── Payment

# Requirement 4 — User Authentication and Authorisation

## Academic Requirement

The application must provide user authentication, including registration and login, with a clear reason for requiring authenticated user accounts.

Authentication must serve a genuine application purpose rather than being included solely to satisfy the assessment requirement.

---

## Purpose of Authentication

Authentication is required because the application will contain personal, operational and financial information that must only be accessible to authorised users.

Authenticated functionality may include:

- Customer profiles
- Vehicles/assets
- Service requests
- Service locations
- Job information
- Service history
- Invoices
- Payment information
- Technician assignments
- Operational staff functionality

Authentication establishes the identity of the user.

Authorisation will then determine which application data and functionality that authenticated user is permitted to access.

---

## Operational Roles

The application will use four main operational roles:

- Customer
- Technician
- Dispatcher / Staff
- Manager / Supervisor

Private and business/fleet customers are different customer account types rather than separate operational permission roles.

---

## Customer Account Types

Public registration will only allow users to create customer accounts.

The available customer account types will be:

- Private Customer
- Business / Fleet Customer

Separate registration/profile workflows will be provided because private and commercial customers require different information.

Users should only be asked for information relevant to their selected account type.

---

## Internal Accounts

Technician, Dispatcher / Staff and Manager / Supervisor are internal operational roles.

These roles will not be available through public registration.

Internal accounts and their permissions may only be created or assigned by an authorised Manager / Supervisor.

A customer must not be able to promote their own account or assign themselves an internal role.

Similarly, internal users must not be able to increase their own privileges unless their existing permissions explicitly authorise that action.

---

## Authentication and Authorisation

Authentication and authorisation will be treated as separate concerns.

Authentication answers:

> Who is this user?

Authorisation answers:

> What is this user permitted to do?

Being logged in will therefore not automatically provide access to all authenticated functionality.

Access will depend on the user's role, ownership of the requested data and the permissions required for the operation.

---

## Planned Access Rules

Examples include:

- Anonymous users may access appropriate public pages.
- Customers may access their own account information.
- Customers may access their own vehicles/assets.
- Customers may access their own service requests and relevant job information.
- Customers must not access another customer's private records.
- Technicians may access operational information required for jobs assigned to them.
- Technicians must not gain unrestricted access to unrelated customer or job records.
- Dispatcher / Staff users may access authorised operational functionality.
- Manager / Supervisor users may perform authorised account, staff and operational management functions.
- Internal roles must not be available through public registration.

The final permission matrix will be defined during detailed application design.

---

## Planned Security Testing

Both positive and negative permission tests will be documented.

Examples:

| Test | Expected Result |
| --- | --- |
| Public user registers as private customer | Allowed |
| Public user registers as business/fleet customer | Allowed |
| Public user attempts to register as technician | Option not available |
| Anonymous user accesses customer dashboard | Denied |
| Customer accesses own service request | Allowed |
| Customer attempts to access another customer's request | Denied |
| Customer attempts to change own operational role | Denied |
| Technician accesses assigned job | Allowed |
| Technician attempts to access unauthorised job | Denied |
| Dispatcher accesses authorised operational functionality | Allowed |
| Dispatcher attempts unauthorised privilege escalation | Denied |
| Manager/Supervisor creates authorised internal account | Allowed |
| Manager/Supervisor assigns authorised internal role | Allowed |

---

## Django Authentication

Django's authentication system will provide the underlying authentication framework.

Application-specific customer profiles, business accounts and internal operational roles will extend this functionality rather than duplicating password or authentication functionality in custom models.

The precise implementation of groups, permissions and role relationships will be determined during detailed database and permissions design.

---

## Planned Evidence

Evidence for this requirement will include:

- Registration forms
- Login/logout functionality
- Customer account-type selection
- Authentication-protected views
- Role-based permissions
- Object-level ownership checks where required
- Positive permission tests
- Negative permission tests
- Screenshots of relevant workflows
- Documented security decisions
- Git history showing incremental authentication and permission development

**Status: PLANNED**

# Requirement 5 — Validated Forms and CRUD

## Academic Requirement

The application must provide at least one validated form that allows users to create or edit data stored in the backend database.

The wider Project 4 requirements also require the application to demonstrate meaningful full CRUD functionality.

CRUD operations will be implemented according to genuine business requirements and user permissions rather than allowing every user to create, read, update and delete every type of record.

---

## Form Validation

Django server-side validation will be the authoritative validation layer for data submitted to the application.

JavaScript may enhance the user experience by providing immediate feedback, conditionally displaying relevant fields or assisting with location information, but client-side validation will not replace server-side validation.

Invalid or manipulated requests must therefore still be rejected by the backend.

---

## Planned Customer Forms

Customer-facing forms may include:

- Private customer registration
- Business / fleet customer registration
- Customer profile update
- Add vehicle / asset
- Edit vehicle / asset
- Create service request
- Enter service location
- Update a service request where permitted
- Cancel a service request where permitted
- Collection / delivery request

Forms will request only information relevant to the selected account, service and location type.

For example, a private customer will not be required to complete irrelevant commercial account fields.

Similarly, selecting a workshop location should not require the customer to enter roadside location information.

---

## Dynamic Location Forms

Service location forms will adapt according to the selected location type.

Initial location types are:

- Workshop
- Customer premises
- Roadside

Examples of conditional information include:

### Workshop

The workshop location is already known and unnecessary customer location fields should not be displayed.

### Customer Premises

Relevant information may include:

- Address
- Postcode
- Access instructions
- Additional location notes

### Roadside

Relevant information may include:

- Current / GPS location
- Road or motorway
- Direction of travel
- Motorway marker/reference where applicable
- Nearest junction
- Map location
- Additional location and safety information

JavaScript may be used to improve this workflow by showing only relevant fields.

Required business rules will also be validated by Django so that bypassing JavaScript does not bypass validation.

---

## CRUD Principles

CRUD functionality will be controlled by:

- Authentication
- User role
- Record ownership
- Operational status
- Business rules
- Record retention requirements

Full CRUD does not mean that every user should have unrestricted CRUD access to every model.

Some records should be cancelled, archived or otherwise made inactive rather than permanently deleted.

---

## Initial CRUD Permission Matrix

| Record | Customer | Technician | Dispatcher / Staff | Manager / Supervisor |
| --- | --- | --- | --- | --- |
| Own profile | Create / Read / Update | Read / Update own where appropriate | Read where authorised | Create / Read / Update / Delete where appropriate |
| Vehicle / Asset | Create / Read / Update own; remove from active account where permitted | Read when required for assigned job | Create / Read / Update where authorised | Full authorised management |
| Service Request | Create / Read / Update own where permitted; Cancel instead of Delete | Read assigned requests | Create / Read / Update / Cancel where authorised | Full authorised management |
| Service Location | Create / Read / Update own where permitted | Read for assigned work | Create / Read / Update where authorised | Full authorised management |
| Job | Read relevant customer information | Read / Update assigned jobs | Create / Read / Update / Cancel where authorised | Full authorised management |
| Technician | No access | Read / limited Update of own relevant information | Read where required | Create / Read / Update / Delete where appropriate |
| Invoice | Read own | Read where operationally required | Create / Read / Update where authorised | Full authorised management |
| Payment | Create payment / Read own payment status | No normal access required | Read where authorised | Read / manage where authorised |

This matrix is an initial design and will be refined when the final models, permissions and workflows are defined.

---

## Service Request Cancellation

Cancelling a service request will not normally delete it from the database.

Once a request has been submitted and entered the operational workflow, the business needs to retain a record of:

- The original request
- Processing already performed
- Technician assignment where applicable
- Status changes
- Cancellation
- Cancellation time
- Cancellation reason where appropriate

A typical workflow may therefore be:

```text
Request Submitted
        ↓
Dispatcher Reviews
        ↓
Technician Assigned
        ↓
Technician Accepts
        ↓
Customer Cancels
        ↓
Status = CANCELLED
        ↓
Operational history retained
```

Cancellation is therefore a business operation and status transition rather than a database deletion.

Whether cancellation is permitted may also depend on the current job/request status.

---

## Asset Removal

Removing an asset from a customer's active account should not automatically destroy legitimate historical service information associated with that asset.

Where appropriate, the relationship between the customer and asset may be ended or archived while necessary asset/service history remains available to authorised users.

This will be considered further during ERD design.

---

## Historical and Transactional Records

Customers will not be permitted to permanently delete legitimate historical business records such as:

- Processed service requests
- Jobs
- Completed work records
- Invoices
- Payment records

Corrections, cancellations, status changes or archival processes should preserve an appropriate historical record rather than silently destroying it.

---

## Record Retention and Deletion

The application will not assume that all records have one universal retention period.

Retention requirements may vary according to:

- Record type
- Business purpose
- Tax/accounting requirements
- Legal obligations
- Warranty or dispute requirements
- Data-protection requirements

The design will therefore distinguish between:

### Delete

Permanent deletion where the record can legitimately be removed and no retention requirement applies.

### Cancel

The transaction remains recorded but its operational status becomes cancelled.

### Archive

The record is removed from normal active workflows while necessary history is retained.

### Anonymise

Where appropriate after the applicable retention period, identifying personal information may be removed while legitimate non-personal historical information is retained.

The final retention policy for a real commercial deployment would need to reflect the business's actual legal, accounting and data-protection obligations.

The diploma project will demonstrate awareness of these requirements without attempting to implement an unsupported universal retention period.

---

## Commercial Collection Validation

Where collection of a commercial vehicle requires a particular driving licence entitlement or other authorisation, assignment must be validated against the selected technician/driver's eligibility.

The application should reject an invalid assignment rather than merely display a warning.

This validation may form part of the application's original Python business logic.

---

## Planned Validation Testing

Testing will include both valid and invalid submissions.

Examples include:

| Test | Expected Result |
| --- | --- |
| Valid private customer registration | Accepted |
| Missing required registration field | Rejected |
| Private customer supplied irrelevant commercial fields | Not requested / ignored as appropriate |
| Valid asset creation | Accepted |
| Customer attempts to edit another customer's asset | Denied |
| Valid service request | Accepted |
| Required location information missing | Rejected |
| Roadside request with required location data | Accepted |
| Customer attempts to delete processed request | Denied |
| Permitted request cancellation | Status changed to Cancelled and record retained |
| Technician updates assigned job | Accepted |
| Technician attempts to update unauthorised job | Denied |
| Commercial collection assigned to suitably eligible technician | Accepted |
| Commercial collection assigned to ineligible technician | Rejected |

The final testing documentation will include the actual inputs, expected result, actual result and supporting evidence.

---

## Planned Evidence

Evidence for this requirement will include:

- Django forms
- ModelForms where appropriate
- Server-side validation
- Custom validation/business rules
- CRUD views and templates
- Authentication and permission checks
- Positive form-validation tests
- Negative form-validation tests
- CRUD permission tests
- Cancellation/status workflow tests
- Screenshots at appropriate responsive breakpoints
- Documented bugs and fixes
- Git commits showing incremental development

**Status: PLANNED**

# Requirement 6 — Stripe Payments and Invoicing

## Academic Requirement

The application must include e-commerce functionality using Stripe in at least one Django app.

Stripe will operate in test mode only.

Successful payment must provide the user with additional functionality or content within the application.

---

## Business Purpose

Stripe will be used to allow customers to securely pay invoices generated for completed work.

Payment functionality will form part of the normal operational workflow rather than being added as an isolated demonstration of Stripe.

The planned workflow is:

```text
Service Request
      ↓
Job Created
      ↓
Technician Assigned
      ↓
Work Carried Out
      ↓
Labour / Parts / Other Charges Recorded
      ↓
Invoice Generated
      ↓
Invoice Issued to Customer
      ↓
Stripe Test Payment
      ↓
Payment Confirmed
      ↓
Invoice Marked PAID
      ↓
Paid Receipt / Final Paid Invoice Available
```

---

## Charge Types

An invoice may contain charges relating to services such as:

- Call-out charges
- Labour
- Parts
- Vehicle recovery
- Mobile fitting
- Collection / delivery
- Workshop work

The exact pricing structure will be determined during detailed application design.

---

## Invoice and Payment Separation

Invoices and payments will be represented separately within the data model.

An `Invoice` represents the amount owed by the customer and the charges that make up that amount.

A `Payment` represents a payment transaction associated with that invoice.

This separation prevents operational and financial responsibilities from being combined unnecessarily within a single model.

Conceptually:

```text
Job
 ↓
Invoice
 ↓
Payment
```

The final relationship and field structure will be defined during ERD and model design.

---

## Invoice Status

The initial invoice lifecycle is expected to include:

- Draft
- Issued
- Paid

Additional states such as:

- Cancelled
- Refunded

may be introduced if justified by the final workflow.

The application will not introduce unnecessary payment states purely for complexity.

---

## Stripe Test Mode

All Stripe functionality developed for this project will use Stripe Test Mode.

No real customer payments or real card transactions will be processed as part of the assessed application.

Stripe test credentials and other secret values will be stored securely using environment variables and will not be committed to the Git repository.

---

## Server-Controlled Payment Amounts

The amount submitted to Stripe must be derived from trusted server-side invoice data.

The application will not trust a payment amount supplied by the browser or customer.

For example, altering an HTML field or request value must not allow a customer to change the amount actually owed.

Conceptually:

```text
Customer selects Pay
        ↓
Server retrieves authorised Invoice
        ↓
Server determines amount due
        ↓
Stripe payment created from trusted amount
```

This provides protection against client-side manipulation of payment values.

---

## Access Control

Payment functionality will follow the authentication, authorisation and record-ownership rules defined in Requirement 4.

Customers may only access and pay invoices associated with their own authorised account.

Payment-specific views will not provide a route around the application's existing access-control rules.

---

## Successful Payment

A successful Stripe payment must result in a meaningful change within the application.

Following verified successful payment:

- A payment record will be created or confirmed as appropriate.
- The related invoice will be marked as paid.
- Payment confirmation information will be stored as appropriate.
- The customer will gain access to the final paid invoice / receipt for that transaction.

The paid receipt or equivalent post-payment functionality will therefore only become available following successful payment confirmation.

This satisfies the requirement for successful payment to grant additional functionality or content.

---

## Failed or Cancelled Payment

A failed or cancelled Stripe payment must not cause the application to mark an invoice as paid.

The customer should be returned to an appropriate application state and given clear feedback.

The invoice should remain outstanding so that another payment attempt can be made where appropriate.

No paid receipt or other payment-dependent functionality should be unlocked following an unsuccessful payment.

---

## Payment Confirmation

The application must not rely solely on the customer's browser reaching a success page as proof that payment succeeded.

The final Stripe implementation will use an appropriate server-side confirmation mechanism so that payment status is based on verified payment information.

The exact Stripe implementation will be determined when the payment functionality is developed using the current Stripe documentation.

---

## Record Retention

Invoices and confirmed payment records are transactional business records and will follow the retention principles defined in Requirement 5.

Customers will not be able to permanently delete legitimate invoice or payment history through their account.

Any future refund, cancellation or correction process should preserve an appropriate transaction history rather than silently removing the original record.

---

## Planned Testing

Testing will cover successful and unsuccessful payment paths.

Examples include:

| Test | Expected Result |
| --- | --- |
| Customer accesses own issued invoice | Allowed |
| Customer attempts to access another customer's invoice | Denied |
| Anonymous user attempts to access protected payment functionality | Authentication required |
| Correct invoice amount supplied to Stripe | Accepted |
| Client attempts to manipulate payment amount | Trusted server-side amount used |
| Successful Stripe test payment | Payment confirmed |
| Successful payment | Invoice status becomes Paid |
| Successful payment | Paid receipt / final invoice becomes available |
| Failed Stripe test payment | Invoice remains unpaid |
| Cancelled payment | Invoice remains unpaid |
| Failed/cancelled payment | Paid receipt remains unavailable |
| Stripe secret credentials checked in repository | No secrets present |

The final testing documentation will record the actual test data, expected result, actual result and supporting evidence.

---

## Planned Evidence

Evidence for this requirement will include:

- Stripe Test Mode integration
- Invoice and Payment models
- Invoice/payment relationship in the ERD
- Payment views and templates
- Server-side payment amount handling
- Successful Stripe test transaction
- Failed/cancelled transaction testing
- Payment status updates
- Paid receipt / final invoice access
- Authentication and ownership testing
- Environment-variable configuration
- Evidence that Stripe secrets are excluded from Git
- Responsive screenshots of the payment workflow
- Documented bugs and fixes
- Incremental Git commits showing development of the payment functionality

**Status: PLANNED**

# Requirement 7 — Main Navigation and Structured Layout

## Academic Requirement

The application must provide a clear main navigation and a structured layout that allows users to move through the application efficiently.

Navigation should support the needs of different user types without exposing irrelevant functionality.

---

## Navigation Principles

The application will use role-aware navigation.

Users will only be shown navigation options that are relevant to their current role and permissions.

The main navigation will remain concise.

More detailed operational actions will be provided through dashboards rather than attempting to place every function in the main navbar.

---

## Public Navigation

Unauthenticated users are expected to see a simple public navigation such as:

- Home
- Services
- Request Assistance
- Login / Register

Public navigation should provide a clear route into the primary customer journey without exposing protected operational functionality.

---

## Customer Navigation

Authenticated customers may see navigation such as:

- Home
- Services
- Request Assistance
- My Account
- My Vehicles / Equipment
- My Requests
- My Invoices
- Logout

The exact labels may be refined during wireframing and usability testing.

Private and business/fleet customers will share the main customer navigation where appropriate, while account-specific functionality may differ within their dashboard or account area.

---

## Technician Navigation

Technicians require a different operational interface from customers.

Possible navigation includes:

- Dashboard
- Assigned Jobs
- Current Job
- Job History
- Profile
- Logout

Technicians should only see jobs and operational information they are authorised to access.

---

## Dispatcher / Staff Navigation

Dispatcher / Staff users may require access to:

- Dashboard
- Incoming Requests
- Active Jobs
- Scheduled Jobs
- Technicians
- Customers / Assets
- Logout

The dashboard should provide access to operational workflow without requiring an excessively large global navbar.

---

## Manager / Supervisor Navigation

Manager / Supervisor users may require access to:

- Dashboard
- Operations
- Technicians
- Customers / Assets
- Invoices
- Staff Management
- Reports
- Logout

Manager / Supervisor navigation will reflect the broader permissions of this role while remaining structured and understandable.

---

## Shared Layout

The application will use a shared Django base template to maintain a consistent structure across pages.

Conceptually:

```text
base.html
├── Header
│   └── Role-aware Navigation
├── Main Content
└── Footer
```

Individual templates will extend the base template rather than duplicating the full page structure.

This should improve:

- Consistency
- Maintainability
- Accessibility
- Navigation reliability
- Reusability

---

## Responsive Design

The application will be designed and tested across:

- Desktop
- Tablet
- Mobile

Navigation must remain usable at all supported screen sizes.

Where a burger menu or collapsible navigation is used on smaller screens, it must remain keyboard accessible and understandable.

Responsive behaviour will be included in the testing evidence rather than relying only on visual inspection during development.

---

## Accessibility

Navigation and layout design will consider:

- Keyboard navigation
- Logical focus order
- Visible focus states
- Semantic HTML
- Appropriate link and button labels
- Sufficient colour contrast
- Clear active/current-page indication where appropriate

Interactive navigation controls must not rely solely on mouse input.

---

## Dashboard-Based Navigation

Role-specific dashboards will provide access to detailed operational functionality.

This prevents the main navbar from becoming overcrowded as application functionality increases.

Examples include:

```text
Customer Dashboard
├── Vehicles / Equipment
├── Service Requests
├── Invoices
└── Account Details
```

```text
Technician Dashboard
├── Assigned Jobs
├── Current Job
└── Job History
```

```text
Dispatcher Dashboard
├── Incoming Requests
├── Active Jobs
├── Scheduled Jobs
└── Technician Allocation
```

```text
Manager / Supervisor Dashboard
├── Operations
├── Staff Management
├── Invoices
└── Reports
```

The final dashboard structure will be refined during wireframing.

---

## Early Homepage Design

The existing early `index.html` file is a conceptual static homepage sketch.

It will not define the final Django structure.

The final implementation will use Django templates and a shared `base.html`.

The early homepage may be used as a visual reference while the final public layout and navigation are redesigned during wireframing and static development.

---

## Planned Testing

Navigation and layout testing will include:

| Test | Expected Result |
| --- | --- |
| Public user views navigation | Only public links shown |
| Customer logs in | Customer navigation shown |
| Technician logs in | Technician navigation shown |
| Dispatcher logs in | Dispatcher/Staff navigation shown |
| Manager/Supervisor logs in | Manager/Supervisor navigation shown |
| Customer attempts to access staff navigation route directly | Denied |
| Navigation tested on desktop | Fully usable |
| Navigation tested on tablet | Fully usable |
| Navigation tested on mobile | Fully usable |
| Navigation tested by keyboard | All controls accessible |
| Focus states tested | Clearly visible |
| Burger/collapsible menu tested without mouse | Fully operable |

---

## Planned Evidence

Evidence for this requirement will include:

- Wireframes
- Shared `base.html`
- Role-aware navigation
- Dashboard layouts
- Desktop screenshots
- Tablet screenshots
- Mobile screenshots
- Keyboard navigation testing
- Focus-state testing
- Accessibility checks
- Responsive testing evidence
- Git history showing layout and navigation development
- Documented bugs and fixes

**Status: PLANNED**

# Requirement 8 — Original JavaScript Logic

## Academic Requirement

The application must include original JavaScript logic that enhances the user experience.

JavaScript functionality will be designed around genuine user and operational needs rather than being included solely to satisfy the assessment requirement.

---

## JavaScript Design Principle

JavaScript will enhance the user interface and provide immediate feedback and interaction.

Django and Python will remain responsible for authoritative server-side validation, permissions and business rules.

The application must not rely on JavaScript for security or for enforcing critical business rules.

Conceptually:

```text
JavaScript
→ Improve user experience
→ Show relevant information
→ Reduce unnecessary form fields
→ Assist with location entry

Django
→ Validate submitted data
→ Enforce permissions
→ Enforce business rules
→ Protect database integrity
```

Disabling or bypassing JavaScript must not allow a user to bypass required backend validation.

---

## Dynamic Service Request Forms

JavaScript will adapt the service request interface according to the type of assistance requested.

The initial distinction will be between:

- Immediate assistance
- Scheduled service

### Immediate Assistance

The interface may prioritise:

- Vehicle / equipment
- Current problem
- Current location
- Contact information
- Request assistance action

The form should avoid unnecessary steps because the customer may be requesting help from the roadside.

### Scheduled Service

The interface may include:

- Vehicle / equipment
- Service required
- Preferred date
- Preferred time
- Service location
- Collection / delivery options
- Additional instructions

JavaScript may reveal or hide relevant fields as the customer makes selections.

---

## Dynamic Service Location Forms

JavaScript will adapt location fields according to where the work or assistance is required.

Initial location types are:

- Workshop
- Customer premises
- Roadside

Conceptually:

```text
Workshop
      ↓
No unnecessary customer location fields

Customer Premises
      ↓
Address
Postcode
Access instructions
Additional notes

Roadside
      ↓
Road / Motorway
Direction of travel
Nearest junction
Marker / reference where applicable
Current location
Location notes
```

This should reduce form complexity and prevent customers being presented with large numbers of irrelevant fields.

All conditionally required information will also be validated server-side.

---

## Collection and Delivery Interaction

Scheduled workshop services may include collection and/or delivery.

JavaScript may dynamically display relevant fields when these services are selected.

Examples include:

```text
Collection required?
        ↓ YES
Show collection location/details
```

and:

```text
Delivery required?
        ↓ YES
Is delivery location the same?
       ↙             ↘
     YES              NO
      ↓                ↓
Reuse location    Request delivery
information       location/details
```

The exact interaction will be refined during wireframing and usability testing.

---

## Browser Geolocation

For roadside assistance, the application may provide a:

`Use My Current Location`

function.

Where supported and with the user's permission, browser geolocation may be used to obtain location coordinates and assist the customer in identifying their current position.

The application must handle situations where:

- The user grants location permission
- The user denies location permission
- Location services are unavailable
- The browser does not support the required functionality
- A location cannot be obtained

Manual location entry must remain available as a fallback.

---

## Mapping

Interactive mapping may be used to help customers identify or confirm a service location.

Potential technologies will be investigated before implementation.

The selected solution should support the application requirements without making the core service-request workflow dependent on an unnecessary external service.

Any external mapping, geocoding or location service will be documented and attributed appropriately.

---

## Progressive Enhancement

Where practical, JavaScript functionality will follow progressive-enhancement principles.

Core operations such as submitting a valid service request must remain protected and validated by the server.

Failure of optional JavaScript functionality should not create an insecure application or corrupt application data.

---

## Accessibility

Dynamic JavaScript functionality must remain accessible.

Considerations will include:

- Keyboard operation
- Focus management
- Clear labels
- Appropriate announcements or status messages where necessary
- Avoiding interactions that depend solely on mouse input
- Maintaining understandable forms when fields are dynamically shown or hidden

Accessibility behaviour will be included in testing.

---

## Planned Testing

JavaScript testing will include both expected and failure scenarios.

| Test | Expected Result |
| --- | --- |
| Immediate assistance selected | Immediate-request fields displayed |
| Scheduled service selected | Scheduled-service fields displayed |
| Workshop selected | Unnecessary location fields hidden |
| Customer premises selected | Relevant address fields displayed |
| Roadside selected | Relevant roadside fields displayed |
| Collection selected | Collection fields displayed |
| Collection not selected | Collection fields not unnecessarily displayed |
| Different delivery location selected | Delivery location fields displayed |
| Geolocation permission granted | Location information obtained where available |
| Geolocation permission denied | Clear fallback/manual entry available |
| Geolocation unavailable | Application remains usable |
| JavaScript-enhanced form submitted with valid data | Accepted by backend |
| Manipulated/invalid submission bypasses JavaScript | Rejected by backend |
| Dynamic controls operated by keyboard | Fully usable |

---

## Originality

The principal original JavaScript functionality is planned to include:

1. Dynamic service-request behaviour based on immediate or scheduled assistance.
2. Dynamic location forms based on workshop, customer-premises or roadside service.
3. Location assistance using browser geolocation and/or interactive mapping where appropriate.
4. Dynamic collection and delivery options where required.

Additional JavaScript may be introduced where it provides genuine usability improvements.

Functionality will not be added merely to increase the quantity of JavaScript in the project.

---

## Planned Evidence

Evidence for this requirement will include:

- Original JavaScript source code
- Explanation of the purpose of each major interaction
- Dynamic service-request form evidence
- Dynamic location form evidence
- Collection/delivery interaction evidence
- Geolocation/map evidence if implemented
- Keyboard testing
- Failure/fallback testing
- Server-side validation tests demonstrating JavaScript cannot bypass business rules
- Desktop, tablet and mobile testing
- Documented bugs and fixes
- Attribution of any external libraries/services
- Incremental Git history showing JavaScript development

**Status: PLANNED**

# Requirement 9 — README and Project Documentation

## Academic Requirement

The project must include a README that clearly explains the application, its purpose and the value it provides to its intended users.

The README will also provide structured evidence of the design, development, testing and deployment of the completed application.

---

## Documentation Strategy

The README will be developed throughout the project rather than written only after development is complete.

Documentation will form part of the normal development cycle:

```text
DESIGN
  ↓
WRITE
  ↓
TEST
  ↓
DOCUMENT EVIDENCE
  ↓
COMMIT
  ↓
CLEAN TREE
```

This should ensure that important design decisions, testing evidence, bugs and development reasoning are recorded while they are still current.

---

## Purpose of the README

The README will explain:

- What the application is
- What business problem it addresses
- Who the intended users are
- What value the application provides
- How the application was designed
- How the application was implemented
- How the application was tested
- How security and permissions were handled
- How the application was deployed
- How the completed project satisfies the assessment requirements

The aim is not simply to produce a long document.

The aim is to produce clear, traceable evidence that allows an assessor to understand and evaluate the project efficiently.

---

## Project Value

The README will explain that Almac & Sons Mobile Fitting Services is intended to manage the complete service workflow rather than act only as an informational garage website.

The planned workflow includes:

```text
Customer
   ↓
Vehicle / Equipment
   ↓
Service Request
   ↓
Service Location
   ↓
Dispatch
   ↓
Technician / Job
   ↓
Work Completed
   ↓
Invoice
   ↓
Payment
```

The application is intended to support both customer-facing and internal operational processes.

---

## Target Users

The README will describe the needs of:

- Private customers
- Business / fleet customers
- Technicians
- Dispatcher / Staff users
- Manager / Supervisor users

Private and business/fleet customers will be documented as customer account types, while Customer, Technician, Dispatcher / Staff and Manager / Supervisor represent the principal operational roles.

---

## Planned README Structure

The final README is expected to contain sections covering:

1. Project Overview
2. Target Users
3. UX Design
4. Application Architecture
5. Features
6. Authentication and Authorisation
7. CRUD and Validation
8. Original Python and JavaScript Logic
9. Stripe / E-commerce
10. Testing
11. Technologies
12. External APIs and Libraries
13. Security
14. Deployment
15. Version Control and Development Methodology
16. Known Issues
17. Future Features
18. Credits and Attribution
19. Assessment Evidence / Criterion Traceability

The exact structure may evolve as the application develops.

---

## UX and Design Evidence

The README will document the design process rather than only showing the finished interface.

Evidence may include:

- Project goals
- User needs
- User stories
- User journeys
- Information architecture
- Wireframes
- Responsive design decisions
- Accessibility decisions
- Significant UX decisions and their justification

Where a design changes during development, the reason for the change should be recorded where it provides useful evidence of the development process.

---

## Architecture and Database Evidence

The README will explain:

- Django project architecture
- Django app responsibilities
- Separation of concerns
- Custom models
- Model relationships
- ERD
- Important database-design decisions
- Relevant business rules

Significant modelling decisions should include their reasoning rather than merely listing model names and fields.

---

## Feature Documentation

Features will be documented according to the users and workflows they support.

This may include:

- Public functionality
- Private customer functionality
- Business / fleet functionality
- Technician functionality
- Dispatcher / Staff functionality
- Manager / Supervisor functionality
- Vehicle / equipment management
- Service requests
- Location functionality
- Collection / delivery
- Job management
- Invoicing
- Stripe payments

Screenshots will be used where they provide useful evidence rather than simply increasing the size of the README.

---

## Assessment Traceability

The completed README will include an assessment evidence matrix.

The purpose of the matrix is to provide a direct route from an assessment criterion to its implementation and supporting evidence.

Conceptually:

```text
Assessment Criterion
        ↓
Design / Requirement
        ↓
Implementation
        ↓
Testing
        ↓
Evidence
        ↓
Result
```

A final matrix may use a structure such as:

| Criterion | Implementation | Evidence | Testing | Status |
| --- | --- | --- | --- | --- |
| Relational database | Custom related models | ERD / model evidence | Relationship tests | Complete |
| Multiple Django apps | Domain-based app architecture | Project structure | Functional testing | Complete |
| CRUD | Permission-controlled CRUD | Forms / views | CRUD tests | Complete |
| Authentication | Django authentication | Registration / login evidence | Access tests | Complete |
| Stripe | Invoice payment workflow | Stripe test evidence | Payment tests | Complete |
| Original JavaScript | Dynamic service/location forms | JS evidence | Interaction/fallback tests | Complete |

The final version will use the actual assessment criteria and wording where available.

---

## Testing Documentation

Testing evidence will be recorded throughout development.

The README will provide evidence of areas including:

- Forms
- Validation
- CRUD
- Authentication
- Authorisation
- Object ownership
- User roles
- Original Python logic
- Original JavaScript
- Stripe
- Responsive behaviour
- Accessibility
- Keyboard navigation
- Browser compatibility
- Deployment

Testing should include both successful and unsuccessful scenarios.

Where appropriate, tests will record:

- Test objective
- Input/action
- Expected result
- Actual result
- Pass/fail result
- Supporting evidence

---

## Responsive Evidence

Representative pages and important workflows will be tested at three principal screen categories:

- Desktop
- Tablet
- Mobile

Responsive evidence will demonstrate actual testing rather than relying solely on a statement that the application is responsive.

---

## Accessibility Evidence

Accessibility documentation will include appropriate evidence relating to:

- Keyboard navigation
- Focus order
- Visible focus states
- Semantic structure
- Labels
- Colour contrast
- Responsive navigation
- Dynamic JavaScript interactions

Accessibility problems discovered during development and their resolution should be documented where relevant.

---

## Bugs and Fixes

Significant bugs will be treated as useful development evidence.

Where appropriate, bugs will be documented using:

```text
Problem
   ↓
Observed Behaviour
   ↓
Diagnosis
   ↓
Change / Fix
   ↓
Retest
   ↓
Result
```

This will demonstrate the development and debugging process rather than presenting the final application as though no problems occurred during development.

Git history should support significant fixes where appropriate.

---

## Security Documentation

The README will document relevant security decisions, including:

- Authentication
- Authorisation
- Role-based access
- Object ownership
- Environment variables
- Secret management
- Production DEBUG configuration
- Payment security
- Server-side validation

Security evidence will cross-reference the relevant implementation and testing sections rather than unnecessarily duplicating documentation.

---

## Deployment Documentation

The README will provide sufficient information to explain how the application is deployed and configured.

This will include relevant information such as:

- Hosting platform
- Production database
- Required environment variables
- Static-file handling
- Deployment process
- Production configuration
- Live application link
- Repository link

No secret values will be included in the documentation.

---

## External Code and Attribution

External libraries, APIs, documentation, tutorials and other significant external resources used during development will be appropriately acknowledged.

Externally sourced or adapted code will be clearly distinguished from original project code where required.

The project will not claim externally sourced functionality as original work.

---

## Planning Document and Final README

`docs/project-planning.md` and `README.md` have different purposes.

The planning document records:

- Proposed requirements
- Early design decisions
- Business reasoning
- Planned implementation
- Planned testing and evidence

The final README records:

- What was actually implemented
- Why final decisions were made
- How functionality works
- How it was tested
- Evidence of the completed application

Plans that change during development will therefore not automatically be presented as completed features in the final README.

---

## Final Assessment Audit

Before submission, the project will be reviewed against the complete available Pass, Merit and Distinction assessment criteria.

For each criterion the final audit will ask:

> What evidence demonstrates that this criterion has been satisfied?

Where evidence is incomplete, the missing evidence should be addressed before submission where possible.

The final README should allow an assessor to move efficiently from criterion to implementation, testing and evidence without having to infer whether functionality exists.

---

## Planned Evidence

Evidence for this requirement will include:

- Continuously maintained README
- User stories and journeys
- Wireframes
- ERD
- Architecture documentation
- Feature documentation
- CRUD matrix
- Authentication/authorisation evidence
- Testing tables
- Responsive evidence
- Accessibility evidence
- Stripe evidence
- Bugs and fixes
- Deployment documentation
- Security documentation
- Credits and attribution
- Assessment traceability matrix
- Supporting Git history

**Status: PLANNED**

