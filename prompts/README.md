# Prompt Templates

This directory contains minimalistic prompt templates that guide AI assistants through common development workflows. Each template provides clear, step-by-step instructions without unnecessary examples or bloat, designed to be context-conscious and efficient.

## Available Templates

### Core Templates

**[bug-fix.md](./bug-fix.md)**  
Systematic approach to identifying, fixing, and validating bugs. Emphasizes root cause analysis and minimal changes.

**[feature.md](./feature.md)**  
Structured feature implementation with incremental layer support. Build data, business logic, or API layers independently using `implementation_scope` parameter. Testing handled separately by test-writing.md.

**[test-writing.md](./test-writing.md)**  
Comprehensive test writing following Arrange-Act-Assert pattern. Covers unit, integration, and E2E tests.

**[documentation.md](./documentation.md)**  
Generate clear documentation for code, APIs, guides, and README files. Includes examples and best practices.

### Advanced Templates

**[code-review.md](./code-review.md)**  
Systematic code review covering correctness, security, performance, and maintainability. Provides structured feedback format.

**[refactoring.md](./refactoring.md)**  
Safe refactoring process with small, testable changes. Covers readability, performance, and modularity improvements.

**[migration.md](./migration.md)**  
Guide for schema, data, dependency, and architecture migrations. Includes rollback planning and validation.

## How to Use Templates

### 1. Customize for Your Stack

Replace variables like `{{LANGUAGE}}`, `{{FRAMEWORK}}`, `{{DATABASE}}` with your specific technologies.

**Quick Method:** Use [setup-assistant.md](../setup-assistant.md) to customize one file at a time:

```
@setup-assistant.md

target_file: "prompts/bug-fix.md"
language: "TypeScript"
framework: "Express.js"
...
```

**Manual Method:** Search for `{{VARIABLE}}` and replace with your values.

### 2. Reference in AI Chat

Once customized, reference templates in your AI conversations:

```
@prompts/bug-fix.md

component_name: "UserService"
bug_description: "Returns 500 when email is null"
expected_behavior: "Should return 400 with validation error"
actual_behavior: "Crashes with 500 error"
```

### 3. Fill in Variables

Each template defines variables in its YAML front-matter. Provide values for all required variables.

## Template Structure

Every template follows this structure:

```markdown
---
name: "Template Name"
category: "category"
description: "Brief description"
version: "1.0"
variables: [...]
---

# Template Title

## Context
[Why and how to use this template]

## Instructions
[Step-by-step guidance]

## Constraints
[Requirements and limitations]

## Examples
[Concrete examples]

## Expected Output
[What should be delivered]
```

## Customization Philosophy

### Context-Conscious Design

Templates are intentionally minimalistic to avoid context bloat. Examples are only included when explicitly requested by the template's placeholder sections.

### Fill Placeholders with Framework-Specific Patterns

Replace `[PLACEHOLDER]` sections with patterns specific to your framework:

```markdown
### Step 2: Root Cause Analysis
- Check for common Express.js issues:
  - Async/await without try-catch
  - Middleware order problems
  - Missing error middleware
  - Route parameter validation
```

### Add Only What's Necessary

Don't add verbose examples unless the template explicitly asks for them. The AI already knows your framework - just activate that knowledge with specific patterns and common issues.

## Examples Directory

See [examples/](../examples/) for fully customized reference implementations:

- **[node-express/](../examples/node-express/)** - TypeScript/Express/Prisma
- **[go-gin/](../examples/go-gin/)** - Go/Gin/GORM
- **[java-spring/](../examples/java-spring/)** - Java/Spring Boot/Hibernate

These show exactly how templates look when fully customized.

## Best Practices

### For Bug Fixing
- Always reproduce the bug first
- Identify root cause, not symptoms
- Make minimal changes
- Add tests that would have caught the bug

### For Features
- Use `implementation_scope` to work on one layer at a time (data, business, api)
- Keeps AI focused and context-efficient for smaller models
- Follow your architecture patterns
- Write tests separately using test-writing.md

### For Testing
- Follow Arrange-Act-Assert pattern
- Use descriptive test names
- Test happy path and edge cases
- Keep tests fast and isolated

### For Documentation
- Write for your target audience
- Include practical examples
- Keep it current with code
- Be concise but complete

## Adding Custom Templates

To create project-specific templates:

1. Copy an existing template as starting point
2. Define variables in YAML front-matter
3. Write clear, step-by-step instructions
4. Add concrete examples from your codebase
5. Define expected output format

## Getting Help

- Check [CUSTOMIZATION-GUIDE.md](../CUSTOMIZATION-GUIDE.md) for detailed instructions
- Use [setup-assistant.md](../setup-assistant.md) for AI-assisted customization
- Review [examples/](../examples/) for reference implementations

## Cross-References

- **Rules**: See [rules/](../rules/) for coding standards to follow
- **Setup**: See [setup-assistant.md](../setup-assistant.md) for customization help
- **Guide**: See [CUSTOMIZATION-GUIDE.md](../CUSTOMIZATION-GUIDE.md) for manual customization

