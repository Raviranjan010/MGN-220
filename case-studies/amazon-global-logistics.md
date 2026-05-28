# Case Study: Amazon Global Logistics

## 1. Background & Context
Amazon's vision is to be Earth's most customer-centric company. Central to this is **Amazon Global Logistics (AGL)**, which manages the physical movement of inventory across international borders, primarily from manufacturers in Asia to fulfillment centers in North America and Europe.

```mermaid
graph LR
    A[Chinese Supplier] -->|Origin Consolidation| B[Amazon Ocean/Air Freight]
    B -->|Customs Clearance| C[Port of Entry]
    C -->|Fulfillment Centers| D[End Customers]
```

## 2. Supply Chain Innovation & Sourcing
- **Direct Freight Forwarding**: Amazon acts as its own ocean freight forwarder (acting as a Non-Vessel Operating Common Carrier - NVOCC). This allows Amazon to book space directly on cargo ships, bypassing traditional third-party logistics (3PL) providers and lowering costs for third-party merchants (FBA - Fulfillment by Amazon).
- **Cross-Border Optimization**: Utilizing AI and machine learning to predict which products will be in demand in specific regional markets, pre-shipping them to nearby regional hubs before orders are even placed.

## 3. Exam-Oriented Analysis & Solved Questions

### Q1: Explain the role of Incoterms in Amazon's international shipping logistics. (5 Marks)
* **Topper's Answer**:
  - **Incoterms Definition**: Standardized international trade terms published by the ICC to define duties, costs, and risks between buyers and sellers.
  - **Amazon Application**: Most sellers shipping to Amazon fulfillment centers use **DDP (Delivered Duty Paid)** or **FCA (Free Carrier)**. Under DDP, the seller handles all transport, import clearance, and duties, ensuring Amazon receives the inventory with zero customs liability.
  - **Operational Advantage**: Utilizing clear Incoterms prevents cargo delays at customs ports, maintaining Amazon's strict inventory turnover metrics.

### Q2: Analyze how global logistics disruptions (e.g., Suez Canal blockages) impact digital marketplaces. (5 Marks)
* **Topper's Answer**:
  - **Inventory Shortages**: Out-of-stock situations leading to loss of search ranking and revenue for sellers.
  - **Increased Freight Rates**: Shipping container costs spike, forcing sellers to increase consumer prices, causing demand contraction.
  - **Mitigation Strategy**: Amazon implements a **multi-modal transportation strategy** (switching to air cargo or rail routes) and maintains safety stock in localized distribution centers.
