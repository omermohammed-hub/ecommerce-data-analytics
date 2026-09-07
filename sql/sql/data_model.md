# E-Commerce Data Model

## 1. Purpose

This document defines the logical data model for the Perfect2Trade
E-Commerce Data Analytics project.

The model represents two main business processes:

1. Procurement and supply chain
2. Customer sales and fulfilment

The model uses primary keys (PK) and foreign keys (FK) to maintain
referential integrity between the tables.

---

# 2. Tables

## 2.1 Customers

**Purpose:** Stores customer master information.

**Primary Key:**
- customer_id

**Key attributes:**
- customer_type
- first_name
- last_name
- email
- postcode_area
- city
- region
- signup_date

---

## 2.2 Suppliers

**Purpose:** Stores supplier master information.

**Primary Key:**
- supplier_id

**Key attributes:**
- supplier_name
- supplier_country
- supplier_region
- standard_lead_time_days
- payment_terms_days
- supplier_status

---

## 2.3 Products

**Purpose:** Stores the product catalogue and supplier information.

**Primary Key:**
- product_id

**Foreign Key:**
- supplier_id → suppliers.supplier_id

**Key attributes:**
- product_name
- category
- subcategory
- brand
- sourcing_country
- cost_price
- selling_price
- reorder_level
- active_flag

---

## 2.4 Purchase Orders

**Purpose:** Records products purchased from suppliers.

**Primary Key:**
- purchase_order_id

**Foreign Keys:**
- supplier_id → suppliers.supplier_id
- product_id → products.product_id

---

## 2.5 Shipments

**Purpose:** Records shipments associated with purchase orders.

**Primary Key:**
- shipment_id

**Foreign Key:**
- purchase_order_id → purchase_orders.purchase_order_id

---

## 2.6 Orders

**Purpose:** Records customer sales orders.

**Primary Key:**
- order_id

**Foreign Key:**
- customer_id → customers.customer_id

---

## 2.7 Order Items

**Purpose:** Stores individual products contained within customer orders.

**Primary Key:**
- order_item_id

**Foreign Keys:**
- order_id → orders.order_id
- product_id → products.product_id

Order Items acts as the transaction-level detail table between
Orders and Products.

---

## 2.8 Payments

**Purpose:** Records payment information associated with customer orders.

**Primary Key:**
- payment_id

**Foreign Key:**
- order_id → orders.order_id

---

## 2.9 Returns

**Purpose:** Records products returned by customers.

**Primary Key:**
- return_id

**Foreign Keys:**
- order_id → orders.order_id
- product_id → products.product_id

A return must relate to a product that was actually included in
the original order.

---

## 2.10 Inventory

**Purpose:** Records inventory movement and stock levels over time.

**Primary Key:**
- inventory_id

**Foreign Key:**
- product_id → products.product_id

Inventory records include opening stock, received units, sold units,
returned units and closing stock.

---

# 3. Relationship Model

## Procurement / Supply Chain

Suppliers provide products.

SUPPLIERS 1 ───────────< PRODUCTS

Suppliers can have many purchase orders.

SUPPLIERS 1 ───────────< PURCHASE_ORDERS

Products can appear in many purchase orders.

PRODUCTS 1 ───────────< PURCHASE_ORDERS

Purchase orders can have associated shipments.

PURCHASE_ORDERS 1 ────< SHIPMENTS


## Customer Sales

Customers can place multiple orders.

CUSTOMERS 1 ──────────< ORDERS

Orders contain one or more order items.

ORDERS 1 ──────────────< ORDER_ITEMS

Products can appear in many order items.

PRODUCTS 1 ────────────< ORDER_ITEMS


## Payments

Orders can have associated payments.

ORDERS 1 ──────────────< PAYMENTS


## Returns

Orders can have associated returns.

ORDERS 1 ──────────────< RETURNS

Products can appear in many returns.

PRODUCTS 1 ────────────< RETURNS


## Inventory

Products can have multiple inventory records over time.

PRODUCTS 1 ────────────< INVENTORY


# 4. High-Level Business Flow

## Procurement

SUPPLIERS
    ↓
PRODUCTS
    ↓
PURCHASE_ORDERS
    ↓
SHIPMENTS
    ↓
INVENTORY


## Sales

CUSTOMERS
    ↓
ORDERS
    ↓
ORDER_ITEMS
    ↓
PRODUCTS


## Supporting Processes

ORDERS → PAYMENTS

ORDERS → RETURNS

PRODUCTS → INVENTORY


# 5. Primary Key / Foreign Key Summary

| Table | Primary Key | Foreign Keys |
|---|---|---|
| Customers | customer_id | — |
| Suppliers | supplier_id | — |
| Products | product_id | supplier_id |
| Purchase Orders | purchase_order_id | supplier_id, product_id |
| Shipments | shipment_id | purchase_order_id |
| Orders | order_id | customer_id |
| Order Items | order_item_id | order_id, product_id |
| Payments | payment_id | order_id |
| Returns | return_id | order_id, product_id |
| Inventory | inventory_id | product_id |

# 6. Data Integrity Rules

The following rules must be maintained when the model is implemented
in the database:

1. Every customer must have a unique customer_id.
2. Every supplier must have a unique supplier_id.
3. Every product must have a unique product_id.
4. Every order must reference an existing customer.
5. Every order item must reference an existing order.
6. Every order item must reference an existing product.
7. Every payment must reference an existing order.
8. Every return must reference an existing order.
9. Every return must reference an existing product.
10. The returned product must have existed in the original order.
11. Every inventory record must reference an existing product.
12. Every shipment must reference an existing purchase order.
13. Purchase orders must reference valid suppliers and products.