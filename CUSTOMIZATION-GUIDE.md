# Customization Guide

This guide shows you how to adapt the minimalistic AI Prompt Starter Kit for your specific tech stack. The kit is designed to be lean and context-conscious, avoiding unnecessary bloat.

## Table of Contents

1. [Understanding the Variable System](#understanding-the-variable-system)
2. [Step-by-Step Customization](#step-by-step-customization)
3. [Using the Setup Assistant](#using-the-setup-assistant)
4. [Customizing Prompts](#customizing-prompts)
5. [Customizing Rules](#customizing-rules)
6. [Adding Your Own Templates](#adding-your-own-templates)
7. [Best Practices](#best-practices)

---

## Understanding the Variable System

Templates use a minimalistic variable system with placeholders in `{{DOUBLE_BRACES}}` format.

### Standard Variables

| Variable | Description | Examples |
|----------|-------------|----------|
| `{{LANGUAGE}}` | Programming language | Python, TypeScript, Go, Java, Rust |
| `{{FRAMEWORK}}` | Main framework | Django, Express, Gin, Spring Boot |
| `{{DATABASE}}` | Primary database | PostgreSQL, MongoDB, MySQL |
| `{{ORM}}` | ORM/data layer | Django ORM, Prisma, GORM, Hibernate |
| `{{TEST_FRAMEWORK}}` | Testing framework | pytest, Jest, testing, JUnit |
| `{{PACKAGE_MANAGER}}` | Package manager | pip, npm, go mod, maven |
| `{{API_STYLE}}` | API architecture | REST, GraphQL, gRPC |
| `{{CONTAINER}}` | Container runtime | Docker, Podman |
| `{{CI_PLATFORM}}` | CI/CD platform | GitHub Actions, GitLab CI |

### Where Variables Appear

**In instructions:**
```markdown
### Step 3: Implement Fix
- Add logging using {{LANGUAGE}}'s standard logging approach
- Follow {{FRAMEWORK}} conventions
```

**In examples:**
````markdown
```{{LANGUAGE}}
// Framework-specific code example
```
````

**In placeholders:**
```markdown
- [PLACEHOLDER: Add {{FRAMEWORK}}-specific patterns here]
```

---

## Step-by-Step Customization

### Step 1: Define Your Tech Stack

Create a configuration file for reference:

```yaml
# my-project-config.yaml
language: TypeScript
framework: Express.js
database: PostgreSQL
orm: Prisma
test_framework: Jest
package_manager: npm
api_style: REST
container: Docker
ci_platform: GitHub Actions
```

### Step 2: Choose Customization Method

**Option A: AI-Assisted (Recommended)**
- Fast, comprehensive, consistent
- Uses `setup-assistant.md`
- Best for first-time setup

**Option B: Manual**
- Full control, learn as you go
- Search and replace variables
- Best for fine-tuning

### Step 3: Customize Prompts

For each file in `prompts/`:

1. Replace all `{{VARIABLE}}` instances
2. Fill in `[PLACEHOLDER]` sections with specific patterns
3. Update examples with realistic code
4. Review for completeness

### Step 4: Customize Rules

For each file in `rules/`:

1. Replace variable placeholders
2. Add language/framework-specific patterns
3. Include common pitfalls for your stack
4. Add relevant reference links

### Step 5: Test with AI Assistant

Try a prompt template:

```
@prompts/bug-fix.md

component_name: "TestComponent"
bug_description: "Simple test bug"
expected_behavior: "Works correctly"
actual_behavior: "Throws error"
```

Verify the AI understands your customized instructions.

---

## Using the Setup Assistant

The setup assistant (`setup-assistant.md`) is a prompt template that customizes one file at a time, keeping context focused and efficient.

### How It Works

1. **You specify** which file to customize and your tech stack
2. **AI reads** the generic template
3. **AI generates** the customized version
4. **You review** and save the result

### Example Workflow

**Step 1: Use setup-assistant.md**

Reference it with your configuration:

```
@setup-assistant.md

target_file: "prompts/bug-fix.md"
language: "TypeScript"
framework: "Express.js"
database: "PostgreSQL"
orm: "Prisma"
test_framework: "Jest"
package_manager: "npm"
api_style: "REST"
external_references: "https://expressjs.com/en/guide/error-handling.html"
additional_context: "We use async/await for all routes, middleware for auth"
```

**Step 2: Review Output**

AI will provide:
- Customized file with all `{{VARIABLE}}` replaced
- `[PLACEHOLDER]` sections filled with framework-specific patterns
- Only includes examples if the template explicitly requests them

**Step 3: Repeat for Other Files**

Customize one file at a time:

```
@setup-assistant.md

target_file: "rules/coding-practices.md"
language: "TypeScript"
framework: "Express.js"
...
```

---

## Customizing Prompts

Each prompt template follows this structure:

```markdown
---
name: "Template Name"
category: "category"
version: "1.0"
variables: [...]
---

# Template Title

## Context
[Why this template exists, general approach]

## Instructions
[Step-by-step guidance]

## Constraints
[Requirements and limitations]

## Examples
[Concrete examples]

## Expected Output
[What should be delivered]
```

### Customization Checklist

For each prompt template:

- [ ] Replace all `{{VARIABLE}}` placeholders
- [ ] Fill in `[PLACEHOLDER]` sections with framework-specific patterns
- [ ] Update "Common Issues" lists with framework-specific bugs
- [ ] Verify instructions match your team's workflow
- [ ] Test with AI assistant

**Note**: Don't add examples unless the template explicitly has placeholder sections requesting them. Keep it lean.

### Example: Customizing bug-fix.md

**Before (Generic):**
```markdown
### Step 2: Root Cause Analysis
- Check for common {{FRAMEWORK}} issues:
  - [PLACEHOLDER: Add 5-7 common issues for your framework]
```

**After (TypeScript/Express):**
```markdown
### Step 2: Root Cause Analysis
- Check for common Express.js issues:
  - Async/await error handling missing try-catch
  - Middleware order causing request issues
  - Prisma client not initialized
  - TypeScript type mismatches
  - Missing error middleware
  - Promise rejections not handled
  - Route parameter validation missing
```

---

## Customizing Rules

Rules files guide the AI on your project's coding standards.

### Rule File Structure

```markdown
---
description: "Brief description with {{VARIABLES}}"
---

# Rule Title

## Section 1
[Specific patterns and conventions]

## Section 2
[More patterns]
```

### Customization Checklist

For each rule file:

- [ ] Replace all `{{VARIABLE}}` placeholders
- [ ] Fill `[PLACEHOLDER]` sections with framework-specific patterns
- [ ] Keep it lean - rules activate AI knowledge, they don't teach
- [ ] Reference official docs/style guides when helpful
- [ ] Remove redundant content covered in other rules or prompts

**Philosophy**: Rules should be brief context activators, not verbose tutorials.

### Example: Customizing coding-practices.md

**Before (Generic):**
```markdown
## {{LANGUAGE}} Style
- [PLACEHOLDER: Add language-specific style rules]
- Follow official style guide
```

**After (TypeScript):**
```markdown
## TypeScript Style
- Follow [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html)
- Use `const` over `let`, never use `var`
- Enable strict mode in tsconfig.json
- Prefer interfaces over type aliases for object shapes
- Use explicit return types for public functions
- Configure ESLint + Prettier for auto-formatting
```

---

## Adding Your Own Templates

You can extend the kit with project-specific templates.

### Creating a New Prompt Template

1. **Copy an existing template** as a starting point
2. **Define the YAML front-matter** with variables
3. **Write the Context** section explaining the approach
4. **Create step-by-step Instructions**
5. **Add Constraints** specific to the workflow
6. **Include realistic Examples**
7. **Define Expected Output**

### Example: Creating a "Database Optimization" Template

```markdown
---
name: "Database Optimization Template"
category: "performance"
version: "1.0"
variables:
  - name: "query_location"
    description: "File/function with slow query"
    required: true
  - name: "performance_issue"
    description: "What's slow (N+1, missing index, etc.)"
    required: true
---

# Database Optimization

## Context
Guide systematic database query optimization for {{DATABASE}} using {{ORM}}.

## Instructions

### Step 1: Identify the Problem
- Measure current performance
- Profile the query
- Identify bottleneck

### Step 2: Analyze Query
- Review {{ORM}} generated SQL
- Check explain plan
- Identify missing indexes

### Step 3: Optimize
- Apply appropriate optimization
- Add indexes if needed
- Use {{ORM}} optimization features

### Step 4: Verify
- Measure improved performance
- Check for regressions

## Examples
[Add examples specific to your ORM]

## Expected Output
- Optimized query code
- Index migrations (if applicable)
- Performance metrics (before/after)
```

### Creating a New Rule File

Follow the same process as prompt templates, but focus on:
- Patterns to follow
- Anti-patterns to avoid
- Code examples
- Links to documentation

---

## Best Practices

### 1. Start Small

Don't customize everything at once:
1. Start with `bug-fix.md` and `coding-practices.md`
2. Test with your AI assistant
3. Expand to other templates as needed

### 2. Keep It Lean

Avoid context bloat:
- Don't add examples unless template explicitly requests them
- Fill placeholders with patterns, not verbose tutorials
- Rules activate AI knowledge, they don't teach from scratch
- Remove redundant content covered elsewhere

### 3. Update as You Learn

Templates evolve. When you discover:
- A new common bug pattern → Add to bug-fix.md
- A better coding pattern → Update rules
- Team conventions change → Update templates

### 4. Share with Your Team

If templates work well:
- Commit to version control
- Document team-specific customizations
- Update as team practices evolve

### 5. Be Specific, Not Generic

The more specific your templates, the better AI assistance you'll get:

- ❌ "Use good error handling"
- ✅ "Wrap async route handlers in try-catch and pass errors to Express error middleware"

---

## Troubleshooting

### AI Not Following Templates

**Issue**: AI ignores template instructions

**Solutions**:
- Make instructions more explicit
- Add concrete examples
- Reference templates at the start of conversations
- Use constraints section to emphasize requirements

### Templates Too Verbose

**Issue**: Templates feel overwhelming

**Solutions**:
- These templates are already lean - don't add unnecessary content
- Remove sections that don't apply to your workflow
- Don't add examples unless template requests them
- Keep placeholders filled with patterns, not tutorials

### Variables Not Clear

**Issue**: Hard to know what to put in variables

**Solutions**:
- Look at examples directory for reference
- Ask AI: "What should I use for {{VARIABLE}} in my Express.js project?"
- Check variable descriptions in YAML front-matter

---

## Next Steps

1. ✅ Understand the variable system
2. ✅ Choose customization approach (AI-assisted or manual)
3. 🔄 Start with `setup-assistant.md` or customize `bug-fix.md` manually
4. 🔄 Test with your AI assistant
5. 🔄 Expand to other templates
6. 🔄 Share with your team

**Need help?** Check the [examples directory](./examples/) for fully customized reference implementations.

---

**Ready to start?** Head to [setup-assistant.md](./setup-assistant.md) for AI-assisted customization.

