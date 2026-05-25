# ML Hypotheticals — Sean MacRae (Senior Staff DS)

**Format:** Spoken 3–5 min answers · tradeoffs · Borrow/lending context.

**How to practice:** Read prompt → talk 3 min without notes → check key points below.

---

## 1. A/B testing in lending

**Prompt:** PM wants to ship a funnel change after 3 days because "winning variant" — what do you say?

**Key points to hit:**

| Topic | What to say |
|-------|-------------|
| **Peeking** | Early stops inflate false positives; pre-register duration or use sequential methods if standard. |
| **Intent-to-treat** | Analyze all assigned users, not only completers — else selection bias. |
| **Primary vs. guardrail** | Primary: fund rate or completion; guardrails: approval rate, loss proxy, fraud, fair lending slices. |
| **Segments** | Heterogeneous treatment effects — win overall but hurt thin-file borrowers. |
| **Power / MDE** | Underpowered tests detect only huge lifts; quote realistic MDE for decision. |
| **Borrow nuance** | Short tests miss loss; consider longer read or holdout for risk metrics. |

**Tradeoff summary:** Speed to learn vs. false launch / risk harm → recommend minimum runtime + guardrail dashboard before full rollout.

---

## 2. Approval model (classification)

**Prompt:** How do you choose a threshold on an approval model?

**Key points:**

- **Precision / recall:** Higher threshold → fewer approvals (precision↑) but missed good members (recall↓).
- **Business objective:** Optimize profit or approval subject to loss constraint — not accuracy or AUC alone.
- **Fair lending:** Monitor approval rate and adverse impact across protected classes; document overrides.
- **Human-in-the-loop:** Policy rules + model; overrides need audit trail.
- **Champion/challenger:** Shadow mode before swapping production decision engine.

**Tradeoff:** Growth (more approvals) vs. expected loss — show a threshold slide or two-scenario table verbally.

---

## 3. Drift & monitoring

**Prompt:** AUC flat but default rate rose — what do you investigate?

**Investigation order (say this as a checklist):**

1. **Data pipeline** — label delay, duplicate rows, missing segments, feature null spike.
2. **Definition drift** — did "default" or "approval" definition change?
3. **Population mix** — channel/campaign shifted to riskier applicants (AUC can hide mix).
4. **Policy / economics** — cutoffs, macro unemployment, competitor rates.
5. **Model calibration** — scores still rank-order but probabilities wrong → recalibrate.
6. **Concept drift** — true relationship changed; retrain or new features.

**Monitoring tools (name-drop appropriately):**

- **PSI** on key features and score distributions.
- **Approval rate / loss** by score decile over time.
- **Calibration plots** — predicted default vs. actual.
- **Alert fatigue** — tier alerts (investigate vs. page).

**Tradeoff:** Sensitive alerts vs. noise — tie to business impact thresholds.

---

## 4. Feature leakage & label timing

**Prompt:** New feature improves offline AUC dramatically — suspect?

**Key points:**

- **Leakage:** Features that encode post-decision info (e.g., verification outcome, disbursement date) predicting approval.
- **Label timing:** Label must be known at decision time; using 90-day default for instant approval label misaligns.
- **Temporal split:** Train on past cohorts, validate on future time window — not random split for time-series lending data.
- **Remediation:** Feature audit with domain owners; point-in-time feature store mindset.

**Borrow example:** "Using 'days to first payment' to predict approval at application — that's leakage."

---

## Bonus: Uplift / targeting (if asked)

- **Uplift model:** Who responds to marketing *because of* marketing vs. would convert anyway.
- **Cannibalization:** PL offer to members who would have borrowed anyway.
- **Ethical targeting:** Don't exclude protected classes from beneficial products; watch disparate impact.

---

## Rehearsal log (check when done aloud)

- [ ] A/B testing — 3 min spoken  
- [ ] Approval threshold — 3 min spoken  
- [ ] AUC flat, default up — 3 min spoken  
- [ ] Feature leakage — 3 min spoken  
