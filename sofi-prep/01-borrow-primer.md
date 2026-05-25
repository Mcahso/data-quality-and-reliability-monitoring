# Borrow Primer — SoFi Senior DS Interview

**Time:** 60–90 min · **Goal:** Fluent product language for Product, Business, SQL, and ML panels.

---

## One-liner (memorize)

*Borrow DS turns lending data into decisions on who we serve, how we price/approve, and how we optimize the path from intent to funded loan—without breaking risk or member trust.*

---

## Lending funnel (personal loan example)

```mermaid
flowchart LR
  visit[Visit_or_Landing] --> start[Apply_Start]
  start --> submit[Submit_Application]
  submit --> approve[Approve]
  approve --> accept[Accept_Offer]
  accept --> fund[Fund_Loan]
```

| Stage | Typical metrics | DS role |
|-------|-----------------|---------|
| Visit / awareness | Sessions, CTR to apply | Campaign attribution, incrementality |
| Apply start | Apply start rate | Funnel UX experiments |
| Submit | Completion rate | Drop-off analysis, form friction |
| Approve | Approval rate | Policy, model, mix shift |
| Accept / fund | Pull-through, time-to-fund | Ops SLA, messaging, pricing |

**Key insight:** A change at one stage can *look* like success elsewhere (e.g., more applications but lower approval rate = worse mix or looser top-of-funnel).

---

## Credit & risk (interview depth, not modeling depth)

| Term | Plain English | Why PM/marketing care |
|------|---------------|------------------------|
| **FICO** | Credit score proxy | Who gets approved; segment messaging |
| **DTI** | Debt / income | Affordability; approval caps |
| **Income verification** | Pay stubs, payroll, Plaid | Fraud vs. friction tradeoff |
| **KYC / fraud** | Identity, synthetic identity | Loss, regulatory, member trust |
| **Policy tightening** | Stricter cutoffs | Approval rate ↓, loss often ↓ |
| **Policy loosening** | More approvals | Volume ↑, loss risk ↑ |
| **Default / charge-off** | Loan not repaid | Unit economics, guardrail metric |

**Tightening vs. loosening:** Always pair with **volume**, **approval rate**, and **loss/default** — never discuss one in isolation.

---

## Unit economics vocabulary

| Metric | Definition | Borrow angle |
|--------|------------|--------------|
| **CAC** | Cost to acquire a funded borrower | Marketing efficiency; payback period |
| **Approval rate** | Approved / submitted (define denominator consistently) | Growth vs. risk lever |
| **Take rate** | Accepted offer / approved | Pricing, UX, competitive pressure |
| **Fund rate** | Funded / approved | Ops, verification, member drop-off |
| **Loss / default rate** | Bad debt / portfolio | Guardrail; lags origination |
| **NIM** | Net interest margin | Profitability on book (more finance-heavy) |

**Growth vs. profitability:** Senior DS frames tradeoffs explicitly — e.g., "We can lift apply starts 5%, but if approval falls 2 pts and loss rises, origination profit may be flat or negative."

---

## SoFi Borrow products (know names)

| Product | Member need | Analytics themes |
|---------|-------------|------------------|
| **Personal loans** | Consolidate debt, large purchase | Funnel, pricing, approval, refi competition |
| **Student loan refi** | Lower rate on existing student debt | Cohort, rate environment, forgiveness policy noise |
| **Private student loans** | In-school financing | Seasonality, co-signer, school certification |
| **Credit cards** | Revolving credit, rewards | Utilization, activation, fraud, cross-sell with bank |

**Role JD themes:** funnel conversion, experimentation, unit economics, KPI consistency, Snowflake/dbt pipelines, AI productivity, analytical storytelling.

---

## Member & company narrative

- **Mission:** Help members reach financial independence.
- **Positioning:** Mobile-first, member-centric fintech → national bank.
- **DS value prop:** Proactive insights, not ticket-taking; influence roadmap; single source of truth for KPIs.
- **Trust:** Fair lending, accurate reporting, explainable decisions to non-technical stakeholders.

---

## Glossary flashcards (self-test)

1. What is the difference between approval rate and fund rate?
2. Name three guardrail metrics for a "faster funding" launch.
3. What is mix shift and how can it explain "applications up, approval rate down"?
4. Why does default rate lag new originations?
5. What does "single source of truth" mean for KPIs across Tableau/dbt/executive decks?

**Answers (after you try):**

1. Approval = credit decision yes; fund = money disbursed (acceptance, verification, ops).
2. Loss/default, fraud, member complaints/SLA breaches, fair lending disparate impact, CAC payback.
3. More low-quality or borderline applicants entered the funnel; segment composition changed.
4. Defaults happen months/years after origination; recent book is immature.
5. One dbt mart / metric definition owned, tested, documented; same number in every dashboard.

---

## 5-minute verbal drill

Explain to an imaginary PM: *"Our approval rate dropped 3 points week over week. Here's how I'd investigate in the first 48 hours."*

Use: hypothesis tree (data bug → policy → model → mix → macro/competition), primary metrics, guardrails, what you'd ask engineering/risk.
