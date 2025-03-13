import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

project_name = 'rufusAgent'

list_of_files = [
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'data/raw/.gitkeep',
    'data/processed/.gitkeep',
    '.env',
    'notebooks/exploration.ipynb',
    'notebooks/web_scraping_tests.ipynb',
    'tests/test_crawler.py',
    'tests/test_api.py',
    'tests/test_nlp.py',
    f'src/__init__.py',
    f'src/rufus_crawler.py',
    f'src/rufus_nlp.py',
    f'src/rufus_api.py',
    f'src/rufus_formatter.py',
    f'src/config.py',
    f'src/logger.py',
    f'scripts/run_spider.py',
    f'scripts/run_api.py',
    f'config/config.yaml',
    'template.py',
    'docker-compose.yml',
    'deployment/k8s/.gitkeep',
    'deployment/cloud_run.yaml',
    'deployment/aws_lambda.py',
    'deployment/heroku.yml'
    f'docs/README.md',
    f'docs/Rufus_API_Docs.md',
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {filedir} for the file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Created empty file: {filename} in the directory: {filedir}')
    else:
        logging.info(f'File: {filename} already exists in the directory: {filedir}')
