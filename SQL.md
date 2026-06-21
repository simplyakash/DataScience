# SQL Analytics Test (Software Subscriptions)

## Table: subscriptions

| Column Name | Data Type |
|------------|------------|
| user_id | INT |
| subscription_id | INT |
| start_date | DATE |
| end_date | DATE |
| monthly_fee | DECIMAL(10,2) |

---

## Sample Data

| user_id | subscription_id | start_date | end_date | monthly_fee |
|----------|----------------|------------|----------|-------------|
| 1 | 101 | 2024-01-01 | 2024-03-31 | 20 |
| 2 | 102 | 2024-01-15 | 2024-02-15 | 15 |
| 3 | 103 | 2024-02-01 | 2024-05-31 | 30 |
| 1 | 104 | 2024-04-01 | 2024-06-30 | 25 |

---

# Q1. Find Active Subscriptions on a Given Date

### Requirement

Find subscriptions active on:

```sql
'2024-02-10'
```

### Query

```sql
SELECT *
FROM subscriptions
WHERE '2024-02-10' BETWEEN start_date AND end_date;
```

---

# Q2. Calculate Total Monthly Revenue

### Requirement

Calculate revenue from all active subscriptions.

### Query

```sql
SELECT
    SUM(monthly_fee) AS total_revenue
FROM subscriptions
WHERE CURRENT_DATE BETWEEN start_date AND end_date;
```

---

# Q3. Find Users With Multiple Subscriptions

### Query

```sql
SELECT
    user_id,
    COUNT(*) AS subscription_count
FROM subscriptions
GROUP BY user_id
HAVING COUNT(*) > 1;
```

---

# Q4. Calculate Subscription Duration (Days)

### MySQL

```sql
SELECT
    subscription_id,
    DATEDIFF(end_date, start_date) AS duration_days
FROM subscriptions;
```

### PostgreSQL

```sql
SELECT
    subscription_id,
    end_date - start_date AS duration_days
FROM subscriptions;
```

---

# Q5. Find Average Subscription Duration

### MySQL

```sql
SELECT
    AVG(DATEDIFF(end_date, start_date)) AS avg_duration
FROM subscriptions;
```

### PostgreSQL

```sql
SELECT
    AVG(end_date - start_date) AS avg_duration
FROM subscriptions;
```

---

# Q6. Monthly Revenue by Month

### PostgreSQL

```sql
SELECT
    DATE_TRUNC('month', start_date) AS month,
    SUM(monthly_fee) AS revenue
FROM subscriptions
GROUP BY 1
ORDER BY 1;
```

---

# Q7. Find Expired Subscriptions

```sql
SELECT *
FROM subscriptions
WHERE end_date < CURRENT_DATE;
```

---

# Q8. Find Currently Active Users

```sql
SELECT DISTINCT user_id
FROM subscriptions
WHERE CURRENT_DATE BETWEEN start_date AND end_date;
```

---

# Q9. Top 3 Highest Paying Users

```sql
SELECT
    user_id,
    SUM(monthly_fee) AS total_paid
FROM subscriptions
GROUP BY user_id
ORDER BY total_paid DESC
LIMIT 3;
```

---

# Q10. Monthly Recurring Revenue (MRR)

### Definition

```text
MRR = Sum of monthly subscription fees from all active subscriptions.
```

### Query

```sql
SELECT
    SUM(monthly_fee) AS MRR
FROM subscriptions
WHERE CURRENT_DATE BETWEEN start_date AND end_date;
```

---

# Q11. Find Churned Users

### Definition

Users whose subscriptions have already ended.

### Query

```sql
SELECT DISTINCT user_id
FROM subscriptions
WHERE end_date < CURRENT_DATE;
```

---

# Q12. Retention Analysis

### Requirement

Find users who renewed subscriptions.

### Query

```sql
SELECT
    user_id,
    COUNT(*) AS total_subscriptions
FROM subscriptions
GROUP BY user_id
HAVING COUNT(*) > 1;
```

---

# Q13. Revenue Generated Per User

```sql
SELECT
    user_id,
    SUM(monthly_fee) AS revenue
FROM subscriptions
GROUP BY user_id
ORDER BY revenue DESC;
```

---

# Q14. Running Revenue Total

### Window Function Example

```sql
SELECT
    subscription_id,
    monthly_fee,
    SUM(monthly_fee) OVER (
        ORDER BY start_date
    ) AS running_revenue
FROM subscriptions;
```

---

# Q15. Rank Users by Revenue

```sql
SELECT
    user_id,
    SUM(monthly_fee) AS revenue,
    RANK() OVER (
        ORDER BY SUM(monthly_fee) DESC
    ) AS revenue_rank
FROM subscriptions
GROUP BY user_id;
```

---

# Q16. Find Overlapping Subscriptions

### Requirement

Detect users having overlapping subscriptions.

```sql
SELECT
    s1.user_id,
    s1.subscription_id,
    s2.subscription_id
FROM subscriptions s1
JOIN subscriptions s2
    ON s1.user_id = s2.user_id
   AND s1.subscription_id < s2.subscription_id
   AND s1.start_date <= s2.end_date
   AND s2.start_date <= s1.end_date;
```

---

# Q17. Find Latest Subscription Per User

```sql
SELECT *
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY start_date DESC
        ) AS rn
    FROM subscriptions
) t
WHERE rn = 1;
```

---

# Q18. Cumulative Revenue Per User

```sql
SELECT
    user_id,
    start_date,
    monthly_fee,
    SUM(monthly_fee) OVER (
        PARTITION BY user_id
        ORDER BY start_date
    ) AS cumulative_revenue
FROM subscriptions;
```

---

# Bonus: Monthly Revenue Trend

```sql
SELECT
    DATE_TRUNC('month', start_date) AS month,
    SUM(monthly_fee) AS revenue
FROM subscriptions
GROUP BY month
ORDER BY month;
```

---

# Bonus: User Lifetime Value (LTV)

```sql
SELECT
    user_id,
    SUM(monthly_fee) AS lifetime_value
FROM subscriptions
GROUP BY user_id
ORDER BY lifetime_value DESC;
```

---

# Bonus: Subscription Count by User

```sql
SELECT
    user_id,
    COUNT(*) AS total_subscriptions
FROM subscriptions
GROUP BY user_id
ORDER BY total_subscriptions DESC;
```

---

# SQL Concepts Covered

```text
✓ SELECT

✓ WHERE

✓ GROUP BY

✓ HAVING

✓ ORDER BY

✓ LIMIT

✓ INNER JOIN

✓ SELF JOIN

✓ AGGREGATE FUNCTIONS

✓ SUM()

✓ AVG()

✓ COUNT()

✓ DATE FUNCTIONS

✓ WINDOW FUNCTIONS

✓ RANK()

✓ ROW_NUMBER()

✓ PARTITION BY

✓ CUMULATIVE SUM

✓ REVENUE ANALYTICS

✓ MRR (Monthly Recurring Revenue)

✓ LTV (Lifetime Value)

✓ CHURN ANALYSIS

✓ RETENTION ANALYSIS

✓ SUBSCRIPTION ANALYTICS
```

---

# Interview Cheat Sheet

```text
Active Users
    ↓
CURRENT_DATE BETWEEN start_date AND end_date

MRR
    ↓
SUM(monthly_fee)

Retention
    ↓
COUNT(*) > 1

Churn
    ↓
end_date < CURRENT_DATE

Latest Subscription
    ↓
ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY start_date DESC)

Running Revenue
    ↓
SUM() OVER(ORDER BY start_date)

Revenue Rank
    ↓
RANK() OVER(ORDER BY revenue DESC)
```
