# Failure Classification API

A backend system designed to **analyze system incidents and classify probable failure causes** using a rule-based scoring engine.

This project simulates how real-world engineering teams (SRE / DevOps / Backend) analyze incidents, identify root causes, determine severity, and suggest corrective actions.

---

## Project Overview

Modern systems generate thousands of logs and alerts, but **incidents require structured analysis**, not raw data.

The **Failure Classification API** receives incident data and returns:
- Probable root cause
- Confidence level
- Severity classification
- Recommended actions (playbooks)
- Similar historical incidents

This project focuses on **engineering reasoning**, not machine learning.

---

## Goals

- Model real-world system incidents
- Classify failures using deterministic rules
- Provide explainable and reproducible analysis
- Store incident history for future correlation
- Expose a clean and well-documented REST API

---

## Domain Definition

### What is an Incident?

An incident is an unexpected event that negatively affects the availability, performance, or reliability of a system.

An incident is **not**:
- A single log entry
- A warning without impact
- A minor bug without users affected

---

## Supported Systems

- `api`
- `web_app`
- `database`
- `message_queue`
- `external_service`

---

## Components

- `auth`
- `payments`
- `users`
- `orders`
- `cache`
- `network`


