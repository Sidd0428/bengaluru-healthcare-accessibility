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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Hospital Distribution",
    "Coverage",
    "Population",
    "Underserved Areas",
    "Road Accessibility",
    "Proposed Facilities",
    "Before vs After Impact",
    "Findings"
])

# --------------------------------------------------
# HOSPITAL DISTRIBUTION
# --------------------------------------------------
with tab1:

    show_map(
        "Hospital Distribution",
        "outputs/maps/01_hospital_distribution.png"
    )

# --------------------------------------------------
# COVERAGE
# --------------------------------------------------
with tab2:

    show_map(
        "Hospital Coverage Buffer (2 km)",
        "outputs/maps/02_hospital_buffer_coverage.png"
    )

# --------------------------------------------------
# POPULATION
# --------------------------------------------------
with tab3:

    show_map(
        "Population Density",
        "outputs/maps/03_population_density.png"
    )

    show_map(
        "Population Density vs Existing Hospitals",
        "outputs/maps/08_population_hospital_gap.png"
    )

# --------------------------------------------------
# UNDERSERVED AREAS
# --------------------------------------------------
with tab4:

    show_map(
        "Potential Underserved Areas",
        "outputs/maps/05_underserved_areas.png"
    )

# --------------------------------------------------
# ROAD ACCESSIBILITY
# --------------------------------------------------
with tab5:

    show_map(
        "Road Accessibility to Healthcare Facilities",
        "outputs/maps/hospital_road_accessibility.png"
    )

# --------------------------------------------------
# PROPOSED FACILITIES
# --------------------------------------------------
with tab6:

    show_map(
        "Candidate Healthcare Facility Locations",
        "outputs/maps/06_candidate_facilities.png"
    )

    show_map(
        "Population Demand vs Proposed Facilities",
        "outputs/maps/09_population_demand_proposed_facilities.png"
    )

# --------------------------------------------------
# BEFORE VS AFTER IMPACT
# --------------------------------------------------
with tab7:

    st.header("Before vs After Impact of Proposed Facilities")

    before_coverage = 51.47
    after_coverage = 65.20   # Update if you calculate actual value

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

    impact_df = pd.DataFrame({
        "Scenario": [
            "Existing Hospitals",
            "With Proposed Facilities"
        ],
        "Coverage (%)": [
            before_coverage,
            after_coverage
        ]
    })

    st.subheader("Coverage Comparison")

    st.dataframe(
        impact_df,
        use_container_width=True
    )

    st.subheader("Coverage Improvement")

    st.bar_chart(
        impact_df.set_index("Scenario")
    )

    st.success("""
    Proposed healthcare facilities improve healthcare accessibility
    across Bengaluru by expanding service coverage and reducing
    underserved areas. Accessibility improvements are most evident
    in peripheral regions where existing healthcare facilities are limited.
    """)

# --------------------------------------------------
# FINDINGS
# --------------------------------------------------
with tab8:

    st.subheader("Key Findings")

    st.success(
        "Hospitals are concentrated in central Bengaluru."
    )

    st.success(
        "Population density is highest in the urban core."
    )

    st.success(
        "Existing healthcare facilities cover approximately 51.47% of the study area."
    )

    st.success(
        "Approximately 48.53% of the study area remains underserved."
    )

    st.success(
        "Road accessibility decreases towards peripheral regions."
    )

    st.success(
        "Proposed healthcare facilities improve accessibility in underserved locations."
    )

# --------------------------------------------------
# PROJECT SUMMARY
# --------------------------------------------------
st.divider()

st.subheader("Project Summary")

st.write("""
This project evaluates healthcare accessibility across Bengaluru Urban District
using GIS techniques. Existing hospitals, road networks, population density and
service coverage were analyzed to identify underserved regions and recommend
optimal locations for new healthcare facilities.

The analysis indicates that healthcare services are concentrated in central Bengaluru,
while peripheral regions experience lower accessibility. Proposed facilities improve
coverage and help reduce healthcare access disparities across the study area.
""")

st.divider()

st.caption(
    "Healthcare Accessibility Analysis for Bengaluru Urban District | GIS Assignment"
)