---
globs: ["[PLACEHOLDER: file extensions, e.g., **/*.py, **/*.ts, **/*.go, **/*.java]"]
description: "{{LANGUAGE}} code style guidelines"
alwaysApply: false
---

# {{LANGUAGE}} Style

## References

- **{{LANGUAGE}} Style Guide:** [PLACEHOLDER: URL to official or preferred style guide]
- **Type System Documentation:** [PLACEHOLDER: URL to type system docs, e.g., PEP 484, TypeScript handbook]
- **Documentation Standard:** [PLACEHOLDER: URL to documentation format standard]
- **Design Principles:** [PLACEHOLDER: URL to design principles reference]

## Formatting

PREFER:
- [PLACEHOLDER: indentation style, e.g., 4 spaces, 2 spaces, tabs]
- [PLACEHOLDER: line length, e.g., 80 characters, 100 characters, 120 characters]
- [PLACEHOLDER: import/module organization style]
- [PLACEHOLDER: bracket/brace style if applicable]

Reference: [PLACEHOLDER: URL to formatting section of style guide]

## Naming Conventions

PREFER:
- [PLACEHOLDER: function/method naming, e.g., snake_case, camelCase]
- [PLACEHOLDER: class/type naming, e.g., PascalCase, CamelCase]
- [PLACEHOLDER: constant naming, e.g., UPPER_SNAKE_CASE, SCREAMING_SNAKE_CASE]
- [PLACEHOLDER: variable naming conventions]
- [PLACEHOLDER: private/internal member conventions, e.g., _leading_underscore, #private]

Reference: [PLACEHOLDER: URL to naming conventions section]

## Type System

[PLACEHOLDER: Language-specific type system guidelines]

PREFER type annotations/declarations for:
- Public APIs
- Function signatures
- Complex data structures

Example:
```{{LANGUAGE_LOWERCASE}}
[PLACEHOLDER: Realistic code example showing type system usage in the language]

Example for TypeScript:
interface UserData {
  id: string;
  email: string;
  role: 'admin' | 'user';
}

function createUser(
  email: string,
  role: UserData['role']
): UserData {
  return {
    id: generateId(),
    email,
    role
  };
}

Example for Python:
from typing import Optional, List
def calculate_total(
    items: List[str],
    discount: Optional[float] = None
) -> float:
    pass

Example for Go:
func CalculateTotal(items []string, discount *float64) (float64, error) {
    // implementation
}

Example for Java:
public Optional<Double> calculateTotal(
    List<String> items,
    Double discount
) {
    // implementation
}
```

Reference: [PLACEHOLDER: URL to type system documentation]

## Design Principles

PREFER:
- **Single Responsibility:** [PLACEHOLDER: How this applies in the language/framework]
- **Composition over Inheritance:** [PLACEHOLDER: Idiomatic patterns for the language]
- **Early Returns:** [PLACEHOLDER: Preferred control flow patterns]
- [PLACEHOLDER: Additional language-specific design principles]

Reference: [PLACEHOLDER: URL to design principles documentation]

## Best Practices

PREFER:
- [PLACEHOLDER: Resource management patterns, e.g., context managers, try-with-resources, defer]
- [PLACEHOLDER: Preferred data structure operations, e.g., comprehensions, streams, loops]
- [PLACEHOLDER: Documentation approach for public APIs]
- [PLACEHOLDER: Error handling patterns - see @error-handling.md]
- [PLACEHOLDER: Async/concurrent programming patterns if applicable]
- [PLACEHOLDER: Include design principles (SOLID, composition, etc.) with `{{LANGUAGE}}`-specific applications]

AVOID:
- [PLACEHOLDER: Common anti-patterns in the language]
- [PLACEHOLDER: Deprecated or discouraged language features]
- Global variables (unless absolutely necessary)
- Premature optimization

## Language-Specific Considerations

[PLACEHOLDER: Unique considerations for this language/ecosystem]

Examples:
- Python: Use virtual environments, follow PEP standards
- TypeScript: Configure strict mode, use proper module resolution
- Go: Follow effective Go patterns, use go fmt
- Java: Use modern Java features (streams, Optional, var), configure linting
- Rust: Follow Rust idioms, use Clippy for linting
- Ruby: Follow Ruby style guide, use RuboCop

## Cross-Reference

- Code organization: @coding-practices.md
- Error handling: @error-handling.md
- Testing patterns: @testing-patterns.md
- Performance: @performance.md

