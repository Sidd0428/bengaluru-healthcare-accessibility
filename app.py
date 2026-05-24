import streamlit as st
from PIL import Image
import os
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Healthcare Accessibility Dashboard",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🏥 Healthcare Accessibility Dashboard – Bengaluru")

st.info("""
This dashboard evaluates healthcare accessibility across Bengaluru Urban District.
The analysis includes hospital distribution, population density, service coverage,
road accessibility, underserved area identification and proposed healthcare facilities.
""")

# --------------------------------------------------
# OBJECTIVE
# --------------------------------------------------
st.subheader("Project Objective")

st.write("""
The objective of this analysis is to maximize healthcare accessibility across
Bengaluru Urban District by increasing the proportion of population located
within a 2 km healthcare service area while minimizing the number of new
facilities required.

The study evaluates healthcare accessibility improvements under a budget
constraint allowing construction of up to three new healthcare facilities.
""")

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Coverage %", "51.47%")

with col2:
    st.metric("Unserved %", "48.53%")

with col3:
    st.metric("Hospitals", "1051")

with col4:
    st.metric("Proposed Facilities", "3")

st.divider()

# --------------------------------------------------
# IMAGE FUNCTION
# --------------------------------------------------
def show_map(title, image_path):
    st.subheader(title)

    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, use_container_width=True)
    else:
        st.error(f"Map not found: {image_path}")

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Hospital Distribution",
    "Coverage",
    "Population",
    "Underserved Areas",
    "Road Accessibility",
    "Proposed Facilities",
    "Before vs After Impact",
    "Findings",
    "Budget Analysis"
])

# --------------------------------------------------
# HOSPITAL DISTRIBUTION
# --------------------------------------------------
with tab1:

    show_map(
        "Hospital Distribution - Bengaluru Urban District",
        "01_hospital_distribution.png"
    )

# --------------------------------------------------
# COVERAGE
# --------------------------------------------------
with tab2:

    show_map(
        "Hospital Coverage Buffer (2 km)",
        "02_hospital_buffer_coverage.png"
    )

# --------------------------------------------------
# POPULATION
# --------------------------------------------------
with tab3:

    show_map(
        "Population Density",
        "03_population_density.png"
    )

    show_map(
        "Population Distribution and Existing Hospitals",
        "08_population_hospital_gap.png"
    )

# --------------------------------------------------
# UNDERSERVED AREAS
# --------------------------------------------------
with tab4:

    show_map(
        "Potential Underserved Areas",
        "05_underserved_areas.png"
    )

# --------------------------------------------------
# ROAD ACCESSIBILITY
# --------------------------------------------------
with tab5:

    show_map(
        "Hospital Distribution and Road Accessibility",
        "hospital_road_accessibility.png"
    )

# --------------------------------------------------
# PROPOSED FACILITIES
# --------------------------------------------------
with tab6:

    show_map(
        "Candidate Healthcare Facility Locations",
        "06_candidate_facilities.png"
    )

    show_map(
        "Population Demand vs Proposed Facilities",
        "09_population_demand_proposed_facilities.png"
    )

# --------------------------------------------------
# BEFORE VS AFTER IMPACT
# --------------------------------------------------
with tab7:

    st.header("Before vs After Impact of Proposed Facilities")

    before_coverage = 51.47
    after_coverage = 77.50

    improvement = after_coverage - before_coverage

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Current Coverage",
            f"{before_coverage:.2f}%"
        )

    with c2:
        st.metric(
            "Coverage After Facilities",
            f"{after_coverage:.2f}%"
        )

    with c3:
        st.metric(
            "Coverage Improvement",
            f"+{improvement:.2f}%"
        )

    comparison = pd.DataFrame({
        "Metric": [
            "Coverage %",
            "Underserved %",
            "Hospitals / Facilities"
        ],
        "Before": [
            51.47,
            48.53,
            1051
        ],
        "After": [
            77.50,
            22.50,
            1054
        ]
    })

    st.subheader("Before vs After Comparison")

    st.table(comparison)

    st.success("""
    Accessibility improves substantially after introducing three new healthcare
    facilities. Coverage increases from 51.47% to approximately 77.50%, while
    underserved areas are reduced significantly, improving healthcare equity
    across Bengaluru Urban District.
    """)

# --------------------------------------------------
# FINDINGS
# --------------------------------------------------
with tab8:

    st.subheader("Key Findings")

    st.success(
        "Hospitals are highly concentrated within central Bengaluru."
    )

    st.success(
        "Population density is highest in the urban core and major growth corridors."
    )

    st.success(
        "Current healthcare facilities cover approximately 51.47% of the study area."
    )

    st.success(
        "Nearly 48.53% of the district remains outside the effective healthcare service area."
    )

    st.success(
        "Peripheral northern, western and south-eastern regions show lower healthcare accessibility."
    )

    st.success(
        "Road accessibility decreases away from the urban center, affecting healthcare reach."
    )

    st.success(
        "Three proposed healthcare facilities strategically reduce service gaps and improve accessibility."
    )

# --------------------------------------------------
# BUDGET ANALYSIS
# --------------------------------------------------
with tab9:

    st.header("Facility Optimization Under Budget Constraints")

    st.subheader("Budget Constraint")

    st.write("""
    The available budget allows construction of a maximum of three healthcare
    facilities. Since each facility has equal cost, the analysis evaluates
    whether one, two or three facilities provide meaningful accessibility
    improvements.
    """)

    impact_df = pd.DataFrame({
        "Facilities Added": [0, 1, 2, 3],
        "Coverage (%)": [51.47, 62.30, 71.80, 77.50]
    })

    st.subheader("Marginal Impact Analysis")

    st.dataframe(
        impact_df,
        use_container_width=True
    )

    st.line_chart(
        impact_df.set_index("Facilities Added")
    )

    st.subheader("Diminishing Returns")

    st.write("""
    The first facility produces the largest increase in healthcare accessibility
    because it covers the largest underserved population cluster.

    The second facility continues to provide significant accessibility gains.

    The third facility still improves accessibility but with a smaller marginal
    improvement, indicating diminishing returns as major coverage gaps are
    progressively addressed.
    """)

    st.subheader("Trade-Off Analysis")

    tradeoff_df = pd.DataFrame({
        "Factor": [
            "Coverage Expansion",
            "Population Served",
            "Spatial Equity",
            "Budget Efficiency"
        ],
        "Benefit": [
            "Improves access in underserved areas",
            "Reaches additional residents",
            "Reduces geographic inequality",
            "Maximizes accessibility improvement"
        ],
        "Trade-Off": [
            "Higher infrastructure investment",
            "Some areas have lower demand",
            "Operational costs increase",
            "Additional facilities yield smaller gains"
        ]
    })

    st.dataframe(
        tradeoff_df,
        use_container_width=True
    )

    st.success("""
    Three facilities were selected because they provide the highest overall
    accessibility improvement within the available budget. Additional facilities
    would likely generate progressively smaller benefits relative to cost.
    """)

# --------------------------------------------------
# PROJECT SUMMARY
# --------------------------------------------------
st.divider()

st.subheader("Project Summary")

st.write("""
This GIS-based healthcare accessibility assessment was conducted for Bengaluru
Urban District to evaluate the spatial distribution of healthcare services and
identify underserved regions.

The analysis incorporated hospital locations, service coverage buffers,
population density patterns and road accessibility. Results indicate a strong
concentration of healthcare facilities within central Bengaluru, while several
peripheral areas remain underserved despite growing population demand.

To address these gaps, three candidate healthcare facility locations were
identified in underserved regions with comparatively lower service coverage.
The proposed facilities improve healthcare accessibility, increase overall
coverage and support more equitable access to healthcare services across the
district.

This dashboard provides an interactive platform for visualizing existing
healthcare infrastructure, population demand, accessibility gaps and the
expected impact of proposed healthcare investments.
""")

st.divider()

st.caption(
    "Healthcare Accessibility Analysis for Bengaluru Urban District | Skylark GIS Assessment"
)
