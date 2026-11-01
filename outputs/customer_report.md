# Executive Report: Customer Behaviour & Strategic Insights

**Evaluation Period:** October 2016 – August 2018  
**Prepared For:** Executive Leadership Team  
**Focus Area:** Customer Analytics, Behaviour, Retention, and Growth Strategy  

---

## 1. Customer Overview

Analysis of the company’s customer dataset from the reliable reporting period of **October 2016 to August 2018** reveals a customer base of **96,096 total customers** generating **99,441 orders**.

### Geographic Distribution
Customer acquisition is heavily concentrated in the Southeastern region of Brazil. The top three states account for **66.5%** of the total customer base (63,945 customers).

| State | Customer Count | % of Total Base | Revenue Contribution (R$) |
| :--- | :--- | :--- | :--- |
| **São Paulo (SP)** | 40,302 | 41.9% | R$ 5,921,678.12 |
| **Rio de Janeiro (RJ)** | 12,384 | 12.9% | R$ 2,129,681.98 |
| **Minas Gerais (MG)** | 11,259 | 11.7% | R$ 1,856,161.49 |
| **Rio Grande do Sul (RS)** | 5,277 | 5.5% | R$ 885,826.76 |
| **Paraná (PR)** | 4,882 | 5.1% | R$ 800,935.44 |
| **Other States (22)** | 21,992 | 22.9% | R$ 4,249,270.45 |

Key regional markets outside the top three include Rio Grande do Sul (5,277 customers), Paraná (4,882 customers), Santa Catarina (3,534 customers), and Bahia (3,277 customers). The lowest customer concentrations are in Northern states such as Roraima (45 customers) and Amapá (67 customers).

---

## 2. Purchasing Behaviour

### Spending & Basket Size
* **Average Order Value (AOV):** R$ 160.58
* **Average Payment Value:** R$ 160.99
* **Average Product Price:** R$ 120.65

### Payment Preferences
Customer transactions are dominated by credit card usage, which accounts for the vast majority of payment transactions, followed by cash-equivalent methods (Boleto).

```
Credit Card : 74,975 transactions
Boleto      : 19,784 transactions
Voucher     :  3,151 transactions
Debit Card  :  1,527 transactions
Not Defined :      3 transactions
```

* **Financing Dynamics:** Customers use an average of **2.93 installments** per payment, indicating a clear reliance on structured payment options for purchasing decisions.

### Category Demand Patterns
Customer buying behaviour varies significantly across categories in terms of order volume versus overall spend:

* **Top Categories by Order Volume:** `bed_bath_table` (11,115 items), `health_beauty` (9,670 items), and `sports_leisure` (8,641 items).
* **Top Categories by Expenditure:** `health_beauty` (R$ 1,441,248.07), `watches_gifts` (R$ 1,305,541.61), and `bed_bath_table` (R$ 1,241,681.72).

---

## 3. Customer Retention Insights

The dataset highlights a severe structural challenge in customer repeat purchase rates.

```
Total Unique Customers : 96,096
Repeat Customers       :  2,997
Repeat Customer Rate   :  3.12%
Avg Orders / Customer  :   1.03
```

### Business Implications
* **Single-Transaction Dominance:** **96.88%** of customers purchased only once during the evaluated 23-month period.
* **Acquisition Efficiency:** The business operates almost entirely as a transactional acquisition engine rather than a subscriber or relationship-based model. Revenue expansion is currently dependent on acquiring new customers rather than extracting lifetime value (LTV) from existing ones.

---

## 4. Customer Risks

### 1. Retention Deficit
With an average of **1.03 orders per customer**, customer lifetime value is capped near the single-order baseline (AOV R$ 160.58). High reliance on continuous customer acquisition exposes the business to rising acquisition costs.

### 2. Negative Review Concentration
While the overall review score is positive (**4.09 out of 5.0** across 98,665 reviews), **14.7% of all reviews** fall into the 1-star or 2-star negative categories.

| Review Rating | Count | Share of Total |
| :--- | :--- | :--- |
| **5 Stars** | 57,008 | 57.8% |
| **4 Stars** | 19,038 | 19.3% |
| **3 Stars** | 8,133 | 8.2% |
| **2 Stars** | 3,131 | 3.2% |
| **1 Star** | 11,363 | 11.5% |

### 3. Category Quality Disconnects
Certain product categories exhibit low customer satisfaction scores, which risks damaging brand perception:

* `security_and_services`: 2.50 average rating
* `Unknown`: 3.16 average rating
* `diapers_and_hygiene`: 3.26 average rating
* `office_furniture`: 3.49 average rating

### 4. Fulfillment Experience Friction
* **Average Delivery Time:** 12.5 days.
* **Delayed Orders:** 6,535 orders out of total orders (99,441), representing a **6.57% delay rate across all orders**.
* *Note:* While the data does not explicitly link delivery delays directly to individual negative reviews, long delivery timelines and order delays **may be related** to customer dissatisfaction and lower review scores.

---

## 5. Customer Growth Opportunities

### 1. Re-Engagement in Consumable & High-Volume Categories
Categories such as `health_beauty` (9,670 orders; R$ 1.44M revenue) and `bed_bath_table` (11,115 orders; R$ 1.24M revenue) feature natural replenishment cycles or product expansion possibilities that are currently uncaptured, given the overall 3.12% repeat purchase rate.

### 2. Geographic Expansion Beyond the Core Southeast
While SP, RJ, and MG generate 66.5% of demand, secondary markets currently demonstrate established baseline demand without primary dominance:
* **Southern Hubs:** RS (5,277 customers), PR (4,882 customers), SC (3,534 customers).
* **Northeastern Hubs:** BA (3,277 customers), PE (1,609 customers).

Expanding market penetration in these secondary states represents an opportunistic growth avenue.

### 3. Payment Optimization Strategy
Given that credit cards represent **75.4%** of payment methods and customers average **2.93 installments**, tailoring promotion structures and financing incentives around multi-installment credit options directly aligns with demonstrated customer payment preferences.

---

## 6. Customer Recommendations

The following evidence-based strategies address identified risks and leverage growth opportunities:

### Executive Action Matrix

| Strategic Focus | Action Item | Expected Impact | Data Justification |
| :--- | :--- | :--- | :--- |
| **Retention Strategy** | Launch post-purchase retention workflows for high-volume categories (`health_beauty`, `bed_bath_table`). | Increase repeat purchase rate above 3.12% and elevate orders-per-customer from 1.03. | 96.88% of customers currently buy only once. |
| **Fulfillment Optimization** | Audit logistics operations to reduce the 12.5-day average delivery cycle, focusing on top customer regions (SP, RJ, MG). | Improve customer satisfaction and reduce exposure to 1-star reviews. | 6,535 delayed orders (6.57% of total) and 11,363 1-star reviews. |
| **Catalog Quality Control** | Audit or delist low-performing vendors/products in poorly rated categories (`diapers_and_hygiene`, `office_furniture`, `security_and_services`). | Eliminate drag on overall review rating (4.09). | Ratings in these categories range from 2.50 to 3.49. |
| **Checkout & Financing** | Optimize credit card checkout experience to support flexible installment plans up to 3–6 cycles. | Improve conversion rates by catering to established spending habits. | Credit card is the top payment method (74,975 uses) with an average of 2.93 installments. |