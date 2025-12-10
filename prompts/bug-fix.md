---
name: "Bug Fix Template"
category: "bug-fix"
description: "Systematic approach to identifying, fixing, and validating bugs in {{FRAMEWORK}} applications"
version: "1.0"
variables:
  - name: "component_name"
    description: "Name of the component/file where the bug occurs (e.g., UserService, OrderController, TaskHandler)"
    required: true
  - name: "bug_description"
    description: "Clear description of the bug behavior"
    required: true
  - name: "expected_behavior"
    description: "What should happen"
    required: true
  - name: "actual_behavior"
    description: "What actually happens"
    required: true
  - name: "error_message"
    description: "Any error messages or stack traces (if applicable)"
    required: false
---

# Bug Fix Template

## Context

This template guides systematic bug fixing in {{FRAMEWORK}} applications using {{LANGUAGE}}. It emphasizes root cause analysis over symptomatic fixes, minimal code changes, and proper validation.

### Debugging Approach
1. Reproduce the issue reliably
2. Identify the root cause (not just symptoms)
3. Implement minimal, focused fix
4. Add appropriate logging
5. Validate the fix with tests
6. Ensure no regressions

## Instructions

### Step 1: Analyze the Bug
- Read the component code: `{{component_name}}`
- Understand the bug: `{{bug_description}}`
- Compare expected vs actual: `{{expected_behavior}}` vs `{{actual_behavior}}`
- Review error messages: `{{error_message}}`
- Identify related code (models, services, handlers, controllers)

### Step 2: Root Cause Analysis
- Trace the code flow from entry point to bug location
- Check for common {{FRAMEWORK}} issues:
  - [PLACEHOLDER: Add 5-7 common issues for your framework, such as:]
  - Database query issues (N+1, missing indexes, incorrect joins)
  - Validation errors or missing validation
  - Authentication/authorization issues
  - Race conditions or concurrency bugs
  - Error handling gaps
  - Null/undefined handling
  - Type mismatches (if using typed language)
- Identify the minimal change needed to fix the root cause

### Step 3: Implement Fix
- Make the smallest code change that fixes the root cause
- Follow existing code patterns and conventions
- Add logging using {{LANGUAGE}}'s standard logging approach
- Update documentation if behavior changes
- Consider edge cases that might have the same issue

### Step 4: Validation
- Write or update tests using {{TEST_FRAMEWORK}} to cover the bug scenario
- Run existing tests to ensure no regressions
- Manually test the fix if applicable
- Check for similar bugs in related code
- Verify fix works in {{CONTAINER}} environment if applicable

## Constraints

- **Minimal Changes**: Only modify what's necessary to fix the root cause
- **Pattern Consistency**: Follow existing project patterns and conventions
- **No Breaking Changes**: Ensure backward compatibility unless explicitly required
- **Add Logging**: Include appropriate log statements for debugging
- **Test Coverage**: Add tests that would have caught this bug
- **Documentation**: Update docstrings/comments if behavior changes

## Expected Output

### 1. Fixed Code
- Modified file(s) with bug fix applied
- Minimal, focused changes
- Added logging statements where appropriate

### 2. Test Coverage
- New test case(s) that verify the fix
- Tests that would have caught this bug originally
- Confirmation that existing tests still pass

### 3. Summary
- Brief explanation of root cause
- Changes made and why
- Any side effects or considerations
- Related components that might need similar fixes

