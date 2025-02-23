from flask import Flask, render_template, request, Response
from models import init_db, save_message, get_chat_history
from ollama import Ollama
import time

app = Flask(__name__, template_folder='.')
init_db()

@app.route('/')
def home():
    return render_template('index.html', messages=get_chat_history())

@app.route('/chat/model', methods=['POST'])
def generate():
    message = request.form.get('message', '')
    chat_handler = Ollama()
    
    def generate_events():
        current_line = []
        
        for chunk in chat_handler.generate_response(message):
            if not chunk.strip():
                continue
                
            current_line.append(chunk)
            combined_text = ''.join(current_line)
            
            if '\n' in chunk:
                lines = combined_text.split('\n')
                for line in lines[:-1]:
                    if line.strip():
                        time.sleep(0.5)
                        yield f"{' '.join(line.strip().split())}\n\n"
                current_line = [lines[-1]]
        
        final_text = ' '.join(''.join(current_line).strip().split())
        if final_text:
            yield f"{final_text}\n\n"

    return Response(generate_events(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True) 
