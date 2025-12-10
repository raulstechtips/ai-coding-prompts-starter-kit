# AI Prompt Starter Kit

A minimalistic, framework-agnostic collection of prompt templates and coding rules designed for AI-assisted development with GitHub Copilot, Cursor, or any AI coding assistant.

## What is This?

This starter kit provides **lean prompt templates** and **context-activating rules** that guide AI assistants to deliver consistent, high-quality code for your specific tech stack. Instead of verbose examples and over-explanation, these templates focus on clear instructions and activating the AI's existing knowledge.

### Key Features

- ✅ **Minimalistic Design**: Context-conscious, no unnecessary examples or bloat
- ✅ **Framework-Agnostic**: Works with any language/framework (Python, TypeScript, Go, Java, etc.)
- ✅ **Simple Customization**: Variable placeholders for quick adaptation
- ✅ **AI-Assisted Setup**: Single-file customization prompt for targeted updates
- ✅ **Context Activation**: Rules activate AI knowledge rather than teaching from scratch
- ✅ **Comprehensive Coverage**: Bug fixes, features, tests, docs, reviews, refactoring, migrations

## Quick Start

### 1. Copy the Kit

```bash
cp -r ai-prompt-starter-kit /path/to/your/project/.ai-prompts
cd /path/to/your/project/.ai-prompts
```

### 2. Customize with AI Assistance

Use `setup-assistant.md` to customize one template at a time:

```
@setup-assistant.md

target_file: "prompts/bug-fix.md"
language: "TypeScript"
framework: "Express.js"
database: "PostgreSQL"
orm: "Prisma"
test_framework: "Jest"
```

Your AI assistant will generate the customized template with framework-specific patterns.

### 3. Use in Your Workflow

Reference templates in your AI chat:

```
@.ai-prompts/prompts/bug-fix.md

component_name: "UserService"
bug_description: "API returns 500 when user email is null"
expected_behavior: "Should return 400 with validation error"
actual_behavior: "Returns 500 Internal Server Error"
```

## Directory Structure

```
ai-prompt-starter-kit/
├── README.md                      # This file
├── CUSTOMIZATION-GUIDE.md         # Detailed customization instructions
├── setup-assistant.md             # AI-assisted setup helper
├── prompts/
│   ├── bug-fix.md                 # Systematic bug fixing
│   ├── feature.md                 # Feature implementation
│   ├── test-writing.md            # Test writing
│   ├── documentation.md           # Documentation generation
│   ├── code-review.md             # Code review guidance
│   ├── refactoring.md             # Refactoring guidance
│   └── migration.md               # Migration guidance
├── rules/
│   ├── language-style.md          # Language style template (customize for your language)
│   ├── framework-specific.md      # Framework-specific template (for targeted use cases)
│   ├── coding-practices.md        # Coding conventions
│   ├── error-handling.md          # Error handling patterns
│   ├── testing-patterns.md        # Testing conventions
│   └── performance.md             # Performance guidelines
└── examples/
    ├── node-express/              # TypeScript/Express reference
    ├── go-gin/                    # Go/Gin reference
    └── java-spring/               # Java/Spring reference
```

## How to Customize

### Option 1: AI-Assisted (Recommended)

Use `setup-assistant.md` to customize one file at a time:

```
@setup-assistant.md

target_file: "prompts/bug-fix.md"
language: "TypeScript"
framework: "Express.js"
database: "PostgreSQL"
orm: "Prisma"
test_framework: "Jest"
```

The AI will replace all `{{VARIABLE}}` placeholders and fill `[PLACEHOLDER]` sections with framework-specific patterns.

### Option 2: Manual

1. Search for `{{VARIABLE}}` placeholders (e.g., `{{LANGUAGE}}`, `{{FRAMEWORK}}`)
2. Replace with your specific technologies
3. Fill `[PLACEHOLDER]` sections with framework-specific patterns

See [CUSTOMIZATION-GUIDE.md](./CUSTOMIZATION-GUIDE.md) for detailed instructions.

## Using with AI Assistants

### GitHub Copilot

Add templates to your project and reference them in comments:

```typescript
// @see .ai-prompts/prompts/bug-fix.md
// Fix: UserService validation error handling
```

## Examples

This kit includes three fully customized reference implementations:

- **[Node.js/Express/TypeScript](./examples/node-express/)** - REST API with Prisma ORM
- **[Go/Gin](./examples/go-gin/)** - REST API with GORM
- **[Java/Spring Boot](./examples/java-spring/)** - REST API with Hibernate

Each shows how templates look when fully customized for a specific stack.

## What Makes This Different?

Unlike generic prompts, these templates:

1. **Minimalistic and context-conscious** - No unnecessary bloat
2. **Guide the AI step-by-step** through systematic processes
3. **Activate existing knowledge** - Rules activate AI's built-in knowledge rather than teaching
4. **Enforce best practices** specific to your tech stack
5. **Maintain consistency** across your entire codebase
6. **Incremental workflows** - Features can be built layer-by-layer (data, business, API)

## Contributing

Found a way to improve these templates? Contributions welcome!

1. Add new templates for common workflows
2. Improve existing template guidance
3. Add reference implementations for new tech stacks
4. Share feedback on what works (or doesn't)


## Acknowledgments

This starter kit evolved from production experience building AI-assisted development workflows. The structure and guidance patterns are based on what actually works when collaborating with AI coding assistants.

---

**Ready to get started?** Open [CUSTOMIZATION-GUIDE.md](./CUSTOMIZATION-GUIDE.md) or jump straight to [setup-assistant.md](./setup-assistant.md) to customize for your project.

