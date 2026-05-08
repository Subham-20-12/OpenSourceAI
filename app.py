from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="gpt2"
)

print("AI Started!")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = chatbot(
        user,
        max_length=50
    )

    print(response[0]["generated_text"])
