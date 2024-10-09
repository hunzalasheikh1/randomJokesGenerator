import streamlit as st
import random 



# title for the app
st.title("Random Joke Generator")


# list of jokes to randomly choose from
jokes =[  

"Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the math book look sad? Because it had too many problems.",
    "Why are elevator jokes so classic and good? They work on many levels.",
    "Why don’t skeletons fight each other? They don’t have the guts."

]
# button to generate a random joke
if st.button("Tell me a Joke!"):
    joke = random.choice(jokes)
    st.write(joke)
else:
    st.write("click the button to hear a Joke! ")










