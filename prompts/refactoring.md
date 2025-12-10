---
name: "Refactoring Template"
category: "refactor"
description: "Systematic refactoring for {{LANGUAGE}}/{{FRAMEWORK}} applications"
version: "1.0"
variables:
  - name: "target_code"
    description: "Code, file, or module to refactor"
    required: true
  - name: "refactoring_goal"
    description: "What to improve: 'readability', 'performance', 'modularity', 'maintainability'"
    required: true
  - name: "constraints"
    description: "What must remain unchanged (API contracts, behavior, etc.)"
    required: false
---

# Refactoring Template

## Context

This template guides systematic refactoring in {{LANGUAGE}}/{{FRAMEWORK}} applications. Refactoring improves code structure while preserving behavior. It emphasizes small, safe changes with tests validating each step.

## Instructions

### Step 1: Understand Current State
- Review target code: `{{target_code}}`
- What does the code currently do?
- What are its dependencies?
- What tests exist for this code?
- What is the public API/contract?
- What are the pain points?

### Step 2: Define Target State
- Refactoring goal: `{{refactoring_goal}}`
- What specific improvements to make?
- What patterns should be applied?
- What {{FRAMEWORK}} conventions should be followed?
- What are the constraints: `{{constraints}}`

### Step 3: Plan Refactoring Steps
- Break down into smallest safe changes
- Order changes to maintain working code throughout
- Identify which tests need updating vs staying same
- Plan for each change to be independently testable
- Consider creating new code alongside old before switching

### Step 4: Execute Refactoring
- Make one logical change at a time
- Run tests after each change
- Commit working states frequently
- Use automated refactoring tools where available
- Keep code working at all times

### Step 5: Validate
- All existing tests pass
- Behavior unchanged (unless intentionally modified)
- Code meets style guidelines for {{LANGUAGE}}
- Performance not regressed (verify if performance-critical)
- API contract preserved (if applicable)

## Constraints

- **Preserve Behavior**: Unless explicitly changing it
- **Maintain Tests**: Tests should pass throughout (update only when necessary)
- **Small Steps**: Each change should be independently reviewable
- **Keep It Working**: Code should remain functional after each change
- **Follow Conventions**: Apply {{FRAMEWORK}}/{{LANGUAGE}} best practices

## Common Refactoring Patterns

### For Readability
- Extract method/function
- Rename variables/functions for clarity
- Break up large functions
- Remove code duplication
- Simplify conditional logic
- Add meaningful comments

### For Performance
- Optimize database queries using {{ORM}}
- Add caching where appropriate
- Reduce unnecessary computations
- Use more efficient algorithms
- Batch operations
- Lazy load data

### For Modularity
- Extract class/module
- Move related functions together
- Reduce coupling between modules
- Apply dependency injection
- Separate concerns

### For Maintainability
- Reduce complexity
- Remove dead code
- Update dependencies
- Standardize patterns
- Improve error handling

## Refactoring Checklist

### Planning
- [ ] Current behavior documented
- [ ] Tests exist for current behavior
- [ ] Refactoring goals clearly defined
- [ ] Constraints identified
- [ ] Steps planned

### Execution
- [ ] Changes made incrementally
- [ ] Tests run after each change
- [ ] Code committed frequently
- [ ] Each commit has working code

### Validation
- [ ] All tests pass
- [ ] Behavior preserved (or intentionally changed)
- [ ] Performance not regressed
- [ ] Code follows {{LANGUAGE}}/{{FRAMEWORK}} conventions
- [ ] Documentation updated if needed

## Expected Output

### 1. Refactored Code
- Improved code meeting the refactoring goal
- All changes applied systematically
- Working, tested code

### 2. Test Updates (if any)
- Updated tests reflecting structural changes
- New tests if refactoring exposed gaps
- All tests passing

### 3. Summary
- What was refactored and why
- Key improvements made
- Any trade-offs or considerations
- Performance impact (if applicable)
- Before/after metrics (lines of code, complexity, performance)

### 4. Migration Notes (if API changed)
- How to update calling code
- Deprecation warnings if phasing out old code
- Timeline for complete migration

