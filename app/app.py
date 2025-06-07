import os
from flask import Flask, request, jsonify # Import jsonify for proper JSON responses
from google import genai
from dotenv import load_dotenv # Assurez-vous d'avoir 'pip install python-dotenv'

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    client = genai.Client(api_key=api_key)
except ValueError as e:
    print(f"Erreur de configuration de l'API : {e}")
    client = None # Si l'API n'est pas configurée, client sera None

app = Flask(__name__)

@app.route('/', methods=['POST']) 
def home():
    if client is None:
        return jsonify({"error": "API client not initialized. Check your API key setup."}), 500

    if request.is_json:
        data = request.get_json()
        user_input = data.get('user_input') # Récupérer 'user_input' de l'objet JSON
    else:
        # Si ce n'est pas du JSON, essaye de récupérer via form (pour compatibilité si besoin)
        user_input = request.form.get('user_input')

    if not user_input:
        return jsonify({"error": "No 'user_input' provided in the request."}), 400

    try:
        ai_response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input
        )
        response_text = ai_response.text
        # Retourner la réponse au format JSON
        return jsonify({"status": "success", "ai_response": response_text})

    except Exception as e:
        print(f"Erreur lors de l'appel à l'API Gemini : {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)