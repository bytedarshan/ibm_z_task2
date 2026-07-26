# IBM Z Summit 2026 – Event Registration System

A lightweight, terminal-based event management system built in Python and MySQL. Designed to streamline attendee onboarding, eliminate registration bottlenecks, and centralize event data for large-scale college summits.

---

## 📌 Project Overview

Hosting large-scale campus events like the **IBM Z Summit 2026** brings unique operational challenges. Managing participant lists, preventing duplicate entries, and ensuring data persists reliably can quickly get messy when handled manually through spreadsheets.

This project offers a simple, lightweight backend system that manages participant registrations via an interactive command-line interface (CLI) and persists all attendee records directly into a relational MySQL database.

---

## 🎯 Problem Statement

Manual event registration processes—such as using paper forms or unvalidated spreadsheets—lead to several common issues:
- **Duplicate Records:** Attendees registering multiple times with the same email.
- **Data Loss:** Inability to reliably store and query hundreds of participant records in real-time.
- **Slow Operations:** Difficulty in quickly searching or viewing event track allocations during peak check-in hours.

This system solves these issues by providing a structured database schema with unique constraints, input validation, and instant retrieval capabilities.

---

## ✨ Features

- **Terminal-Driven Menu:** Clean, intuitive command-line interface for volunteers to operate without training.
- **Automated Schema Initialization:** Automatically sets up the database table structure on startup if it doesn't already exist.
- **Duplicate Email Protection:** Enforces database-level uniqueness to prevent double registrations.
- **Structured Data Display:** Clean, tabular output formatting for quick attendee lookups and reporting.
- **Relational Storage:** Powered by MySQL to ensure reliable data persistence and quick queries.

---

## 🛠️ Technology Stack

- **Language:** Python 3.10+
- **Database:** MySQL Server
- **Database Driver:** `mysql-connector-python`

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3 installed on your machine.
- MySQL Server installed and running locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/bytedarshan/ibm-z-summit-registration.git](https://github.com/bytedarshan/ibm-z-summit-registration.git)
cd ibm-z-summit-registration