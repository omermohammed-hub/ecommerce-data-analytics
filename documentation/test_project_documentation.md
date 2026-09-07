# Perfect2Trade E-Commerce Data Analytics Project

## 1. Project Overview

Perfect2Trade is an end-to-end e-commerce data analytics project designed to demonstrate how business data can be transformed into actionable insights using Python, Power Query, Power BI, and DAX.

The project analyses sales, customers, products, inventory, suppliers, procurement, payments, shipments, and returns across an interconnected e-commerce dataset.

The final solution combines data preparation, data modelling, analytical calculations, and interactive Power BI dashboards to evaluate business performance and identify opportunities and operational risks.

---

## 2. Business Problem

An e-commerce business generates data across multiple operational areas, but individual datasets do not provide management with a single view of overall performance.

The business needs to understand:

- How much revenue is being generated?
- How profitable are sales?
- How is revenue changing over time?
- Which product categories perform best?
- Which categories generate strong revenue but weaker margins?
- Are inventory levels creating potential stock-out risks?
- How reliable are suppliers and deliveries?
- What is the scale and nature of customer returns?
- Where are the main opportunities for profitable growth?

The objective of this project was to consolidate these areas into a single analytical solution that enables management to monitor performance and make evidence-based decisions.

---

## 3. Project Objectives

The project objectives were to:

1. Analyse overall e-commerce revenue and profitability.
2. Identify revenue trends and year-on-year performance.
3. Compare product-category performance and gross margins.
4. Analyse customer and sales-channel performance.
5. Identify products approaching insufficient inventory levels.
6. Evaluate supplier purchasing and delivery performance.
7. Analyse customer returns and refund activity.
8. Develop an interactive Power BI dashboard for business users.
9. Translate analytical findings into practical business recommendations.

---

## 4. Data Sources & Dataset

The project uses a synthetic e-commerce dataset designed to represent a realistic multi-table business environment.

The dataset contains ten core business tables:

| Table | Purpose |
|---|---|
| Customers | Customer information and customer segmentation |
| Products | Product details, categories, prices, and reorder levels |
| Suppliers | Supplier information and locations |
| Orders | Customer order-level information |
| Order_items | Individual products and quantities within orders |
| Payments | Payment transactions and payment status |
| Inventory | Product stock and inventory movements |
| Purchase_Orders | Supplier purchase orders and procurement information |
| Shipments | Shipment and delivery information |
| Returns | Customer return and refund information |

A data dictionary was also created to document the fields and structure of the datasets.

---

## 5. Data Preparation & ETL

The data preparation process was designed to ensure that the datasets were suitable for analysis before being loaded into Power BI.

### Python

Python was used during the data preparation and validation stage to:

- Generate the synthetic datasets.
- Inspect the data model.
- Create a data dictionary.
- Validate individual datasets.
- Check data quality and consistency.
- Perform additional inventory validation, including month-by-month checks.

Validation scripts were created for the main business tables to identify potential issues before analysis.

### Power Query

Power Query was used within Power BI for the main ETL process.

The transformation workflow included:

- Loading the source datasets.
- Reviewing column structures.
- Setting appropriate data types.
- Checking for missing or invalid values.
- Reviewing data quality.
- Preparing fields for analysis.
- Ensuring consistent structures across related tables.

The objective was to keep the transformation process reproducible and separate from the analytical calculations performed using DAX.

---

## 6. Data Model

The Power BI solution uses a relational model containing the ten business tables together with a dedicated date table and measures table.

The model follows a star-schema-style approach where appropriate, separating descriptive dimensions from transactional fact tables.

### Dimension Tables

- Customers
- Products
- Suppliers
- DimDate

### Fact Tables

- Orders
- Order_items
- Payments
- Inventory
- Purchase_Orders
- Returns
- Shipments

A dedicated **Measures** table was also created to organise DAX measures separately from the source data tables.

### Relationships

Relationships were established between the relevant business entities to allow filters and calculations to flow correctly through the model.

A dedicated `DimDate` table was created and marked as the model's date table.

Date relationships were configured carefully, including inactive relationships where necessary to avoid ambiguous filter paths.

---

## 7. DAX & Analytical Measures

DAX was used to create reusable business measures rather than relying only on raw columns.

### Total COGS

Cost of goods sold was calculated by multiplying the quantity sold by the related product cost price.

```DAX
Total COGS =
SUMX(
    Order_items,
    Order_items[quantity] * RELATED(Products[cost_price])
)
### Gross Profit

```dax
Gross Profit =
[Total Revenue] - [Total COGS]
```

### Gross Margin %

```dax
Gross Margin % =
DIVIDE(
    [Gross Profit],
    [Total Revenue]
)
```

### Revenue Previous Year

```dax
Revenue Previous Year =
CALCULATE(
    [Total Revenue],
    DATEADD(DimDate[Date], -1, YEAR)
)
```

### Revenue YoY %

```dax
Revenue YoY % =
IF(
    ISINSCOPE(DimDate[Year Month]),
    DIVIDE(
        [Total Revenue] - [Revenue Previous Year],
        [Revenue Previous Year]
    )
)
```

### Products Below Reorder Level

```dax
Products Below Reorder Level =
SUMX(
    VALUES(Products[product_id]),
    VAR CurrentStock = [Ending Stock]
    VAR ReorderLevel = MAX(Products[reorder_level])
    RETURN
        IF(CurrentStock < ReorderLevel, 1, 0)
)
```

### Delivery Delay Days

A calculated column was created to measure the difference between estimated and actual shipment arrival dates.

```dax
Delivery Delay Days =
DATEDIFF(
    Shipments[estimated_arrival_date],
    Shipments[actual_arrival_date],
    DAY
)
```

Additional measures were created for average delivery delay, late shipments, late shipment percentage, returns, refunds, return rate, and other dashboard KPIs.

---

## 8. Power BI Dashboard

The final Power BI solution contains five analytical pages.

### Page 1 — E-Commerce Overview

Provides an executive-level view of:

- Total revenue
- Orders
- Customers
- Average order value
- Discounts
- Units sold
- Revenue trends
- Revenue by category
- Revenue by sales channel
- Revenue by region

This page is designed to provide a quick overview of overall business performance.

### Page 2 — Sales & Customer Analysis

Focuses on customer and sales performance.

Key analysis includes:

- Revenue by customer type
- Revenue by sales channel
- Revenue trends
- Revenue by region
- Revenue by product category
- Top products by revenue

This page allows users to investigate where sales are being generated and which customer and product segments contribute to revenue.

### Page 3 — Product & Inventory

Focuses on product performance and stock levels.

Key analysis includes:

- Units sold by category
- Revenue by category
- Stock by category
- Product-level performance
- Inventory information

This page helps identify product categories with different sales and inventory characteristics and supports stock-level investigation.

### Page 4 — Procurement & Supplier Analysis

Focuses on supplier and purchasing activity.

Key analysis includes:

- Purchase orders
- Purchase quantity
- Purchase spend
- Supplier count
- Units sold
- Average lead time
- Procurement spend by supplier country

This page provides visibility into purchasing activity and supplier-related performance.

### Page 5 — Returns & Operations

Focuses on customer returns and operational performance.

Key analysis includes:

- Total returns
- Units returned
- Refund amount
- Return rate
- Average refund per return
- Returns by reason
- Returns by category
- Return trends
- Return status

This page helps identify areas where returns may require further investigation.

---

## 9. Key Business Insights

The analysis identified seven primary findings.

### Revenue Performance

Total revenue was £74.33M, but revenue performance weakened during 2026. July 2026 revenue was approximately 17% below July 2025.

This indicates that recent sales performance should be investigated before the decline becomes more significant.

### Category Profitability

- Pet Care generated approximately £13.30M in revenue but had the lowest category gross margin at 34.8%.
- Electrical generated approximately £10.82M in revenue but achieved the highest category gross margin at 40.5%.

This highlights the difference between revenue generation and profitability.

### Overall Profitability

The business generated:

| Metric | Value |
|---|---|
| Revenue | £74.33M |
| COGS | £46.01M |
| Gross Profit | £28.31M |
| Gross Margin | 38.1% |

The business therefore remains fundamentally profitable despite recent revenue weakness.

### Inventory Risk

223 products were below their defined reorder levels.

This creates a potential stock-out risk and highlights the need for targeted replenishment and review of reorder thresholds.

### Supplier Performance

There were 664 late shipments, with an average delivery delay of 1.50 days.

Supplier performance should therefore be monitored to identify recurring delivery issues.

### Returns

The business recorded approximately:

- 6K returns
- 20K units returned
- £2.01M in refunds
- 2.68% return rate

Quality Issue was the most frequent recorded return reason, while Garden & Outdoor had the highest return volume.

### Profitable Growth Opportunity

Electrical has the highest category margin but the lowest category revenue.

This creates a potential opportunity to investigate whether additional sales can be generated while maintaining the category's relatively strong margin.

---

## 10. Business Recommendations

Based on the analysis, the main recommendations are:

1. **Investigate the 2026 Revenue Decline**
   Analyse the decline by category, region, customer type, sales channel, and individual products to identify where the reduction is concentrated.

2. **Review Pet Care Profitability**
   Investigate pricing, supplier costs, product mix, and discounting to identify opportunities to improve the category's margin.

3. **Prioritise Inventory Replenishment**
   Review the 223 products below reorder level and prioritise replenishment according to demand and sales velocity.

4. **Monitor Supplier Performance**
   Track late shipments and delivery delays by supplier and route to identify recurring operational issues.

5. **Investigate Return Drivers**
   Focus on quality-related returns and the Garden & Outdoor category to identify recurring products or operational issues.

6. **Evaluate Electrical for Profitable Growth**
   Assess opportunities to increase Electrical sales through targeted promotions, product expansion, and customer targeting while protecting margin.

7. **Focus on Profitable Growth**
   Revenue growth should be evaluated alongside gross margin so that increased sales do not come at the expense of profitability.

---

## 11. Analytical Limitations

The findings in this project identify patterns and areas for investigation. They do not automatically establish causation.

For example:

- The July revenue decline does not by itself identify its underlying cause.
- Supplier delays do not prove that stock-outs or customer dissatisfaction resulted from those delays.
- Return reasons represent recorded classifications and do not independently establish root cause.
- Category-level margins should be investigated at product and supplier level before major commercial decisions are made.

These limitations are considered when translating dashboard findings into business recommendations.

---

## 12. Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Dataset generation, inspection, and validation |
| Pandas | Data handling and validation |
| Power Query | ETL and data transformation |
| Power BI | Data modelling, visualisation, and dashboard development |
| DAX | Business measures and analytical calculations |
| Git | Version control |
| GitHub | Repository and portfolio documentation |
| Visual Studio Code | Development environment and project management |

---

## 13. Skills Demonstrated

This project demonstrates practical experience in:

- Data cleaning and preparation
- ETL using Power Query
- Relational data modelling
- Star-schema-style modelling
- Power BI dashboard development
- DAX measures
- Time-intelligence analysis
- KPI development
- Profitability analysis
- Inventory analysis
- Supplier and procurement analysis
- Returns analysis
- Data validation
- Business insight generation
- Data-driven recommendations
- Git and GitHub version control
- Technical documentation

---

## 14. Project Outcome

The final solution provides an integrated analytical view of an e-commerce business across sales, customers, products, inventory, procurement, suppliers, shipments, and returns.

The project demonstrates the complete analytical workflow:

**Business Problem → Data → ETL → Data Model → DAX → Dashboard → Insights → Recommendations**

Rather than focusing only on visualisation, the project demonstrates how analytical results can be translated into business questions, findings, and practical recommendations.

---

## 15. Conclusion

The Perfect2Trade project demonstrates how a Data Analyst can combine technical and analytical skills to transform multiple business datasets into a practical decision-support solution.

The analysis shows a profitable business with £74.33M in revenue and £28.31M in gross profit, while also highlighting areas requiring attention across revenue performance, category profitability, inventory, supplier delivery, and returns.

The overall recommendation is to pursue targeted profitable growth, protect existing margins, and improve operational control using data-driven monitoring.
## Git Practice Update

This section was added after the first version was pushed to GitHub.