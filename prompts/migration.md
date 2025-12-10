---
name: "Migration Template"
category: "migration"
description: "Guide data/schema/dependency/architecture migrations for {{LANGUAGE}}/{{FRAMEWORK}}"
version: "1.0"
variables:
  - name: "migration_type"
    description: "Type: 'schema', 'data', 'dependency', 'architecture'"
    required: true
  - name: "source_state"
    description: "Current state/version"
    required: true
  - name: "target_state"
    description: "Desired state/version"
    required: true
  - name: "rollback_plan"
    description: "How to revert if needed"
    required: false
---

# Migration Template

## Context

This template guides migrations in {{LANGUAGE}}/{{FRAMEWORK}} applications. Migrations change system state (database schema, data structure, dependencies, or architecture) while minimizing downtime and risk.

### Migration Types
- **Schema**: Database schema changes ({{ORM}})
- **Data**: Data transformation or cleanup
- **Dependency**: Upgrading libraries, frameworks, or {{LANGUAGE}} version
- **Architecture**: Major system redesign or component replacement

## Instructions

### Step 1: Analyze Migration
- Migration type: `{{migration_type}}`
- Source: `{{source_state}}`
- Target: `{{target_state}}`
- Impact assessment: What breaks if we do nothing?
- Risk level: Low/Medium/High
- Reversibility: Can this be rolled back?

### Step 2: Plan Migration Strategy

**For Schema Migrations ({{ORM}}):**
- Create migration files using {{ORM}}'s migration tool
- Handle data transformation if schema changes affect existing data
- Plan for zero-downtime deployment if required
- Test rollback procedure
- Consider backwards compatibility

**For Data Migrations:**
- Identify affected records/documents
- Create transformation logic
- Plan for large dataset handling (batching, pagination)
- Verify data integrity before and after
- Handle failures gracefully
- Create backups

**For Dependency Migrations:**
- Review changelog for breaking changes
- Update {{PACKAGE_MANAGER}} configuration
- Update code for API changes
- Run full test suite
- Update CI/CD pipeline if needed
- Plan gradual rollout if possible

**For Architecture Migrations:**
- Document current vs target architecture
- Identify incremental migration steps
- Plan feature flags for gradual rollout
- Define success metrics
- Prepare monitoring and alerts
- Plan data synchronization if needed

### Step 3: Prepare Safety Measures
- Create database backup (if applicable)
- Set up monitoring and alerting
- Prepare rollback plan: `{{rollback_plan}}`
- Test migration in staging/test environment
- Document runbook with step-by-step commands
- Schedule migration during low-traffic period

### Step 4: Execute Migration
- Follow {{FRAMEWORK}} migration best practices
- Run migration with monitoring active
- Log progress and any errors
- Watch key metrics (error rates, performance, resource usage)
- Have rollback ready to execute
- Document any deviations from plan

### Step 5: Verify Migration
- Run data integrity checks
- Execute smoke tests
- Check application functionality
- Verify performance hasn't degraded
- Confirm rollback capability still works
- Monitor for 24-48 hours post-migration

## Constraints

- **Safety First**: Always have rollback plan
- **Test Thoroughly**: Test in non-production first
- **Monitor Closely**: Watch metrics during and after
- **Communicate**: Keep stakeholders informed
- **Document**: Record what was done and why
- **Reversibility**: Ensure you can undo if needed

## Migration Checklist

### Pre-Migration
- [ ] Migration tested in staging/test environment
- [ ] Backup created (if applicable)
- [ ] Rollback plan documented and tested
- [ ] Team notified of migration schedule
- [ ] Monitoring and alerts configured
- [ ] Runbook prepared with exact commands

### During Migration
- [ ] Monitoring active
- [ ] Progress logged
- [ ] Key metrics tracked
- [ ] Team on standby
- [ ] Communication channel open

### Post-Migration
- [ ] Data integrity verified
- [ ] Smoke tests passed
- [ ] Performance validated
- [ ] Rollback capability confirmed
- [ ] Documentation updated
- [ ] Post-mortem if any issues

## Expected Output

### 1. Migration Plan Document
- Detailed steps to execute
- Timeline and schedule
- Risk assessment
- Team responsibilities

### 2. Migration Code/Scripts
- {{ORM}} migration files (for schema)
- Data transformation scripts (for data)
- Updated configuration (for dependencies)
- Deployment manifests (for architecture)

### 3. Rollback Plan
- Exact steps to revert changes
- Commands to execute rollback
- Expected time to rollback
- Data restoration procedure

### 4. Verification Procedure
- Tests to run post-migration
- Metrics to monitor
- Success criteria
- Acceptable thresholds

### 5. Post-Migration Report
- What was executed
- Any deviations from plan
- Issues encountered and resolved
- Final verification results
- Lessons learned

