import sqlite3
import os
import json
from datetime import datetime
from typing import Optional, List, Dict, Any

DB_PATH = os.path.expanduser("~/clovethecreative/data/agent.db")

def get_db():
    """Get database connection with proper settings."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    """Initialize database schema."""
    conn = get_db()
    
    # Core tables for agent memory
    conn.executescript('''
        -- Agent identity and state
        CREATE TABLE IF NOT EXISTS agent_state (
            key TEXT PRIMARY KEY,
            value TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        -- Learnings and insights
        CREATE TABLE IF NOT EXISTS learnings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            category TEXT NOT NULL,
            task TEXT,
            what_tried TEXT,
            result TEXT,
            lesson TEXT,
            applied BOOLEAN DEFAULT FALSE,
            tags TEXT
        );
        
        -- Capability inventory
        CREATE TABLE IF NOT EXISTS capabilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            status TEXT DEFAULT 'active',
            learned_date DATE,
            description TEXT,
            usage_count INTEGER DEFAULT 0,
            last_used TIMESTAMP
        );
        
        -- Projects and tasks
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            description TEXT,
            priority INTEGER DEFAULT 5
        );
        
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'todo',
            priority INTEGER DEFAULT 3,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects(id)
        );
        
        -- Session tracking
        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY,
            started TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ended TIMESTAMP,
            summary TEXT,
            key_decisions TEXT,
            files_modified TEXT
        );
        
        -- Business metrics
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            metric_type TEXT,
            value REAL,
            context TEXT
        );
        
        -- Decisions log
        CREATE TABLE IF NOT EXISTS decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            context TEXT,
            decision TEXT,
            rationale TEXT,
            outcome TEXT
        );
    ''')
    
    conn.commit()
    conn.close()
    print(f"✓ Database initialized at {DB_PATH}")

if __name__ == "__main__":
    init_db()
