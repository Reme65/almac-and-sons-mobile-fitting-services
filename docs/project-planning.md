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
