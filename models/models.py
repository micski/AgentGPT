from transformers import pipeline

class AIModel:
    def __init__(self):
        # Inicjalizacja modelu do generacji tekstu
        self.pipeline = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

    def generate_response(self, prompt):
        # Generowanie odpowiedzi na podstawie wprowadzonego promptu
        result = self.pipeline(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text']
