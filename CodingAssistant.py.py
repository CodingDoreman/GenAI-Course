import streamlit as st
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage
import os

# Page configuration
st.set_page_config(
    page_title="Code Assistant",
    page_icon="💻",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

# Title and description
st.title("💻 Code Assistant")
st.markdown("Get help with coding questions, debugging, and code improvements!")

# Sidebar for API key and settings
with st.sidebar:
    st.header("Settings")
    
    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        value=st.session_state.api_key,
        help="Enter your Anthropic API key"
    )
    
    if api_key:
        st.session_state.api_key = api_key
    
    model = st.selectbox(
        "Select Model",
        ["claude-sonnet-4-20250514", "claude-3-5-sonnet-20241022", "claude-3-haiku-20240307"],
        index=0
    )
    
    temperature = st.slider("Temperature", 0.0, 1.0, 0.3, 0.1)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("### Features")
    st.markdown("""
    - Code generation
    - Bug fixing
    - Code explanation
    - Code optimization
    - Multiple languages
    """)

# Main chat interface
if not st.session_state.api_key:
    st.warning("⚠️ Please enter your Anthropic API key in the sidebar to start.")
    st.info("Don't have an API key? Get one at: https://console.anthropic.com/")
else:
    # Initialize LangChain ChatAnthropic
    try:
        llm = ChatAnthropic(
            anthropic_api_key=st.session_state.api_key,
            model=model,
            temperature=temperature,
            max_tokens=4096
        )
        
        # Create system prompt for code assistant
        system_prompt = """You are an expert code assistant. Help users with:
        - Writing clean, efficient code
        - Debugging and fixing errors
        - Explaining code concepts
        - Code optimization and best practices
        - Multiple programming languages
        
        Always provide clear explanations and well-formatted code with comments."""
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask me anything about coding..."):
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Create prompt template
                    chat_prompt = ChatPromptTemplate.from_messages([
                        ("system", system_prompt),
                        ("human", "{input}")
                    ])
                    
                    # Create chain
                    chain = chat_prompt | llm
                    
                    # Get response
                    response = chain.invoke({"input": prompt})
                    
                    # Display response
                    st.markdown(response.content)
                    
                    # Add assistant message to chat
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response.content
                    })
        
        # Example prompts
        st.markdown("---")
        st.markdown("### 💡 Example Questions")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Write a binary search function"):
                st.session_state.messages.append({
                    "role": "user",
                    "content": "Write a binary search function in Python"
                })
                st.rerun()
        
        with col2:
            if st.button("Explain list comprehensions"):
                st.session_state.messages.append({
                    "role": "user",
                    "content": "Explain how list comprehensions work in Python"
                })
                st.rerun()
        
        with col3:
            if st.button("Optimize this code"):
                st.session_state.messages.append({
                    "role": "user",
                    "content": "How can I optimize a nested loop that searches for duplicates in a list?"
                })
                st.rerun()
                
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Please check your API key and try again.")