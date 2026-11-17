# SchedulAI — AI-Powered Personalized To-Do List Manager & Smart Scheduler

> **A full-stack, intelligent task orchestration system combining modern To-Do list management with AI-Powered Personalized Smart Scheduling and Adaptive Automatic Rescheduling.**

---

## 🌟 Core Innovation: Smart Scheduling & Adaptive Rescheduling

Most to-do lists are passive lists of text where users struggle to know:
- Which task should be tackled first
- How much time to allocate
- When to schedule each task according to availability and deadlines
- What to do when a scheduled task is missed
- How to adapt schedules to personal working habits (e.g. peak evening focus)

**SchedulAI solves this problem dynamically:**
1. **Multi-Factor Priority Scoring**: `Priority Score = Base Priority (Urgent=100, High=75, Medium=50, Low=25) + Deadline Urgency + Personal Productivity Factor + Delay Factor`.
2. **AI Smart Scheduling Engine**: Slices user-defined working hours into conflict-free time slots, preferentially places high-focus/coding tasks into preferred productive periods (e.g. 5:00 PM – 8:00 PM), and inserts restorative breaks when work exceeds maximum continuous durations.
3. **Task Completion & History Tracking**: Records real on-time vs. delayed completions and computes individual habit profiles.
4. **Missed Task Detection**: Continuously monitors scheduled tasks whose time has lapsed without completion, marking them as `Missed` / `Delayed`.
5. **Adaptive Automatic Rescheduling**: Automatically finds the next optimal conflict-free future time slot before the task's deadline, generating clear personalized reasoning for the move.
6. **AI Scheduling Assistant**: Conversational agent connected directly to the database and scheduling engine for natural language scheduling and task manipulation.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.13, Flask 3.1.1, Flask-SQLAlchemy 3.1.1, SQLAlchemy 2.0.41, psycopg2-binary 2.9.13
- **Database**: PostgreSQL 16 (production database with full relationship constraints, indexes, and user isolation; supports local or remote via `DATABASE_URL`)
- **Frontend**: Vanilla HTML5, Vanilla CSS3 (modern glassmorphism, responsive grid & flex, custom animations), Vanilla JavaScript ES6+
- **Data Visualization**: Chart.js 4.4.7 (Hourly Productivity, Category Delay Rates, 7-Day Completion Trends)
- **AI & NLP**:
  - OpenAI GPT-4o-mini client (configured via `.env`)
  - Built-in **Rule-Based NLP & Smart Heuristic Engine** (automatic fallback ensuring 100% functionality with or without an OpenAI API key)
- **Testing**: Python `unittest` test suite covering authentication, isolation, scheduler, rescheduler, analytics, and chatbot

---

## 📁 Project Structure

```
To-Do-list/
├── app.py                      # Flask application entry point & SPA router
├── requirements.txt            # Python dependencies
├── .env                        # Local environment variables
├── .env.example                # Example environment configuration
├── .gitignore                  # Git ignore rules
├── README.md                   # Full documentation & feature breakdown
│
├── database/
│   ├── __init__.py
│   └── db.py                   # SQLAlchemy instance and init_db()
│
├── models/
│   ├── __init__.py
│   ├── user.py                 # User and UserPreferences models
│   ├── task.py                 # Task model (priorities, categories, deadlines, durations)
│   ├── schedule.py             # Schedule model (start/end times, date, status, ai_reason)
│   └── history.py              # ProductivityHistory model (on-time, delayed, missed)
│
├── services/
│   ├── __init__.py
│   ├── task_analyzer.py        # Multi-factor priority scoring & AI badge generation
│   ├── personalization.py      # Behavioral history analysis & peak focus detection
│   ├── scheduler.py            # AI Smart Scheduling Engine & conflict-free slot planner
│   ├── rescheduler.py          # Missed task detector & Adaptive Automatic Rescheduler
│   ├── productivity.py         # Real KPI analytics & data-driven behavioral insights
│   ├── ai_service.py           # OpenAI API client + Rule-based NLP fallback engine
│   └── demo_data.py            # Student scenario & historical record generator
│
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py          # /api/register, /api/login, /api/logout, /api/me
│   ├── task_routes.py          # CRUD /api/tasks, /complete, /pending, /ai-input
│   ├── schedule_routes.py      # /api/schedule, /generate, /reschedule, /delayed
│   ├── analytics_routes.py     # /api/analytics, /demo-data
│   ├── assistant_routes.py     # /api/assistant, /assistant/status
│   └── preference_routes.py    # /api/preferences
│
├── static/
│   ├── css/
│   │   ├── style.css           # Design tokens, typography, glassmorphism, responsive shell
│   │   └── components.css      # Badges, timeline, stat cards, chat widget, modals
│   └── js/
│       ├── api.js              # REST API client & toast notifications
│       ├── auth.js             # Authentication, session state, demo login autofill
│       ├── app.js              # App orchestrator, task manager, modal controller
│       ├── schedule.js         # AI timeline view, "What should I do now?", calendar grid
│       ├── analytics.js        # Chart.js renderers & AI insight cards
│       └── assistant.js        # Interactive chatbot & direct system action executor
│
├── templates/
│   └── index.html              # Modern single-page application shell
│
└── tests/
    ├── conftest.py             # Pytest fixtures and test client setup
    ├── test_auth.py            # Auth & user data isolation tests
    ├── test_tasks.py           # Task CRUD & natural language input tests
    ├── test_scheduler.py       # Priority scoring & conflict avoidance tests
    ├── test_rescheduler.py     # Missed task detection & adaptive rescheduling tests
    ├── test_analytics.py       # Productivity analytics & demo scenario tests
    ├── test_assistant.py       # Assistant intent routing & database action tests
    └── run_tests.py            # Standalone unittest runner (runs offline with 0 dependencies)
```

---

## 🚀 Quickstart & Setup Guide

### 1. Requirements
Ensure Python 3.10+ is installed on your machine.

### 2. Environment Configuration
Inspect or edit `.env` in the root directory:
```env
# PostgreSQL Database URL
# Format: postgresql://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/todo_scheduler_db

# OpenAI API Configuration (Optional)
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini

# Flask Configuration
SECRET_KEY=dev-secret-key-ai-todo-2026-super-secure
FLASK_ENV=development
PORT=5000
```

### 3. Database Initialization & Migration (if migrating from SQLite)
To initialize the PostgreSQL tables and migrate any existing data:
```powershell
python database/migrate.py
```

### 4. Run the Automated Test Suite
Verify that all core features, scheduling algorithms, PostgreSQL integration, and data isolation are working:
```powershell
python -m pytest
```

### 4. Start the Application
Start the Flask development server:
```powershell
python app.py
```
Open your web browser and navigate to:
**`http://127.0.0.1:5000`**

---

## 🧭 Key Walkthrough Scenarios

### Scenario 1: Quick Demo Scenario (Java, Python, Presentation)
1. In the login modal, click **"Autofill Demo Student Credentials"** or create a new account.
2. Click the **"Load Demo Data"** button in the sidebar or top navigation.
3. This automatically instantiates:
   - **Java Assignment**: High Priority, 2 hours duration, deadline Tomorrow 8:00 PM (Coding)
   - **Presentation**: High Priority, 1 hour duration, deadline in 2 days (Work)
   - **Python Project**: Medium Priority, 1 hour duration, deadline in 3 days (Coding)
   - **DBMS Preparation**: Medium Priority, 1.5 hours duration (Study)
   - **Coding Practice**: Low Priority, 45 mins (Coding)
   - **Resume Preparation**: Medium Priority, 1 hour (Personal)
   - **5 Days of Realistic Completion History** featuring 5:00 PM – 8:00 PM peak focus productivity and coding delay patterns.
4. Navigate to **AI Schedule**: Click **"Generate AI Schedule"** -> Watch how Java Assignment and Python projects are scheduled into the evening focus window with built-in buffers and restorative breaks!
5. Navigate to **Productivity Analytics**: View the Hourly Productivity chart highlighting the 5 PM – 8 PM peak completion zone and category delay risk rates.

### Scenario 2: Adaptive Automatic Rescheduling
1. Navigate to **Delayed Tasks** or simulate an uncompleted scheduled task.
2. Click **"Auto Reschedule Missed"**.
3. The adaptive rescheduler:
   - Identifies the remaining duration and deadline.
   - Finds the next conflict-free available slot within preferred working hours.
   - Updates the schedule and explains:
     > *"Java Assignment was missed and has been automatically rescheduled to tomorrow at 05:00 PM based on your available time and matches your peak productive evening period."*

### Scenario 3: AI Natural Language Task Input
1. Click **"+ Add Task"**.
2. Select **"Method 2: AI Natural Language Input"**.
3. Enter:
   > *"I need to prepare for my Machine Learning exam on Friday at 4 PM for 90 minutes"*
4. Click **"Extract Task Info"** -> Review the structured parsed preview (Title: Machine Learning Exam, Category: Study, Priority: High, Duration: 90 mins, Deadline: Friday 4 PM).
5. Click **"Create Directly"** -> Saved into database with multi-factor priority score.

### Scenario 4: Conversational AI Assistant
1. Navigate to the **AI Assistant** tab.
2. Click one of the quick suggestions or type:
   - *"What is my schedule today?"* -> Reads today's scheduled tasks and AI reasons.
   - *"What should I do first today?"* -> Identifies top-priority item.
   - *"I have 2 hours free today. What should I do?"* -> Matches pending tasks that fit into 120 minutes.
   - *"Add Java assignment tomorrow at 6 PM"* -> Creates task directly in database.
   - *"Mark Java assignment as completed"* -> Updates task status and logs productivity history.
   - *"Reschedule my missed tasks"* -> Triggers adaptive rescheduler.
   - *"How productive was I this week?"* -> Summarizes completion rates and behavioral insights.

### Scenario 5: Strict User Isolation
1. Register **User A** and create private tasks.
2. Log out and register **User B**.
3. Observe that User B has a clean workspace with 0 tasks, 0 schedules, and independent preferences. User A's data is never visible to User B.

---

## 🔒 Security & Robustness

- **Password Hashing**: PBKDF2 with SHA-256 via Werkzeug Security.
- **Session Protection**: HTTP-only session cookies with user ID association.
- **SQL Injection Prevention**: Parameterized queries via SQLAlchemy ORM.
- **API Key Safety**: OpenAI keys are read strictly from `.env` on the server and are never exposed to clientside JavaScript.
- **Graceful Fallback**: In the absence of an external AI API key or during network disruptions, the built-in rule-based NLP engine ensures zero downtime or crashing.
