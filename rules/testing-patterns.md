---
description: "Testing patterns using {{TEST_FRAMEWORK}}"
---

# Testing Patterns

Follow Arrange-Act-Assert pattern and {{TEST_FRAMEWORK}} conventions for all tests.

## Test Structure

### Arrange-Act-Assert Pattern

1. **Arrange**: Set up test data and preconditions
2. **Act**: Execute the code under test
3. **Assert**: Verify expected outcomes

### Naming Convention

Use descriptive test names: `test_[method]_[scenario]_[expected_result]`

## Test Types

- **Unit Tests**: Test individual functions in isolation with mocked dependencies
- **Integration Tests**: Test component interactions with real {{DATABASE}}
- **End-to-End Tests**: Test complete workflows through the API

## Test Isolation

- Tests should not depend on each other or execution order
- Clean up created resources in teardown
- Use transactions that rollback (if testing database)
- Don't share mutable state between tests

## Code Coverage

- Aim for meaningful coverage, not just high percentages
- Focus on business logic, error handling, and edge cases
- 80%+ coverage for business-critical code

## Best Practices

**Do:**
- Test one thing per test
- Use descriptive test names
- Keep tests fast with mocking
- Test edge cases and error conditions

**Don't:**
- Test implementation details - test behavior
- Write flaky tests
- Share state between tests
- Over-mock - balance unit and integration tests

