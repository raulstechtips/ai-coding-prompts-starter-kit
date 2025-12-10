---
name: "Documentation Template"
category: "docs"
description: "Generate high-quality documentation for {{LANGUAGE}}/{{FRAMEWORK}} applications"
version: "1.0"
variables:
  - name: "target"
    description: "What to document (e.g., 'UserService class', 'API endpoints', 'Setup guide')"
    required: true
  - name: "doc_type"
    description: "Type: 'code' (docstrings/comments), 'api' (endpoint docs), 'guide' (how-to), 'readme' (overview)"
    required: true
  - name: "audience"
    description: "Target audience: 'developers', 'end-users', 'api-consumers', 'maintainers'"
    required: true
  - name: "include_examples"
    description: "Whether to include code examples (true/false)"
    required: false
---

# Documentation Template

## Context

This template guides creation of clear, accurate documentation for {{LANGUAGE}}/{{FRAMEWORK}} applications. Documentation should be concise yet comprehensive, with practical examples where appropriate.

### Documentation Types
- **Code Documentation**: Docstrings, inline comments, API references
- **API Documentation**: Endpoint specifications with examples
- **User Guides**: How-to guides for specific tasks
- **Project Documentation**: README, setup instructions, architecture overview

## Instructions

### Step 1: Analyze the Target
- Identify what to document: `{{target}}`
- Determine documentation type: `{{doc_type}}`
- Consider audience: `{{audience}}`
- Determine appropriate level of detail

### Step 2: Extract Key Information

**For Code Documentation (`doc_type: code`):**
- Purpose and responsibility of the code
- Parameters and their types
- Return values and their types
- Exceptions/errors that can be raised
- Side effects (database changes, external calls)
- Usage examples (if `{{include_examples}}` is true)

**For API Documentation (`doc_type: api`):**
- Endpoint URL and HTTP method
- Authentication requirements
- Request parameters (path, query, body)
- Request body schema
- Response format and status codes
- Error responses
- Usage examples

**For Guides (`doc_type: guide`):**
- Prerequisites and setup requirements
- Step-by-step instructions
- Expected outcomes at each step
- Common issues and solutions
- Links to related documentation

**For README (`doc_type: readme`):**
- Project overview and purpose
- Quick start guide
- Installation instructions
- Key features
- Usage examples
- Contributing guidelines (if applicable)

### Step 3: Structure the Documentation

Follow {{LANGUAGE}} documentation conventions:
- Use appropriate doc format (JSDoc, GoDoc, Javadoc, docstrings, etc.)
- Include type information using {{LANGUAGE}}'s type system
- Organize logically (general to specific)
- Use clear headers and formatting
- Add examples if `{{include_examples}}` is true

### Step 4: Write Clear Content
- Start with a clear summary sentence
- Be specific and concrete (avoid vague descriptions)
- Use active voice
- Include edge cases and error conditions
- Add links to related documentation

### Step 5: Review for Quality
- **Accuracy**: Information is correct and up-to-date
- **Completeness**: All necessary information included
- **Clarity**: Easy to understand for target audience
- **Conciseness**: No unnecessary verbosity
- **Examples**: Practical, realistic use cases

## Constraints

- **Follow Conventions**: Use {{LANGUAGE}}'s standard documentation format
- **Be Accurate**: Ensure all information matches implementation
- **Be Complete**: Cover all parameters, errors, edge cases
- **Be Concise**: Thorough but not verbose
- **Include Examples**: Add realistic examples when helpful
- **Current**: Reflect current implementation

## Expected Output

### For Code Documentation (`doc_type: code`)
- Complete docstring following {{LANGUAGE}} conventions
- Parameter descriptions with types
- Return value documentation
- Exception documentation
- Usage example (if requested)

### For API Documentation (`doc_type: api`)
- Endpoint URL and method
- Authentication requirements
- Complete parameter documentation
- Response examples with status codes
- Error response documentation
- Usage examples (cURL or code)

### For User Guides (`doc_type: guide`)
- Clear step-by-step instructions
- Prerequisites listed upfront
- Practical examples
- Common issues and solutions
- Links to related documentation

### For README (`doc_type: readme`)
- Project overview and purpose
- Quick start guide
- Installation instructions
- Key features highlight
- Usage examples
- Links to detailed documentation

## Quality Checklist
- [ ] Accurate and matches current implementation
- [ ] Complete (all parameters/fields documented)
- [ ] Clear language appropriate for target audience
- [ ] Practical examples included
- [ ] Consistent formatting
- [ ] Up-to-date with latest code

