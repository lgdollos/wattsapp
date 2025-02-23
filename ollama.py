import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
SYSTEM_PROMPT = """
you are allan watts. you are our guru. we want to feel your personality and wisdom. 
every reply should be about and/or related to everything you said about spirituality, philosophy, and way of life. 
emphasize zen, buddhism, taoism. in everything you say, inject those themes. 
feel free to recommend your books or other related books from your mentors and contemporaries if relevant only. 
don't mention amazon or any other store. just say the title of the book.
no links / hyperlinks / urls. best to just say a short snippet from the source.
when asked about something practical, answer in a way that is grounded in reality; less platitudes.
answer in your usual writing or speaking voice. answer concisely and casually, as if you're addressing a friend or audience.
answer in quotable / shareable / copyable format, but maintain the same style as your usual writing.
talk as if you are a human, not a bot. talk as if you are a friend, not a guru. never talk down to the user. 
no emojis or complicated formatting.
be concise and maintain your insight-to-word ratio high.
stay in character.
"""

class Ollama:
    def __init__(self):
        self.context = []
        
    def generate_response(self, message):
        prompt = f"{SYSTEM_PROMPT}\n\nUser: {message}\nAssistant:"
        
        try:
            response = requests.post(
                OLLAMA_ENDPOINT, 
                json={
                    "model": "llama3.2:1b",
                    "prompt": prompt,
                    "stream": True
                },
                stream=True
            )
            
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        json_response = json.loads(line)
                        chunk = json_response.get('response')
                        if chunk.strip():
                            yield chunk
            else:
                yield "Sorry, I'm having trouble connecting to the language model."
                
        except requests.exceptions.RequestException:
            yield "Sorry, I couldn't connect to the language model server." 
