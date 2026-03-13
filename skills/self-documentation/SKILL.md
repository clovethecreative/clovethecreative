---
name: self-documentation
description: Document agent capabilities, learnings, and growth over time. Use when: (1) the agent learns a new capability or pattern, (2) reflecting on what worked/didn't work in a task, (3) updating capability inventory, (4) planning next growth steps, (5) onboarding a new agent to existing capabilities.
---

# Self Documentation

## Overview

This skill enables systematic self-improvement through documentation. It helps track:
- **Capabilities** — What I can do now
- **Learnings** — What worked, what didn't
- **Growth** — Progress over time
- **Gaps** — What I still need to learn

## Workflow

### When to Document

**Always document when:**
- Completing a complex task for the first time
- Discovering a new tool or pattern
- Making a mistake worth remembering
- Setting up new infrastructure
- Onboarding to a new system

**Never document:**
- Routine operations already covered
- Speculation about future capabilities
- Other people's personal information

### Documentation Types

| Type | Location | Trigger |
|------|----------|---------|
| Daily log | `memory/YYYY-MM-DD.md` | End of session |
| Capability | `docs/capabilities.md` | New tool/pattern learned |
| Learning | `memory/learnings.md` | Mistake or insight |
| Skill | `skills/` | Reusable workflow identified |
| Architecture | `docs/architecture.md` | System change |

## Quick Reference

### Add a new capability

```markdown
## Capability: [Name]
**Learned:** [Date]
**Status:** [Active/Deprecated/Experimental]

**What it does:**
- Bullet points

**How to use:**
```bash
# Example commands
```

**Limitations:**
- What doesn't work

**Related:** [Links to other capabilities]
```

### Log a learning

```markdown
## [Date] - [Topic]
**Situation:** What happened
**What I tried:** Approach taken
**Result:** Outcome
**Lesson:** What to remember
**Next time:** Improved approach
```

## Resources

### scripts/
- `capability-check.py` — Audit current capabilities
- `learning-extract.py` — Extract learnings from memory files

### references/
- `capability-template.md` — Template for new capabilities
- `growth-framework.md` — How to prioritize what to learn next
