# AURA Project Structure

The Aura project follows a structured and modular approach to organize the codebase, resources, and documentation.
Here's the detailed breakdown of the project structure:

```bash
aura/
│
├── docs/                   # Documentation files
│   ├── requirements.txt    # Project dependencies
│   └── design_document.md  # Design documentation
│
├── src/                    # Source code
│   ├── app/                # Package for AURA application
│   │   ├── controllers/    # Controllers for handling user inputs and interactions
│   │   ├── models/         # Data models and structures
│   │   ├── services/       # Business logic and service layer
│   │   ├── views/          # User interface components
│   │   ├── __init__.py     # Package initialization file
│   │   └── __main__.py     # Entry point of the application
│   │
│   ├── tests/              # Unit tests
│   └── __init__.py         # Package initialization file
│
├── data/                   # Data files and resources
│
├── config/                 # Configuration files
│   └── settings.py         # Application settings
│
├── scripts/                # Utility scripts
│
├── resources/              # Miscellaneous resources (e.g., images, icons)
│
├── README.md               # Project README file
├── LICENSE                 # Project license file
├── setup.py                # Setup script for packaging the application
└── .env                    # Project secrets
```

## Root Directory

- **aura/**: The root directory contains the main components of the project.

## Subdirectories

### docs/

- **requirements.txt**: This file list all the Python packages dependencies required by the project. It is used to install the necessary packages and libraries.

- **design-document.md**: This file contains the design documentation for the AURA application. It outlines the architectural decisions, data flow, and other design considerations.

### src/

- **app/**: This python package contains the core application code for AURA.
    - **controllers/**: This directory houses the controller classes responsible for handling user inputs and interactions with the application.
    - **models/**: This directory contains the data models and structures used by the application.
    - **services/**: This directory includes the service layer code, which encapsulates the business logic of the application.
    - **views/**: This directory holds the user interface components, such as the Tkinter-based GUI elements.
    - **\__init__.py**: This file marks the `app` directory as a python package and can be used for package initialization.
    - **\__main__.py**: This is the entry point of the AURA application. It serves as the main script that launches the application.
    - **tests/**: This directory contains the unit tests for the AURA application code.
    - **\__init__.py**: This file marks the `src` directory as a python package and can be used for package initialization.

### data/

- This directory is intended to store data files and resources used by the AURA application, such as the user data, learning materials, or any other relevant files.

### config/

- **settings.py**: This python file contains the configuration settings for the AURA application, such as application preferences, paths, or any other configurable options.


### scripts/

- This directory is designated for utility scripts that may be required for various tasks, such as data processing, deployment, or any other ancillary operations.

### resources/

- This directory holds miscellaneous resources used by the AURA application, such as image files, icons, or other assets.

### Other Files

- **README.md**: This Markdown file provides an overview of the AURA project, including its purpose, features, and instructions for installation and usage.
- **LICENSE**: This file contains the license information for the AURA project, specifying the terms and conditions under which the software can be used, modified, and distributed.
- **setup.py**: This Python script is used for packaging and distributing the AURA application. It includes metadata and instructions for creating an installable package.
