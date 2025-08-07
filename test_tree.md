codellama_python_ai_project/
├── data/
│   ├── raw_docs/
│   │   ├── python_docs_latest/  # Cloned or downloaded latest Python documentation
│   │   ├── library_docs/         # Documentation for specific Python libraries
│   │   └── code_examples/        # Curated code examples
│   ├── processed_data/
│   │   ├── train_data.jsonl      # Formatted dataset for training (prompt-completion pairs)
│   │   ├── validation_data.jsonl # Formatted dataset for validation
│   │   └── test_data.jsonl       # Formatted dataset for evaluation
│   └── data_processing_scripts/
│       ├── doc_parser.py         # Script to parse raw documentation
│       ├── data_formatter.py     # Script to format data into JSONL
│       └── data_cleaner.py       # Script for data cleaning and preprocessing
├── models/