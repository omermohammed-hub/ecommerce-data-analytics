# 📊 OmerTrade Retail Analytics
### E-Commerce Data Analytics & Power BI Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-217346?style=flat)
![Power Query](https://img.shields.io/badge/Power%20Query-6E4C95?style=flat)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> **Note:** OmerTrade Retail Analytics is a fictional company created for this independent portfolio project. All data is synthetically generated and does not represent any real business, customer, sales, inventory, or financial data.

An end-to-end retail and e-commerce analytics case study — from raw operational data to a five-page interactive Power BI dashboard, built to demonstrate practical Data Analyst skills across data preparation, modelling, DAX, and business insight generation.

---
## 📑 Contents


- [Overview](#overview)
- [Dashboard Preview](#dashboard-preview)
- [Key Highlights](#key-highlights)
- [Tech Stack](#tech-stack)
- [Project Workflow](#project-workflow)
- [Data Model](#data-model)
- [Repository Structure](#repository-structure)
- [Documentation](#documentation)
- [Skills Demonstrated](#skills-demonstrated)

---

## 🧭 Overview

This project simulates a UK retail business trading across multiple product categories, serving both B2C and B2B customers. Raw operational data is transformed into a structured analytical model and used to build a Power BI dashboard supporting business performance analysis and decision-making.

**Business questions this project answers:**

| Area | Question |
|---|---|
| Revenue | How is revenue trending, and where is it under pressure? |
| Profitability | Which categories drive revenue vs. which drive margin? |
| Inventory | Which products are at risk of stocking out? |
| Suppliers | How reliable are suppliers on delivery lead times? |
| Returns | Where is refund exposure concentrated, and why? |

---

## 📈 Dashboard Preview

| Page Focus | Description |
|---|---|
| **01 · Executive Overview** | Revenue, orders, customers, units sold, gross profit, gross margin |
| **02 · Sales & Customer Analysis** | Customer type, sales channel, region, top products |
| **03 · Product & Inventory** | Category performance, stock levels, reorder risk |
| **04 · Procurement & Supplier Analysis** | Purchase orders, spend, supplier lead times, delays |
| **05 · Returns & Operations** | Return volume, reasons, refund value, return rate, category performance |

*See [`screenshots/`](screenshots/) for full-resolution page images.*

---

## 🔑 Key Highlights

- 💰 **£74.33M** total revenue, **£28.31M** gross profit (**38.1%** margin)
- 📉 Revenue softened through 2026 — **July down ~17%** year-on-year
- 🐾 **Pet Care**: highest revenue, weakest margin (34.8%)
- 🔌 **Electrical**: lowest category revenue, strongest margin (40.5%) — potential profitable-growth opportunity
- 📦 **223 products** below reorder level
- 🚚 **664 late shipments**, average delay **1.5 days**
- ↩️ **~6K returns** / **£2.01M** refunded, **2.68%** return rate

*Full findings and recommendations:* [`business_insights.md`](documentation/business_insights.md)

---

## 🛠 Tech Stack

`Python` · `Pandas` · `Power Query` · `Power BI` · `DAX` · `Git` · `GitHub` · `VS Code`

---

## 🔄 Project Workflow

```text
Raw Data
   ↓
Validation & Profiling
   ↓
Power Query ETL
   ↓
Power BI Data Model
   ↓
DAX Measures
   ↓
Interactive Dashboard
   ↓
Business Insights
   ↓
Recommendations
```

---

## 🗂 Data Model

Star-schema-style relational model.

- **Dimensions:** Customers · Products · Suppliers · DimDate
- **Facts:** Orders · Order Items · Payments · Inventory · Purchase Orders · Shipments · Returns
- **Measures table** organises all DAX calculations separately from source data

Full entity relationships and PK/FK reference: [`data_model.md`](documentation/data_model.md)

---

## 📁 Repository Structure

```text
ecommerce-data-analytics/
│
├── data/
│   ├── profiling/
│   └── raw/
│
├── documentation/
│   ├── business_insights.md
│   ├── data_model.md
│   └── project_documentation.md
│
├── python/
├── screenshots/
├── .gitignore
└── README.md
```

---

## 📚 Documentation

| Document | Contents |
|---|---|
| [`project_documentation.md`](documentation/project_documentation.md) | Full methodology, ETL approach, DAX measures, dashboard breakdown |
| [`business_insights.md`](documentation/business_insights.md) | Detailed findings, evidence, business implications, recommendations |
| [`data_model.md`](documentation/data_model.md) | Table definitions, relationships, PK/FK reference |

---

## 🧠 Skills Demonstrated

Data cleaning & validation · Power Query ETL · relational data modelling · DAX & time intelligence · Power BI dashboard development · profitability & inventory analysis · supplier performance analysis · returns analysis · business insight generation · Git/GitHub version control

---

## ⚠️ Analytical Limitations

Findings identify patterns and areas for investigation, not proven causes — e.g. the July revenue decline, supplier delays, and return reasons all warrant deeper analysis before real commercial decisions would be made on them.
