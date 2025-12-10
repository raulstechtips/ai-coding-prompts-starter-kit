---
description: "{{LANGUAGE}}/{{FRAMEWORK}} coding conventions and patterns"
---

# Coding Practices

Follow {{LANGUAGE}} and {{FRAMEWORK}} conventions for consistent, maintainable code.

## Logging

Use {{LANGUAGE}}'s standard logging library.

**Log levels:**
- DEBUG: Detailed diagnostic info (development only)
- INFO: Normal operation events
- WARNING: Unusual but handled events
- ERROR: Failures requiring attention
- CRITICAL: System-level failures

**Include context:**
- Request IDs
- Operation being performed
- Relevant parameters (sanitized, no PII)

## Constants and Configuration

- Prefer named constants over magic numbers/strings
- Group related constants appropriately
- Use environment variables for configuration
- Never hardcode secrets or credentials
- Use configuration files for environment-specific settings

## Code Organization

Follow {{FRAMEWORK}}'s standard project structure.

- Keep modules focused on single responsibility
- Split large files into smaller, cohesive units
- Group related functionality together

## Comments and Documentation

- Write self-documenting code with clear names
- Add comments for "why", not "what"
- Document public APIs using {{LANGUAGE}}'s standard documentation format
- Keep comments up-to-date with code changes


## Version Control

- Write clear, descriptive commit messages
- Keep commits atomic and focused
- Reference issue numbers in commits
- Use feature branches for development
- Squash commits before merging (if team convention)

