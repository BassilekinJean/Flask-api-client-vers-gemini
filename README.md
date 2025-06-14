# Flask-api-client-vers-gemini
une api backend permettant de communiquer avec gemini  

MODE D'EMPLOI 

  
créer un environement virtuel python :

    python3 -m venv venv
ou vous utilisez la commande que vous maitrisez 


activer le :

    source ~/venv/bin/activate

cloner le repository :

    git clone https://github.com/BassilekinJean/Flask-api-client-vers-gemini.git

installer l'environnement :

    pip install -r requirements.txt

créer un fichier .env dans le dossier racine tel quel :

          FLASK_APP=run.py
          FLASK_ENV=development
          GEMINI_API_KEY=VOTRE CLE API

lancez l'application avec la commande depuis le répertoire /app:

    python3 app.py

Test sur Postman :
  url :
  
    http://127.0.0.1:5000
  méthode :

    POST

  format de la requete en JSON:

      {"user_input": "votre message"}
