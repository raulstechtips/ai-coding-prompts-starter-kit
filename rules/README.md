# Coding Rules

This directory contains lean rule files that activate AI assistants' existing knowledge about coding standards, patterns, and best practices. Rather than teaching from scratch, these rules are context-activators that remind the AI of relevant patterns for your specific tech stack.

## Available Rules

**[language-style.md](./language-style.md)** _(Template)_  
Generic template for language-specific style guides. Customize with @setup-assistant.md to create style guides for Python, TypeScript, Go, Java, etc. Covers formatting, naming conventions, type systems, design principles, and language-specific best practices.

**[framework-specific.md](./framework-specific.md)** _(Template)_  
Lean template for framework-specific use cases. Create focused rules for Django REST Framework error handling, Express middleware patterns, Spring Boot annotations, etc. Relies on external_references and additional_context to build targeted guidance.

**[coding-practices.md](./coding-practices.md)**  
Language style, naming conventions, framework patterns, logging, and code organization.

**[error-handling.md](./error-handling.md)**  
Error handling patterns, API error responses, validation, and logging errors properly.

**[testing-patterns.md](./testing-patterns.md)**  
Lean test structure, AAA pattern, test types, isolation, and coverage goals. Activates testing knowledge without verbose examples.

**[performance.md](./performance.md)**  
Database optimization, caching, async patterns, memory management, and profiling.

## How to Use Rules

### 1. Customize for Your Stack

Replace variables like `{{LANGUAGE}}`, `{{FRAMEWORK}}`, `{{ORM}}` throughout the rule files.

### 2. AI Assistants Reference Automatically

When you use prompt templates, AI assistants will reference relevant rules automatically. You don't need to explicitly mention them (though you can).

### 3. Reference Explicitly When Needed

```
Review this code following @rules/security.md and @rules/coding-practices.md

[paste code]
```

## Rule File Structure

Each rule file follows this format:

```markdown
---
description: "Brief description with {{VARIABLES}}"
---

# Rule Title

## Section 1
[Patterns and guidelines]

## Section 2
[More patterns]
```

## Customization Priority

Customize rules in this order:

1. **coding-practices.md** (Most important - sets foundation)
2. **error-handling.md** (Common across all code)
3. **testing-patterns.md** (Essential for quality)
4. **performance.md** (Important but can wait)

## What to Customize

### Language-Specific

Add your language's conventions:

**Before (Generic):**
```markdown
## {{LANGUAGE}} Style
- [PLACEHOLDER: Add language-specific style rules]
```

**After (TypeScript):**
```markdown
## TypeScript Style
- Use const over let, never use var
- Enable strict mode in tsconfig.json
- Prefer interfaces over type aliases for objects
- Use explicit return types for public functions
```

### Framework-Specific

Add your framework's patterns:

**Before (Generic):**
```markdown
## {{FRAMEWORK}} Patterns
- [PLACEHOLDER: Add framework-specific patterns]
```

**After (Express.js):**
```markdown
## Express.js Patterns
- Route → Controller → Service → Repository
- Use middleware for cross-cutting concerns
- Keep route handlers thin (1-5 lines)
- Use async/await with try-catch or error middleware
```

### Common Pitfalls

Add bugs/issues specific to your stack:

```markdown
## Common Express.js Pitfalls
- Forgetting try-catch in async routes
- Middleware order causing issues
- Not calling next() in middleware
- Memory leaks from unclosed connections
```

## Rules vs Prompts

**Rules** activate AI's existing knowledge:
- Context activators for coding standards
- Remind AI of framework-specific patterns
- Brief, not verbose
- No redundant teaching

**Prompts** define workflows:
- Step-by-step task instructions
- Specific guidance for deliverables
- Reference rules implicitly

**Philosophy**: Rules and prompts work together without redundancy. Rules don't repeat what's in prompts (e.g., testing rules don't duplicate test-writing.md).

## Examples

See [examples/](../examples/) for fully customized rule files:

- **[node-express/](../examples/node-express/rules/)** - TypeScript/Express patterns
- **[go-gin/](../examples/go-gin/rules/)** - Go/Gin patterns
- **[java-spring/](../examples/java-spring/rules/)** - Java/Spring patterns

## Rule Categories

### language-style.md (Template)

**Purpose:**  
A comprehensive template for creating language-specific style guides that activate the AI's deep knowledge of language conventions, idioms, and best practices.

**When to create:**
- Starting a new project with a specific language
- Establishing team-wide language conventions
- Creating a comprehensive style reference for your codebase

**How to customize:**

Use @setup-assistant.md with minimal parameters (only `language` is required):

```
@setup-assistant.md

target_file: "rules/language-style.md"
language: "TypeScript"
external_references: "https://www.typescriptlang.org/docs/handbook/intro.html"
additional_context: "Use ESLint with Airbnb config, prefer functional patterns"
```

The assistant will use its knowledge of the language ecosystem to fill in:
- File extension globs (e.g., `**/*.ts`, `**/*.tsx`)
- Official style guide references (inferred from language)
- Formatting conventions (indentation, line length, imports)
- Naming conventions (functions, classes, variables, constants)
- Type system examples with idiomatic patterns
- Design principles with language-specific applications
- Best practices and anti-patterns
- Language-specific tooling (linters, formatters)

Save the customized version with a descriptive name (e.g., `typescript-style.mdc`, `python-style.mdc`).

**What it covers:**
- Formatting (indentation, line length, imports)
- Naming conventions (functions, classes, constants, privates)
- Type system usage (type hints, interfaces, generics)
- Design principles (SOLID, composition, control flow)
- Best practices (resource management, data structures, docs)
- Language-specific considerations (tooling, ecosystem patterns)

**Note:** This template is more comprehensive than coding-practices.md, focusing specifically on language style and conventions. See `python-style.mdc` for a real-world example.

### framework-specific.md (Template)

**Purpose:**  
A lean template for creating framework-specific rules for targeted use cases. Perfect for capturing specific patterns like "Django REST Framework serialization", "Express.js middleware", or "Spring Boot exception handling".

**When to create:**
- Need focused guidance on a specific framework feature or pattern
- Want to document team conventions for a particular framework aspect
- Have external documentation to reference for a specific use case

**How to customize:**

Use @setup-assistant.md with external references and additional context:

```
@setup-assistant.md

target_file: "rules/framework-specific.md"
language: "Python"
framework: "Django REST Framework"
external_references: "https://www.django-rest-framework.org/api-guide/exceptions/"
additional_context: "Custom error handling: always return 'error_code' field, use consistent error response format, log all 500 errors to Sentry"
```

The assistant will create a focused rule file covering:
- Overview of the specific use case
- Core patterns from external references
- Implementation details based on additional context
- Best practices and anti-patterns
- Focused code example

Save with a descriptive name like `django-drf-errors.mdc`, `express-middleware.mdc`, etc.

**What it covers:**
- Specific framework feature or pattern
- Targeted best practices
- Team-specific conventions
- Focused examples

**Note:** This template is intentionally lean and context-driven. The quality of output depends heavily on the external_references and additional_context you provide.

### coding-practices.md

**When to reference:**
- Reviewing any code
- Implementing new features
- Refactoring existing code

**Key sections:**
- Logging standards (levels, context)
- Constants and configuration
- Code organization
- Comments and documentation
- Version control conventions

**Note**: Language style, naming, architecture, and data access patterns are handled elsewhere or by the AI's existing knowledge.

### error-handling.md

**When to reference:**
- Implementing error handling
- Reviewing error paths
- Fixing bugs
- Writing API endpoints

**Key sections:**
- Language-specific error patterns
- API error responses
- Validation errors
- Database errors
- Logging errors

### testing-patterns.md

**When to reference:**
- Writing any tests
- Reviewing test code
- Setting up test infrastructure

**Key sections:**
- AAA pattern (Arrange-Act-Assert)
- Test types (brief definitions)
- Test isolation principles
- Coverage goals and priorities
- Do's and Don'ts

**Note**: Lean version focuses on activating knowledge. Detailed testing instructions are in test-writing.md prompt.

### performance.md

**When to reference:**
- Optimizing slow code
- Reviewing database queries
- Implementing caching
- Profiling bottlenecks

**Key sections:**
- Database optimization
- Caching strategies
- Async/concurrency patterns
- Memory management
- Profiling tools

## Best Practices

### Keep Rules Lean

Rules should be context activators, not tutorials:
- Remove redundant content covered in prompts
- Don't teach what the AI already knows
- Focus on framework-specific activators
- Keep examples minimal or omit them

### Be Specific

When you do add content, be concrete:

**❌ Vague:**
```markdown
- Use good error handling
```

**✅ Specific:**
```markdown
- Wrap all async route handlers in try-catch
- Pass errors to Express error middleware with next(error)
```

### Avoid Redundancy

- Don't duplicate prompt content in rules
- Don't repeat error handling in coding-practices.md (it has its own file)
- Don't add testing details in coding-practices.md (use testing-patterns.md)
- If another rule or prompt covers it, reference it or omit it

## Adding Custom Rules

Create project-specific rules:

1. Create new .md file in rules/
2. Use same front-matter format
3. Structure with clear sections
4. Include concrete examples
5. Link to related rules

Example custom rule:

```markdown
---
description: "Team-specific API versioning strategy"
---

# API Versioning

## Strategy

We use URL-based versioning: `/api/v1/resource`

## Rules

- All endpoints include version
- Support N and N-1 versions
- Deprecate over 6 months
- Document breaking changes
```

## Getting Help

- See [CUSTOMIZATION-GUIDE.md](../CUSTOMIZATION-GUIDE.md) for detailed customization instructions
- Use [setup-assistant.md](../setup-assistant.md) for AI-assisted customization
- Check [examples/](../examples/) for reference implementations

## Cross-References

- **Prompts**: See [prompts/](../prompts/) for task-specific templates
- **Setup**: See [setup-assistant.md](../setup-assistant.md) for customization
- **Examples**: See [examples/](../examples/) for fully customized rules

