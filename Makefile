PYTHON := python3
VENV := venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python
TRAIN_SCRIPT := train.py
PREDICT_SCRIPT := predict.py
PLOT_SCRIPT := plot.py
EVAL_SCRIPT := evaluate.py
DATA_FILE := data.csv
THETAS_FILE := thetas.json
REQ_FILE := requirements.txt

all: clean setup train predict

setup: $(VENV)/bin/activate

$(VENV)/bin/activate:
	@echo "🐍 Création de l'environnement virtuel..."
	@$(PYTHON) -m venv $(VENV)
	@echo "📦 Installation des dépendances Python..."
	@$(PIP) install --upgrade pip
	@$(PIP) install -r $(REQ_FILE)

train:
	@echo "🚀 Entraînement du modèle..."
	@$(PY) $(TRAIN_SCRIPT)

predict:
	@echo "🔍 Lancement du script de prédiction..."
	@$(PY) $(PREDICT_SCRIPT)

plot:
	@echo "📊 Affichage du graphique des données et de la régression..."
	@$(PY) $(PLOT_SCRIPT)

evaluate:
	@echo "📈 Évaluation de la précision du modèle..."
	@$(PY) $(EVAL_SCRIPT)

clean:
	@echo "🧹 Suppression des fichiers générés..."
	@rm -f $(THETAS_FILE)
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.pyo' -delete
	@find . -type f -name '*.log' -delete
	@find . -type f -name '.DS_Store' -delete

fclean: clean
	@echo "🧨 Suppression de l'environnement virtuel..."
	@rm -rf $(VENV)

.PHONY: all train predict plot evaluate clean fclean
