from openai import OpenAI
 
# Create a client (reads OPENAI_API_KEY from env)
client = OpenAI(api_key="")
 
SYSTEM_PROMPT = """
You are a helpful AI agent.
- Answer clearly and concisely.
- Ask for clarification only when truly needed.
"""
 
def run_agent():
    print("Simple AI agent. Type 'quit' to exit.\n")
 
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"quit", "exit"}:
            print("Agent: Goodbye! 👋")
            break
 
        # Call the LLM via Responses API
        response = client.responses.create(
            model="gpt-5-mini",   # or gpt-4.1-mini, etc.
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
        )
 
        # Convenient helper: output_text aggregates all text output
        agent_reply = response.output_text
        print(f"Agent: {agent_reply}\n")
 
 
if __name__ == "__main__":
    run_agent()
