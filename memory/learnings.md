# Learnings Log

## 2026-03-13 - Day 1

### What I Learned: GitHub Setup

**Situation:** Needed to set up GitHub access for autonomous operations

**What I tried:**
1. Generated SSH key pair
2. Configured SSH to use the new key
3. Set up git config with name and email
4. Attempted to use `gh repo create` with PAT

**Result:** SSH works perfectly for git operations, but PAT doesn't have `createRepository` scope

**Lesson:** 
- SSH + PAT is a good combo: SSH for git, PAT for API operations
- PAT scope matters — fine-grained tokens are more secure but limited
- Manual repo creation is acceptable; most operations work fine

**Next time:**
- Use SSH for all git operations
- Use PAT for API queries, issues, PRs
- Don't expect full automation if token is limited

### What I Learned: OpenClaw Architecture

**Situation:** Understanding how the system works

**Key insights:**
- Gateway is the control plane (port 18789)
- Skills are modular packages with SKILL.md + resources
- Sub-agents run isolated with `sessions_spawn`
- Canvas can display HTML on iOS/Android/Mac nodes
- Memory is session-local + file-based persistence

**Skill system architecture:**
```
Skill/
├── SKILL.md (triggers + instructions)
├── scripts/ (executable code)
├── references/ (documentation)
└── assets/ (templates, files)
```

**Lesson:** Skills are the key to extending capabilities systematically

### What I Learned: My Identity

**Established:**
- Name: Jarvis 🤖
- Creature: Agent operating partner
- Vibe: Grounded, practical, direct
- Timezone: US Eastern (Andy's timezone)
- GitHub: clovethecreative

**Role:** Early-stage coordinator in a forming multi-agent system

### Mistakes Made

**None yet** — Day 1, mostly setup. But potential pitfalls noted:
- Don't assume full web access (I can't browse)
- Don't assume full GitHub API access (token scopes limit)
- Don't build before understanding existing tools (many skills already exist)

### Next Steps Prioritized

1. Commit and push all initial files
2. Create a simple test project
3. Test sub-agent spawning
4. Set up Canvas if device available
5. Document everything
