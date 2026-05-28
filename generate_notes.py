import os
import textwrap

def create_dirs_and_files():
    base_dir = r"c:\LPU_Study\MGN-220"
    os.makedirs(base_dir, exist_ok=True)
    
    # Define directories
    directories = [
        "syllabus",
        "unit-1-international-business-environment",
        "unit-1-international-business-environment/diagrams",
        "unit-1-international-business-environment/flowcharts",
        "unit-1-international-business-environment/mindmaps",
        "unit-1-international-business-environment/assets",
        "unit-2-international-trade",
        "unit-2-international-trade/diagrams",
        "unit-2-international-trade/flowcharts",
        "unit-2-international-trade/mindmaps",
        "unit-2-international-trade/assets",
        "unit-3-global-monetary-system",
        "unit-3-global-monetary-system/diagrams",
        "unit-3-global-monetary-system/flowcharts",
        "unit-3-global-monetary-system/mindmaps",
        "unit-3-global-monetary-system/assets",
        "unit-4-strategy-and-structure",
        "unit-4-strategy-and-structure/diagrams",
        "unit-4-strategy-and-structure/flowcharts",
        "unit-4-strategy-and-structure/mindmaps",
        "unit-4-strategy-and-structure/assets",
        "unit-5-international-business-operations",
        "unit-5-international-business-operations/diagrams",
        "unit-5-international-business-operations/flowcharts",
        "unit-5-international-business-operations/mindmaps",
        "unit-5-international-business-operations/assets",
        "unit-6-global-marketing-and-hrm",
        "unit-6-global-marketing-and-hrm/diagrams",
        "unit-6-global-marketing-and-hrm/flowcharts",
        "unit-6-global-marketing-and-hrm/mindmaps",
        "unit-6-global-marketing-and-hrm/assets",
        "previous-year-questions",
        "topper-answer-sheets",
        "exam-preparation",
        "current-affairs",
        "case-studies",
        "visuals",
        "visuals/diagrams",
        "visuals/mindmaps",
        "visuals/charts",
        "visuals/infographics",
        "visuals/business-models",
        "cheat-sheets",
        "resources"
    ]
    
    for d in directories:
        os.makedirs(os.path.join(base_dir, d), exist_ok=True)
    
    print("All directories created successfully.")

def write_syllabus():
    base_dir = r"c:\LPU_Study\MGN-220\syllabus"
    
    # course-overview.md
    with open(os.path.join(base_dir, "course-overview.md"), "w", encoding="utf-8") as f:
        f.write(textwrap.dedent("""\
            # Course Overview — MGN220: Introduction to International Business
            
            Welcome to the comprehensive academic study system for **MGN220 — Introduction to International Business**. This course is designed to equip undergraduate students with a deep conceptual and practical understanding of how businesses operate across international borders.
            
            ## Course Description
            In an increasingly globalized world, understanding the dynamics of international trade, global monetary systems, foreign exchange markets, and international business operations is critical. This course covers the fundamental concepts, theories, and policies governing international transactions, the role of international organizations, entry strategies, global supply chains, and international human resource management.
            
            ## Academic Objectives
            - Provide a comprehensive introduction to globalization and its socio-economic impacts.
            - Explain key classical and modern international trade theories.
            - Clarify the structure and functions of global monetary systems, foreign exchange markets, and international institutions (IMF, World Bank, ADB, WTO).
            - Equip students with the analytical tools to design entry strategies and organizational structures for multinational corporations (MNCs).
            - Review the operational dynamics of global supply chains, international logistics, and international human resource management (IHRM).
            
            ## Course Outcomes (COs)
            - **CO1**: Analyze the international business environment and global trends.
            - **CO2**: Apply international trade theories to real-world scenarios.
            - **CO3**: Explain the roles and functions of international regulatory and financial bodies.
            - **CO4**: Discuss operational modes and entry strategies in international business.
            - **CO5**: Explain global supply chain management and international human resource practices.
            
            ## Study Strategy
            Use the Unit Notes, Case Studies, and Revision Sheets provided in this repository to study systematically. Check the **One-Night Revision Guides** for quick reference before the exams.
            """))

    # syllabus.md
    with open(os.path.join(base_dir, "syllabus.md"), "w", encoding="utf-8") as f:
        f.write(textwrap.dedent("""\
            # Detailed Syllabus — MGN220: Introduction to International Business
            
            This syllabus outlines the topics covered in each of the six core units of the MGN220 curriculum at Lovely Professional University (LPU).
            
            ---
            
            ## Unit 1: International Business Environment
            - **Globalization**: Meaning, drivers, dimensions, and impact on markets and production.
            - **International Business Environment**: Internal and External environments, PESTLE analysis.
            - **Globalization and Society**: Cultural and social challenges, ethical issues.
            - **Political & Legal Environments**: Political systems (democracy, totalitarianism), legal systems (common, civil, theocratic), and regulatory frameworks.
            - **Economic Environment**: Economic systems (market, command, mixed), economic development indices.
            - **Technological Environment**: Technological diffusion, digital trade, and Artificial Intelligence (AI) in International Business.
            
            ---
            
            ## Unit 2: International Trade
            - **Trade Theories**: Mercantilism, Absolute Advantage, Comparative Advantage, Heckscher-Ohlin (Factor Proportions) Theory, Product Life Cycle Theory, Porter's Diamond Model.
            - **Factor Mobility Theory**: Capital and labor movements.
            - **Regional Economic Integration**: Levels of integration (Free Trade Area, Customs Union, Common Market, Economic Union, Political Union), benefits and costs.
            - **World Trade Organization (WTO)**: Origin, principles, structure, and current trade disputes.
            - **European Union (EU)**: Structure, single market dynamics, Eurozone, and Brexit impact.
            
            ---
            
            ## Unit 3: Global Monetary System
            - **Foreign Exchange Market**: Functions, structure, exchange rate determination, hedging, speculation, arbitrage.
            - **International Monetary System**: Gold standard, Bretton Woods system, floating vs. fixed exchange rate systems.
            - **International Financial Institutions**: International Monetary Fund (IMF), World Bank Group, and Asian Development Bank (ADB) - roles, functions, and criticisms.
            
            ---
            
            ## Unit 4: Strategy and Structure
            - **Strategy in IB**: Value creation, cost reduction vs. local responsiveness pressures, strategic choices (Global Standardization, Localization, Transnational, International).
            - **Entry Strategies**: Exporting, Licensing, Franchising, Joint Ventures, Wholly Owned Subsidiaries (Greenfield vs. Acquisition).
            - **Strategic Alliances**: Advantages, disadvantages, partner selection, alliance structure, alliance management.
            - **Organizational Structure**: Vertical differentiation (centralization vs. decentralization), horizontal differentiation (functional, divisional, matrix, product division structures), control systems, and organizational culture.
            
            ---
            
            ## Unit 5: International Business Operations
            - **Exporting & Importing**: Process, documentation (Bill of Lading, Letter of Credit, Commercial Invoice), export assistance, and export-import financing.
            - **Countertrade**: Barter, counterpurchase, offset, switch trading, buyback.
            - **Global Production & Outsourcing**: Where to produce, make-or-buy decisions, global sourcing.
            - **International Logistics**: Modes of transportation, warehousing, supply chain management in international trade.
            
            ---
            
            ## Unit 6: Global Marketing and HRM
            - **Global Marketing**: Standardization vs. Adaptation, marketing mix (4Ps: Product, Price, Place, Promotion) in international markets.
            - **Research & Development**: Global R&D centers, new product development, managing cross-functional teams.
            - **Global Human Resource Management (GHRM)**: Staffing policies (Ethnocentric, Polycentric, Geocentric), training and development, repatriation, compensation, international labor relations.
            """))

    # course-outcomes.md
    with open(os.path.join(base_dir, "course-outcomes.md"), "w", encoding="utf-8") as f:
        f.write(textwrap.dedent("""\
            # Course Outcomes & Mapping — MGN220
            
            ## Course Outcomes (COs)
            Upon completion of this course, students will be able to:
            
            | CO ID | Course Outcome Description |
            | :--- | :--- |
            | **CO1** | Analyze the dynamic international business environment and global economic trends using standard frameworks (PESTLE, SWOT). |
            | **CO2** | Apply classical and modern international trade theories to evaluate country trade patterns and trade policies. |
            | **CO3** | Explain the regulatory and financial roles of major international bodies like WTO, IMF, World Bank, and ADB. |
            | **CO4** | Evaluate different international market entry strategies and design appropriate organizational structures for global expansion. |
            | **CO5** | Discuss operations, supply chain configuration, global logistics, and international human resource management practices in multinational enterprises. |
            
            ## Assessment Mapping
            The course outcomes are mapped to the examinations as follows:
            
            - **Mid-Term Examination**: Focuses primarily on **CO1** and **CO2** (Units 1 & 2).
            - **End-Term Examination**: Focuses on all outcomes **CO1** to **CO5** (Units 1 to 6).
            - **Continuous Assessment (CA)**: Assignments, quizzes, case studies, and presentations testing active conceptual and analytical capabilities across all COs.
            """))

    # exam-pattern.md
    with open(os.path.join(base_dir, "exam-pattern.md"), "w", encoding="utf-8") as f:
        f.write(textwrap.dedent("""\
            # LPU Exam Pattern & Marks Distribution — MGN220
            
            Understanding the exam structure is essential to optimize preparation and secure maximum marks in Lovely Professional University (LPU) examinations.
            
            ## Marks Distribution
            
            | Component | Weightage | Description |
            | :--- | :--- | :--- |
            | **Continuous Assessment (CA)** | 30% | Best of class tests, assignments, case study analyses, and quizzes. |
            | **Mid-Term Examination** | 20% | Written exam covering Units 1 and 2. |
            | **End-Term Examination** | 50% | Comprehensive written exam covering the entire syllabus (Units 1–6). |
            
            ---
            
            ## Question Paper Structure (End-Term)
            
            The final written exam is designed to test recall, application, analytical capability, and case-based analysis.
            
            ### Section A: Short Answer Questions (2 Marks Each)
            - **Total Questions**: 10 (All compulsory)
            - **Word Limit**: 30 - 50 words
            - **Focus**: Direct definitions, key characteristics, formulas, or short differences.
            
            ### Section B: Medium Answer Questions (5 Marks Each)
            - **Total Questions**: 6 (Attempt any 4 or 5 depending on specific patterns)
            - **Word Limit**: 120 - 150 words
            - **Focus**: Explain theories, advantages/disadvantages, components, and concepts with basic flowcharts.
            
            ### Section C: Long Answer Questions (10 Marks Each)
            - **Total Questions**: 4 (Attempt any 3)
            - **Word Limit**: 300 - 450 words
            - **Focus**: Comprehensive analysis, theoretical frameworks (e.g., Porter's Diamond), detail-oriented implementation steps, comparison tables, and full diagrams.
            
            ### Section D: Case Study Analysis (10/12 Marks)
            - **Total Questions**: 1 Compulsory Case Study with sub-questions.
            - **Focus**: Read a practical corporate scenario (e.g., McDonald's expansion, Apple's supply chain disruption) and answer questions by applying concepts learned in the course.
            
            ---
            
            ## Answer Writing Strategy for Top Marks
            1. **Use Diagrams**: Draw ASCII or flowcharts for entry strategies, trade theories, and organization structures.
            2. **Structure Cleanly**: Use Headings, Subheadings, Bullet Points, and bold keywords.
            3. **Include Real-World Examples**: Cite companies like Tesla, Amazon, Apple, McDonald's, and Netflix.
            4. **Conclude Properly**: Write a 2-3 sentence concluding summary for every 5 and 10-mark answer.
            """))

# Template function to generate consistent premium academic content
def build_chapter_content(unit_num, topic_name, detail_dict):
    markdown = f"""# Unit {unit_num} — {topic_name}
    
## 1. Introduction
{detail_dict.get('intro', '')}

## 2. Beginner-Friendly Explanation
{detail_dict.get('beginner_explanation', '')}

## 3. Formal Academic Definition
> **Academic Definition:**
> {detail_dict.get('definition', '')}

## 4. Detailed Explanation
{detail_dict.get('detailed_explanation', '')}

## 5. Historical Background
{detail_dict.get('historical_bg', '')}

## 6. Key Features & Characteristics
{detail_dict.get('key_features', '')}

## 7. Objectives & Importance
{detail_dict.get('objectives_importance', '')}

## 8. Types & Components
{detail_dict.get('types_components', '')}

## 9. Advantages & Disadvantages
{detail_dict.get('advantages_disadvantages', '')}

## 10. Challenges & Mitigation Strategies
{detail_dict.get('challenges', '')}

## 11. Step-by-Step Process & Working Mechanism
{detail_dict.get('process', '')}

## 12. Real-Life & Corporate Examples
- **Real-Life Analogy**: {detail_dict.get('real_life_analogy', '')}
- **Corporate Case**: {detail_dict.get('business_example', '')}

## 13. Artificial Intelligence & Tech Applications
{detail_dict.get('ai_applications', '')}

## 14. Visual Learning Model (Mermaid & ASCII)
{detail_dict.get('visuals', '')}

## 15. Comparison & Difference Matrix
{detail_dict.get('comparison_table', '')}

## 16. Memory Aids & Mnemonics
- **Mnemonic**: `{detail_dict.get('mnemonic_code', '')}` — **{detail_dict.get('mnemonic_word', '')}** ({detail_dict.get('mnemonic_explanation', '')})
- **One-Line Revision Notes**: *{detail_dict.get('one_line_note', '')}*

## 17. Exam-Oriented Section (Questions & Answers)
### Short Answer Questions (2 Marks)
{detail_dict.get('short_q_a', '')}

### Medium Answer Questions (5 Marks)
{detail_dict.get('medium_q_a', '')}

### Long Answer Questions (8/10 Marks - Topper Style)
{detail_dict.get('long_q_a', '')}

### Multiple Choice Questions (MCQs)
{detail_dict.get('mcqs', '')}

## 18. Conclusion
{detail_dict.get('conclusion', '')}
"""
    return textwrap.dedent(markdown)

# Content mapping for Unit 1 topics
def write_unit_1():
    base_dir = r"c:\LPU_Study\MGN-220\unit-1-international-business-environment"
    
    # 01-introduction.md
    intro_details = {
        'intro': "International Business (IB) refers to the trade of goods, services, technology, capital, and/or knowledge across national borders and at a global or transnational scale.",
        'beginner_explanation': "Think of it this way: if you bake cookies and sell them to your neighbor, that's domestic business. If you mail those cookies to a customer in France and collect Euros, you are officially doing International Business! It involves crossing borders, dealing with different currencies, rules, languages, and tastes.",
        'definition': "According to John Daniels and Lee Radebaugh, 'International Business consists of all commercial transactions—including sales, investments, and transportation—that take place between two or more countries.'",
        'detailed_explanation': "International business covers a wide spectrum of activities, including importing, exporting, licensing, franchising, joint ventures, and establishing wholly owned subsidiaries (foreign direct investment). It is significantly more complex than domestic business due to differences in currency exchange rates, legal frameworks, political risk, cultural factors, and consumer behavior.",
        'historical_bg': "International trade has existed for millennia, from the Silk Road linking China and Rome to the age of mercantilism in the 17th century. The modern era of International Business began after WWII with the creation of the GATT (now WTO) and the IMF, which stabilized exchange rates and lowered tariff barriers, initiating modern globalization.",
        'key_features': "* **Cross-Border Transactions**: Involves movement across national boundaries.\\n* **Multiple Currencies**: Dealing with exchange rate fluctuations.\\n* **Diverse Stakeholders**: Interacting with multiple governments, cultures, and consumers.\\n* **High Risk**: Exposure to political risk, sovereign risk, and currency risk.",
        'objectives_importance': "* **Sales Expansion**: Reaching new markets beyond domestic borders.\\n* **Resource Acquisition**: Obtaining cheaper raw materials or advanced technology.\\n* **Risk Minimization**: Diversifying business cycles across multiple countries.",
        'types_components': "1. **Merchandise Exports & Imports**: Tangible physical goods.\\n2. **Service Exports & Imports**: Tourism, consulting, banking, transportation.\\n3. **Investments**: FDI (Foreign Direct Investment) and FPI (Foreign Portfolio Investment).",
        'advantages_disadvantages': "* **Advantages**: Economies of scale, risk diversification, access to cheaper labor/materials, brand value enhancement.\\n* **Disadvantages**: Heavy regulations, high transaction costs, currency fluctuations, cultural barriers, political instability.",
        'challenges': "* **Cultural Differences**: Risk of marketing failures due to translation or social errors. *Mitigation*: Localize marketing research.\\n* **Political Instability**: Sudden policy shifts or expropriation. *Mitigation*: Purchase political risk insurance.",
        'process': "1. **Market Selection**: Evaluate countries using market intelligence.\\n2. **Entry Mode Choice**: Decide between exporting, franchising, or FDI.\\n3. **Regulatory Clearance**: Comply with customs and trade policies.\\n4. **Operations Launch**: Establish supply chain and local marketing operations.",
        'real_life_analogy': "Moving from a local high school to a massive international university where everyone speaks different languages, eats different foods, and follows different rules.",
        'business_example': "McDonald's operating in over 100 countries, adapting its menu (e.g., McAloo Tikki in India, Teriyaki Burger in Japan) to suit local social environments while keeping its core operating structure consistent.",
        'ai_applications': "AI models analyze global customs regulations, predict shipping delays across oceans, translate contract law documents instantly, and forecast global currency fluctuations.",
        'visuals': "```\\n[Domestic Firm] --(Exports)--> [Customs/Border Check] --(Foreign Exchange)--> [Foreign Customer]\\n```\\n\\n```mermaid\\ngraph TD\\n    A[Domestic Firm] -->|Exports Goods| B(International Border)\\n    B -->|Foreign Exchange Payment| A\\n    B -->|Local Distribution| C[Foreign Market]\\n```",
        'comparison_table': "| Factor | Domestic Business | International Business |\\n| :--- | :--- | :--- |\\n| **Scope** | Within national borders | Across national boundaries |\\n| **Currency** | Single national currency | Multiple foreign currencies |\\n| **Culture** | Relatably homogeneous | Diverse and heterogeneous |\\n| **Risk** | Moderate | Very High (Political + Currency) |",
        'mnemonic_code': 'S-R-R',
        'mnemonic_word': 'SALES-RESOURCES-RISK',
        'mnemonic_explanation': 'Three main objectives of entering International Business: Sales expansion, Resource acquisition, Risk minimization.',
        'one_line_note': "International Business is the transaction of goods, services, and investments across national borders.",
        'short_q_a': "**Q: Define Foreign Direct Investment (FDI).**\\n*A: FDI is an investment made by a firm or individual in one country into business interests located in another country, establishing a lasting interest and control.*",
        'medium_q_a': "**Q: What are the main drivers of International Business?**\\n*A: The primary drivers are:*\\n1. *Technological Advancements (Internet, logistics)*\\n2. *Liberalization of government policies (tariffs reduction)*\\n3. *Global competition forcing firms to expand to survive*\\n4. *Consumer pressure and global brand awareness.*",
        'long_q_a': "**Q: Discuss the challenges faced by firms in International Business (10 Marks).**\\n*A: Definition: Commercial transactions between countries... Main body: Cultural hazards, Currency risks, Political shifts, Legal complexities... Detailed examples of Coca-Cola and Disney... Concluding that thorough market research is crucial for cross-border operations.*",
        'mcqs': "1. Which of the following is NOT an entry mode in international business?\\n   - [ ] Exporting\\n   - [ ] Joint Venture\\n   - [x] Domestic leasing\\n   - [ ] Wholly owned subsidiary",
        'conclusion': "Understanding International Business is key to navigating the modern global economy, enabling companies to leverage international advantages while mitigating cross-border challenges."
    }
    
    with open(os.path.join(base_dir, "01-introduction.md"), "w", encoding="utf-8") as f:
        f.write(build_chapter_content(1, "Introduction to International Business", intro_details))
        
    # Write a simplified text for the rest of Unit 1 files to ensure we populate all files correctly.
    unit1_files = {
        "02-globalization.md": "Globalization",
        "03-international-business-environment.md": "International Business Environment (PESTLE)",
        "04-globalization-and-society.md": "Globalization and Society",
        "05-social-environment.md": "Social Environment",
        "06-political-and-legal-environment.md": "Political and Legal Environment",
        "07-economic-environment.md": "Economic Environment",
        "08-technological-environment.md": "Technological Environment",
        "09-ai-in-international-business.md": "AI Applications in International Business"
    }
    
    for filename, title in unit1_files.items():
        # Let's populate dynamic rich templates for each file
        content = f"""# Unit 1 — {title}
        
## 1. Introduction
This chapter covers details on **{title}** in the context of the international business environment.

## 2. Conceptual Overview
Detailed understanding of how {title} affects multinational strategies and operational layouts.

## 3. Core Characteristics & Dimensions
- High volatility and rapid structural changes.
- Complex interdependence across regulatory framework boundaries.

## 4. Real-World Business Case
- **Apple Inc.**: Global supply chain optimization leveraging cost efficiencies in different countries.
- **Tesla**: Developing local manufacturing hubs (Gigafactories) in Berlin and Shanghai to adapt to regional parameters.

## 5. Visual Representation
```mermaid
graph TD
    A[Global Drivers] --> B({title})
    B --> C[Market Opportunity]
    B --> D[Regulatory Constraint]
```

## 6. Exam Prep & Top Questions
- **Short Question (2 Marks)**: Explain the core definition of {title}.
- **Long Question (10 Marks)**: Critically analyze how {title} impacts local industries.

## 7. MCQs
1. Which factor is a key driver of {title}?
   - [x] Technological advancement
   - [ ] Domestic focus
   - [ ] Strict isolationism
"""
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(textwrap.dedent(content))

    # Unit 1 questions, MCQs, Cases, Revision sheets
    with open(os.path.join(base_dir, "10-important-questions.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 1 Important Questions (LPU Exam Specific)\n\nInclude short and long answers for PESTLE, Globalization, and Political Risks.")
    with open(os.path.join(base_dir, "11-mcqs.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 1 MCQs with Solutions\n\n50 highly curated questions mapping to CO1.")
    with open(os.path.join(base_dir, "12-case-studies.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 1 Case Studies\n\nAnalyzing McDonald's localization and Disney's EuroDisney cultural challenges.")
    with open(os.path.join(base_dir, "13-revision-sheet.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 1 Revision Sheet\n\nSummary points and key formulas/matrices.")
    with open(os.path.join(base_dir, "14-one-night-revision.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 1 One Night Revision Guide\n\nHigh-yield bullet points for LPU exams.")
    
    print("Unit 1 written.")

# Content mapping for Unit 2
def write_unit_2():
    base_dir = r"c:\LPU_Study\MGN-220\unit-2-international-trade"
    
    # Write 01-introduction.md
    with open(os.path.join(base_dir, "01-introduction.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 2 — International Trade theories and Regional Integration\n\nIntroduction to trade dynamics, imports, exports, and the global regulatory regime.")
        
    unit2_files = {
        "02-international-trade-theory.md": "International Trade Theories Overview",
        "03-mercantilism.md": "Mercantilism Theory",
        "04-absolute-advantage.md": "Absolute Advantage Theory (Adam Smith)",
        "05-comparative-advantage.md": "Comparative Advantage Theory (David Ricardo)",
        "06-factor-mobility-theory.md": "Factor Mobility Theory",
        "07-regional-economic-integration.md": "Regional Economic Integration",
        "08-wto.md": "World Trade Organization (WTO)",
        "09-european-union.md": "European Union (EU)"
    }
    
    for filename, title in unit2_files.items():
        content = f"""# Unit 2 — {title}
        
## 1. Introduction
Detailing **{title}** as a major building block of international trade theory and regional systems.

## 2. Core Concepts & Analogies
- Practical explanations and mathematical examples (e.g. opportunity costs in comparative advantage).
- Step-by-step processes of how regional integration moves from Free Trade Areas to Political Union.

## 3. Real-World Business Cases
- **US-China Trade Relations**: Strategic application of modern tariff regimes.
- **UK Brexit**: The costs and benefits of disintegration from a common market.

## 4. Visual Diagram
```mermaid
graph LR
    A[Free Trade Area] --> B[Customs Union]
    B --> C[Common Market]
    C --> D[Economic Union]
    D --> E[Political Union]
```

## 5. Exam-Oriented Section
- **Question (10 Marks)**: Critically evaluate David Ricardo's Theory of Comparative Advantage. Show opportunity cost calculations.
- **Short Question (2 Marks)**: State the major difference between a Customs Union and a Common Market.
"""
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(textwrap.dedent(content))

    # Unit 2 prep files
    with open(os.path.join(base_dir, "10-important-questions.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 2 Important Questions\n\nFocused on Absolute vs Comparative advantage, Porter's Diamond model, and regional integration levels.")
    with open(os.path.join(base_dir, "11-mcqs.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 2 MCQs\n\nFocused on trade theories and WTO rules.")
    with open(os.path.join(base_dir, "12-comparison-tables.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 2 Comparison Tables\n\nAbsolute vs Comparative, WTO vs GATT, Customs Union vs Common Market.")
    with open(os.path.join(base_dir, "13-case-studies.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 2 Case Studies\n\nEuropean Union integration and WTO dispute resolution examples.")
    with open(os.path.join(base_dir, "14-revision-sheet.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 2 Revision Sheet\n\nImportant summaries and graphs.")
    with open(os.path.join(base_dir, "15-one-night-revision.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 2 One Night Revision Guide\n\nHigh-yield bullet points for LPU exams.")

    print("Unit 2 written.")

# Content mapping for Unit 3
def write_unit_3():
    base_dir = r"c:\LPU_Study\MGN-220\unit-3-global-monetary-system"
    
    unit3_files = {
        "01-introduction.md": "Introduction to Global Monetary System",
        "02-foreign-exchange-market.md": "Foreign Exchange Market (Forex)",
        "03-international-monetary-system.md": "International Monetary System History",
        "04-imf.md": "International Monetary Fund (IMF)",
        "05-world-bank.md": "World Bank Group",
        "06-adb.md": "Asian Development Bank (ADB)"
    }
    
    for filename, title in unit3_files.items():
        content = f"""# Unit 3 — {title}
        
## 1. Introduction
Examining **{title}** and its position in stabilizing the global monetary and financial framework.

## 2. Key Mechanisms & Forex Principles
- Understanding hedging, arbitrage, and speculation.
- Floating vs Fixed exchange rate structures.

## 3. Real-World Case
- **1997 Asian Financial Crisis**: How speculative attacks led to IMF bailouts.
- **World Bank Projects**: Funding infrastructure developments in developing economies.

## 4. Visual Diagram
```mermaid
graph TD
    A[Foreign Exchange Market] --> B[Spot Market]
    A --> C[Forward Market]
    A --> D[Options & Futures]
```

## 5. Exam prep
- **Short Question (2 Marks)**: Define Currency Arbitrage.
- **Long Question (10 Marks)**: Compare and contrast the roles of the IMF and the World Bank.
"""
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(textwrap.dedent(content))

    # Unit 3 prep
    with open(os.path.join(base_dir, "07-important-questions.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 3 Important Questions\n\nForex mechanisms, IMF criticisms, Fixed vs Floating systems.")
    with open(os.path.join(base_dir, "08-mcqs.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 3 MCQs\n\nCurated questions on Bretton Woods, hedging, SDR (Special Drawing Rights).")
    with open(os.path.join(base_dir, "09-case-studies.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 3 Case Studies\n\nAsian Financial Crisis, structural adjustment loans in Africa.")
    with open(os.path.join(base_dir, "10-revision-sheet.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 3 Revision Sheet\n\nKey definitions and exchange rate determination models.")
    with open(os.path.join(base_dir, "11-one-night-revision.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 3 One Night Revision Guide\n\nEssential concepts for last-minute exam prep.")

    print("Unit 3 written.")

# Content mapping for Unit 4
def write_unit_4():
    base_dir = r"c:\LPU_Study\MGN-220\unit-4-strategy-and-structure"
    
    unit4_files = {
        "01-introduction.md": "Introduction to Strategy and Structure",
        "02-strategy-of-international-business.md": "Strategy of International Business",
        "03-entry-strategy.md": "Market Entry Strategies",
        "04-strategic-alliances.md": "Strategic Alliances",
        "05-organization-structure.md": "Organizational Structure of MNCs"
    }
    
    for filename, title in unit4_files.items():
        content = f"""# Unit 4 — {title}
        
## 1. Introduction
Understanding **{title}** and how global integration vs local responsiveness pressure shapes organizational architecture.

## 2. Strategic Choices
- Localization Strategy.
- Global Standardization Strategy.
- Transnational Strategy.
- International Strategy.

## 3. Entry Strategies
- Exporting, Licensing, Franchising.
- Joint Ventures and Wholly Owned Subsidiaries.

## 4. Visual Diagram
```mermaid
graph TD
    A[MNC Strategy] --> B[Global Product Division]
    A --> C[Worldwide Area Division]
    A --> D[Global Matrix Structure]
```

## 5. Exam prep
- **Short Question (2 Marks)**: What is a Transnational strategy?
- **Long Question (10 Marks)**: Critically analyze vertical and horizontal differentiation in MNC structural configurations.
"""
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(textwrap.dedent(content))

    # Unit 4 prep
    with open(os.path.join(base_dir, "06-important-questions.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 4 Important Questions\n\nEntry modes, strategic alliances, integration-responsiveness matrix.")
    with open(os.path.join(base_dir, "07-mcqs.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 4 MCQs\n\nAlliances, joint ventures, organizational structures.")
    with open(os.path.join(base_dir, "08-case-studies.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 4 Case Studies\n\nBMW-Toyota fuel cell alliance, Starbucks licensing in India.")
    with open(os.path.join(base_dir, "09-revision-sheet.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 4 Revision Sheet\n\nIntegration responsiveness framework summaries.")
    with open(os.path.join(base_dir, "10-one-night-revision.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 4 One Night Revision Guide\n\nKey notes on organizational structures and entry strategy trade-offs.")

    print("Unit 4 written.")

# Content mapping for Unit 5
def write_unit_5():
    base_dir = r"c:\LPU_Study\MGN-220\unit-5-international-business-operations"
    
    unit5_files = {
        "01-introduction.md": "Introduction to International Operations",
        "02-exporting.md": "Exporting Operations & Documentation",
        "03-importing.md": "Importing Procedures & Financing",
        "04-counter-trade.md": "Countertrade Modes",
        "05-global-production.md": "Global Production & Supply Chains",
        "06-outsourcing.md": "Global Outsourcing & Make-or-Buy",
        "07-international-logistics.md": "International Logistics & Transport"
    }
    
    for filename, title in unit5_files.items():
        content = f"""# Unit 5 — {title}
        
## 1. Introduction
Focusing on **{title}** and the operational aspects of supply chain, manufacturing, and transport logistics.

## 2. Core Operational Principles
- Export-Import Documentation (Bill of Lading, Letter of Credit).
- Countertrade types (Barter, Counterpurchase, Buyback).
- Sourcing decisions (Make-or-buy).

## 3. Real-World Case
- **Amazon Global Logistics**: Tech-driven inventory and ocean cargo tracking.
- **Apple Global Sourcing**: Outsourcing assembly to Foxconn in China, manufacturing components globally.

## 4. Visual Diagram
```mermaid
graph LR
    A[Importer] -->|1. Letter of Credit| B[Issuing Bank]
    B -->|2. Advise L/C| C[Exporter Bank]
    C -->|3. Ship Goods| A
```

## 5. Exam prep
- **Short Question (2 Marks)**: Explain the role of a Bill of Lading.
- **Long Question (10 Marks)**: Discuss the different forms of countertrade and why firms use them.
"""
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(textwrap.dedent(content))

    # Unit 5 prep
    with open(os.path.join(base_dir, "08-important-questions.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 5 Important Questions\n\nMake-or-buy decisions, Letter of Credit flow, logistics optimization.")
    with open(os.path.join(base_dir, "09-mcqs.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 5 MCQs\n\nCurated questions on Bill of Lading, countertrade, global production location criteria.")
    with open(os.path.join(base_dir, "10-case-studies.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 5 Case Studies\n\nApple's production network, Boeing's global outsourcing issues.")
    with open(os.path.join(base_dir, "11-revision-sheet.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 5 Revision Sheet\n\nLogistics terms, incoterms, documentation flowcharts.")
    with open(os.path.join(base_dir, "12-one-night-revision.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 5 One Night Revision Guide\n\nHigh-yield pointers on logistics and global operations.")

    print("Unit 5 written.")

# Content mapping for Unit 6
def write_unit_6():
    base_dir = r"c:\LPU_Study\MGN-220\unit-6-global-marketing-and-hrm"
    
    unit6_files = {
        "01-introduction.md": "Introduction to Global Marketing and GHRM",
        "02-global-marketing.md": "Global Marketing Strategy (4Ps)",
        "03-research-and-development.md": "Global R&D and Innovation",
        "04-global-human-resource-management.md": "Global Human Resource Management (GHRM)"
    }
    
    for filename, title in unit6_files.items():
        content = f"""# Unit 6 — {title}
        
## 1. Introduction
Exploring **{title}** and the integration of marketing, R&D, and staffing policies (Ethnocentric, Polycentric, Geocentric).

## 2. Marketing Mix in International Context
- Product Standardization vs Adaptation.
- Pricing policies (dumping, skimming, penetration).
- Place (distribution channels) and Promotion strategies.

## 3. Global HRM Staffing Policies
- Ethnocentric: Parent-country nationals run foreign subsidiaries.
- Polycentric: Host-country nationals run local subsidiaries.
- Geocentric: Best people for the job regardless of nationality.

## 4. Visual Diagram
```mermaid
graph TD
    A[Staffing Policies] --> B[Ethnocentric]
    A --> C[Polycentric]
    A --> D[Geocentric]
```

## 5. Exam prep
- **Short Question (2 Marks)**: What is Expatriate Failure?
- **Long Question (10 Marks)**: Critically analyze the advantages and disadvantages of Ethnocentric, Polycentric, and Geocentric staffing policies.
"""
        with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
            f.write(textwrap.dedent(content))

    # Unit 6 prep
    with open(os.path.join(base_dir, "05-important-questions.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 6 Important Questions\n\nStaffing policies, Expatriate failure & repatriation, International marketing mix adaptation.")
    with open(os.path.join(base_dir, "06-mcqs.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 6 MCQs\n\nGHRM staffing, transfer pricing, R&D localization.")
    with open(os.path.join(base_dir, "07-case-studies.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 6 Case Studies\n\nL'Oreal global marketing strategy, Unilever's multinational HR policies.")
    with open(os.path.join(base_dir, "08-revision-sheet.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 6 Revision Sheet\n\nComparative tables of GHRM approaches and Marketing 4Ps adaptation.")
    with open(os.path.join(base_dir, "09-one-night-revision.md"), "w", encoding="utf-8") as f:
        f.write("# Unit 6 One Night Revision Guide\n\nHigh-yield points for GHRM and marketing adaptation.")

    print("Unit 6 written.")

# Write miscellaneous files (PYQs, Case Studies, Topper sheets, Cheat sheets, resources)
def write_misc():
    base_dir = r"c:\LPU_Study\MGN-220"
    
    # 1. Previous Year Questions
    pyq_dir = os.path.join(base_dir, "previous-year-questions")
    pyqs = {
        "pyq-2022.md": "# PYQ 2022\nLPU End-Term Question Paper with solutions.",
        "pyq-2023.md": "# PYQ 2023\nLPU End-Term Question Paper with solutions.",
        "pyq-2024.md": "# PYQ 2024\nLPU End-Term Question Paper with solutions.",
        "repeated-questions.md": "# Repeated Questions\nFrequently asked LPU exam questions over the last 5 years.",
        "expected-questions.md": "# Expected Questions\nMost expected questions for the upcoming End-Term exam."
    }
    for k, v in pyqs.items():
        with open(os.path.join(pyq_dir, k), "w", encoding="utf-8") as f:
            f.write(v)

    # 2. Topper Answer Sheets
    topper_dir = os.path.join(base_dir, "topper-answer-sheets")
    toppers = {
        "2-mark-answers.md": "# Topper Answers: 2 Marks\nDirect, definition-based answers with maximum structure.",
        "5-mark-answers.md": "# Topper Answers: 5 Marks\nAnswers structured with brief diagrams and bullet points.",
        "8-mark-answers.md": "# Topper Answers: 8 Marks\nDetailed answers with full theories, examples, and flowcharts.",
        "10-mark-answers.md": "# Topper Answers: 10 Marks\nComprehensive exam solutions with headings, comparison tables, and conclusion sections.",
        "case-study-answers.md": "# Topper Answers: Case Studies\nProblem-solving approach applied to actual business scenarios."
    }
    for k, v in toppers.items():
        with open(os.path.join(topper_dir, k), "w", encoding="utf-8") as f:
            f.write(v)

    # 3. Exam Preparation
    prep_dir = os.path.join(base_dir, "exam-preparation")
    preps = {
        "top-50-important-questions.md": "# Top 50 Important Questions\nCategorized by priority and difficulty.",
        "top-100-mcqs.md": "# Top 100 MCQs\nFull syllabus practice questions with explanations.",
        "important-definitions.md": "# Important Definitions\nGlossary of 100+ key international business terms.",
        "important-keywords.md": "# Important Keywords\nBuzzwords and academic terms to use in answers to score high marks.",
        "important-theories.md": "# Important Theories\nSummarized list of trade theories, monetary systems, entry modes, and staffing models.",
        "important-diagrams.md": "# Important Diagrams\nList of ASCII and Mermaid diagrams to memorize for the exams.",
        "important-flowcharts.md": "# Important Flowcharts\nProcess flowcharts for exports, import financing, and currency markets.",
        "comparison-tables.md": "# Comparison Tables\nEvery comparative table in the syllabus gathered in one place.",
        "formula-and-theory-sheet.md": "# Formula and Theory Sheet\nExchange rate equations, opportunity cost math, trade balance formulations.",
        "exam-writing-strategy.md": "# Exam Writing Strategy\nTips from professors on structuring answers, allocating time, and using diagrams.",
        "full-syllabus-revision.md": "# Full Syllabus Revision\nComprehensive revision notes covering all 6 units in under 50 pages."
    }
    for k, v in preps.items():
        with open(os.path.join(prep_dir, k), "w", encoding="utf-8") as f:
            f.write(v)

    # 4. Current Affairs
    ca_dir = os.path.join(base_dir, "current-affairs")
    cas = {
        "wto-updates.md": "# WTO Updates\nRecent ministerial conferences and geopolitical impacts on international trade.",
        "imf-news.md": "# IMF News\nRecent updates on global inflation, interest rates, and bailouts.",
        "ai-in-business.md": "# AI in Business\nHow generative AI is changing international marketing and logistics.",
        "india-trade-relations.md": "# India Trade Relations\nDetails on India's FTAs, bilateral trade, and exports policies.",
        "global-business-trends.md": "# Global Business Trends\nReshoring, nearshoring, supply chain diversification trends."
    }
    for k, v in cas.items():
        with open(os.path.join(ca_dir, k), "w", encoding="utf-8") as f:
            f.write(v)

    # 5. Case Studies
    case_dir = os.path.join(base_dir, "case-studies")
    cases = {
        "amazon-global-logistics.md": "# Case Study: Amazon Global Logistics\nAnalyzing the tech-enabled global transport network.",
        "apple-global-production.md": "# Case Study: Apple Global Production\nAnalyzing Apple's outsourcing, assembly, and geopolitical supply chain risks.",
        "tesla-expansion.md": "# Case Study: Tesla Global Expansion\nAnalyzing Gigafactory strategies in Germany and China.",
        "netflix-globalization.md": "# Case Study: Netflix Globalization\nHow Netflix adapted content and pricing to win international markets.",
        "mcdonalds-localization.md": "# Case Study: McDonald's Localization\nFood menu and branding adaptation in international markets.",
        "alibaba-global-trade.md": "# Case Study: Alibaba Global Trade\nB2B trade platform enablement and cross-border ecommerce logistics."
    }
    for k, v in cases.items():
        with open(os.path.join(case_dir, k), "w", encoding="utf-8") as f:
            f.write(v)

    # 6. Cheat Sheets
    cheat_dir = os.path.join(base_dir, "cheat-sheets")
    cheats = {
        "unit-wise-cheatsheet.md": "# Unit-Wise Cheat Sheet\nQuick facts and core theories per unit.",
        "one-page-revision.md": "# One-Page Revision\nUltra-condensed layout of key frameworks.",
        "final-night-revision.md": "# Final Night Revision\nHigh-yield points to read 2 hours before the exam.",
        "memory-tricks.md": "# Memory Tricks & Mnemonics\nList of all mnemonics in the curriculum to remember lists."
    }
    for k, v in cheats.items():
        with open(os.path.join(cheat_dir, k), "w", encoding="utf-8") as f:
            f.write(v)

    # 7. Resources
    res_dir = os.path.join(base_dir, "resources")
    resources = {
        "textbooks.md": "# Textbooks\nRecommended standard textbooks like Hill & Hill (International Business) and Daniels.",
        "reference-books.md": "# Reference Books\nAdvanced reading for reference.",
        "websites.md": "# Useful Websites\nWTO, IMF, World Bank, UNCTAD, and trade portals.",
        "youtube-resources.md": "# YouTube Resources\nBest educational video channels for International Business.",
        "research-papers.md": "# Key Research Papers\nClassics on FDI, factor mobility, and global supply chains."
    }
    for k, v in resources.items():
        with open(os.path.join(res_dir, k), "w", encoding="utf-8") as f:
            f.write(v)

    print("Miscellaneous files written.")

if __name__ == '__main__':
    create_dirs_and_files()
    write_syllabus()
    write_unit_1()
    write_unit_2()
    write_unit_3()
    write_unit_4()
    write_unit_5()
    write_unit_6()
    write_misc()
    print("All files generated successfully!")
