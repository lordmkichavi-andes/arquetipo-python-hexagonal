# arquetipo-python-hexagonal

pip install -r requirements.txt
pytest --cov=domain --cov=application --cov=infrastructure --cov=presentation --cov-report=term-missing
python presentation/app.py
docker-compose up --build
