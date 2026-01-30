import os

def create_project_structure():
    """
    Creates a project directory structure for a Flask ML application.
    """
    
    # Define the directory structure
    directories = [
        'flask_app',
        'src',
        'src/data',
        'src/model'
    ]
    
    # Define files to create (path: initial content)
    files = {
        'src/data/data_ingestion.py': '# Data Ingestion Module\n',
        'src/data/data_preprocessing.py': '# Data Preprocessing Module\n',
        'src/model/model_building.py': '# Model Building Module\n',
        'src/model/model_evaluation.py': '# Model Evaluation Module\n',
        'src/model/model_registery.py': '# Model Registry Module\n',
        'params.yaml': '# Parameters Configuration\n',
        'setup.py': '# Setup Configuration\n',
        'requirements.txt': '# Project Dependencies\n'
    }
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Create files
    for filepath, content in files.items():
        with open(filepath, 'w') as f:
            f.write(content)

if __name__ == "__main__":
    create_project_structure()