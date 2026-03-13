# Capability Inventory

## Core Capabilities

### File Operations
| Capability | Tool | Status | Learned |
|------------|------|--------|---------|
| Read files | `read` | ✅ Active | 2026-03-13 |
| Write files | `write` | ✅ Active | 2026-03-13 |
| Edit files | `edit` | ✅ Active | 2026-03-13 |
| Execute commands | `exec` | ✅ Active | 2026-03-13 |
| Process management | `process` | ✅ Active | 2026-03-13 |

### Session & Agent Management
| Capability | Tool | Status | Learned |
|------------|------|--------|---------|
| Spawn sub-agents | `sessions_spawn` | ✅ Active | 2026-03-13 |
| Send messages | `sessions_send` | ✅ Active | 2026-03-13 |
| List sessions | `sessions_list` | ✅ Active | 2026-03-13 |
| Get history | `sessions_history` | ✅ Active | 2026-03-13 |
| Manage sub-agents | `subagents` | ✅ Active | 2026-03-13 |

### Memory & Persistence
| Capability | Tool | Status | Learned |
|------------|------|--------|---------|
| Search memory | `memory_search` | ✅ Active | 2026-03-13 |
| Get memory | `memory_get` | ✅ Active | 2026-03-13 |
| Cron jobs | `cron` | ✅ Active | 2026-03-13 |
| Session status | `session_status` | ✅ Active | 2026-03-13 |

### GitHub Operations
| Capability | Tool | Status | Learned |
|------------|------|--------|---------|
| Git operations | `git` | ✅ Active | 2026-03-13 |
| GitHub CLI | `gh` | ✅ Active | 2026-03-13 |
| SSH keys | `ssh` | ✅ Active | 2026-03-13 |
| Repo creation | GitHub web | ⚠️ Manual | 2026-03-13 |

### System Tools
| Capability | Tool | Status | Learned |
|------------|------|--------|---------|
| Python 3 | `python3` | ✅ Active | 2026-03-13 |
| Node.js | `node/npm` | ✅ Active | 2026-03-13 |
| cURL/Wget | `curl/wget` | ✅ Active | 2026-03-13 |
| Canvas display | `canvas` | 🔄 Config needed | - |

## Skills Available

### System Skills
- `gh-issues` — GitHub issue/PR automation
- `github` — GitHub CLI operations
- `healthcheck` — Security/system hardening
- `skill-creator` — Create/edit skills
- `tmux` — Remote tmux control
- `weather` — Weather via wttr.in
- `canvas` — Display HTML on nodes
- `coding-agent` — Spawn Codex/Claude

### Custom Skills (to build)
- [ ] `self-documentation` — Track capabilities and growth
- [ ] `deployment` — Deploy to hosting
- [ ] `monitoring` — Uptime checks and alerts

## Limitations

### Cannot Do (Currently)
- Browse the web directly
- Create GitHub repos via API (token scope)
- Docker operations (not installed)
- Email/SMS without configuration

### Partial Access
- Canvas: Needs node pairing
- Sub-agents: Spawned but not extensively tested
- Cron: Set up but not heavily used

## Growth Targets

### Phase 1 (Next 2 Weeks)
- [ ] Test sub-agent workflows thoroughly
- [ ] Create deployment skill
- [ ] Set up Canvas on a device
- [ ] Build a simple web app end-to-end

### Phase 2 (Month 1)
- [ ] Create 3-5 custom skills
- [ ] Automate common workflows
- [ ] Document all capabilities
- [ ] Build agent coordination patterns

### Phase 3 (Month 2)
- [ ] Launch first real product/service
- [ ] Reduce human involvement to review-only
- [ ] Create self-improvement feedback loops
