#!/usr/bin/env python3
"""
CLI interface for agent operations.
"""

import sys
import json
from agent_core import (
    log_learning, get_recent_learnings, search_learnings,
    add_capability, use_capability, list_capabilities,
    create_project, add_task, complete_task, get_active_tasks,
    log_decision, set_state, get_state, get_status
)

def main():
    if len(sys.argv) < 2:
        print("Usage: agent_cli.py <command> [args]")
        print("\nCommands:")
        print("  learn <category> <task> <tried> <result> <lesson>")
        print("  recent_learnings [limit]")
        print("  search_learnings <query>")
        print("  capability <name> <description> [status]")
        print("  capabilities [status]")
        print("  project <name> [description] [priority]")
        print("  task <project_id> <title> [priority]")
        print("  complete_task <task_id>")
        print("  tasks")
        print("  decision <context> <decision> <rationale>")
        print("  set <key> <value>")
        print("  get <key>")
        print("  status")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "learn":
        if len(sys.argv) < 7:
            print("Usage: learn <category> <task> <tried> <result> <lesson>")
            sys.exit(1)
        id = log_learning(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
        print(f"Logged learning #{id}")
    
    elif cmd == "recent_learnings":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        for l in get_recent_learnings(limit):
            print(f"[{l['timestamp']}] {l['category']}: {l['task']}")
    
    elif cmd == "search_learnings":
        if len(sys.argv) < 3:
            print("Usage: search_learnings <query>")
            sys.exit(1)
        for l in search_learnings(sys.argv[2]):
            print(f"[{l['timestamp']}] {l['task']}: {l['lesson']}")
    
    elif cmd == "capability":
        if len(sys.argv) < 4:
            print("Usage: capability <name> <description> [status]")
            sys.exit(1)
        status = sys.argv[4] if len(sys.argv) > 4 else 'active'
        id = add_capability(sys.argv[2], sys.argv[3], status)
        print(f"Added/updated capability #{id}")
    
    elif cmd == "capabilities":
        status = sys.argv[2] if len(sys.argv) > 2 else 'active'
        for c in list_capabilities(status):
            print(f"{c['status']:12} {c['name']}: {c['description'][:50]}...")
    
    elif cmd == "project":
        if len(sys.argv) < 3:
            print("Usage: project <name> [description] [priority]")
            sys.exit(1)
        desc = sys.argv[3] if len(sys.argv) > 3 else ""
        priority = int(sys.argv[4]) if len(sys.argv) > 4 else 5
        id = create_project(sys.argv[2], desc, priority)
        print(f"Created project #{id}")
    
    elif cmd == "task":
        if len(sys.argv) < 4:
            print("Usage: task <project_id> <title> [priority]")
            sys.exit(1)
        priority = int(sys.argv[4]) if len(sys.argv) > 4 else 3
        id = add_task(int(sys.argv[2]), sys.argv[3], priority)
        print(f"Added task #{id}")
    
    elif cmd == "complete_task":
        if len(sys.argv) < 3:
            print("Usage: complete_task <task_id>")
            sys.exit(1)
        complete_task(int(sys.argv[2]))
        print(f"Completed task #{sys.argv[2]}")
    
    elif cmd == "tasks":
        for t in get_active_tasks():
            print(f"P{t['priority']} [{t['project_name']}] {t['title']}")
    
    elif cmd == "decision":
        if len(sys.argv) < 5:
            print("Usage: decision <context> <decision> <rationale>")
            sys.exit(1)
        id = log_decision(sys.argv[2], sys.argv[3], sys.argv[4])
        print(f"Logged decision #{id}")
    
    elif cmd == "set":
        if len(sys.argv) < 4:
            print("Usage: set <key> <value>")
            sys.exit(1)
        set_state(sys.argv[2], sys.argv[3])
        print(f"Set {sys.argv[2]} = {sys.argv[3]}")
    
    elif cmd == "get":
        if len(sys.argv) < 3:
            print("Usage: get <key>")
            sys.exit(1)
        value = get_state(sys.argv[2])
        print(f"{sys.argv[2]} = {value}")
    
    elif cmd == "status":
        print(json.dumps(get_status(), indent=2))
    
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
