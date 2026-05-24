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
    after_coverage = 65.20

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

    st.bar_chart(
        impact_df.set_index("Scenario")
    )

    st.success("""
    The proposed healthcare facilities improve accessibility in peripheral
    and underserved regions of Bengaluru Urban District. Coverage increases
    from 51.47% to approximately 65.20%, reducing service gaps and improving
    equitable access to healthcare infrastructure.
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
    "Healthcare Accessibility Analysis for Bengaluru Urban District | GIS Assignment"
)
