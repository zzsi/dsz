import os
import streamlit as st
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

PASSCODE = os.getenv("PASSCODE")

@dataclass
class UserContext:
    target_market: Optional[str] = None
    industry: Optional[str] = None
    business_type: Optional[str] = None
    data_handling: List[str] = None
    specific_concerns: str = None
    current_page: int = 1

# Initialize session state
if 'user_context' not in st.session_state:
    st.session_state.user_context = UserContext()
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Data for type-ahead
MARKETS = [
    "European Union", "United Kingdom", "Saudi Arabia", "UAE", "Qatar", 
    "Singapore", "Japan", "South Korea", "Australia"
]

INDUSTRIES = [
    "Software & Technology", "Financial Services", "Healthcare & Medical Devices",
    "E-commerce & Retail", "Manufacturing", "Professional Services",
    "Education & Training", "Media & Entertainment"
]

BUSINESS_TYPES = [
    "Digital Services Only", "Physical Products", "Hybrid (Digital + Physical)",
    "Consulting Services", "Licensed Software", "SaaS Platform"
]

DATA_TYPES = [
    "Personal Customer Data", "Financial Data", "Health Records",
    "Employee Data", "Business Partner Data", "Technical Data",
    "Location Data", "Behavioral Data", "Children's Data"
]

def show_login():
    """Display login screen"""
    st.title("Market Entry Compliance Navigator")
    passcode = st.text_input("Enter passcode", type="password")
    if st.button("Login"):
        if passcode == PASSCODE:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid passcode. Please try again.")

def render_page_1():
    """Initial Questions - Market and Industry"""
    st.header("Let's understand your market entry plans")
    
    # Type-ahead for market selection
    selected_market = st.selectbox(
        "Which market are you planning to enter?",
        options=MARKETS,
        index=None,
        placeholder="Start typing or select...",
    )
    
    # Type-ahead for industry selection
    selected_industry = st.selectbox(
        "What industry are you in?",
        options=INDUSTRIES,
        index=None,
        placeholder="Start typing or select...",
    )
    
    if selected_market and selected_industry:
        if st.button("Next"):
            st.session_state.user_context.target_market = selected_market
            st.session_state.user_context.industry = selected_industry
            st.session_state.user_context.current_page = 2
            st.rerun()

def render_page_2():
    """Business Model and Data Handling"""
    st.header("Tell us about your business model")
    
    # Show AI response based on previous inputs
    st.info(f"Based on your interest in entering {st.session_state.user_context.target_market} "
            f"as a {st.session_state.user_context.industry} company, let's understand more about "
            "your specific business model and data handling practices.")
    
    # Business type selection
    selected_business = st.selectbox(
        "What best describes your business model?",
        options=BUSINESS_TYPES,
        index=None,
        placeholder="Start typing or select...",
    )
    
    # Multiple selection for data handling
    selected_data = st.multiselect(
        "What types of data will you handle? (Select all that apply)",
        options=DATA_TYPES,
        placeholder="Start typing or select multiple..."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back"):
            st.session_state.user_context.current_page = 1
            st.rerun()
    
    with col2:
        if selected_business and selected_data:
            if st.button("Next"):
                st.session_state.user_context.business_type = selected_business
                st.session_state.user_context.data_handling = selected_data
                st.session_state.user_context.current_page = 3
                st.rerun()

def render_page_3():
    """Specific Concerns and AI Response"""
    st.header("Specific Compliance Concerns")
    
    # Show AI analysis based on previous inputs
    st.info(f"I've analyzed your profile as a {st.session_state.user_context.business_type} "
            f"business in {st.session_state.user_context.industry} handling "
            f"{', '.join(st.session_state.user_context.data_handling[:2])} "
            f"{'and other data types' if len(st.session_state.user_context.data_handling) > 2 else ''}.")
    
    # Key compliance areas identified
    st.write("Based on your profile, here are key compliance areas to consider:")
    st.markdown("""
    1. **Data Protection & Privacy**
       - Relevant frameworks and requirements
       - Data localization needs
    
    2. **Industry-Specific Regulations**
       - Licensing requirements
       - Operational standards
    
    3. **Business Registration**
       - Legal entity requirements
       - Local representation needs
    """)
    
    # Free text for specific concerns
    specific_concerns = st.text_area(
        "Do you have any specific compliance concerns you'd like to explore?",
        placeholder="e.g., specific regulations, timeline constraints, etc."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back"):
            st.session_state.user_context.current_page = 2
            st.rerun()
    
    with col2:
        if st.button("Generate Detailed Report"):
            st.session_state.user_context.specific_concerns = specific_concerns
            st.session_state.user_context.current_page = 4
            st.rerun()

def render_page_4():
    """Final Report and Next Steps"""
    st.header("Your Customized Compliance Roadmap")
    # This would integrate with your LLM to generate detailed guidance
    # For now, we'll show a placeholder structured response
    
    st.success("Based on our analysis, here's your customized compliance roadmap")
    
    # Placeholder for LLM-generated content
    st.markdown("### Immediate Actions (0-30 days)")
    st.markdown("1. Register with relevant authorities")
    st.markdown("2. Begin data protection impact assessment")
    
    st.markdown("### Short-term Requirements (30-90 days)")
    st.markdown("1. Establish local entity structure")
    st.markdown("2. Implement data handling procedures")
    
    if st.button("← Start Over"):
        st.session_state.user_context = UserContext()
        st.rerun()

# Main app logic
def main():
    st.set_page_config(page_title="Market Entry Compliance Navigator", layout="wide")
    
    # hide_streamlit_style = """
    # <style>
    # #MainMenu {visibility: hidden;}
    # footer {visibility: hidden;}
    # </style>
    # """
    # st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Check authentication
    if not st.session_state.authenticated:
        show_login()
        return

    # Progress indicator
    progress = (st.session_state.user_context.current_page - 1) * 25
    st.progress(progress)
    
    # Render appropriate page
    if st.session_state.user_context.current_page == 1:
        render_page_1()
    elif st.session_state.user_context.current_page == 2:
        render_page_2()
    elif st.session_state.user_context.current_page == 3:
        render_page_3()
    elif st.session_state.user_context.current_page == 4:
        render_page_4()

if __name__ == "__main__":
    main()