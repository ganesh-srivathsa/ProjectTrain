# Step 1: Create a multiline string template
template = """You are a patient Python tutor.
Explain {topic} for a beginner.
Give one example in at most {limit} words."""

# Step 2: Replace the placeholders with actual values
prompt = template.format(topic="for loops", limit=40)

# Step 3: Print the final prompt
print(prompt)