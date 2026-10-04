from commands.ai import ask_ai
# Imports the JARVIS AI function


question = "What is machine learning? Explain it in 2 simple sentences."
# Gives the AI a simple test question


answer = ask_ai(question)
# Sends the question to Gemini


print("Jarvis AI:", answer)
# Displays the AI response