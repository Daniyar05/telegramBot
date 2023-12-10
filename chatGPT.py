import openai
openai.api_key = "sk-3Y3zheYSCJLkftRjL4GwT3BlbkFJlUAPvUI1V8AdXJBTqXt"
engine="gpt-3.5-turbo-instruct" 

# Модель 


def get_requests(prompt):
    completion = openai.Completion.create(engine=engine, prompt=prompt, 
                                        temperature=0.5, 
                                        max_tokens=1000) 
    return  completion["choices"][0]["text"]

