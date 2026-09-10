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

# Requirement 10 — Git and GitHub

## Academic Requirement

The project must use Git for version control and GitHub for remote repository hosting.

Version control should provide evidence of the development process through regular, meaningful commits.

---

## Version Control Strategy

Git will be used throughout the complete development lifecycle rather than only being used to upload the finished application.

Development will follow the established project workflow:

```text
DESIGN
  ↓
WRITE
  ↓
TEST
  ↓
DOCUMENT EVIDENCE
  ↓
REVIEW CHANGES
  ↓
COMMIT
  ↓
PUSH
  ↓
CLEAN / KNOWN-GOOD WORKING STATE
```

Each commit should represent a logical and understood development step.

---

## Incremental Development

Large groups of unrelated changes will be avoided where practical.

Features will be developed incrementally so that each stage can be:

- Reviewed
- Tested
- Documented where appropriate
- Committed independently
- Returned to a known-good working state

This should make the Git history useful both for development and as evidence of how the project evolved.

---

## Commit Messages

Commit messages will describe the purpose of the change rather than use vague messages such as:

- Update
- Changes
- Fix stuff
- Work

Examples of meaningful commits include:

```text
Add authentication and authorisation planning
Add validated forms and CRUD planning
Add Stripe payments and invoicing planning
Add navigation and layout planning
Add original JavaScript planning
Add README and documentation planning
```

Implementation commits will follow the same principle.

---

## Selective Staging

Files will be staged deliberately.

Commands such as:

```bash
git status
git diff
git add <specific-file>
```

will be used where appropriate so that unrelated or unintended files are not automatically included in a commit.

`git add .` will not be used automatically where selective staging provides better control over the commit.

---

## Review Before Commit

Changes should be reviewed before being committed.

Where appropriate this may include:

```bash
git diff
```

and:

```bash
git status
```

The aim is to understand what is entering the repository before creating the commit.

---

## Remote Repository

The GitHub repository will act as the remote version-controlled source for the project.

Completed logical development stages will be pushed regularly so that the remote repository reflects the development history.

The repository will not be treated merely as a final submission upload.

---

## Secrets and Excluded Files

Sensitive or environment-specific information must not be committed to GitHub.

The `.gitignore` file will exclude appropriate files such as:

- `.env`
- Virtual environments
- Python cache files
- Local SQLite database
- Collected production static files
- Editor-specific files where appropriate
- Operating-system-generated files

Secret values such as:

- Django secret keys
- Stripe secret keys
- Database credentials
- External API credentials

must not appear in committed source code.

Before submission, the repository will be checked for accidentally committed secrets or inappropriate files.

---

## Branching

The project does not require unnecessary branching purely to demonstrate Git usage.

Branches may be used where they provide a genuine development benefit.

The priority is a clear, understandable and reliable version history rather than introducing additional Git complexity without a practical reason.

---

## Early Design Files

Files will not be committed simply because they exist in the working directory.

Early experiments or design sketches will only enter the tracked project history when they have a clear purpose within the development process.

This ensures that the repository history represents deliberate project development.

---

## Git as Development Evidence

Git history will support the documentation of the project.

Where significant functionality or bugs are discussed in the README, corresponding commits should make it possible to follow the relevant development where practical.

The intended relationship is:

```text
Design Decision
      ↓
Implementation
      ↓
Testing
      ↓
Documentation
      ↓
Git Commit
```

This provides supporting evidence that the application was developed incrementally rather than appearing as a single completed codebase.

---

## Planned Final Checks

Before submission, Git/GitHub checks will include:

- Working tree reviewed
- Required files tracked
- No unintended files tracked
- No secrets committed
- `.gitignore` reviewed
- Meaningful commit history present
- Local and remote repositories synchronised
- Deployment source matches the intended submitted version
- Repository link verified

---

## Planned Evidence

Evidence for this requirement will include:

- GitHub repository
- Incremental commit history
- Meaningful commit messages
- `.gitignore`
- Git status checkpoints
- Development commits corresponding to documented features
- Bug-fix commits where appropriate
- Regular pushes to the remote repository
- Final repository audit

**Status: PLANNED**

# Requirement 11 — Attribution and Separation of External Code

## Academic Requirement

External code, libraries, frameworks, APIs, media and other third-party resources used within the project must be appropriately acknowledged.

Externally sourced or adapted work must be clearly distinguishable from original project work.

---

## Attribution Strategy

External resources will be recorded throughout development rather than reconstructed immediately before submission.

Where an external resource contributes materially to the application, the project will record:

```text
Resource
   ↓
Source
   ↓
Purpose
   ↓
How It Was Used
   ↓
Where It Appears
   ↓
Required Attribution
```

This should provide a clear record of third-party resources while also demonstrating which parts of the application represent original project work.

---

## Frameworks and Libraries

The application will use established frameworks and libraries where they provide appropriate functionality.

Expected examples include:

- Django
- Stripe
- Database libraries
- Deployment libraries
- Static-file handling libraries
- Potential mapping/location libraries

These technologies will be documented in the README together with their purpose within the application.

Use of an established framework or library will not be presented as original project functionality.

---

## External APIs and Services

External APIs or services may be used where they provide useful supporting functionality.

Potential examples include:

- Stripe
- Mapping
- Geolocation
- Address or postcode lookup
- Future vehicle-data services

Before implementation, appropriate current documentation, terms, licensing, availability and costs will be reviewed where relevant.

The core application should not unnecessarily depend on optional external services where a suitable manual workflow can be provided.

---

## External Code and Snippets

If code is copied or materially adapted from an external source, the source will be recorded.

Possible sources may include:

- Official documentation
- Tutorials
- Technical articles
- Community resources
- Code examples

Where appropriate, attribution may be provided:

- In the source code
- In the README
- In the project credits section
- In more than one location where this improves clarity

Attribution should identify the original source and explain whether the code was used directly or adapted.

---

## Learning Versus Copying

Using documentation to understand a technology or programming concept does not automatically mean that every implementation requires individual code attribution.

For example, learning how Django model relationships, forms or authentication work from official documentation is part of normal software development.

However, where a specific implementation or substantial code example is copied or materially adapted, the relevant source should be acknowledged.

---

## Original Project Logic

Original functionality developed specifically for this project will be clearly distinguishable from third-party functionality.

This is particularly important for assessment evidence relating to original logic.

Potential original project logic includes:

- Service-request workflow
- Role and permission logic
- Technician eligibility logic
- Commercial collection licence-entitlement validation
- Job workflow and status transitions
- Invoice/payment business logic
- Dynamic JavaScript service-request forms
- Dynamic location forms
- Collection/delivery interactions
- JavaScript fallback behaviour

The final README will explain significant original logic and provide appropriate implementation and testing evidence.

---

## AI-Assisted Development

AI-assisted development tools may be used as part of the development and learning process where permitted by the course and assessment rules.

Any required declaration of AI-assisted development will follow the current Code Institute or assessment requirements applicable at submission time.

AI-generated or AI-assisted suggestions will not be accepted into the project solely because they were generated.

Code entering the project must be:

- Understood
- Reviewed
- Appropriate to the project
- Tested
- Compatible with the existing application
- Consistent with project security and quality requirements

The developer remains responsible for the final implementation.

---

## Media and Images

Third-party images, icons, fonts or other media will be checked for appropriate usage rights before being included in the final application.

Where attribution is required, information should be recorded when the resource is selected.

Relevant information may include:

- Resource name
- Creator
- Source
- Licence
- Required attribution
- Location within the application

This avoids relying on reconstructing the origin of project media at the end of development.

---

## Attribution Record

A simple attribution record will be maintained during development where useful.

A possible structure is:

| Resource | Source | Usage | Project Location | Attribution Required |
| --- | --- | --- | --- | --- |
| Django | Official Django project | Web framework | Application-wide | README technology section |
| Stripe | Official Stripe service/documentation | Test payments | Payments app | README / credits |
| External media | Recorded when selected | UI content | Relevant template/static directory | According to licence |

Additional resources will be added as they are introduced.

The final attribution table will reflect resources actually used rather than resources considered during planning.

---

## Separation of Original and External Work

The project documentation should allow an assessor to distinguish between:

```text
Third-Party Technology
        ↓
Integration / Configuration
        ↓
Original Application Logic
        ↓
Testing and Evidence
```

Using third-party technology does not reduce the importance of demonstrating original implementation.

Where external technology performs a specialised function, the project will explain the original application logic built around that technology.

---

## Source Comments

Source-code comments may be used where they provide useful attribution or clarification.

Comments should be particularly considered where:

- A specific snippet has been adapted
- An unusual solution originated from an external source
- Licence terms require attribution
- The source would otherwise be difficult to identify from the README

Comments will not be added unnecessarily to standard framework usage merely to increase apparent documentation.

---

## Final Attribution Audit

Before submission, the project will be reviewed for external resources.

The audit will check:

- Frameworks and libraries documented
- External APIs documented
- Adapted/copied code appropriately attributed
- Media sources recorded
- Required licences or attribution respected
- Credits section complete
- Original logic clearly identified
- External functionality not represented as original work
- AI declaration requirements checked against current assessment rules
- Dead or unused external resources removed from documentation

---

## Planned Evidence

Evidence for this requirement will include:

- README Technologies section
- README External APIs and Libraries section
- README Credits and Attribution section
- Source comments where appropriate
- Media attribution records
- External-resource attribution table
- Original Python logic documentation
- Original JavaScript documentation
- Testing evidence for original functionality
- Appropriate Git history
- AI declaration where required by current assessment rules

**Status: PLANNED**

# Assessment Criteria Traceability

The project will be audited throughout development against the published assessment criteria for Unit 4: Full Stack Frameworks with Django.

The purpose of this section is to provide a direct relationship between:

```text
Assessment Criterion
        ↓
Project Design
        ↓
Implementation
        ↓
Testing
        ↓
Evidence
```

This traceability record is a planning and development tool.

A final assessment evidence matrix will be included in the completed project documentation and will describe the functionality that was actually implemented.

---

# Learning Outcome 1

## Design, Develop and Implement a Full Stack Django Application

### Criterion 1.1 — Full Stack Application Design

**Assessment focus:**  
Design a Full Stack web application using Django that incorporates a relational database and multiple apps representing potentially reusable components.

**P4 Plan:**

Almac & Sons Mobile Fitting Services will be developed as a brand-new Django project.

Working Django project:

```text
almac_mobile
```

Planned Django apps:

```text
core
accounts
assistance
payments
```

Each app represents a genuine application responsibility rather than being created solely to increase the number of Django apps.

The application will use a relational database with related domain models.

**Planned Evidence:**

- Project architecture documentation
- Django app structure
- App responsibility descriptions
- Database design
- ERD
- Git history showing creation and development of the project/apps
- Final README architecture section

**Status: PLANNED**

---

### Criterion 1.2 — Front-End Design, UX and Accessibility

**Assessment focus:**  
Design the front end so that it meets accessibility guidelines, follows UX principles, satisfies the application's purpose and provides appropriate user interactions.

**P4 Plan:**

The interface will be designed around the needs of the application's principal users:

- Private customers
- Business / fleet customers
- Technicians
- Dispatcher / Staff users
- Manager / Supervisor users

UX planning will include:

- User stories
- User journeys
- Information hierarchy
- Wireframes
- Navigation design
- Responsive layouts
- User feedback
- Error handling
- Accessibility
- Role-appropriate interfaces

The application will avoid requesting information already available from an authenticated user's account where that information can safely and appropriately be reused.

**Planned Evidence:**

- User stories
- User journeys
- Wireframes
- Design decisions
- Desktop testing
- Tablet testing
- Mobile testing
- Keyboard-navigation testing
- Focus-state testing
- Colour-contrast testing
- Semantic HTML review
- Screenshots of representative workflows
- README UX section

**Status: PLANNED**

---

### Criterion 1.3 — Full Stack Django Implementation

**Assessment focus:**  
Develop and implement a Django Full Stack application containing a relational database, interactive front end and multiple apps.

**P4 Plan:**

The completed application will connect the Django back end, relational data model and interactive front end through real business workflows.

The principal workflow is planned as:

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

CRUD operations and changes to application data will be reflected appropriately in the user interface.

**Planned Evidence:**

- Working Django application
- Relational models
- Views
- Templates
- Forms
- Interactive JavaScript
- CRUD evidence
- Functional tests
- Deployed application
- README feature documentation

**Status: PLANNED**

---

### Criterion 1.4 — Validated Create and Edit Forms

**Assessment focus:**  
Implement at least one validated form allowing users to create and edit back-end models.

**P4 Plan:**

The application will contain multiple validated Django forms supporting genuine business operations.

Potential examples include:

- Customer profile management
- Vehicle / equipment management
- Service requests
- Service locations
- Collection / delivery information
- Job updates where permitted

Validation will be enforced on the server side.

JavaScript may improve the user experience but will not replace authoritative Django validation.

**Planned Evidence:**

- Django forms
- Create workflow
- Edit workflow
- Valid submission tests
- Invalid submission tests
- Validation messages
- Server-side validation tests
- README CRUD/testing evidence

**Status: PLANNED**

---

### Criterion 1.5 — Django File Structure

**Assessment focus:**  
Use a consistent and logical file structure following Django conventions.

**P4 Plan:**

The project will follow standard Django conventions while maintaining clear separation between application responsibilities.

Files and directories will use descriptive, consistent naming.

Static resources will be organised logically and HTML, CSS, JavaScript and Python will remain appropriately separated.

**Planned Evidence:**

- Repository structure
- Django project structure
- App structure
- Static-file organisation
- Template organisation
- Final repository audit

**Status: PLANNED**

---

### Criterion 1.6 — Clean Code

**Assessment focus:**  
Write code demonstrating characteristics of clean code.

**P4 Plan:**

Project code will use:

- Consistent naming conventions
- Descriptive class, function and variable names
- Consistent formatting
- Appropriate separation of concerns
- Logical file organisation
- Appropriate comments
- Minimal unnecessary duplication
- Semantic HTML
- Separate linked CSS and JavaScript
- Python style consistent with PEP8

Validation and code-quality checks will form part of the testing process.

**Planned Evidence:**

- Code review
- Python style checks
- HTML validation
- CSS validation
- JavaScript linting
- Appropriate source comments
- Repository structure
- Final code-quality audit

**Status: PLANNED**

---

### Criterion 1.7 — Consistent Application URLs

**Assessment focus:**  
Define application URLs consistently.

**P4 Plan:**

URL patterns will use descriptive and consistent naming appropriate to each Django app and business workflow.

URL design will support intuitive navigation and maintain clear separation between application areas.

**Planned Evidence:**

- Django URL configuration
- Named URL patterns
- Template URL usage
- Navigation testing
- Broken-link testing
- Back/forward browser-navigation testing

**Status: PLANNED**

---

### Criterion 1.8 — Main Navigation and Structured Layout

**Assessment focus:**  
Provide a main navigation menu and structured application layout.

**P4 Plan:**

A shared Django base template will provide the principal site structure.

Navigation will adapt appropriately to authentication state and operational role.

Detailed functionality will be accessed through role-specific dashboards rather than placing every available operation in the main navigation.

The interface will remain usable across desktop, tablet and mobile layouts.

**Planned Evidence:**

- `base.html`
- Main navigation
- Role-aware navigation
- Role dashboards
- Responsive testing
- Keyboard-navigation testing
- Active/focus-state evidence
- Screenshots

**Status: PLANNED**

---

### Criterion 1.9 — Original Python Logic

**Assessment focus:**  
Include custom logic demonstrating proficiency in Python.

**P4 Plan:**

Original Python logic will solve genuine business problems within the application rather than being added solely to satisfy the assessment criterion.

Potential examples include:

- Technician eligibility
- Service capability matching
- Commercial vehicle licence-entitlement validation
- Job workflow rules
- Role/ownership restrictions
- Invoice/payment workflow rules

Final documentation will identify the original logic actually implemented.

**Planned Evidence:**

- Original Python source code
- Explanation of business logic
- Automated tests
- Positive and negative scenarios
- Git development history
- README Original Logic section

**Status: PLANNED**

---

### Criterion 1.10 — Python Compound Statements

**Assessment focus:**  
Use Python functions containing compound statements such as conditions and/or loops.

**P4 Plan:**

Conditions and loops will be used where naturally required by the application's business rules.

They will not be inserted artificially merely to demonstrate language syntax.

Likely examples occur within:

- Technician eligibility
- Permission/business-rule checks
- Service-request processing
- Job workflow
- Invoice/payment processing

**Planned Evidence:**

- Relevant Python functions
- Automated tests
- Code-quality review
- README explanation of significant original logic

**Status: PLANNED**

---

### Criterion 1.11 — Testing

**Assessment focus:**  
Design and implement manual or automated procedures assessing functionality, usability, responsiveness and data management.

**P4 Plan:**

Testing will be planned as part of development rather than performed only immediately before submission.

Testing will include:

- Functional testing
- Model testing
- Form validation
- CRUD
- Authentication
- Authorisation
- Object ownership
- Business rules
- Original Python logic
- JavaScript interactions
- Stripe
- Error handling
- Responsive behaviour
- Accessibility
- Browser behaviour
- Data integrity

Both successful and unsuccessful scenarios will be tested.

---

## Test-Driven Development

Where appropriate original Python and/or JavaScript functionality is suitable for automated testing, development will use a demonstrable Test Driven Development process.

The intended cycle is:

```text
DESIGN BEHAVIOUR
      ↓
WRITE TEST
      ↓
RUN TEST
      ↓
RED — EXPECTED FAILURE
      ↓
IMPLEMENT MINIMUM FUNCTIONALITY
      ↓
RUN TEST
      ↓
GREEN — TEST PASSES
      ↓
REFACTOR
      ↓
RUN TESTS AGAIN
      ↓
DOCUMENT
      ↓
COMMIT
      ↓
CLEAN TREE
```

TDD evidence must arise naturally during implementation and must not be reconstructed retrospectively for assessment purposes.

Git commits should provide supporting evidence of the testing and implementation sequence where practical.

Manual testing will continue to be used for areas such as:

- UX
- Responsive behaviour
- Accessibility
- Browser interaction
- Visual feedback
- End-to-end workflows

Automated and manual testing therefore complement one another rather than one replacing the other.

**Planned Evidence:**

- Automated test files
- Red/Green/Refactor development evidence
- Git commits
- Manual testing records
- Responsive testing at desktop/tablet/mobile sizes
- Accessibility testing
- Validation testing
- CRUD testing
- Permission testing
- Error/fallback testing
- Final testing documentation

**Status: PLANNED**

---

## Learning Outcome 1 Audit

| Criterion | Primary P4 Coverage | Evidence Required | Planning Status |
| --- | --- | --- | --- |
| 1.1 | New Django project, relational DB, multiple domain apps | Architecture, apps, ERD, Git | PLANNED |
| 1.2 | UX, accessibility, responsive role-based interfaces | Wireframes, user stories, accessibility/responsive tests | PLANNED |
| 1.3 | Django + relational DB + interactive front end | Application, models, templates, tests, deployment | PLANNED |
| 1.4 | Validated create/edit forms | Forms and positive/negative tests | PLANNED |
| 1.5 | Conventional Django structure | Repository/app structure | PLANNED |
| 1.6 | Clean code | Validators, linters, style/code review | PLANNED |
| 1.7 | Consistent URLs | URL configuration and link/navigation tests | PLANNED |
| 1.8 | Main navigation and structured layout | Base template, role navigation, responsive evidence | PLANNED |
| 1.9 | Original Python business logic | Source, tests, explanation, Git history | PLANNED |
| 1.10 | Genuine conditions/loops | Python implementation and tests | PLANNED |
| 1.11 | Comprehensive manual/automated testing and TDD | Tests, records, Git history | PLANNED — TDD now explicit |

# Learning Outcome 3

## Authentication, Authorisation and Permissions

### Criterion 3.1 — Authentication

**Assessment focus:**  
Implement an authentication mechanism allowing users to register and log in, with a clear reason why users need to authenticate.

**P4 Plan:**

Django authentication will provide the underlying authentication mechanism for Almac & Sons Mobile Fitting Services.

Authentication is necessary because the application contains personal, operational and transactional information that must be associated with the correct user and protected from unauthorised access.

Authenticated customer functionality is expected to include:

- Managing account/profile information
- Managing vehicles / equipment
- Creating service requests
- Viewing existing service requests
- Viewing relevant job progress
- Viewing invoices
- Making payments
- Accessing paid receipts / final paid invoices

Authentication also provides the identity required for internal operational roles.

The principal operational roles are:

```text
Customer
Technician
Dispatcher / Staff
Manager / Supervisor
```

Private and Business / Fleet represent customer account types rather than separate permission roles.

---

## Customer Registration

Public registration will be available only for customer accounts.

The planned public registration choices are:

```text
Private Customer

Business / Fleet Customer
```

Registration will create the appropriate authenticated customer account/profile structure.

Internal operational accounts will not be publicly self-registerable.

**Planned Evidence:**

- Registration implementation
- Login implementation
- Logout implementation
- Private customer registration
- Business / fleet registration
- Authentication tests
- Protected-page tests
- README explanation of why authentication is required

**Status: PLANNED**

---

### Criterion 3.2 — Anonymous-Only Login and Registration

**Assessment focus:**  
Ensure login and registration pages are available only to anonymous users.

**P4 Plan:**

Login and registration will be accessible to anonymous users.

Once authenticated, users will not be permitted to use the login or public registration workflows again.

The restriction will be enforced by application logic rather than merely hiding navigation links.

Expected behaviour:

```text
Anonymous User
    ↓
Login       → ALLOWED
Registration → ALLOWED
```

```text
Authenticated User
    ↓
Login       → REDIRECTED / RESTRICTED
Registration → REDIRECTED / RESTRICTED
```

The final implementation will provide an appropriate destination and useful user experience for authenticated users who attempt to access these routes.

**Planned Evidence:**

- Anonymous login test
- Anonymous registration test
- Authenticated login-route test
- Authenticated registration-route test
- Navigation evidence
- Redirect/feedback evidence

**Status: PLANNED**

---

### Criterion 3.3 — Protected Data Access

**Assessment focus:**  
Prevent non-admin users from accessing the data store directly without going through the application's controlled code.

**P4 Plan:**

Application data will be accessed through controlled Django functionality.

Regular users will not receive direct database access.

Access to records will be governed by:

```text
Authentication
      ↓
Role
      ↓
Permission
      ↓
Object Ownership / Responsibility
      ↓
Business Rules
```

Hiding a link or button will not be treated as sufficient security.

Server-side code must independently verify that the requesting user is authorised to perform the requested action.

For example:

```text
Customer A
    ↓
Requests Customer A ServiceRequest
    ↓
ALLOWED
```

```text
Customer A
    ↓
Attempts Customer B ServiceRequest by changing URL/object ID
    ↓
DENIED
```

Similar restrictions will apply to update and delete operations.

Internal roles will receive only the access appropriate to their responsibilities.

**Planned Evidence:**

- Authentication-required tests
- Role-permission tests
- Object-ownership tests
- Direct URL manipulation tests
- Cross-account access tests
- Create/read/update/delete permission tests
- Appropriate 403/404 behaviour where applicable
- Security documentation

**Status: PLANNED**

---

## Internal Account Provisioning

The internal operational roles are:

- Technician
- Dispatcher / Staff
- Manager / Supervisor

These roles will not be available through public self-registration.

Only an appropriately authorised Manager / Supervisor will be able to create or assign internal operational accounts and roles.

A customer must not be able to promote themselves to:

- Technician
- Dispatcher / Staff
- Manager / Supervisor

A Technician or Dispatcher / Staff user must not be able to grant themselves Manager / Supervisor privileges.

These restrictions will be enforced server-side.

**Planned Evidence:**

- Internal account creation workflow
- Role-assignment permissions
- Customer self-promotion negative test
- Technician self-promotion negative test
- Dispatcher / Staff privilege-escalation negative test
- Manager / Supervisor positive test

**Status: PLANNED**

---

## Role-Based Authorisation

Authentication and authorisation will be treated as separate concepts.

```text
Authentication
WHO is the user?

        ↓

Authorisation
WHAT may this user do?

        ↓

Object-Level Permission
WHICH records may this user act upon?
```

The planned responsibility boundaries are:

### Customer

May access appropriate functionality relating to their own:

- Profile/account
- Vehicles / equipment
- Service requests
- Jobs where customer visibility is appropriate
- Invoices
- Payments
- Paid receipts

Customers must not access another customer's protected records.

### Technician

May access operational information required for assigned work.

Potential functionality includes:

- Assigned jobs
- Current job
- Appropriate service/location information
- Job-status updates
- Work/completion information
- Job history where appropriate

Technicians must not receive unrestricted access to unrelated customer, financial or management information.

### Dispatcher / Staff

May manage appropriate operational information such as:

- Incoming requests
- Active jobs
- Scheduled jobs
- Technician allocation
- Customer/asset information required for operations

Dispatcher / Staff users must not automatically receive unrestricted Manager / Supervisor permissions.

### Manager / Supervisor

May perform broader authorised operational and management functions, potentially including:

- Staff/role management
- Technician management
- Operational oversight
- Customer/asset management where appropriate
- Invoice/payment oversight
- Reporting
- Other restricted management functions

The exact permission matrix will be finalised during implementation.

---

## Principle of Least Privilege

Users should receive the access required to perform their role without receiving unnecessary additional permissions.

The application will therefore avoid treating every authenticated internal user as an unrestricted administrator.

Django's technical administration functionality and the application's operational Manager / Supervisor role will remain conceptually distinct.

---

# Merit Criterion M(vi) — Django Template Syntax and Appropriate Placement of Logic

**Assessment focus:**  
Demonstrate solid understanding of Django template syntax and place logic in the component where it is best suited.

**P4 Plan:**

The application will follow Django conventions and maintain appropriate separation between:

```text
Models
   ↓
Data structure and model-level rules

Views / Application Logic
   ↓
Request handling and workflow/business logic

Forms
   ↓
Input handling and validation

Templates
   ↓
Presentation and appropriate display logic

JavaScript
   ↓
Client-side UX enhancement
```

Templates may use appropriate Django template functionality such as:

- Template inheritance
- URL tags
- Static tags
- Conditional presentation
- Loops
- Context variables
- Reusable template components where appropriate

Complex business or data-handling logic will not be placed in templates simply because Django template syntax makes some logic possible.

Similarly, security decisions will not rely on template conditions alone.

For example:

```django
{% if user_can_edit %}
    <!-- display edit control -->
{% endif %}
```

may improve the interface, but the corresponding Django view must still verify permission if the user directly requests the edit URL.

---

## Shared Template Structure

A shared `base.html` is planned to provide consistent:

- Document structure
- Header
- Navigation
- Main content area
- Feedback/messages
- Footer
- Shared static resources

Individual templates will extend the shared structure rather than unnecessarily duplicating complete page layouts.

Role-aware presentation will be used where appropriate while server-side authorisation remains authoritative.

---

## User Feedback

Authenticated and data-changing operations will provide appropriate feedback.

Examples may include:

- Registration confirmation
- Login/logout feedback
- Record-created confirmation
- Record-updated confirmation
- Cancellation confirmation
- Validation errors
- Permission/access feedback
- Payment success
- Payment failure/cancellation

Feedback will be clear and useful rather than exposing unnecessary internal technical details.

---

## Permission Testing Strategy

Permission testing will include both positive and negative scenarios.

For each important protected operation, testing should ask both:

```text
Should this user be allowed?
```

and:

```text
Who must NOT be allowed?
```

Example:

| Scenario | Expected Result |
| --- | --- |
| Customer views own request | Allowed |
| Customer views another customer's request | Denied |
| Customer edits permitted own record | Allowed |
| Customer edits another customer's record | Denied |
| Anonymous user accesses protected account page | Redirected/denied |
| Technician accesses assigned operational data | Allowed |
| Technician attempts restricted management action | Denied |
| Dispatcher performs authorised dispatch action | Allowed |
| Dispatcher attempts restricted manager action | Denied |
| Manager performs authorised role-management action | Allowed |

The final matrix will reflect the functionality actually implemented.

---

# Learning Outcome 3 — Distinction Alignment

The authentication and authorisation design will aim to demonstrate the Distinction characteristics relating to security, user control and appropriate access.

In particular:

- Authentication-required functionality will be protected.
- Users will have permissions appropriate to their responsibilities.
- Customers will not be able to access another customer's protected records.
- Internal users will not automatically receive unrestricted privileges.
- Public users will not be able to create privileged internal accounts.
- Security will be enforced server-side.
- Template logic will improve presentation without replacing authorisation checks.
- Data access will follow the application's controlled Django logic.
- User actions will receive appropriate feedback.
- Authentication and authorisation behaviour will be comprehensively tested.

The aim is to demonstrate a genuine role-based application rather than merely the existence of a login page.

---

# Learning Outcome 3 Audit

| Criterion | Primary P4 Coverage | Evidence Required | Planning Status |
| --- | --- | --- | --- |
| 3.1 | Django authentication with private/business customer registration and protected functionality | Registration/login/logout implementation and tests | PLANNED |
| 3.2 | Login/registration restricted to anonymous users | Positive and negative route tests | PLANNED |
| 3.3 | Controlled server-side data access | Ownership, permission and URL-manipulation tests | PLANNED |
| M(vi) | Appropriate Django template syntax and separation of logic | Templates, views/forms/models, code review and tests | PLANNED |

