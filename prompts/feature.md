---
name: "Feature Implementation Template"
category: "feature"
description: "Structured approach to implementing new features in {{FRAMEWORK}} applications"
version: "1.0"
variables:
  - name: "feature_name"
    description: "Name of the feature to implement (e.g., 'User Authentication', 'File Upload System')"
    required: true
  - name: "requirements"
    description: "Detailed feature requirements and specifications"
    required: true
  - name: "acceptance_criteria"
    description: "How to verify the feature works correctly"
    required: true
  - name: "implementation_scope"
    description: "Which layer to implement: 'data', 'business', or 'api'"
    required: true
  - name: "affected_modules"
    description: "Which parts of the system will be modified (models, API, services, etc.)"
    required: false
---

# Feature Implementation Template

## Context

This template guides feature implementation in {{FRAMEWORK}} applications using {{LANGUAGE}}, following established architectural patterns including proper separation of concerns, data validation, authentication/authorization, and comprehensive testing.

### {{FRAMEWORK}} Architecture Flow
1. **Data Layer**: Database schema and entities ({{ORM}})
2. **Business Logic Layer**: Service/use case layer
3. **API Layer**: Controllers/handlers + routing configuration

### Implementation Scope
Based on `{{implementation_scope}}`, implement the specified layer:
- **data**: Database models/entities and migrations
- **business**: Service/business logic layer (requires existing data layer)
- **api**: API controllers/handlers and routing (requires existing business layer)

## Instructions

### Step 1: Planning & Design
- Analyze requirements: `{{feature_name}}`
- Review specifications: `{{requirements}}`
- Implementation scope: `{{implementation_scope}}`
- Identify affected modules: `{{affected_modules}}`
- Design components for the layers you're implementing
- Consider security and permissions
- Identify dependencies on other layers

### Step 2: Implement the Specified Layer

**If `{{implementation_scope}}` is 'data':**
- Create or modify {{ORM}} models/entities/schemas
- Define fields with appropriate types and constraints
- Add validation rules at the data layer
- Create indexes for query optimization
- Add model methods for data-related logic
- Create database migrations (if applicable to {{ORM}})
- Include documentation explaining the model purpose

**If `{{implementation_scope}}` is 'business':**
- Create service class/module to encapsulate business logic
- Implement core feature logic (validation, calculations, workflows)
- Handle transactions appropriately for {{DATABASE}}
- Add logging at key decision points
- Keep business logic independent of HTTP/framework context
- Return domain objects or DTOs, not framework-specific responses
- Handle errors and edge cases appropriately

**If `{{implementation_scope}}` is 'api':**
- Create controller/handler/route functions
- Add URL patterns/routes for new endpoints
- Configure authentication and authorization middleware
- Call service layer for business logic (keep controllers thin)
- Handle errors gracefully with proper status codes
- Validate input data at the API boundary
- Use framework's routing conventions
- Follow {{API_STYLE}} best practices (RESTful, GraphQL, gRPC patterns)
- Add API documentation (OpenAPI/Swagger if using {{API_STYLE}})
- Organize routes logically with other endpoints

### Step 3: Documentation
Document the implemented layers:
- Add docstrings/comments to all classes and methods
- For API layer: Document endpoints (parameters, responses, examples)
- Update relevant README or docs if needed
- Include usage examples for your implemented scope

## Constraints

- **Separation of Concerns**: Business logic in services, not in controllers/handlers
- **Framework Conventions**: Follow {{FRAMEWORK}} best practices and patterns
- **Security First**: Implement proper authentication, permissions, and input validation
- **Transaction Safety**: Use transactions for multi-step database operations
- **Query Optimization**: Use {{ORM}} features to avoid N+1 queries
- **Logging**: Add structured logging at INFO level for important actions
- **Type Safety**: Use {{LANGUAGE}}'s type system effectively
- **Testing**: Comprehensive test coverage for all new code

## Expected Output

Deliver output based on `{{implementation_scope}}`:

**If 'data':**
- Model/entity definitions with proper fields, relationships, and constraints
- Database migrations (if applicable to {{ORM}})
- Docstrings on all models and methods
- Brief summary of data layer implementation

**If 'business':**
- Service class(es) with well-documented methods
- Transaction handling for data integrity
- Appropriate logging
- Docstrings on all service methods
- Brief summary of business logic implementation

**If 'api':**
- Controllers/handlers with proper HTTP methods
- URL patterns/routes configured
- Input validation and error handling at API boundary
- Authentication/authorization middleware applied
- API documentation (if applicable)
- Docstrings on all controllers/handlers
- Brief summary of API implementation

**Always include:**
- Summary of what was implemented
- Dependencies on other layers (if any)
- Next steps if implementing incrementally
