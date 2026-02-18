import os
from groq import Groq, APIConnectionError, RateLimitError, APIStatusError, AuthenticationError, PermissionDeniedError, NotFoundError, UnprocessableEntityError, APITimeoutError

def send_ai_request(system: str, user: str, model: str, api_key: str):
    try:
        client = Groq(
            api_key=api_key
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system
                },
                {
                    "role": "user",
                    "content": user
                }
            ],
            model=model,
        )

        return chat_completion.choices[0].message.content
    
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
        return None
    except APITimeoutError as e:
        print(f"Request timed out: {e}")
        return None
    except APIConnectionError as e:
        print(f"Server could not be reached: {e.__cause__}")
        return None
    except AuthenticationError as e:
        print(f"Invalid API key or token: {e.status_code}")
        return None
    except PermissionDeniedError as e:
        print(f"No permission to access this resource: {e.status_code}")
        return None
    except NotFoundError as e:
        print(f"Resource not found: {e.status_code}")
        return None
    except UnprocessableEntityError as e:
        print(f"Request could not be processed (invalid audio?): {e.status_code}")
        return None
    except RateLimitError as e:
        print(f"Rate limit exceeded. Please wait before retrying: {e.status_code}")
        return None
    except APIStatusError as e:
        print(f"Unexpected API error {e.status_code}: {e.message}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None