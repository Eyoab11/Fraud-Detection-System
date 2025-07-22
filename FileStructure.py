# setup_project.py
import os

# --- Configuration ---
# Use "." to represent the current directory, so no parent folder is created.
ROOT_DIR = "." 

# List of directories to create
DIRECTORIES = [
    "data/01_raw",
    "data/02_intermediate",
    "data/03_processed",
    "models",
    "notebooks",
    "reports/figures",
    "src"
]

# List of files to create with optional placeholder content
FILES = {
    ".gitignore": None,  # Special content will be added below
    "README.md": "# Improved Fraud Detection System\n\nProject overview and setup instructions will go here.",
    "requirements.txt": "pandas\nnumpy\nscikit-learn\nmatplotlib\nseaborn\nlightgbm\nxgboost\nshap\njoblib\n",
    "notebooks/01_ecommerce_eda_and_preprocessing.ipynb": None,
    "notebooks/02_creditcard_eda_and_preprocessing.ipynb": None,
    "notebooks/03_modelling_and_evaluation.ipynb": None,
    "notebooks/04_model_interpretation_with_shap.ipynb": None,
    "reports/Interim_1_Report.md": "# Interim Report 1",
    "src/__init__.py": None,
    "src/data_processing.py": "# Functions for loading and cleaning data\n",
    "src/feature_engineering.py": "# Functions for creating new features\n",
    "src/modelling.py": "# Functions for training and evaluating models\n"
}

# Content for the .gitignore file
GITIGNORE_CONTENT = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Jupyter Notebook
.ipynb_checkpoints

# Data and Models - often large and not version controlled
# Use .gitkeep to ensure the directories are tracked by git
data/01_raw/*
!data/01_raw/.gitkeep
data/02_intermediate/*
!data/02_intermediate/.gitkeep
data/03_processed/*
!data/03_processed/.gitkeep
models/*
!models/.gitkeep

# IDE settings
.idea/
.vscode/
"""

def generate_structure():
    """Creates the project directory structure in the current folder."""
    print("Creating project structure in the current directory...")

    # Create subdirectories
    for dir_path in DIRECTORIES:
        full_path = os.path.join(ROOT_DIR, dir_path)
        os.makedirs(full_path, exist_ok=True)
        # Create a .gitkeep file in empty directories to ensure git tracks them
        if not os.listdir(full_path):
             with open(os.path.join(full_path, ".gitkeep"), "w") as f:
                pass

    # Create files
    for file_path, content in FILES.items():
        full_path = os.path.join(ROOT_DIR, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, "w", encoding="utf-8") as f:
            if file_path == ".gitignore":
                f.write(GITIGNORE_CONTENT.strip())
            elif content:
                f.write(content.strip() + "\n")
    
    print("\nProject structure created successfully.")
    print("Next steps:")
    print("1. Place your raw CSV files in the 'data/01_raw/' folder.")
    print("2. Initialize a git repository with 'git init'.")


if __name__ == "__main__":
    generate_structure()