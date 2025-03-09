# Discord Username Availability Checker

### ![English](https://flagcdn.com/20x15/gb.png) English

A Python script to check the availability of a list of usernames via HTTP POST requests to an API. It manages rate limiting, interacts with the user to stop or continue the process, and displays results in a user-friendly way. 😊

### Features
- **Automated Username Testing:** Sends HTTP POST requests to check if a username is available.
- **Rate Limit Handling:** Detects rate limits and waits before retrying.
- **Interactive User Choice:** Allows the user to stop the process upon finding an available username.
- **Detailed Logging:** Displays results for each tested username.
- **Easy Customization:** Modify headers, API URL, or username list as needed.

### Installation & Usage
#### 1️⃣ Install Required Dependencies
Ensure you have `requests` installed:
```bash
pip install requests
```

2️⃣ Configure the Script
Modify the `headers`, `url`, and `usernames` list inside the script.

3️⃣ Run the Script
```bash
python discord_username_checker.py
```

  <hr>
  
### ![Français](https://flagcdn.com/20x15/fr.png) Français

Un script Python permettant de tester la disponibilité d'une liste de noms d'utilisateur via des requêtes HTTP POST envoyées à une API. Il gère les limitations de taux, interagit avec l'utilisateur pour arrêter ou continuer le processus, et affiche les résultats de manière conviviale. 😊

### Features
- **Test automatisé des noms d'utilisateur :** Envoie des requêtes HTTP POST pour vérifier la disponibilité.
- **Gestion des limitations de taux :** Détecte les restrictions et attend avant de réessayer.
- **Interaction avec l'utilisateur :** Permet d'arrêter le script si un nom disponible est trouvé.
- **Journalisation détaillée :** Affiche les résultats pour chaque nom testé.
- **Personnalisation facile :** Modifiez les en-têtes, l'URL de l'API ou la liste des noms selon vos besoins

### Installation & Utilisation
#### 1️⃣ Installer les dépendances nécessaires
Assurez-vous d'avoir `requests` installé :
```bash
pip install requests
```

2️⃣ Configurer le script
Modifiez les `headers`, `url`, et la liste `usernames` dans le script.

3️⃣ Exécuter le script
```bash
python discord_username_checker.py
```

