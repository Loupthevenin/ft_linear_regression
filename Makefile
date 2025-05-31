PYTHON := python3
TRAIN_SCRIPT := train.py
PREDICT_SCRIPT := predict.py
DATA_FILE := data.csv
THETAS_FILE := thetas.json

all: fclean train predict

train:
	@echo "🚀 Entraînement du modèle..."
	@$(PYTHON) $(TRAIN_SCRIPT)

predict:
	@echo "🔍 Lancement du script de prédiction..."
	@$(PYTHON) $(PREDICT_SCRIPT)

clean:
	@echo "🧹 Suppression des fichiers générés..."
	@rm -f $(THETAS_FILE)

fclean: clean

.PHONY: all train predict clean fclean
