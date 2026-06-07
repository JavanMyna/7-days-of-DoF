# 🧭 Life Simulation Project Plan (Structured Development Guide)

This document outlines a step-by-step approach to building a small life simulation game. The goal is to **finish a playable core first**, then gradually expand it into a structured, portfolio-worthy project.

---

## ⚠️ Core Warning

This type of project can either become:

- ✅ A **strong portfolio project**
- ❌ Or a “forever unfinished simulator” with too many features

### Golden Rule:
> Always prioritize finishing a small working system over adding more features.

---

# 🧭 Core Strategy: Vertical Slice First, Expansion Later

You are **NOT** building a full life simulator.

You ARE building:

> A small playable loop that already feels like a complete game
Then you expand it step by step.

---

# 🧱 PHASE 1 — MVP (Minimum Viable Product)

⏱️ Target: 2–4 days max

## 🎯 Goal
Create a complete playable loop:
> Day 1 → Day 7 simulation

---

## 📅 1. Time System

- Day counter: `Day 1 → Day 7`
- Each day has 3 time blocks:
  - Morning
  - Afternoon
  - Night

---

## 📊 2. Stats System (ONLY 3)

Keep it minimal:
- Energy
- Focus
- Knowledge (1 subject only, e.g. CS)

---

## 🎮 3. Actions (ONLY 3)

Player can choose:
- Study
- Rest
- Scroll

---

## 🎲 4. Event System (VERY SIMPLE)

- Maximum: **1 random event per day**
- Occurs with low probability (e.g. 1/10 chance per time block or day)

### Example Events:

- Lecturer gives surprise quiz → (+/- focus)
- Feeling mentally drained → (-energy)

### Life Events Examples:

- Mom asks you to buy something → (-energy, +bond)
- Brother asks for math help → (-energy, +bond)
- Cooking responsibility → (+cooking, -energy)

---

## 🧠 Why Phase 1 matters

This phase proves that:

- Your code architecture works
- The gameplay loop is fun
- You can actually finish a project

> If you don’t finish this phase, later phases don’t matter.

---

# 🧱 PHASE 2 — Make it Feel Like a Real System

Only start this AFTER MVP works.

---

## 📚 1. Multiple Subjects

Start small:
- Math
- CS
- Physics (optional later)

---

## 📈 2. Progression System

- Each subject has its own knowledge level
- Track improvement over time

---

## 🎲 3. Improved Event System

Organize events into categories:
- Study-related events
- Life-related events
- Random fatigue events

---

## 🏗️ 4. Introduce OOP Structure (ONLY when needed)

Start refactoring into:
- `Student`
- `Subject`
- `Game`
- `Event`

> Only create classes when you actually need them.

---

# 🧱 PHASE 3 — Portfolio-Grade Project

Focus: structure and polish, not new chaos.

---

## 💾 1. Save / Load System

- Save game state using JSON
- Resume from last session

---

## 🧹 2. Clean Architecture

Separate your code into layers:
- Logic layer (game rules)
- Data layer (stats, subjects)
- UI layer (CLI or simple interface)

---

## 📊 3. Logging System
- Daily performance summary
- Progress tracking
- Activity history

---

> This is where the project starts looking like real software.

---

# 🧱 PHASE 4 — Showcase Upgrade

Optional enhancements for presentation value:
- Simple GUI (Tkinter or web-based UI)
- Graphs (e.g. energy over time)
- Branching story events
- Music integration (VN-style OST idea)
- Balancing system for gameplay tuning

---

# ⚠️ Golden Rule (VERY IMPORTANT)

Before adding any feature, ask:
> “Does this change the core loop?”

### Core Loop:
> Choose action → time passes → stats change → next day

- If ❌ NO → save it for later
- If ✅ YES → consider adding it now

---

# 🧠 Anti-Overengineering Rule
Only design what you currently need.

Examples:
- Need energy system → create `Student.energy`
- Need subjects → add `Subject` class
- Need events → introduce `Event` system

### This prevents:
- Overcomplicated architecture early
- Wasted planning time
- Abandoned projects

---

# 🎯 Why This Becomes Portfolio-Worthy

Recruiters don’t care about:
- Massive feature lists

They care about:
- Clear structure evolution
- Clean, readable code
- Ability to scale a project
- Evidence of iteration

---

## 🧾 Final Result (What your GitHub shows)

> “Started as a simple CLI life simulator → evolved into a structured OOP system with events, progression, and save/load mechanics”

---
