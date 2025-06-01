PYTHON := python3
PIP := pip3
TRAIN_SCRIPT := train.py
PREDICT_SCRIPT := predict.py
PLOT_SCRIPT := plot.py
EVAL_SCRIPT := evaluate.py
DATA_FILE := data.csv
THETAS_FILE := thetas.json
REQ_FILE := requirements.txt

all: fclean setup train predict

setup:
	@echo "📦 Installation des dépendances Python..."
	@$(PIP) install --upgrade pip
	@$(PIP) install -r $(REQ_FILE)

train:
	@echo "🚀 Entraînement du modèle..."
	@$(PYTHON) $(TRAIN_SCRIPT)

predict:
	@echo "🔍 Lancement du script de prédiction..."
	@$(PYTHON) $(PREDICT_SCRIPT)

plot:
	@echo "📊 Affichage du graphique des données et de la régression..."
	@$(PYTHON) $(PLOT_SCRIPT)

evaluate:
	@echo "📈 Évaluation de la précision du modèle..."
	@$(PYTHON) $(EVAL_SCRIPT)

clean:
	@echo "🧹 Suppression des fichiers générés..."
	@rm -f $(THETAS_FILE)

fclean: clean

.PHONY: all train predict plot evaluate clean fclean
