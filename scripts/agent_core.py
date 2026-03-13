#!/usr/bin/env python3
"""
Agent Core Operations
Business partner capabilities for Jarvis.
"""

import sqlite3
import os
import sys
from datetime import datetime
from typing import Optional, Dict, Any, List

DB_PATH = os.path.expanduser("~/clovethecreative/data/agent.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# --- LEARNINGS ---

def log_learning(category: str, task: str, what_tried: str, 
                 result: str, lesson: str, tags: str = "") -> int:
    """Log a learning/insight."""
    conn = get_db()
    cursor = conn.execute('''
        INSERT INTO learnings (category, task, what_tried, result, lesson, tags)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (category, task, what_tried, result, lesson, tags))
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id

def get_recent_learnings(limit: int = 10) -> List[Dict]:
    """Get recent learnings."""
    conn = get_db()
    rows = conn.execute('''
        SELECT * FROM learnings ORDER BY timestamp DESC LIMIT ?
    ''', (limit,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]

def search_learnings(query: str) -> List[Dict]:
    """Search learnings by text."""
    conn = get_db()
    rows = conn.execute('''
        SELECT * FROM learnings 
        WHERE task LIKE ? OR lesson LIKE ? OR tags LIKE ?
        ORDER BY timestamp DESC
    ''', (f'%{query}%', f'%{query}%', f'%{query}%')).fetchall()
    conn.close()
    return [dict(row) for row in rows]

# --- CAPABILITIES ---

def add_capability(name: str, description: str, status: str = 'active') -> int:
    """Add a new capability."""
    conn = get_db()
    try:
        cursor = conn.execute('''
            INSERT INTO capabilities (name, description, status, learned_date)
            VALUES (?, ?, ?, date('now'))
        ''', (name, description, status))
        conn.commit()
        row_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.execute('''
            UPDATE capabilities 
            SET description = ?, status = ?
            WHERE name = ?
        ''', (description, status, name))
        conn.commit()
        row = conn.execute('SELECT id FROM capabilities WHERE name = ?', (name,)).fetchone()
        row_id = row['id']
    conn.close()
    return row_id

def use_capability(name: str):
    """Record that a capability was used."""
    conn = get_db()
    conn.execute('''
        UPDATE capabilities 
        SET usage_count = usage_count + 1, last_used = CURRENT_TIMESTAMP
        WHERE name = ?
    ''', (name,))
    conn.commit()
    conn.close()

def list_capabilities(status: str = 'active') -> List[Dict]:
    """List all capabilities."""
    conn = get_db()
    if status == 'all':
        rows = conn.execute('SELECT * FROM capabilities ORDER BY learned_date DESC').fetchall()
    else:
        rows = conn.execute('''
            SELECT * FROM capabilities WHERE status = ? ORDER BY learned_date DESC
        ''', (status,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]

# --- PROJECTS & TASKS ---

def create_project(name: str, description: str = "", priority: int = 5) -> int:
    """Create a new project."""
    conn = get_db()
    cursor = conn.execute('''
        INSERT INTO projects (name, description, priority)
        VALUES (?, ?, ?)
    ''', (name, description, priority))
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id

def add_task(project_id: int, title: str, priority: int = 3) -> int:
    """Add a task to a project."""
    conn = get_db()
    cursor = conn.execute('''
        INSERT INTO tasks (project_id, title, priority)
        VALUES (?, ?, ?)
    ''', (project_id, title, priority))
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id

def complete_task(task_id: int):
    """Mark a task as completed."""
    conn = get_db()
    conn.execute('''
        UPDATE tasks SET status = 'done', completed_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()

def get_active_tasks() -> List[Dict]:
    """Get all active tasks."""
    conn = get_db()
    rows = conn.execute('''
        SELECT t.*, p.name as project_name 
        FROM tasks t
        JOIN projects p ON t.project_id = p.id
        WHERE t.status = 'todo'
        ORDER BY t.priority DESC, t.created_at
    ''').fetchall()
    conn.close()
    return [dict(row) for row in rows]

# --- DECISIONS ---

def log_decision(context: str, decision: str, rationale: str) -> int:
    """Log a significant decision."""
    conn = get_db()
    cursor = conn.execute('''
        INSERT INTO decisions (context, decision, rationale)
        VALUES (?, ?, ?)
    ''', (context, decision, rationale))
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id

# --- STATE ---

def set_state(key: str, value: str):
    """Set agent state."""
    conn = get_db()
    conn.execute('''
        INSERT OR REPLACE INTO agent_state (key, value, updated_at)
        VALUES (?, ?, CURRENT_TIMESTAMP)
    ''', (key, value))
    conn.commit()
    conn.close()

def get_state(key: str) -> Optional[str]:
    """Get agent state."""
    conn = get_db()
    row = conn.execute('SELECT value FROM agent_state WHERE key = ?', (key,)).fetchone()
    conn.close()
    return row['value'] if row else None

# --- SUMMARY ---

def get_status() -> Dict:
    """Get overall agent status."""
    conn = get_db()
    stats = {}
    
    for table in ['learnings', 'capabilities', 'projects', 'tasks', 'decisions']:
        count = conn.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]
        stats[table] = count
    
    active_tasks = conn.execute('''
        SELECT COUNT(*) FROM tasks WHERE status = 'todo'
    ''').fetchone()[0]
    stats['active_tasks'] = active_tasks
    
    conn.close()
    return stats

if __name__ == "__main__":
    print("Agent Core Operations loaded")
    print(f"Database: {DB_PATH}")
    print(f"Status: {get_status()}")
