"""
Enhanced AI interpretation component
"""

import streamlit as st
from typing import Optional
from services.ai_service import AIService
from repositories.session_repository import SessionRepository
from config.settings import settings
from config.ui_config import (
    INTERPRETATION_SECTION_TITLE, INTERPRETATION_DESCRIPTION,
    INTERPRET_BUTTON_TEXT, INTERPRETATION_LOADING
)
from domain.exceptions import VNGError
from domain.models import AnalysisResults, AnalysisResult, MetricData


def render_interpretation_section():
    """Render enhanced AI interpretation section"""
    st.header(f"🤖 {INTERPRETATION_SECTION_TITLE}")
    st.write(INTERPRETATION_DESCRIPTION)
    
    # Get API key
    api_key = settings.get_api_key()
    
    if not api_key:
        st.warning("⚠️ AI API key not found. Please set it in `.streamlit/secrets.toml` or as environment variable `AI_API_KEY`.")
        st.code("""
# In .streamlit/secrets.toml:
AI_API_KEY = "your-api-key-here"
        """)
        return
    
    # Interpretation button
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button(INTERPRET_BUTTON_TEXT, type="primary"):
            get_interpretation()
    
    # Display interpretation if available
    interpretation_text = SessionRepository.get_interpretation_text()
    if interpretation_text:
        st.divider()
        st.subheader("📝 Interpretation Results")
        
        # Display in expandable sections
        with st.expander("View Full Interpretation", expanded=True):
            st.markdown(interpretation_text)
        
        # Export button
        st.download_button(
            label="📥 Download Interpretation",
            data=interpretation_text,
            file_name="vng_interpretation.txt",
            mime="text/plain"
        )


def get_interpretation():
    """Get AI interpretation of analysis results"""
    with st.spinner(INTERPRETATION_LOADING):
        try:
            # Get analysis results and convert to domain model
            analysis_results_dict = SessionRepository.get_analysis_results()
            file_data_list = SessionRepository.get_file_data_list()
            
            if not analysis_results_dict or not file_data_list:
                st.error("No analysis results available. Please analyze files first.")
                return
            
            # Convert to domain model for service
            results = {
                category: AnalysisResult(
                    category=category,
                    metrics={
                        metric: MetricData(
                            values=data['values'],
                            flags=data['flags'],
                            delta=data['delta'],
                            percent_change=data['percent_change'],
                            std_dev=data['std_dev']
                        )
                        for metric, data in metrics.items()
                    }
                )
                for category, metrics in analysis_results_dict.items()
            }
            
            analysis_results = AnalysisResults(
                results=results,
                file_count=len(file_data_list),
                total_metrics=sum(len(m) for m in analysis_results_dict.values())
            )
            
            # Get interpretation using service
            interpretation = AIService.get_interpretation(analysis_results)
            
            if interpretation:
                SessionRepository.set_interpretation_text(interpretation)
                st.success("Interpretation generated successfully!")
            else:
                st.error("Failed to get interpretation. Please try again.")
        except VNGError as e:
            st.error(f"Error getting interpretation: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")

