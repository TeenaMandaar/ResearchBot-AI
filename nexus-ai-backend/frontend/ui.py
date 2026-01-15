import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="ResearchBot AI", page_icon="🧠")
st.title("🧠 ResearchBot: Friendly Assistant")

# Step 1: Initialize Session State
# We need to make sure these variables exist before we use them
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

# Step 2: Sidebar for Memory Controls
with st.sidebar:
    st.header("Memory Controls")
    
    # Button to clear history and start over
    if st.button("🔥 Start New Chat"):
        st.session_state.session_id = None
        st.session_state.messages = []
        st.rerun()
    
    # Text box to load an old conversation
    session_input = st.text_input("📂 Load Session ID:", value="")
    
    if st.button("Load"):
        if session_input.isdigit():
            # Convert text to number and save it
            st.session_state.session_id = int(session_input)
            st.session_state.messages = [] # Clear screen for the new chat
            st.success(f"Switched to Session {session_input}")
            
    # Show current session ID if it exists
    if st.session_state.session_id:
        st.write(f"🟢 Active Session: **{st.session_state.session_id}**")

# Step 3: Show previous messages
for message in st.session_state.messages:
    # Check who sent the message (user or assistant)
    role = message["role"]
    content = message["content"]
    
    with st.chat_message(role):
        st.markdown(content)

# Step 4: Handle new user input
prompt = st.chat_input("What is on your mind?")

if prompt:
    # Show the user's message immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Save user message to the local list
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call the Backend API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Prepare data to send to FastAPI
                api_url = "http://127.0.0.1:8000/chat"
                my_payload = {
                    "query": prompt,
                    "session_id": st.session_state.session_id
                }
                
                # Send the request
                response = requests.post(api_url, json=my_payload)
                
                if response.status_code == 200:
                    data = response.json()
                    ai_answer = data["response"]
                    new_id = data["session_id"]
                    
                    # Update the Session ID
                    st.session_state.session_id = new_id
                    
                    # Show the answer
                    st.markdown(ai_answer)
                    
                    # Save AI message to the local list
                    st.session_state.messages.append({"role": "assistant", "content": ai_answer})
                    
                else:
                    st.error(f"Server Error: {response.text}")
                    
            except Exception as e:
                st.error(f"Connection Failed: {e}")