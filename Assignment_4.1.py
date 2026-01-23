# Email Classification using Prompt Engineering Techniques

# Categories
categories = ["Billing", "Technical Support", "Feedback", "Others"]

# Sample emails
emails = [
    "I have not received my bill for this month.",
    "My payment was deducted twice.",
    "I am unable to log into my account.",
    "The application is not opening on my phone.",
    "Your service is very good.",
    "I like the new features in your app.",
    "Please change my registered mobile number.",
    "What are your customer care working hours?",
    "I was charged even after canceling the plan.",
    "The website is very slow today."
]

# -----------------------------
# ZERO-SHOT PROMPTING
# -----------------------------
def zero_shot(email):
    prompt = f"""
Classify the following email into one of the categories:
Billing, Technical Support, Feedback, Others.

Email: "{email}"
"""
    return prompt


# -----------------------------
# ONE-SHOT PROMPTING
# -----------------------------
def one_shot(email):
    prompt = f"""
Example:
Email: "My payment was deducted twice."
Category: Billing

Now classify the following email:
Email: "{email}"
"""
    return prompt


# -----------------------------
# FEW-SHOT PROMPTING
# -----------------------------
def few_shot(email):
    prompt = f"""
Email: "My payment was deducted twice."
Category: Billing

Email: "The app is not opening."
Category: Technical Support

Email: "I love your service."
Category: Feedback

Now classify:
Email: "{email}"
"""
    return prompt


# -----------------------------
# DISPLAY PROMPTS
# -----------------------------
test_email = "I am unable to log into my account."

print("ZERO-SHOT PROMPT:\n")
print(zero_shot(test_email))

print("\nONE-SHOT PROMPT:\n")
print(one_shot(test_email))

print("\nFEW-SHOT PROMPT:\n")
print(few_shot(test_email))
