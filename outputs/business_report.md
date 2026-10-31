# Strategic Business Performance Report

**To:** Executive Leadership Team  
**From:** Senior Business Consultant  
**Subject:** Comprehensive E-Commerce Commercial & Operational Performance Audit  
**Data Scope:** September 2016 – October 2018 (Historical Baseline)  
**Currency Base:** Brazilian Real (R$)  

---

## 1. Executive Summary

This performance report synthesizes commercial, customer, product, and supply chain data across 99,441 lifetime orders. The platform has scaled to **R$ 15,843,553.24** in cumulative Gross Merchandise Value (GMV), maintaining an Average Order Value (AOV) of **R$ 160.58**. 

### Primary Takeaways:
* **Sustained Scale with Seasonality Peaks:** Following rapid growth throughout 2017, monthly revenue stabilized above **R$ 1.0M** from January through August 2018, peaking at **R$ 1,179,143.77** in November 2017 due to Black Friday demand.
* **Customer Retention Deficit:** The platform operates predominantly as a single-transaction acquisition engine. Only **2,997** of **96,096** total customers are repeat buyers (**3.12% repeat rate**), with an average purchase frequency of **1.03 orders per customer**.
* **Regional & Seller Concentration:** The business is heavily anchored in Brazil's Southeast. The state of São Paulo (SP) alone generates **37.38%** of total revenue (**R$ 5,921,678.12**) and houses 9 of the top 10 marketplace sellers. The top three states (SP, RJ, MG) account for **62.53%** of all revenue.
* **Fulfillment Friction:** While **97.02%** of orders are marked as delivered, the overall delivery cycle averages **12.09 days**, and **7.86%** of deliveries (**7,821 orders**) suffer delays, directly contributing to a concentration of **11,363 1-star reviews**.

---

## 2. Revenue Analysis

```
Monthly Revenue Trend (Excluding partial boundary months: 2016-09/12, 2018-09/10)
R$ 1.2M ─────────────────────────────────── [Nov-17: R$ 1.18M] ─── [Mar-18: R$ 1.16M]
R$ 1.0M ───────────────────────────────────────────────────────────── [2018 Sustained Baseline]
R$ 0.6M ────────────────────── [May-17: R$ 586K]
R$ 0.2M ── [Jan-17: R$ 137K]
```

### Observations
* **Growth Profile:** Excluding initial ramp-up periods (2016-09, 2016-10, 2016-12) and platform collection cutoffs (2018-09, 2018-10), run-rate revenue expanded from **R$ 137,188.49** in January 2017 to **R$ 1,003,308.47** in August 2018.
* **Predictable 2018 Run Rate:** Between January and August 2018, the business achieved a steady operational plateau, averaging **R$ 1.08M** per month with low variance (low of R$ 986,908.96 in February; high of R$ 1,159,698.04 in April).
* **Holiday Acceleration:** November 2017 showed a **53.27% month-over-month surge** over October 2017 (R$ 1.18M vs. R$ 769.3K), highlighting high sensitivity to retail promotional calendars.
* **Basket Metrics:** The platform Average Order Value is **R$ 160.58**, aligning closely with the Average Payment Value of **R$ 160.99**.

---

## 3. Customer Analysis

```
Customer Segmentation by Purchase Frequency
┌───────────────────────────────────────────────┬────────────┬─────────────┐
│ Customer Type                                 │ Headcount  │ % of Base   │
├───────────────────────────────────────────────┼────────────┼─────────────┤
│ Single-Purchase Customers                     │ 93,099     │ 96.88%      │
│ Repeat Customers                              │  2,997     │  3.12%      │
│ Total Unique Customers                        │ 96,096     │ 100.00%     │
└───────────────────────────────────────────────┴────────────┴─────────────┘
*Average orders per customer: 1.03
```

### Observations
* **Extreme Churn / Lack of Repurchase:** 96.88% of the customer base transacts only once. 
* **LTV Compression:** With an average order frequency of **1.03**, Customer Lifetime Value (LTV) is essentially capped at the first-order value (**R$ 160.58**), forcing the platform to rely on continuous top-of-funnel acquisition to maintain volume.
* **Geographic Distribution of Demand:** Customer distribution closely matches revenue, with SP leading at **40,302 customers** (41.94%), followed by RJ (**12,384**) and MG (**11,259**).

---

## 4. Product Performance

Category performance indicates distinct drivers for transaction volume versus absolute monetary yield:

```
Top 5 Categories: Revenue vs. Volume Dynamics
┌───────────────────────────┬────────────────────┬───────────────┬────────────────┐
│ Category                  │ Total Revenue (R$) │ Order Volume  │ Implied Unit R$│
├───────────────────────────┼────────────────────┼───────────────┼────────────────┤
│ health_beauty             │ R$ 1,441,248.07    │  9,670        │ R$ 149.04      │
│ watches_gifts             │ R$ 1,305,541.61    │  5,991        │ R$ 217.92      │
│ bed_bath_table            │ R$ 1,241,681.72    │ 11,115        │ R$ 111.71      │
│ sports_leisure            │ R$ 1,156,656.48    │  8,641        │ R$ 133.86      │
│ computers_accessories     │ R$ 1,059,272.40    │  7,827        │ R$ 135.34      │
└───────────────────────────┴────────────────────┴───────────────┴────────────────┘
*Overall average product price across catalog: R$ 120.65
```

### Observations
* **Top 5 Revenue Concentration:** The top five categories generate **R$ 6,204,400.28**, representing **39.16%** of all recorded platform revenue.
* **Volume Leader vs. Premium Driver:** 
  * `bed_bath_table` leads the catalog in volume (**11,115 orders**), but yields a lower average unit price (~R$ 111.71).
  * `watches_gifts` delivers higher monetary efficiency, capturing the #2 revenue rank (**R$ 1.31M**) on only **5,991 units** (~R$ 217.92/unit).
* **Long-Tail Dilution:** The catalog spans over 70 defined categories, with the bottom 20 categories (such as `fashion_childrens_clothes` at R$ 665.36 and `security_and_services` at R$ 324.51) contributing negligible GMV.

---

## 5. Payment Behaviour

```
Payment Method Breakdown (Total Transactions: 99,440 recorded)
┌───────────────────┬──────────────┬───────────────┬───────────────────────┐
│ Method            │ Transactions │ Volume Share  │ Operational Profile   │
├───────────────────┼──────────────┼───────────────┼───────────────────────┤
│ Credit Card       │ 74,975       │ 75.40%        │ Avg 2.93 Installments │
│ Boleto (Bancário) │ 19,784       │ 19.90%        │ Deferred settlement   │
│ Voucher           │  3,151       │  3.17%        │ Store credit/refunds  │
│ Debit Card        │  1,527       │  1.54%        │ Immediate settlement  │
│ Not Defined       │      3       │ <0.01%        │ Data integrity gap    │
└───────────────────┴──────────────┴───────────────┴───────────────────────┘
```

### Observations
* **Credit Dependency & Installments:** Over three-quarters of transactions (75.40%) are funded via credit cards, with consumers utilizing an average of **2.93 installments** to clear purchases averaging **R$ 160.99**.
* **Prevalence of Boleto:** Nearly one in five purchases (19.90%) is processed via Boleto Bancário, a cash-based or direct-invoice settlement mechanism typical to Brazil.
* **Low Direct Debit Penetration:** Debit cards represent only 1.54% of checkout activity.

---

## 6. Customer Review Analysis

```
Customer Review Score Distribution (Total: 98,673 reviews; Average: 4.09 / 5.00)
[5.0 Stars] ████████████████████████████████████████ 57,008 (57.77%)
[4.0 Stars] █████████████ 19,038 (19.29%)
[3.0 Stars] █ 8,133 (8.24%)
[2.0 Stars] ▌ 3,131 (3.17%)
[1.0 Stars] ████████ 11,363 (11.52%)
```

### Observations
* **Bimodal Polarization:** While overall sentiment is positive (77.06% at 4 or 5 stars, lifting the mean rating to **4.09**), there is a significant pocket of severe dissatisfaction: **11,363 customers gave 1-star ratings** (11.52% of all reviews).
* **Total Negative Volume:** Combined 1-star and 2-star feedback reaches **14,494 reviews** (14.69% of all submissions).
* **Category Quality Disparity:**
  * **Top-Rated:** Niche categories excel, including `cds_dvds_musicals` (4.64), `fashion_childrens_clothes` (4.50), and `books_general_interest` (4.45).
  * **Severely Low-Rated:** Sub-par ratings concentrate in `security_and_services` (2.50), `diapers_and_hygiene` (3.26), and `office_furniture` (3.49). Notably, `office_furniture` represents substantial revenue (**R$ 342,532.65**) despite its poor score.
  * **Uncategorized Inventory Drag:** Products labeled `Unknown` generated **R$ 213,662.90** across the platform and average an unsatisfactory **3.16** rating.

---

## 7. Geographic Insights

```
Geographic Contribution: Top 5 States
┌───────┬────────────────────┬──────────────┬───────────────┬──────────────────┐
│ State │ Total Revenue (R$) │ Orders       │ Customers     │ Revenue Share    │
├───────┼────────────────────┼──────────────┼───────────────┼──────────────────┤
│ SP    │ R$ 5,921,678.12    │ 41,746       │ 40,302        │ 37.38%           │
│ RJ    │ R$ 2,129,681.98    │ 12,852       │ 12,384        │ 13.44%           │
│ MG    │ R$ 1,856,161.49    │ 11,635       │ 11,259        │ 11.72%           │
│ RS    │ R$   885,826.76    │  5,466       │  5,277        │  5.59%           │
│ PR    │ R$   800,935.44    │  5,045       │  4,882        │  5.05%           │
└───────┴────────────────────┴──────────────┴───────────────┴──────────────────┘
```

```
Seller Concentration (Top 10 Sellers by Revenue)
• Seller 4869f7a5dfa277a7dca6462dcf3b52b2 (SP): R$ 249,640.70
• Seller 7c67e1448b00f6e969d365cea6b010ab (SP): R$ 239,536.44
• Seller 53243585a1d6dc2643021fd1853d8905 (BA): R$ 235,856.68
• Seller 4a3ca9315b744ce9f8e9374361493884 (SP): R$ 235,539.96
• Seller fa1c13f2614d7b5c4749cbc52fecda94 (SP): R$ 204,084.73
• Seller da8622b14eb17ae2831f4ac5b9dab84a (SP): R$ 185,192.32
• Seller 7e93a43ef30c4f03f38b393420bc753a (SP): R$ 182,754.05
• Seller 1025f0e2d44d7041d6cf58b6550e0bfa (SP): R$ 172,860.69
• Seller 7a67c85e85bb2ce8582c35f2203ad736 (SP): R$ 162,648.38
• Seller 955fee9216a65b617aa5c0531780ce60 (SP): R$ 160,602.68
```

### Observations
* **Severe Macro-Regional Clustering:** The Southeast triangle (SP, RJ, MG) commands **R$ 9.91M**, or **62.53%** of total business turnover.
* **Supply-Side Centralization:** Marketplace fulfillment is centered in São Paulo. **9 of the top 10 sellers** are located in SP; only 1 top-performing seller operates outside SP (Bahia - BA, generating R$ 235,856.68).
* **Underpenetrated Frontiers:** Major populous states in the North and Center-West account for a tiny fraction of total volume (e.g., Amazonas has only 143 customers; Roraima has 45).

---

## 8. Operational Insights

```
Order Pipeline Health (Total Orders: 99,441)
┌──────────────────┬──────────────┬───────────────┐
│ Status           │ Count        │ % of Total    │
├──────────────────┼──────────────┼───────────────┤
│ Delivered        │ 96,478       │ 97.02%        │
│ Shipped          │  1,107       │  1.11%        │
│ Canceled         │    625       │  0.63%        │
│ Unavailable      │    609       │  0.61%        │
│ Invoiced         │    314       │  0.32%        │
│ Processing       │    301       │  0.30%        │
│ Created          │      5       │ <0.01%        │
│ Approved         │      2       │ <0.01%        │
└──────────────────┴──────────────┴───────────────┘
```

### Observations
* **Core Logistics Metrics:** 
  * **Average Delivery Time:** **12.09 days**.
  * **Delayed Deliveries:** **7,821 orders** arrived after the promised delivery window, an operational delay rate of **7.86%**.
* **Operational Leakage:** An aggregate of **1,234 orders** failed to reach fulfillment (**625 canceled** and **609 unavailable**), representing **1.24%** of total demand that converted at checkout but was lost to operational issues.

---

## 9. Business Risks

* **Risk 1: Fragile Single-Purchase Unit Economics (Retention Failure)**  
  With only **3.12% repeat buyers** and an order frequency of **1.03**, the business is on an acquisition treadmill. Any increase in digital media acquisition costs will directly compress margins, as the platform cannot amortize acquisition expenses across multiple transactions.
* **Risk 2: Supply Chain Exposure and Geographic Bottlenecks**  
  With 9 of the top 10 sellers based in SP, outbound logistics to northern and peripheral states must travel long transit lanes. This contributes to an extended **12.09-day delivery cycle** and **7,821 delayed orders**, increasing the risk of negative reviews.
* **Risk 3: Correlation Between Delivery Failures and Brand Detraction**  
  The volume of 1-star reviews (**11,363**) aligns closely with the total volume of operational friction (**7,821 delayed orders** plus **1,234 canceled or unavailable orders** = 9,055 direct logistical failures). Delivery delays are likely the primary driver of customer dissatisfaction.
* **Risk 4: Financial Working Capital Lag via Boleto Processing**  
  With **19,784 orders (19.90%)** executed through Boleto Bancário, the platform faces settlement delays and order expirations, which can tie up seller inventory while awaiting payment confirmation.

---

## 10. Growth Opportunities

* **Opportunity 1: Category Re-allocation Toward High-Value Assortments**  
  `watches_gifts` generates R$ 1.31M across only 5,991 orders (~R$ 217.92/order), showing high pricing headroom. Expanding listings in high-AOV, high-satisfaction categories can lift overall revenue without increasing order processing volume.
* **Opportunity 2: Post-Purchase Monetization and Cross-Selling**  
  The gap between 96,096 unique customers and only 2,997 repeat buyers is the largest commercial opportunity in the business. High-frequency consumable categories (such as `health_beauty`, our #1 category at R$ 1.44M) can serve as an ideal base for replenishment purchases to raise the 1.03 purchase frequency.
* **Opportunity 3: Targeted Regional Logistics Programs in Secondary Hubs**  
  RJ and MG combined represent **24,487 orders** and **R$ 3.99M in GMV**, yet supply is concentrated in SP. Establishing fulfillment partnerships or dedicated logistics lanes between SP, RJ, and MG could reduce the 12.09-day transit time and lower the 7.86% delay rate.
* **Opportunity 4: Remediation of Uncataloged (`Unknown`) Inventory**  
  The unclassified category `Unknown` accounts for **R$ 213,662.90** in sales and a poor **3.16 average rating**. Correcting taxonomy and metadata for these listings can improve search discovery, reduce buyer mismatch, and raise review scores.

---

## 11. Strategic Recommendations

The following phased roadmap outlines concrete actions to address operational bottlenecks, customer retention, and commercial performance:

```
Strategic Roadmap
┌──────────────────────────────────────┬───────────────────────┬──────────────────────────────┐
│ Strategic Initiative                 │ Core Metric Impacted  │ Direct Evidence Base         │
├──────────────────────────────────────┼───────────────────────┼──────────────────────────────┤
│ 1. Delivery SLA Remediation          │ 7.86% Delay Rate      │ 7,821 delayed orders;        │
│    (SP-RJ-MG express lanes)          │ 11,363 1-Star Reviews │ 12.09-day avg delivery time  │
├──────────────────────────────────────┼───────────────────────┼──────────────────────────────┤
│ 2. Category Assortment Restructuring │ R$ 160.58 AOV;        │ Watches/Gifts: R$ 217.92/unit│
│    (Target high-margin/AOV segments) │ Total Gross GMV       │ Office Furniture: 3.49 rating│
├──────────────────────────────────────┼───────────────────────┼──────────────────────────────┤
│ 3. Automated Repurchase Campaigns    │ 3.12% Repeat Rate;    │ 93,099 single-order buyers;  │
│    (Focus on Health & Beauty)        │ 1.03 Orders/Customer  │ R$ 1.44M Health & Beauty GMV │
├──────────────────────────────────────┼───────────────────────┼──────────────────────────────┤
│ 4. Inventory Data Cleansing          │ 3.16 Rating (Unknown) │ R$ 213,662.90 in unclassified│
│    (Classify "Unknown" category)     │ 609 Unavailable Orders│ sales; 1,234 failed orders   │
└──────────────────────────────────────┴───────────────────────┴──────────────────────────────┘
```

### Milestone 1: Operational & Delivery Remediation (Days 1–90)
* **Action:** Audit shipping lanes linking São Paulo sellers to buyers in RJ, MG, and the Northeast. Establish strict service-level agreements (SLAs) for sellers who experience dispatch delays.
* **Evidence Base:** 7,821 orders were delayed (7.86% failure rate), contributing to a long 12.09-day average delivery timeline and 11,363 1-star reviews.
* **Expected Outcome:** Lower overall fulfillment delays to protect customer sentiment across the core Southeast corridors.

### Milestone 2: Retention & Re-engagement Programs (Days 30–120)
* **Action:** Build automated post-purchase marketing flows for consumable categories—focusing on `health_beauty` (9,670 orders, R$ 1.44M revenue)—targeting re-orders at 30-, 60-, and 90-day intervals.
* **Evidence Base:** Repeat buyers account for just 3.12% of the customer base (2,997 of 96,096), leaving average frequency at 1.03 orders per customer.
* **Expected Outcome:** Drive repeat purchases in high-performing consumable categories to improve customer lifetime value.

### Milestone 3: Catalog Pruning and Inventory Quality Controls (Days 60–180)
* **Action:** Quarantine or re-catalogue the **R$ 213,662.90** worth of inventory currently designated as `Unknown`. Implement quality thresholds for underperforming product categories like `office_furniture` (3.49 rating across R$ 342.5K GMV) and address stock tracking to reduce the 609 "unavailable" order cancellations.
* **Evidence Base:** 1,234 orders failed due to cancellations (625) or unfulfilled inventory (609), while low-rated categories continue to pull down the platform's 4.09 average score.
* **Expected Outcome:** Reduce inventory-related fulfillment cancellations and eliminate low-rated catalog offerings that create customer friction.