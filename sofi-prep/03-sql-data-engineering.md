# SQL & Data Engineering — Alina Zheng (Staff DS)

**Format:** HackerRank-style · windows, joins, CTE · plus pipeline conversation.

---

## 4 practice problems (with solutions)

Run in any SQL engine (Snowflake syntax is close to standard SQL). Time yourself: **25–35 min each**.

### Problem 1: Latest application per member (window)

**Schema:**

```sql
-- applications(application_id, member_id, created_at, status)
```

**Ask:** For each `member_id`, return the most recent application row.

<details>
<summary>Solution</summary>

```sql
WITH ranked AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY member_id
      ORDER BY created_at DESC
    ) AS rn
  FROM applications
)
SELECT application_id, member_id, created_at, status
FROM ranked
WHERE rn = 1;
```

**Variant:** use `QUALIFY ROW_NUMBER() ... = 1` in Snowflake.

</details>

---

### Problem 2: Funnel conversion by apply week (CTE + aggregation)

**Schema:**

```sql
-- events(member_id, event_name, event_ts)
-- event_name: 'apply_start', 'submit', 'approve', 'fund'
```

**Ask:** By week of first `apply_start`, compute counts and rates: submit/start, approve/submit, fund/approve.

<details>
<summary>Solution sketch</summary>

```sql
WITH first_start AS (
  SELECT member_id, DATE_TRUNC('week', MIN(event_ts)) AS cohort_week
  FROM events
  WHERE event_name = 'apply_start'
  GROUP BY 1
),
member_flags AS (
  SELECT
    e.member_id,
    fs.cohort_week,
    MAX(CASE WHEN e.event_name = 'submit'  THEN 1 ELSE 0 END) AS did_submit,
    MAX(CASE WHEN e.event_name = 'approve' THEN 1 ELSE 0 END) AS did_approve,
    MAX(CASE WHEN e.event_name = 'fund'    THEN 1 ELSE 0 END) AS did_fund
  FROM events e
  JOIN first_start fs ON e.member_id = fs.member_id
  GROUP BY 1, 2
)
SELECT
  cohort_week,
  COUNT(*) AS starters,
  SUM(did_submit)  AS submitters,
  SUM(did_approve) AS approvers,
  SUM(did_fund)    AS funders,
  SUM(did_submit)::FLOAT  / NULLIF(COUNT(*), 0) AS submit_rate,
  SUM(did_approve)::FLOAT / NULLIF(SUM(did_submit), 0) AS approve_rate,
  SUM(did_fund)::FLOAT    / NULLIF(SUM(did_approve), 0) AS fund_rate
FROM member_flags
GROUP BY 1
ORDER BY 1;
```

</details>

---

### Problem 3: Members who applied but never funded (join + anti-join)

**Schema:** same `events` table.

**Ask:** List `member_id` with `apply_start` but no `fund` event.

<details>
<summary>Solution</summary>

```sql
SELECT DISTINCT a.member_id
FROM events a
WHERE a.event_name = 'apply_start'
  AND NOT EXISTS (
    SELECT 1
    FROM events f
    WHERE f.member_id = a.member_id
      AND f.event_name = 'fund'
  );
```

**Fan-out trap:** don't join apply_start to all events without aggregation — duplicates inflate counts.

</details>

---

### Problem 4: Running total originations by day (window)

**Schema:**

```sql
-- fundings(funding_id, member_id, funded_at, amount)
```

**Ask:** Daily funded count and cumulative count; also 7-day rolling average of daily amount.

<details>
<summary>Solution</summary>

```sql
WITH daily AS (
  SELECT
    DATE_TRUNC('day', funded_at) AS fund_day,
    COUNT(*) AS n_loans,
    SUM(amount) AS total_amount
  FROM fundings
  GROUP BY 1
)
SELECT
  fund_day,
  n_loans,
  SUM(n_loans) OVER (ORDER BY fund_day) AS cumulative_loans,
  total_amount,
  AVG(total_amount) OVER (
    ORDER BY fund_day
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS amount_7d_avg
FROM daily
ORDER BY fund_day;
```

</details>

---

## Syntax quick reference (day-of card)

| Need | Pattern |
|------|---------|
| Latest per group | `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ts DESC) = 1` |
| Previous value | `LAG(col) OVER (PARTITION BY id ORDER BY ts)` |
| Running sum | `SUM(col) OVER (ORDER BY ts)` |
| Dedupe join | Aggregate to user grain before joining |
| Readable pipeline | `WITH` stages: raw → clean → flags → metrics |

---

## DE talking points (5 min conversation)

### dbt

- **Layers:** staging (source-shaped) → intermediate (business logic) → marts (BI/DS-facing).
- **Tests:** `unique`, `not_null`, `relationships` — contracts with PM/BI.
- **Docs:** column descriptions = shared language for "approval rate."
- **Your story:** You've built expectation-style checks; same mindset as dbt tests + downstream impact docs in this repo.

### Snowflake

- Separate **warehouse** size for ETL vs. ad hoc.
- **Incremental models** for large event tables; merge keys matter.
- **Clustering** on common filters (e.g., `event_date`, `product`).
- Cost awareness: avoid `SELECT *` on wide history tables in notebooks.

### Airflow

- DAG dependencies, SLAs, alert on failure.
- Backfills: document metric restatements for stakeholders.
- Idempotent tasks: reruns shouldn't double-count.

### Data quality (differentiator)

Link to `data_quality_framework.py`: expectations, failure history, explanations for executives — maps to SoFi "single source of truth" for KPIs.

---

## Questions to ask Alina

1. How is the Borrow mart layer organized in dbt today?
2. What was the hardest KPI consistency or data quality issue the team fixed recently?
3. Where do DS own transforms vs. analytics engineering?
4. How do you test metric changes before exec-facing dashboards go out?

---

## External drill links (optional extra reps)

- LeetCode: 184, 180, 550, 262 (window / join classics)
- HackerRank: SQL Medium — "Top Competitors", "Weather Observation Station"

Track completions:

- [ ] Problem 1 — latest per member  
- [ ] Problem 2 — funnel by cohort week  
- [ ] Problem 3 — anti-join never funded  
- [ ] Problem 4 — running + rolling window  
