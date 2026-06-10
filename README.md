# Personalized Travel Accommodation Prototype — Data Modeling & Analytics

## 📌 Project Overview
This repository contains a fully functional data prototype developed for **WinWin.travel**, a platform designed to help users book holiday accommodations through a personalized, stress-free experience. 

The main purpose of this project is to showcase an analytical approach to data architecture and product evaluation in the travel domain. It covers everything from designing a relational database architecture and generating synthetically biased telemetry data, to writing production-ready SQL scripts that extract core product adoption, user retention, and demand behavior insights.

---

## 🛠️ Tech Stack & Database Engine
* **Language:** Python 3.13.7 (used for logical data generation via `csv`, `random`, and `datetime`)
* **Database Management System:** PostgreSQL
* **Documentation Methodology:** Markdown, Analytical Data Dictionary, and Executive Product Summary

---

## 📂 Repository Structure
The workspace is organized into clean, production-grade directories matching the component pipeline:

```text
├── dataset/
│   ├── data.csv                # Generated operational log containing 1,050 behavioral rows
│   └── dataset.py              # Python 3.13 simulation script embedded with product biases
├── sql/
│   ├── dataset_schema.sql      # Clean PostgreSQL DDL schema with relational constraints
│   └── solution.sql            # Commented, optimized analytical queries answering business goals
├── Data analyst test task.pdf  # Target business requirements provided by WinWin.travel
└── README.md                   # Executive project documentation & analysis summary
