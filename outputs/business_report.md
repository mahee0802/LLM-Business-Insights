# Executive Performance Report: E-Commerce Business Analysis

**Evaluation Period:** October 2016 – August 2018  
**Prepared For:** Executive Leadership Team  
**Focus Areas:** Retail Analytics, Revenue Optimization, Customer Behavior, Product Strategy, Supply Chain Analytics, Business Intelligence  

---

## 1. Executive Summary

Between October 2016 and August 2018 (the reliable full-month reporting window), the enterprise generated **R$ 15,843,553.24** in total revenue across **99,441 orders** and **96,096 unique customers**. The average order value (AOV) stood at **R$ 160.58**, supported by an average product price of **R$ 120.65**.

Revenue demonstrated sustained expansion over the analysis window, increasing from **R$ 56,808.84** in October 2016 to a peak of **R$ 1,179,143.77** in November 2017, and maintaining monthly revenues above **R$ 1.0M** throughout most of 2018. 

However, structural vulnerabilities exist in customer retention and geographic distribution:
* **Customer Retention:** Average orders per customer stand at **1.03**, with only **2,997 repeat customers** out of 96,096 total customers.
* **Geographic Concentration:** The state of São Paulo (**SP**) accounts for **37.37%** of total revenue (**R$ 5,921,678.12**) and **9 of the top 10 sellers**.
* **Operational Performance:** Average delivery time is **12.5 days**, with **6,535 delayed orders** representing **6.57%** of total orders.

---

## 2. Revenue Analysis

### Monthly Revenue Trends
*Note: Per data governance guidelines, months with partial data collection (2016-09, 2016-12, 2018-09, 2018-10) are excluded from trend evaluations.*

* **Initial Phase (Oct 2016 – Dec 2016):** October 2016 recorded **R$ 56,808.84**.
* **Scaling Phase (Jan 2017 – Oct 2017):** Monthly revenue grew steadily from **R$ 137,188.49** (Jan 2017) to **R$ 769,312.37** (Oct 2017).
* **Peak & Stabilization (Nov 2017 – Aug 2018):** November 2017 reached a historical peak of **R$ 1,179,143.77**. Following a pull-back in December 2017 (**R$ 863,547.23**), monthly revenue stabilized at an average exceeding **R$ 1.06M** per month between January 2018 and August 2018 (ranging from **R$ 986,908.96** in Feb 2018 to **R$ 1,159,698.04** in Apr 2018).

```
+-------------------+--------------------+
| Monthly Timeline  | Revenue (R$)       |
+-------------------+--------------------+
| 2016-10           | R$ 56,808.84       |
| 2017-01           | R$ 137,188.49      |
| 2017-05           | R$ 586,190.95      |
| 2017-11           | R$ 1,179,143.77    |
| 2018-01           | R$ 1,107,301.89    |
| 2018-04           | R$ 1,159,698.04    |
| 2018-08           | R$ 1,003,308.47    |
+-------------------+--------------------+
```

### Top Categories by Revenue
The enterprise catalog spans over 70 categories, but revenue generation is concentrated in top-performing product lines:

| Category | Revenue (R$) | % of Total Revenue |
| :--- | :--- | :--- |
| **health_beauty** | R$ 1,441,248.07 | 9.10% |
| **watches_gifts** | R$ 1,305,541.61 | 8.24% |
| **bed_bath_table** | R$ 1,241,681.72 | 7.84% |
| **sports_leisure** | R$ 1,156,656.48 | 7.30% |
| **computers_accessories** | R$ 1,059,272.40 | 6.69% |
| **furniture_decor** | R$ 902,511.79 | 5.70% |
| **housewares** | R$ 778,397.77 | 4.91% |
| **cool_stuff** | R$ 719,329.95 | 4.54% |
| **auto** | R$ 685,384.32 | 4.33% |
| **garden_tools** | R$ 584,219.21 | 3.69% |
| *Top 10 Total* | *R$ 9,874,243.32* | *62.32%* |

* **Data Anomaly Note:** An "Unknown" product category accounts for **R$ 213,662.90** across the dataset, indicating uncategorized transactions requiring catalog cleanup.

---

## 3. Customer Analysis

### Metrics Summary
* **Total Unique Customers:** 96,096
* **Repeat Customers:** 2,997
* **Repeat Customer Rate:** 3.12%
* **Average Orders per Customer:** 1.03

### Behavioral Observations
The customer base is overwhelmingly single-purchase oriented. Out of 96,096 total customers, 93,099 made only a single purchase. 

```
Customer Retention Breakdown:
- One-Time Purchasers: 96.88% (93,099 customers)
- Repeat Purchasers:   3.12%  (2,997 customers)
```

### Business Implications
The enterprise operates primarily on acquisition revenue rather than lifetime customer value. High reliance on acquiring new customers without retaining existing ones increases long-term acquisition cost pressures.

---

## 4. Product Performance

### Volume vs. Revenue Comparison
Top product categories exhibit varying price dynamics and order densities:

| Category | Units Sold (Volume) | Total Revenue (R$) | Revenue per Unit (R$) |
| :--- | :--- | :--- | :--- |
| **bed_bath_table** | 11,115 | R$ 1,241,681.72 | R$ 111.71 |
| **health_beauty** | 9,670 | R$ 1,441,248.07 | R$ 149.04 |
| **sports_leisure** | 8,641 | R$ 1,156,656.48 | R$ 133.86 |
| **furniture_decor** | 8,334 | R$ 902,511.79 | R$ 108.29 |
| **computers_accessories** | 7,827 | R$ 1,059,272.40 | R$ 135.34 |
| **housewares** | 6,964 | R$ 778,397.77 | R$ 111.77 |
| **watches_gifts** | 5,991 | R$ 1,305,541.61 | R$ 217.92 |

* **High Volume Driver:** `bed_bath_table` leads total unit sales (11,115 orders) but generates lower revenue per unit compared to `health_beauty` and `watches_gifts`.
* **High Unit Value Driver:** `watches_gifts` ranks 7th in volume (5,991 units) but 2nd in revenue (R$ 1,305,541.61), with an average unit yield of **R$ 217.92** compared to the overall catalog average product price of **R$ 120.65**.

---

## 5. Payment Behaviour

### Method Distribution & Financial Structure
* **Average Payment Value:** R$ 160.99
* **Average Installments:** 2.93

| Payment Method | Volume (Transactions) | Share of Total Transactions |
| :--- | :--- | :--- |
| **Credit Card** | 74,975 | 75.39% |
| **Boleto** | 19,784 | 19.89% |
| **Voucher** | 3,151 | 3.17% |
| **Debit Card** | 1,527 | 1.54% |
| **Not Defined** | 3 | 0.00% |
| **Total** | **99,440** | **100.00%** |

```
Payment Breakdown:
- Credit Card: [====================================] 75.39%
- Boleto:      [==========] 19.89%
- Voucher:     [=] 3.17%
- Debit Card:  [=] 1.54%
```

### Analysis
* Credit card is the dominant payment instrument (75.39%), followed by boleto (19.89%).
* The overall average installment count of **2.93** across transactions indicates that customers frequently leverage financing options for their purchases.

---

## 6. Customer Review Analysis

### Overall Satisfaction Profile
* **Average Review Rating:** 4.09 out of 5.00
* **Total Reviews:** 98,673

| Rating Score | Review Count | Percentage |
| :--- | :--- | :--- |
| **5 Stars** | 57,008 | 57.77% |
| **4 Stars** | 19,038 | 19.29% |
| **3 Stars** | 8,133 | 8.24% |
| **2 Stars** | 3,131 | 3.17% |
| **1 Star** | 11,363 | 11.52% |

* **Positive Sentiment (4-5 Stars):** 77.07% (76,046 reviews)
* **Negative Sentiment (1-2 Stars):** 14.69% (14,494 reviews)

### Ratings by Category

#### Best Rated Categories (Highest Mean Score)
1. **cds_dvds_musicals:** 4.64
2. **fashion_childrens_clothes:** 4.50
3. **books_general_interest:** 4.45
4. **costruction_tools_tools:** 4.44
5. **flowers:** 4.42

#### Worst Rated Categories (Lowest Mean Score)
1. **security_and_services:** 2.50
2. **Unknown:** 3.16
3. **diapers_and_hygiene:** 3.26
4. **office_furniture:** 3.49
5. **home_comfort_2:** 3.63

---

## 7. Geographic Insights

### Market Breakdown by State

| State | Revenue (R$) | Orders | Customers | Revenue Share |
| :--- | :--- | :--- | :--- | :--- |
| **SP** (São Paulo) | R$ 5,921,678.12 | 41,746 | 40,302 | 37.37% |
| **RJ** (Rio de Janeiro) | R$ 2,129,681.98 | 12,852 | 12,384 | 13.44% |
| **MG** (Minas Gerais) | R$ 1,856,161.49 | 11,635 | 11,259 | 11.72% |
| **RS** (Rio Grande do Sul) | R$ 885,826.76 | 5,466 | 5,277 | 5.59% |
| **PR** (Paraná) | R$ 800,935.44 | 5,045 | 4,882 | 5.05% |
| **BA** (Bahia) | R$ 611,506.67 | 3,380 | 3,277 | 3.86% |
| **SC** (Santa Catarina) | R$ 610,213.60 | 3,637 | 3,534 | 3.85% |
| **DF** (Distrito Federal) | R$ 353,229.44 | 2,140 | 2,075 | 2.23% |
| **GO** (Goiás) | R$ 347,706.93 | 2,020 | 1,952 | 2.19% |
| **ES** (Espírito Santo) | R$ 324,801.91 | 2,033 | 1,964 | 2.05% |

```
Regional Concentration (Top 3 States vs. Rest of Country):
- SP, RJ, MG: [====================================] 62.53%
- Other 24 States: [====================] 37.47%
```

### Seller Concentration
* **Top Seller Revenue:** R$ 249,640.70 (`seller_id: 4869f7a5dfa277a7dca6462dcf3b52b2`, SP).
* **Geographic Origin of Top Sellers:** **9 out of the top 10** revenue-generating sellers are located in São Paulo (**SP**), with 1 located in Bahia (**BA**).

---

## 8. Operational Insights

### Order Fulfillment Status
Out of **99,441 total orders**:

| Order Status | Count | Percentage of Total |
| :--- | :--- | :--- |
| **Delivered** | 96,478 | 97.02% |
| **Shipped** | 1,107 | 1.11% |
| **Canceled** | 625 | 0.63% |
| **Unavailable** | 609 | 0.61% |
| **Invoiced** | 314 | 0.32% |
| **Processing** | 301 | 0.30% |
| **Created** | 5 | 0.01% |
| **Approved** | 2 | 0.00% |

### Logistics & Fulfillment Performance Metrics
* **Average Delivery Time:** 12.5 days.
* **Delayed Orders:** 6,535 orders.
* **Delayed Order Rate:** **6.57%** measured against total orders (99,441).
* **Fulfillment Failure Total:** 1,234 orders were either `canceled` (625) or `unavailable` (609), representing 1.24% of all orders placed.

---

## 9. Business Risks

1. **Severe Retention Deficit (Single-Purchase Risk):**
   * *Observation:* Repeat purchase rate is 3.12% (1.03 orders/customer).
   * *Risk:* Top-line revenue depends almost entirely on continuous customer acquisition. If acquisition costs increase, revenue stability is directly threatened.

2. **Supply Base & Geographic Concentration Risk:**
   * *Observation:* SP generates 37.37% of revenue and houses 90% of top-performing sellers.
   * *Risk:* Supply chain disruptions or local regulatory/tax shifts in SP present disproportionate risks to platform revenue.

3. **Logistics Performance & Fulfillment Failures:**
   * *Observation:* 6.57% of total orders (6,535 orders) experienced delivery delays, and 1,234 orders ended in cancellation or unavailability.
   * *Risk:* Delivery delays and inventory shortages may be related to negative review scores (14.69% 1- and 2-star reviews), though current KPIs do not explicitly confirm direct causality.

4. **Product Line Dissatisfaction:**
   * *Observation:* Specific categories exhibit low customer satisfaction scores, including `security_and_services` (2.50), `diapers_and_hygiene` (3.26), and `office_furniture` (3.49).
   * *Risk:* Poor category ratings risk brand reputation and increase operational overhead from customer support and returns.

5. **Data Quality & Catalog Management Deficit:**
   * *Observation:* The "Unknown" category generated R$ 213,662.90 in revenue and received a low average review rating of 3.16. 
   * *Risk:* Unmapped SKUs hinder category management, inventory forecasting, and targeted marketing efforts.

---

## 10. Growth Opportunities

1. **Customer Base Monetization & Re-engagement:**
   * *Opportunity:* 93,099 single-time buyers represent a primary re-engagement pool. Converting even a fraction of these single-purchase customers into repeat buyers would scale revenue without additional acquisition costs.

2. **High-Value Category Expansion:**
   * *Opportunity:* Categories like `watches_gifts` yield **R$ 217.92** per unit sold compared to `bed_bath_table` at **R$ 111.71**. Expanding the catalog of higher unit-value categories can increase total AOV above R$ 160.58.

3. **Geographic Diversification Outside SP:**
   * *Opportunity:* Major population hubs like RJ (R$ 2.13M revenue) and MG (R$ 1.86M revenue) generate significant demand but rely predominantly on SP-based sellers. Onboarding sellers local to RJ, MG, and RS could optimize regional fulfillment.

4. **Category Quality Standardization:**
   * *Opportunity:* Upgrading seller quality standards in underperforming categories (`office_furniture`, `diapers_and_hygiene`) can improve product reviews closer to top-tier categories like `cds_dvds_musicals` (4.64) and `books_general_interest` (4.45).

---

## 11. Strategic Recommendations

### Section A: Immediate Operational Actions (0–30 Days)
* **Resolve Uncategorized SKUs:** Audit and reclassify products sitting under the "Unknown" category (R$ 213,662.90 revenue) to establish accurate performance tracking.
* **Review Underperforming Categories:** Audit seller listings in categories with average reviews below 3.50 (`security_and_services`, `diapers_and_hygiene`, `office_furniture`) to address product quality issues.

### Section B: Medium-Term Revenue Optimization (30–90 Days)
* **Deploy Repeat-Purchase Programs:** Establish cross-selling incentives tailored to single-purchase customers (focusing on high-volume categories like `bed_bath_table` and high-margin categories like `health_beauty`).
* **Address Delayed Orders:** Focus fulfillment optimization efforts on reducing the **6.57% delay rate** (6,535 orders) and minimizing the **1,234 canceled/unavailable orders**.

### Section C: Long-Term Growth & Expansion (>90 Days)
* **Regional Seller Recruitment:** Recruit high-volume sellers in secondary key states (RJ, MG, RS, PR) to reduce geographic reliance on SP sellers (who currently comprise 9 of the top 10 sellers).
* **Payment Strategy Alignment:** Optimize credit card installment offerings for high-ticket items, supporting purchases above the average order value of R$ 160.58.

---

### Key Performance Summary Table

| Metric Category | Key Indicator | Data Value |
| :--- | :--- | :--- |
| **Financials** | Total Revenue | R$ 15,843,553.24 |
| | Average Order Value (AOV) | R$ 160.58 |
| | Average Product Price | R$ 120.65 |
| **Customers** | Total Customers | 96,096 |
| | Repeat Purchase Rate | 3.12% (2,997 customers) |
| | Orders Per Customer | 1.03 |
| **Operations** | Total Orders | 99,441 |
| | Average Delivery Time | 12.5 Days |
| | Delayed Order Rate | 6.57% (6,535 orders) |
| **Quality** | Average Review Rating | 4.09 / 5.00 |
| | 5-Star Rating Share | 57.77% (57,008 reviews) |
| **Geography** | Top State Revenue Share (SP) | 37.37% (R$ 5,921,678.12) |
| | Top 3 States Revenue Share | 62.53% (SP, RJ, MG) |