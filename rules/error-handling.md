---
description: "Error handling patterns for {{LANGUAGE}}/{{FRAMEWORK}}"
---

# Error Handling

## Principles

1. **Catch specific errors**, not generic exceptions
2. **Fail fast** - detect and report errors early
3. **Provide context** - include relevant information in errors
4. **Log appropriately** - don't swallow errors silently
5. **Clean up resources** - use try/finally or language equivalents
6. **Be user-friendly** - return helpful error messages to users

## {{LANGUAGE}} Error Patterns

### Error Types/Exceptions
- [PLACEHOLDER: Language-specific error handling. Examples:
  - For TypeScript: Use Error subclasses, throw typed errors
  - For Python: Use specific exception types (ValueError, TypeError, etc.)
  - For Go: Use error interface, wrap errors with context
  - For Java: Use exception hierarchy, prefer unchecked for runtime errors]

- Use custom error/exception types for domain-specific errors
- Include context in error messages (what operation failed, why)
- Preserve error chains/stack traces when re-throwing

### Error Propagation
- [PLACEHOLDER: How errors bubble up. Examples:
  - For TypeScript/Java: throw exceptions, catch at appropriate level
  - For Python: raise exceptions, catch at handler level
  - For Go: return errors, check and handle at each level
  - For Rust: return Result types, use ? operator]

- Wrap errors with additional context when rethrowing
- Don't catch errors you can't handle
- Let errors bubble up to appropriate handler

## {{FRAMEWORK}} Error Patterns

### API Error Responses

Return consistent error format:
```{{LANGUAGE}}
// [PLACEHOLDER: Framework-specific error response format]
// Include: status code, error code, message, details
// Example structure:
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [...],
    "requestId": "..."
  }
}
```

### Validation Errors

- Validate input at system boundaries (API layer)
- Return all validation errors, not just the first one
- Use {{FRAMEWORK}}'s validation mechanisms
- [PLACEHOLDER: Framework-specific validation. Examples:
  - For Express: Use express-validator or joi
  - For Django REST: Use serializer validation
  - For Spring: Use @Valid and ConstraintValidator
  - For Gin: Use binding tags]

### Database Errors

- Catch database-specific exceptions
- Log full error details for debugging
- Return safe, user-friendly message to client
- Handle common cases:
  - Connection errors
  - Constraint violations
  - Deadlocks (retry logic)
  - Query timeout

### External Service Errors

- Use timeouts for external API calls
- Implement retry logic with exponential backoff
- Have fallback behavior when possible
- Log external service failures with context

## Common Patterns

### 1. Try-Catch-Finally / Defer


### 2. Graceful Degradation

When non-critical operations fail:
- Log the error
- Return partial result or cached data
- Continue operation
- Don't fail entire request


### 3. Circuit Breaker Pattern

For unreliable external services:
- Track failure rate
- Open circuit after threshold
- Fail fast while circuit open
- Periodically retry to check if recovered

## Logging Errors

### What to Log

- Error message and type
- Stack trace
- Request context (ID, user, endpoint)
- Input parameters (sanitized)
- Timestamp
- Environment info

### Log Levels

- **ERROR**: Unexpected failures requiring attention
- **WARNING**: Handled errors that might indicate problems
- **INFO**: Expected error conditions (e.g., validation failures)


## Error Recovery

### 1. Transient Failures

For temporary issues (network, rate limits):
- Implement retry with exponential backoff
- Set maximum retry attempts
- Log each retry attempt
- Eventually give up and return error


### 2. Partial Failures

For operations with multiple steps:
- Use transactions where possible
- Implement compensation/rollback logic
- Track which steps completed
- Enable retry from failure point

## 3. Anti-Patterns to Avoid

- Swallowing Errors
- Generic Error Handling
- Logging Without Context
- Exposing Internal Errors

## Cross-References

- Coding practices: See `coding-practices.md`
- Logging patterns: See `coding-practices.md#logging`
