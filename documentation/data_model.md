# E-Commerce Data Model

## 1. Purpose

This document defines the logical data model for the OmerTrade Retail Analytics E-Commerce Data Analytics project.

The model represents two main business processes:

1. Procurement and supply chain
2. Customer sales and fulfilment

The model uses primary keys (PK) and foreign keys (FK) to define relationships and support data integrity across the datasets.

The relational model was implemented for analysis using Power Query and Power BI. The model supports data preparation, relationship management, DAX calculations and business analysis.

---

## 2. Tables

### 2.1 Customers

**Purpose:** Stores customer master information.

**Primary Key:** customer_id

**Key attributes:** customer_type, first_name, last_name, email, postcode_area, city, region, signup_date

---

### 2.2 Suppliers

**Purpose:** Stores supplier master information.

**Primary Key:** supplier_id

**Key attributes:** supplier_name, supplier_country, supplier_region, standard_lead_time_days, payment_terms_days, supplier_status

---

### 2.3 Products

**Purpose:** Stores the product catalogue and supplier information.

**Primary Key:** product_id

**Foreign Key:** supplier_id → suppliers.supplier_id

**Key attributes:** product_name, category, subcategory, brand, sourcing_country, cost_price, selling_price, reorder_level, active_flag

---

### 2.4 Purchase Orders

**Purpose:** Records products purchased from suppliers.

**Primary Key:** purchase_order_id

**Foreign Keys:**
- supplier_id → suppliers.supplier_id
- product_id → products.product_id

---

### 2.5 Shipments

**Purpose:** Records shipments associated with purchase orders.

**Primary Key:** shipment_id

**Foreign Key:** purchase_order_id → purchase_orders.purchase_order_id

---

### 2.6 Orders

**Purpose:** Records customer sales orders.

**Primary Key:** order_id

**Foreign Key:** customer_id → customers.customer_id

---

### 2.7 Order Items

**Purpose:** Stores individual products contained within customer orders.

**Primary Key:** order_item_id

**Foreign Keys:**
- order_id → orders.order_id
- product_id → products.product_id

Order Items acts as the transaction-level detail table between Orders and Products.

---

### 2.8 Payments

**Purpose:** Records payment information associated with customer orders.

**Primary Key:** payment_id

**Foreign Key:** order_id → orders.order_id

---

### 2.9 Returns

**Purpose:** Records products returned by customers.

**Primary Key:** return_id

**Foreign Keys:**
- order_id → orders.order_id
- product_id → products.product_id

Returns are associated with customer orders and the products included in those orders.

---

### 2.10 Inventory

**Purpose:** Records inventory movement and stock levels over time.

**Primary Key:** inventory_id

**Foreign Key:** product_id → products.product_id

Inventory records include opening stock, received units, sold units, returned units and closing stock.

---

## 3. Relationship Model

### Procurement / Supply Chain

Suppliers provide products.

```text
SUPPLIERS 1 ───────────< PRODUCTS
```

Suppliers can have many purchase orders.

```text
SUPPLIERS 1 ───────────< PURCHASE_ORDERS
```

Products can appear in many purchase orders.

```text
PRODUCTS 1 ───────────< PURCHASE_ORDERS
```

Purchase orders can have associated shipments.

```text
PURCHASE_ORDERS 1 ────< SHIPMENTS
```

Products can have multiple inventory records over time.

```text
PRODUCTS 1 ───────────< INVENTORY
```

### Customer Sales

Customers can place multiple orders.

```text
CUSTOMERS 1 ──────────< ORDERS
```

Orders contain one or more order items.

```text
ORDERS 1 ──────────────< ORDER_ITEMS
```

Products can appear in many order items.

```text
PRODUCTS 1 ────────────< ORDER_ITEMS
```

### Payments

Orders can have associated payments.

```text
ORDERS 1 ──────────────< PAYMENTS
```

### Returns

Orders can have associated returns.

```text
ORDERS 1 ──────────────< RETURNS
```

Products can appear in many returns.

```text
PRODUCTS 1 ────────────< RETURNS
```

---

## 4. High-Level Business Flow

**Procurement**

```text
SUPPLIERS
    │
    ├──────────→ PRODUCTS
    │               │
    ↓               ↓
PURCHASE_ORDERS   INVENTORY
    │
    ↓
SHIPMENTS
```

**Sales**

```text
CUSTOMERS
    ↓
ORDERS
    ↓
ORDER_ITEMS
    ↓
PRODUCTS
```

**Supporting Processes**

```text
ORDERS → PAYMENTS
ORDERS → RETURNS
PRODUCTS → INVENTORY
```

---

## 5. Primary Key / Foreign Key Summary

| Table | Primary Key | Foreign Key(s) |
|---|---|---|
| Customers | customer_id | — |
| Suppliers | supplier_id | — |
| Products | product_id | supplier_id → Suppliers |
| Purchase Orders | purchase_order_id | supplier_id → Suppliers; product_id → Products |
| Shipments | shipment_id | purchase_order_id → Purchase Orders |
| Orders | order_id | customer_id → Customers |
| Order Items | order_item_id | order_id → Orders; product_id → Products |
| Payments | payment_id | order_id → Orders |
| Returns | return_id | order_id → Orders; product_id → Products |
| Inventory | inventory_id | product_id → Products |

---

## 6. Power BI Analytical Layer

In addition to the core business tables above, the Power BI model includes supporting analytical components:

- **DimDate** — dedicated date dimension used for time-based analysis and time-intelligence calculations.
- **Measures** — dedicated table used to organise DAX measures.

The DimDate table provides the date structure used for reporting, including year, month and other date attributes. The Measures table provides a central location for the project's DAX measures, including revenue, cost, gross profit, gross margin, year-over-year analysis and operational metrics.

---

## 7. Data Integrity Rules

The following data integrity rules were considered when designing and validating the project data model:

- Every customer must have a unique customer_id.
- Every supplier must have a unique supplier_id.
- Every product must have a unique product_id.
- Every order must reference an existing customer.
- Every order item must reference an existing order.
- Every order item must reference an existing product.
- Every payment must reference an existing order.
- Every return must reference an existing order.
- Every return must reference an existing product.
- The returned product should correspond to a product included in the original order.
- Every inventory record must reference an existing product.
- Every shipment must reference an existing purchase order.
- Purchase orders must reference valid suppliers and products.

These rules were supported through the project's Python validation, Power Query data preparation and Power BI relationship modelling processes.
