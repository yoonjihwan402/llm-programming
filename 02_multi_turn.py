from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.9
    )
    return response.choices[0].message.content

def turn(turn_type="single"):
    conversation_history = []

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("Exiting the chat.")
            break
        if turn_type == "single":
            messages = [
                {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},
                {"role": "user", "content": user_input}
            ]
        elif turn_type == "multi":

            if not conversation_history:
                conversation_history.append({"role": "system", "content": "너는 사용자를 도와주는 상담사야."})
            conversation_history.append({"role": "user", "content": user_input})
            messages = conversation_history

        assistant_response = get_response(messages)

        print("Assistant:", assistant_response)

        if turn_type == "multi":
            conversation_history.append({"role": "assistant", "content": assistant_response})

print("Choose mode: 'single' or 'multi' ")
mode = input("Enter mode: ").strip().lower()
if mode in ["single", "multi"]:
    turn(turn_type=mode)
else:
    print("Invalid mode. Please restart and choose 'single' or 'multi'.")