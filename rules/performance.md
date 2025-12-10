---
description: "Performance guidelines for {{LANGUAGE}}/{{FRAMEWORK}}"
---

# Performance

## Database Performance

### Query Optimization

**Avoid N+1 Queries:**

Use {{ORM}} features to eagerly load related data:

```{{LANGUAGE}}
// [PLACEHOLDER: N+1 query problem and solution using {{ORM}}]
// Bad: Loading relations in loop (N+1 queries)
// Good: Eager loading with single query
```

**Use Indexes:**

- Add indexes for frequently queried fields
- Index foreign keys
- Composite indexes for multi-column queries
- Monitor slow query logs

```{{LANGUAGE}}
// [PLACEHOLDER: Adding index using {{ORM}} or migration]
```

**Optimize Queries:**

- Select only needed columns
- Use appropriate joins
- Limit result sets
- Use pagination for large datasets
- Cache expensive queries

```{{LANGUAGE}}
// [PLACEHOLDER: Optimized query example]
// Show selecting specific fields, using limits
```

### Connection Pooling

Configure {{DATABASE}} connection pool:

```{{LANGUAGE}}
// [PLACEHOLDER: Connection pool configuration]
// Show setting pool size, timeout, etc.
```

### Transactions

- Keep transactions short
- Don't hold transactions during external calls
- Use appropriate isolation level
- Batch operations when possible

```{{LANGUAGE}}
// [PLACEHOLDER: Efficient transaction usage]
```

## Caching

### What to Cache

- Expensive computations
- Frequently accessed data
- External API responses
- Database query results

### Caching Strategies

**In-Memory Cache:**

```{{LANGUAGE}}
// [PLACEHOLDER: In-memory caching example]
// Show simple cache using Map or similar
```

**{{DATABASE}} as Cache:**

Use Redis, Memcached, or {{DATABASE}} caching features:

```{{LANGUAGE}}
// [PLACEHOLDER: External cache usage]
// Show storing and retrieving from cache
```

**Cache Invalidation:**

```{{LANGUAGE}}
// [PLACEHOLDER: Cache invalidation strategy]
// Show when and how to invalidate cache
```

## Async/Concurrency

### {{LANGUAGE}}-Specific Patterns

- [PLACEHOLDER: Concurrency patterns. Examples:
  - For Node.js: Don't block event loop, use worker threads for CPU-intensive
  - For Python: Use async/await, avoid GIL with multiprocessing
  - For Go: Use goroutines, channels, avoid goroutine leaks
  - For Java: Use virtual threads (Java 21+), CompletableFuture, parallel streams]

```{{LANGUAGE}}
// [PLACEHOLDER: Async/concurrent operation example]
// Show proper async pattern for your language
```

### Parallel Processing

For independent operations:

```{{LANGUAGE}}
// [PLACEHOLDER: Parallel processing example]
// Show processing multiple items concurrently
```

### Background Jobs

For long-running tasks:
- Use job queue (Celery, Bull, etc.)
- Return immediately to user
- Process asynchronously
- Update user when complete

```{{LANGUAGE}}
// [PLACEHOLDER: Background job example]
// Show queuing job and processing separately
```

## Memory Management

### Avoid Memory Leaks

- [PLACEHOLDER: Language-specific leak prevention. Examples:
  - For Node.js: Clear timers, remove event listeners, close connections
  - For Python: Be careful with global variables, circular references
  - For Go: Don't leak goroutines, close channels
  - For Java: Close resources, avoid holding references unnecessarily]

```{{LANGUAGE}}
// [PLACEHOLDER: Memory leak prevention example]
```

### Process Large Datasets Efficiently

**Use Streaming:**

```{{LANGUAGE}}
// [PLACEHOLDER: Streaming data example]
// Show processing data in chunks, not loading all at once
```

**Batch Processing:**

```{{LANGUAGE}}
// [PLACEHOLDER: Batch processing example]
// Show processing records in batches
```

**Pagination:**

```{{LANGUAGE}}
// [PLACEHOLDER: Pagination example]
// Show fetching and processing pages of data
```

## API Performance

### Response Time

- Optimize database queries
- Use caching appropriately
- Minimize external API calls
- Use async where beneficial
- Implement timeouts

### Payload Size

- Only return needed fields
- Compress responses (gzip)
- Use pagination for lists
- Consider GraphQL for flexible queries (if using GraphQL)

```{{LANGUAGE}}
// [PLACEHOLDER: Optimized API response example]
// Show returning only necessary fields
```

### Rate Limiting

Implement rate limiting to prevent abuse:

```{{LANGUAGE}}
// [PLACEHOLDER: Rate limiting implementation]
```

## Profiling and Monitoring

### Profiling Tools

Use {{LANGUAGE}}'s profiling tools:

```bash
# [PLACEHOLDER: Profiling commands. Examples:
# Node.js: node --prof, clinic.js
# Python: cProfile, py-spy
# Go: go tool pprof, go test -bench
# Java: JProfiler, VisualVM
```

### Application Performance Monitoring (APM)

- Use APM tools (New Relic, DataDog, etc.)
- Monitor response times
- Track database query performance
- Monitor memory usage
- Set up alerts for slow operations

### Logging Performance

- Use appropriate log levels
- Avoid logging in hot paths
- Log asynchronously in production
- Aggregate and analyze logs

## Algorithm Efficiency

### Time Complexity

Choose efficient algorithms:
- O(1): Constant time (ideal)
- O(log n): Logarithmic (good)
- O(n): Linear (acceptable)
- O(n log n): Good for sorting
- O(n²): Avoid if possible
- O(2ⁿ): Avoid

### Data Structure Selection

Choose appropriate data structures:

```{{LANGUAGE}}
// [PLACEHOLDER: Efficient data structure usage]
// Show choosing right data structure for use case
```

## Network Performance

### Reduce Round Trips

- Batch API calls
- Use HTTP/2 or HTTP/3
- Implement connection pooling
- Use CDN for static assets

### Minimize Latency

- Deploy close to users
- Use caching at edge
- Optimize DNS resolution
- Use keep-alive connections

## Build and Bundle Size

For {{LANGUAGE}} applications:

- [PLACEHOLDER: Build optimization. Examples:
  - For Node.js: Minimize bundle size, code splitting, tree shaking
  - For Go: Optimize binary size, use -ldflags="-s -w"
  - For Java: Optimize JAR size, remove unused dependencies]

```bash
# [PLACEHOLDER: Build optimization commands]
```

## Cold Start Optimization

For serverless or containerized apps:

- Minimize dependencies
- Use lazy loading where possible
- Keep initialization code efficient
- Consider using provisioned capacity

```{{LANGUAGE}}
// [PLACEHOLDER: Cold start optimization example]
```

## Best Practices Summary

### Do's:

- **Profile before optimizing** - measure, don't guess
- **Optimize hot paths** - focus on frequently executed code
- **Use caching appropriately** - cache expensive operations
- **Optimize database queries** - avoid N+1, use indexes
- **Use async for I/O** - don't block on I/O operations
- **Monitor performance** - track metrics over time
- **Set performance budgets** - define acceptable limits

### Don't

- **Premature optimization** - don't optimize without measuring
- **Over-caching** - cache invalidation is hard
- **Ignoring memory** - watch for memory leaks
- **Blocking operations** - use async where appropriate
- **Inefficient algorithms** - choose right data structures
- **Ignoring database** - often the bottleneck

## Performance Testing

### Load Testing

Test application under load:

```bash
# [PLACEHOLDER: Load testing tools and commands]
# Examples: k6, Apache JMeter, Gatling, ab
```

### Benchmarking

Benchmark critical code paths:

```{{LANGUAGE}}
// [PLACEHOLDER: Benchmarking example using {{TEST_FRAMEWORK}}]
// Show measuring execution time
```

### Performance Regression Testing

- Include performance tests in CI
- Track metrics over time
- Alert on regressions
- Set performance SLOs

## Cross-References

- Database patterns: See `coding-practices.md#data-access`
- Caching strategies: See framework documentation
- Monitoring: See deployment documentation

