# 🎧 Social Listening & Response Agent

[![A2A Compatible](https://img.shields.io/badge/A2A-Compatible-blueviolet)](https://github.com/mateusoliveiradev1/social-listening-responder)
[![Payment x402](https://img.shields.io/badge/Payment-x402-gold)](https://nevermined.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Never miss a critical brand mention. Never send the wrong response.**

Community managers spend hours manually reading through mentions, guessing tone, and drafting replies. One wrong response to a viral complaint costs brand equity. This agent uses a **deterministic sentiment baseline script** to classify every mention before the LLM drafts a single word — eliminating toxic positivity responses to angry customers.

### ✨ Enterprise Features
* **Deterministic Sentiment Scoring:** `sentiment_baseline.py` classifies mentions as Positive, Negative, or Neutral using keyword analysis — no LLM guessing.
* **Intent Categorization:** Automatically labels each mention as Support Request, Praise, or Escalation Risk.
* **On-Brand Draft Responses:** All replies are locked to the brand voice you define at intake.
* **Escalation SOP:** If "Negative" is detected, outputs an immediate 3-step escalation procedure for your team.

### 🚀 Installation (A2A Protocol)
```bash
npx skillsadd mateusoliveiradev1/social-listening-responder
```

---
<p align="center">Developed by <strong>Mateus Oliveira</strong> · <em>Community Management & Agent Architecture</em></p>
