# OmerTrade Retail Analytics — Project Documentation

> **Disclaimer:** OmerTrade Retail Analytics is a fictional company created for this independent portfolio project. The dataset is synthetically generated and does not represent any real business, customer, sales, inventory, or financial data.

## 1. Project Overview

This is an end-to-end e-commerce data analytics project designed to demonstrate how business data can be transformed into actionable insights using Python, Power Query, Power BI, and DAX.

The project analyses sales, customers, products, inventory, suppliers, procurement, payments, shipments, and returns across an interconnected e-commerce dataset.

The final solution combines data preparation, data modelling, analytical calculations, and interactive Power BI dashboards to evaluate business performance and identify opportunities and operational risks.

## 2. Business Problem

An e-commerce business generates data across multiple operational areas, but individual datasets do not provide management with a single view of overall performance. The business needs to understand:

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

## 3. Project Objectives

- Analyse overall e-commerce revenue and profitability
- Identify revenue trends and year-on-year performance
- Compare product-category performance and gross margins
- Analyse customer and sales-channel performance
- Identify products approaching insufficient inventory levels
- Evaluate supplier purchasing and delivery performance
- Analyse customer returns and refund activity
- Develop an interactive Power BI dashboard for business users
- Translate analytical findings into practical business recommendations

## 4. Data Sources & Dataset

The dataset contains ten core business tables:

`Customers` · `Products` · `Suppliers` · `Orders` · `Order Items` · `Payments` · `Inventory` · `Purchase Orders` · `Shipments` · `Returns`

The dataset covers the period from **1 January 2025** to **25 July 2026**.

A data dictionary was also created to document the fields and structure of the datasets.

## 5. Data Preparation & ETL

### Python

Used during data preparation and validation to:

- Generate the synthetic datasets
- Inspect the data model
- Create a data dictionary
- Validate individual datasets
- Check data quality and consistency
- Perform additional inventory validation, including month-by-month checks

Validation scripts were created for the main business tables to identify potential issues before analysis.

### Power Query

Used within Power BI for the main ETL process:

- Loading source datasets
- Reviewing column structures
- Setting appropriate data types
- Checking for missing or invalid values
- Reviewing data quality
- Preparing fields for analysis
- Ensuring consistent structures across related tables

The objective was to keep the transformation process reproducible and separate from the analytical calculations performed using DAX.

## 6. Data Model

The Power BI solution uses a relational model containing the ten business tables together with a dedicated date table and measures table, following a star-schema-style approach where appropriate.

- **Dimension Tables:** Customers, Products, Suppliers, DimDate
- **Fact Tables:** Orders, Order_items, Payments, Inventory, Purchase_Orders, Returns, Shipments

A dedicated Measures table was created to organise DAX measures separately from the source data tables.

### Relationships

Relationships were established between relevant business entities to allow filters and calculations to flow correctly through the model. A dedicated DimDate table was created and marked as the model's date table. Date relationships were configured carefully, including inactive relationships where necessary to avoid ambiguous filter paths.

## 7. DAX & Analytical Measures

```dax
Total COGS =
SUMX(
    Order_items,
    Order_items[quantity] * RELATED(Products[cost_price])
)

Gross Profit =
[Total Revenue] - [Total COGS]

Gross Margin % =
DIVIDE(
    [Gross Profit],
    [Total Revenue]
)

Revenue Previous Year =
CALCULATE(
    [Total Revenue],
    DATEADD(DimDate[Date], -1, YEAR)
)

Revenue YoY % =
IF(
    ISINSCOPE(DimDate[Year Month]),
    DIVIDE(
        [Total Revenue] - [Revenue Previous Year],
        [Revenue Previous Year]
    )
)

Products Below Reorder Level =
SUMX(
    VALUES(Products[product_id]),
    VAR CurrentStock = [Ending Stock]
    VAR ReorderLevel = MAX(Products[reorder_level])
    RETURN
        IF(CurrentStock < ReorderLevel, 1, 0)
)

Delivery Delay Days =
DATEDIFF(
    Shipments[estimated_arrival_date],
    Shipments[actual_arrival_date],
    DAY
)
```

Additional measures were created for average delivery delay, late shipments, late shipment percentage, returns, refunds, return rate, and other dashboard KPIs.

## 8. Power BI Dashboard

Five analytical pages:

- **Page 1 — E-Commerce Overview:** total revenue, orders, customers, average order value, discounts, units sold, revenue trends, revenue by category/sales channel/region.
- **Page 2 — Sales & Customer Analysis:** revenue by customer type, sales channel, region, category; top products by revenue.
- **Page 3 — Product & Inventory:** units sold by category, revenue by category, stock by category, product-level performance, inventory information.
- **Page 4 — Procurement & Supplier Analysis:** purchase orders, purchase quantity, purchase spend, supplier count, units sold, average lead time, procurement spend by supplier country.
- **Page 5 — Returns & Operations:** total returns, units returned, refund amount, return rate, average refund per return, returns by reason/category, return trends, return status.

## 9. Key Business Insights

- **Revenue Performance:** Total revenue was £74.33M, but revenue performance weakened during 2026 — July 2026 revenue was approximately 17% below July 2025.
- **Category Profitability:** Pet Care generated ~£13.30M in revenue but had the lowest category gross margin at 34.8%. Electrical generated ~£10.82M but achieved the highest category gross margin at 40.5%.
- **Overall Profitability:** £28.31M gross profit from £74.33M revenue (38.1% gross margin) — the business remains fundamentally profitable despite recent revenue weakness.
- **Inventory Risk:** 223 products were below their defined reorder levels.
- **Supplier Performance:** 664 late shipments, average delivery delay of 1.50 days.
- **Returns:** ~6K returns, ~20K units returned, £2.01M in refunds, 2.68% return rate. Quality Issue was the most frequent reason; Garden & Outdoor had the highest return volume.
- **Profitable Growth Opportunity:** Electrical has the highest category margin but the lowest category revenue.

## 10. Business Recommendations

1. Investigate the 2026 revenue decline by category, region, customer type, sales channel, and product
2. Review Pet Care profitability (pricing, supplier costs, product mix, discounting)
3. Prioritise inventory replenishment for the 223 products below reorder level
4. Monitor supplier performance — track late shipments and delays by supplier/route
5. Investigate return drivers, focusing on quality-related returns and Garden & Outdoor
6. Evaluate Electrical for profitable growth through targeted promotion and expansion
7. Focus on profitable growth — evaluate revenue growth alongside gross margin

## 11. Analytical Limitations

The findings identify patterns and areas for investigation; they do not establish causation. For example, the July revenue decline does not by itself identify its cause, supplier delays do not prove stock-outs or dissatisfaction resulted, and return reasons are recorded classifications rather than confirmed root causes. Category-level margins should be investigated at product and supplier level before major commercial decisions are made.

## 12. Tools & Technologies

`Python` · `Pandas` · `Power Query` · `Power BI` · `DAX` · `Git` · `GitHub` · `Visual Studio Code`

## 13. Skills Demonstrated

Data cleaning and preparation, ETL using Power Query, relational data modelling, star-schema-style modelling, Power BI dashboard development, DAX measures, time-intelligence analysis, KPI development, profitability analysis, inventory analysis, supplier and procurement analysis, returns analysis, data validation, business insight generation, data-driven recommendations, Git and GitHub version control, technical documentation.

## 14. Project Outcome

The final solution provides an integrated analytical view of a retail e-commerce business across sales, customers, products, inventory, procurement, suppliers, shipments, and returns:

```text
Business Problem
      ↓
Data
      ↓
ETL & Validation
      ↓
Data Model
      ↓
DAX & Analysis
      ↓
Power BI Dashboard
      ↓
Business Insights
      ↓
Recommendations
```

## 15. Conclusion

This project demonstrates how a Data Analyst can combine technical and analytical skills to transform multiple business datasets into a practical decision-support solution. The analysis shows a profitable business with £74.33M in revenue and £28.31M in gross profit, while also highlighting areas requiring attention across revenue performance, category profitability, inventory, supplier delivery, and returns. The analysis supports a focus on targeted profitable growth, margin protection, and improved operational control through data-driven monitoring..
