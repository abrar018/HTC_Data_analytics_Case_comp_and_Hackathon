# Keyera WCSB Data Dashboard - Case Competition

## 📌 Overview  
This repository contains cleaned and processed datasets used for the **HTC Data Analytics Case Competition**, sponsored by **Keyera Corp. & AWS**. The competition focuses on optimizing **gas infrastructure operations** by leveraging **data analytics and AWS QuickSight** to develop a dynamic **WCSB Gas Plant Dashboard**.

## 🏆 Case Competition Context  
The **Western Canadian Sedimentary Basin (WCSB)** is home to **600+ active gas plants**, generating vast amounts of operational data. Keyera’s **Business Development Team** relies on this data to **identify growth opportunities, optimize assets, and drive sustainability**. However, the **manual process** of extracting and analyzing this data is inefficient.  

### **Objective**  
The goal of this project is to develop a **data-driven dashboard** that:  
✔ **Geospatially visualizes gas plants** across the WCSB  
✔ Allows **targeted search & filtering** (by company, plant code, location, etc.)  
✔ Displays **critical gas plant metrics** (capacity, utilization, throughput, liquid yields)  
✔ **Integrates emissions data** to evaluate environmental impact  

---

## 📊 Cleaned Data & Processing  
To ensure accurate and actionable insights, **data cleaning & integration** was a crucial step.  

### **🔹 Data Sources Provided**  
- **Gas Facilities Dataset** – Contains general information on WCSB gas plants  
- **Greenhouse Gas Reporting Program Dataset** – Lists facilities that report emissions  
- **Additional Public Data Sources** – Used for validation and enrichment  

### **🔹 Data Cleaning & Processing**  
✔ **Standardized formats** (column naming, data types, missing values handling)  
✔ **Merged datasets** using **latitude & longitude** to link emissions data to Keyera-affiliated plants  
✔ **Removed duplicates** and corrected inconsistencies  
✔ **Created calculated fields** for enhanced analysis  

### **🔹 Key Metrics Extracted**  
- **Gas throughput & utilization rates**  
- **Liquid yields (ethane, propane, butane, condensate)**  
- **Total emissions per plant**  
- **Emissions intensity (per unit of gas processed)**  

---

## 🌍 Greenhouse Gas Emissions Dashboard  
A key component of this project is the **GHG Emissions Dashboard**, which integrates emissions data to support **Keyera’s sustainability initiatives**.  

### **🔹 Features & Insights**  
✔ **Geospatial Mapping:** Identifies high-emission facilities and regional patterns  
✔ **Key Performance Indicators (KPIs):** Displays total CO₂ emissions, CH₄ leakage, and overall emissions intensity  
✔ **Flaring & Methane Leakage Analysis:** Highlights facilities with inefficiencies in gas combustion and pipeline integrity  
✔ **Emissions Breakdown by Facility:** Categorizes CO₂, CH₄, and other emissions to identify reduction opportunities  

### **🔹 Impact on Decision-Making**  
🚀 **Regulatory Compliance:** Supports environmental reporting requirements  
🚀 **Operational Efficiency:** Identifies areas where gas losses can be minimized  
🚀 **Sustainability Strategy:** Helps prioritize investments in emissions reduction technologies  

By using **data visualization and analytics**, Keyera can **proactively manage environmental impact while improving overall business efficiency**.  

---

## 🚀 Project Impact  
By integrating **cleaned and structured data** into the **AWS QuickSight dashboard**, this project enhances **Keyera’s ability to make data-driven decisions**. The dashboard provides **real-time insights** to optimize operations, improve sustainability efforts, and maximize efficiency.  

🔹 **Time Savings:** Eliminates manual data extraction  
🔹 **Improved Accuracy:** Reliable, structured dataset for decision-making  
🔹 **Sustainability Insights:** Helps track emissions and optimize processes  
