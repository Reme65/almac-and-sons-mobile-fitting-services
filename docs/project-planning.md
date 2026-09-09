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