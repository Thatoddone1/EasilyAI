import google.generativeai as googleai
from easilyai.exceptions import (
    AuthenticationError, RateLimitError, InvalidRequestError,
    APIConnectionError, NotFoundError, ServerError, MissingAPIKeyError
)

class GeminiService:
    def __init__(self, apikey, model):
        if not apikey:
            raise MissingAPIKeyError(
                "Gemini API key is missing! Please provide your API key when initializing the service. "
                "Refer to the EasyAI documentation for more information."
            )
        googleai.configure(api_key=apikey)
        self.model = googleai.GenerativeModel(model)

    def generate_text(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response['choices'][0]['message']['content']
        except Exception as e:
            raise ServerError(
                f"Unkown error occurred! 😱 Please try again later or look at the EasilyAi Docs. Error: {e}"
            )
        