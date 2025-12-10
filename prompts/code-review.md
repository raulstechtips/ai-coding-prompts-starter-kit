---
name: "Code Review Template"
category: "review"
description: "Systematic code review for {{LANGUAGE}}/{{FRAMEWORK}} applications"
version: "1.0"
variables:
  - name: "files_to_review"
    description: "Files or PR diff to review"
    required: true
  - name: "review_focus"
    description: "Areas to focus on: 'security', 'performance', 'readability', 'all'"
    required: false
---

# Code Review Template

## Context

This template guides systematic code review for {{LANGUAGE}}/{{FRAMEWORK}} applications. Reviews should focus on correctness, maintainability, performance, and security while being constructive and helpful.

## Instructions

### Step 1: Understand the Change
- Read files/diff: `{{files_to_review}}`
- What is the purpose of this change?
- What problem does it solve?
- What are the expected behaviors?
- Review any linked issues or requirements

### Step 2: Review for Correctness
- Does the code do what it claims to do?
- Are edge cases handled properly?
- Is error handling appropriate for {{FRAMEWORK}}?
- Are there potential bugs or logic errors?
- Does it handle null/undefined/empty cases?

### Step 3: Review for {{LANGUAGE}} Best Practices
- Follows {{LANGUAGE}} style conventions and idioms
- Uses idiomatic {{FRAMEWORK}} patterns
- Proper use of {{LANGUAGE}}'s type system (if applicable)
- Appropriate error handling patterns for {{LANGUAGE}}
- Follows DRY (Don't Repeat Yourself) principle

### Step 4: Review for Security
- Input validation present and comprehensive
- Authentication/authorization checks correct
- No sensitive data exposed in logs or responses
- SQL injection prevention (if using {{DATABASE}})
- XSS prevention (if applicable)
- CSRF protection (if web app)
- {{FRAMEWORK}}-specific security patterns followed

### Step 5: Review for Performance
- No N+1 queries (if using {{ORM}})
- Appropriate use of caching
- Resource cleanup (connections, file handles, etc.)
- No blocking operations where async expected
- Efficient algorithms and data structures
- Proper indexing for {{DATABASE}} queries

### Step 6: Review for Maintainability
- Code is readable and self-documenting
- Functions/methods are appropriately sized
- No unnecessary code duplication
- Clear variable and function names
- Sufficient comments for complex logic
- Test coverage adequate
- Documentation updated if needed

### Step 7: Review Testing
- Are there tests for new functionality?
- Do tests cover happy path and edge cases?
- Are tests using {{TEST_FRAMEWORK}} correctly?
- Are mocks used appropriately?
- Do tests actually test the right things?

## Constraints

- **Be Constructive**: Suggest improvements, don't just criticize
- **Be Specific**: Point to exact lines and explain the issue
- **Prioritize**: Distinguish between "must fix" and "nice to have"
- **Consider Context**: Understand the bigger picture and constraints
- **Reference Standards**: Link to style guides or documentation

## Review Checklist

### Correctness
- [ ] Logic is correct and handles edge cases
- [ ] Error handling is appropriate
- [ ] No obvious bugs

### Code Quality
- [ ] Follows {{LANGUAGE}}/{{FRAMEWORK}} conventions
- [ ] Code is readable and maintainable
- [ ] No unnecessary complexity
- [ ] Appropriate comments where needed

### Security
- [ ] Input validation present
- [ ] Authentication/authorization correct
- [ ] No security vulnerabilities

### Performance
- [ ] No obvious performance issues
- [ ] Database queries optimized
- [ ] Resources properly managed

### Testing
- [ ] New code has test coverage
- [ ] Tests are meaningful
- [ ] Existing tests still pass

### Documentation
- [ ] Code is well-documented
- [ ] API changes documented
- [ ] README updated if needed

## Expected Output

### Review Summary

**Approval Status**: [Approve / Request Changes / Comment]

**Overall Assessment**: [1-2 sentence summary of the changes]

### Critical Issues (Must Fix)

List any blocking issues that must be addressed:

1. **[Issue Title]**
   - **Location**: [File and line number]
   - **Problem**: [Description of the issue]
   - **Suggestion**: [How to fix it]
   - **Reason**: [Why this is important]

### Questions

List any clarifications needed:

1. **[Question]**
   - **Context**: [Why you're asking]
   - **Impact**: [How answer affects review]
