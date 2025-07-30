---
### Structure

/codellama_python_ai_project
├── /data
│   ├── /raw_docs
│   │   ├── python_docs_latest/  # Cloned or downloaded latest Python documentation
│   │   ├── library_docs/         # Documentation for specific Python libraries
│   │   └── code_examples/        # Curated code examples
│   ├── /processed_data
│   │   ├── train_data.jsonl      # Formatted dataset for training (prompt-completion pairs)
│   │   ├── validation_data.jsonl # Formatted dataset for validation
│   │   └── test_data.jsonl       # Formatted dataset for evaluation
│   └── /data_processing_scripts
│       ├── doc_parser.py         # Script to parse raw documentation
│       ├── data_formatter.py     # Script to format data into JSONL
│       └── data_cleaner.py       # Script for data cleaning and preprocessing
├── /models
│   ├── /base_models
│   │   └── codellama-7b-hf/       # Downloaded CodeLlama base model (e.g., from Hugging Face)
│   ├── /checkpoints
│   │   ├── checkpoint_epoch_1/  # Saved model checkpoints during fine-tuning
│   │   └── checkpoint_epoch_N/
│   └── /fine_tuned_models
│       └── codellama_python_expert/ # The final fine-tuned model
├── /notebooks
│   ├── 01_data_exploration.ipynb   # Exploratory Data Analysis (EDA) of raw documentation
│   ├── 02_data_preparation.ipynb   # Steps for data processing and formatting
│   ├── 03_model_selection.ipynb    # Experiments with different model architectures or fine-tuning techniques
│   └── 04_model_evaluation.ipynb   # Analysis of model performance and results
├── /src
│   ├── /fine_tuning
│   │   ├── train.py                # Script for fine-tuning the CodeLlama model
│   │   └── config.py               # Configuration file for fine-tuning parameters
│   ├── /inference
│   │   ├── inference.py            # Script for running inference with the fine-tuned model
│   │   └── prompt_engineering.py   # Helper functions for crafting effective prompts
│   ├── /utils
│   │   └── helpers.py              # General utility functions
│   └── requirements.txt            # List of required Python packages and their versions
├── /docs
│   ├── README.md                   # Project overview, installation instructions, and usage
│   ├── project_plan.md             # Detailed project plan and objectives
│   └── model_card.md               # Documentation of the fine-tuned model's capabilities and limitations
├── .gitignore                      # Specifies files and folders to ignore in version control
└── environment.yml                 # Conda or other environment configuration file
---