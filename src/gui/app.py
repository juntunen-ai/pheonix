import streamlit as st

def main():
    st.title("Phoenix Financial Analysis")
    st.write("A LangGraph AI application for financial data analysis")
    
    st.header("Natural Language Query")
    user_query = st.text_input("Enter your financial data question:")
    
    if user_query:
        st.info("Query processing will be implemented in future versions.")
        
        # Placeholder for visualization
        st.header("Results")
        st.write("Visualization will appear here.")
    
    st.sidebar.header("About")
    st.sidebar.write("This application uses LangGraph to analyze financial data from BigQuery.")
    st.sidebar.write("It enables natural language queries and visualizations of government budget data.")

if __name__ == "__main__":
    main()