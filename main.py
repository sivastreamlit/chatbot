import streamlit as st
import sqlite3
import hashlib
import streamlit_custome_css as siva

siva.header_hide()
siva.bg_image("https://th.bing.com/th/id/OIP.NpwMNKg85cQixL1MiYZ2QAHaE7?w=626&h=417&rs=1&pid=ImgDetMain")
siva.sidebar_bg_image("https://th.bing.com/th/id/OIP.x0QxaKQdPpu2XXlOfU4bfAHaEo?w=2560&h=1600&rs=1&pid=ImgDetMain")
# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# Signup function
def signup(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Login function
def login(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user is not None

# Chatbot categories
def chatbot_dashboard():
    st.sidebar.title("Chatbot Categories")
    options = ["General Chat", "school Bot", "Education Bot", "admission Bot"]
    choice = st.sidebar.selectbox("Select a chatbot category:", options)
    st.write(f"You selected: {choice}")

#you can change the question and answer
    if choice=="General Chat":
        qa_pairs = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there! What can I do for you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name?": "I am a mini chatbot built using Streamlit!",
        "who created you?": "I was created by a developer using Python and Streamlit.",
        "what is streamlit?": "Streamlit is an open-source Python library for creating interactive web apps.",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! 😊"
        }

        st.title("💬School Chatbot")

# Initialize session state for chat history
        if "messages" not in st.session_state:
                st.session_state.messages = []

# Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# User input
        user_input = st.chat_input("Ask me something...")

        if user_input:
    # Store user message
            st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
            response = qa_pairs.get(user_input.lower(), "I'm not sure about that. Can you ask something else?")
    
    # Store bot message
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Display bot response
            with st.chat_message("assistant"):
                st.markdown(response)

#you can change the question and answer
    elif choice=="school Bot":
        qa_pairs = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there! What can I do for you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name?": "I am a mini chatbot built using Streamlit!",
        "who created you?": "I was created by a developer using Python and Streamlit.",
        "what is streamlit?": "Streamlit is an open-source Python library for creating interactive web apps.",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! 😊"
        }

        st.title("💬 Mini Chatbot with Predefined Responses")

# Initialize session state for chat history
        if "messages" not in st.session_state:
                st.session_state.messages = []

# Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# User input
        user_input = st.chat_input("Ask me something...")

        if user_input:
    # Store user message
            st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
            response = qa_pairs.get(user_input.lower(), "I'm not sure about that. Can you ask something else?")
    
    # Store bot message
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Display bot response
            with st.chat_message("assistant"):
                st.markdown(response)

#you can change the question and answer
    elif choice=="Education Bot":
        qa_pairs = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there! What can I do for you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name?": "I am a mini chatbot built using Streamlit!",
        "who created you?": "I was created by a developer using Python and Streamlit.",
        "what is streamlit?": "Streamlit is an open-source Python library for creating interactive web apps.",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! 😊"
        "who is your favourite teacher?":"Dr.K.Maheswaran"    
        }

        st.title("💬 Mini Chatbot with Predefined Responses")

# Initialize session state for chat history
        if "messages" not in st.session_state:
                st.session_state.messages = []

# Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# User input
        user_input = st.chat_input("Ask me something...")

        if user_input:
    # Store user message
            st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
            response = qa_pairs.get(user_input.lower(), "I'm not sure about that. Can you ask something else?")
    
    # Store bot message
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Display bot response
            with st.chat_message("assistant"):
                st.markdown(response)


#you can change the question and answer
    elif choice=="admission Bot":
        qa_pairs = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there! What can I do for you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name?": "I am a mini chatbot built using Streamlit!",
        "who created you?": "I was created by a developer using Python and Streamlit.",
        "what is streamlit?": "Streamlit is an open-source Python library for creating interactive web apps.",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! 😊"
        }

        st.title("💬 Mini Chatbot with Predefined Responses")

# Initialize session state for chat history
        if "messages" not in st.session_state:
                st.session_state.messages = []

# Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# User input
        user_input = st.chat_input("Ask me something...")

        if user_input:
    # Store user message
            st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
            response = qa_pairs.get(user_input.lower(), "I'm not sure about that. Can you ask something else?")
    
    # Store bot message
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Display bot response
            with st.chat_message("assistant"):
                st.markdown(response)












# Main app function
def main():
    #st.title("Signup & Login System with Chatbot Access")
    init_db()
    
    menu = ["Login", "Signup"]
    st.sidebar.title("Menu")
    choice = st.sidebar.radio(" ", menu)
    
    if choice == "Signup":
        st.subheader("Create an Account")
        name=st.text_input("Name",placeholder="Enter your Name")
        new_user = st.text_input("Username",placeholder="Enter your UserName")
        email=st.text_input("Email",placeholder="Enter your Valide Email ID")
        new_password = st.text_input("Password", type="password",placeholder="Password")
        if st.button("Signup"):
            if signup(new_user, new_password):
                st.success("Signup successful! Please login.")
            else:
                st.error("Username already exists. Try another one.")
    
    elif choice == "Login":
        he=st.empty()
        he.subheader("Login to Your Account")
        us=st.empty()
        pa=st.empty()
        che=st.empty()
        
        
        username = us.text_input("Username")
        password = pa.text_input("Password", type="password")
        if che.checkbox("Login"):
            if login(username, password):
                
                us.empty()
                pa.empty()
                che.empty()
                he.empty()
                chatbot_dashboard()
            else:
                st.error("Invalid credentials, please try again.")

if __name__ == "__main__":
    main()
