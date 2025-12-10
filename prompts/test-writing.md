---
name: "Test Writing Template"
category: "testing"
description: "Write comprehensive tests for {{FRAMEWORK}} applications using {{TEST_FRAMEWORK}}"
version: "1.0"
variables:
  - name: "component_name"
    description: "Component to test (e.g., 'UserService', 'OrderController', 'PaymentHandler')"
    required: true
  - name: "test_type"
    description: "Type of test: 'unit', 'integration', 'end-to-end', 'api'"
    required: true
  - name: "coverage_areas"
    description: "Specific areas to cover (e.g., 'validation, edge cases, error handling')"
    required: false
---

# Test Writing Template

## Context

This template guides writing comprehensive tests for {{FRAMEWORK}} applications using {{LANGUAGE}} and {{TEST_FRAMEWORK}}. Tests should follow the Arrange-Act-Assert pattern, use descriptive names, cover edge cases, and align with the project's testing conventions.

### Testing Framework: {{TEST_FRAMEWORK}}

### Test Coverage Goals
- Happy path (normal operation with valid inputs)
- Edge cases (boundary conditions, empty inputs, large datasets)
- Error cases (invalid input, permissions, not found, timeouts)
- Integration with {{DATABASE}} (if applicable)
- Race conditions (for concurrent operations)

## Instructions

### Step 1: Analyze the Component
- Identify component to test: `{{component_name}}`
- Determine test type: `{{test_type}}`
- Review coverage areas: `{{coverage_areas}}`
- Read the implementation code
- Identify test scenarios (happy path, edge cases, errors)

### Step 2: Setup Test Environment
- Choose appropriate test setup for {{TEST_FRAMEWORK}}
- Create test fixtures or factory functions for test data
- Set up mocks for external dependencies
- Configure test database or data storage if needed
- Set up authentication/authorization context if testing API endpoints

### Step 3: Write Test Cases

For each test method:
1. **Arrange**: Set up test data and preconditions
2. **Act**: Execute the code under test
3. **Assert**: Verify expected outcomes

Follow naming convention appropriate for {{LANGUAGE}}:
- Descriptive test names: `test_[method]_[scenario]_[expected_result]`
- Or BDD style: `should_[expected_behavior]_when_[condition]`

### Step 4: Cover Key Scenarios

**For Unit Tests:**
- Test each function/method in isolation
- Mock external dependencies
- Focus on business logic correctness
- Test return values and side effects

**For Integration Tests:**
- Test component interactions
- Use real or test {{DATABASE}} instance
- Verify data persistence
- Test transaction behavior

**For API/Endpoint Tests:**
- Test all HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Verify authentication and authorization
- Test request validation
- Check response format and status codes
- Test pagination and filtering

**For End-to-End Tests:**
- Test complete user workflows
- Use realistic test data
- Verify multiple components working together
- Test happy paths and critical error paths

### Step 5: Add Edge Cases and Error Tests
- Null/undefined/empty inputs
- Boundary values (min, max, zero, negative)
- Invalid data types
- Missing required fields
- Permission denied scenarios
- Not found scenarios
- Timeout or network error scenarios

### Step 6: Review Test Quality
- Descriptive test names that explain what they verify
- One assertion focus per test (generally)
- No interdependencies between tests
- Fast execution
- Deterministic results (no flaky tests)
- Meaningful coverage (not just high percentage)

## Constraints

- **Arrange-Act-Assert**: Follow this pattern consistently
- **Descriptive Names**: Test names should describe what they verify
- **Isolation**: Tests should not depend on each other or execution order
- **Fast**: Keep tests fast by using mocks and in-memory databases
- **Deterministic**: Tests should produce same results every run
- **Clean Assertions**: Use appropriate assertion methods from {{TEST_FRAMEWORK}}
- **Coverage**: Aim for meaningful coverage of important code paths

## Expected Output

### Test File Structure
```{{LANGUAGE}}
// [PLACEHOLDER: Test file structure for {{TEST_FRAMEWORK}}]
// Include:
// - Imports
// - Test class/describe blocks
// - Setup/teardown methods
// - Test methods with descriptive names
// - Helper functions if needed
```

### Coverage Summary
- Number of test cases written
- Scenarios covered (happy path, edge cases, errors)
- Integration points tested
- Any uncovered edge cases with reasoning

### Quality Checklist
- [ ] Descriptive test names
- [ ] Clear documentation of what each test verifies
- [ ] Arrange-Act-Assert pattern followed
- [ ] Appropriate assertions using {{TEST_FRAMEWORK}}
- [ ] Edge cases covered
- [ ] Error cases covered
- [ ] No test interdependencies
- [ ] Fast execution (< [appropriate time] for unit tests)
- [ ] All tests pass

