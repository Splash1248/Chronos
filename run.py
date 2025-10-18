from flask import Flask, render_template, request, jsonify
import main as core_logic
import os
from dotenv import load_dotenv


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reconstruct', methods=['POST'])
def reconstruct():
    data = request.get_json()

    if not data or 'fragment' not in data:
        return jsonify({'error': 'Missing fragment text in request.'}), 400

    fragment_text = data.get('fragment')


    try:
        reconstructed_text = core_logic.reconstruct_text_with_gemini(GEMINI_API_KEY, fragment_text)
        if "An error occurred" in reconstructed_text:
             return jsonify({'error': reconstructed_text}), 500

        context_links = core_logic.search_for_context(SEARCH_API_KEY, SEARCH_ENGINE_ID, fragment_text)

        response_data = {
            'reconstructed_text': reconstructed_text,
            'context_links': context_links
        }

        return jsonify(response_data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'An internal server error occurred.'}), 500



if __name__ == '__main__':
    app.run(debug=True)