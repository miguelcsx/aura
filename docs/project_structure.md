# AURA Project Structure

The Aura project follows a structured and modular approach to organize the codebase, resources, and documentation. It utilizes a layered architecture to separate concerns and promote maintainability.
Here's the detailed breakdown of the project structure:

```bash
aura/
│
├── docs/                   # Documentation files
│   └── design_document.md  # Design documentation
│
├── src/                    # Source code
│    ├── app/                # Package for AURA application
│    │   ├── business/       # Business Layer
│    │   │   ├── models/     # Domain models
│    │   │   │   └── user.py # User domain model
│    │   │   └── services/   # Business services
│    │   │       └── user_service.py # User service
│    │   │
│    │   ├── database/       # Database Layer
│    │   │   ├── db.py       # Database connection and session management
│    │   │   └── models/     # Database models
│    │   │       └── user_model.py # User database model
│    │   │
│    │   ├── discord/        # Discord Bot Package
│    │   │   ├── bot.py      # Discord bot initialization and setup
│    │   │   ├── commands/   # Discord bot commands
│    │   │   └── events/     # Discord bot event handlers
│    │   │
│    │   ├── __init__.py     # Package initialization file
│    │   ├── main.py         # Entry point of the application
│    │   │
│    │   ├── persistence/    # Persistence Layer
│    │   │   ├── mappers/    # Mapping between domain models and database models
│    │   │   │   └── user_mapper.py # User model mapper
│    │   │   └── repositories/ # Data access and persistence operations
│    │   │       └── user_repository.py # User repository
│    │   │
│    │   ├── presentation/   # Presentation Layer
│    │   │   ├── controllers/  # Controllers for handling user inputs and interactions
│    │   │   │   └── user_controller.py # User controller
│    │   │   └── views/      # User interface components
│    │   │       └── user_view.py # User view
│    │   │
│    │   └── wikipedia/      # Wikipedia Scraping Package
│    │       └── scraper.py  # Wikipedia scraping module
│    │
│    ├── config/             # Configuration files
│    ├── data/               # Data files and resources
│    │   └── db/             # Directory for database files
│    ├── resources/          # Miscellaneous resources (e.g., images, icons)
│    ├── scripts/            # Utility scripts
│    └── tests/              # Unit tests
│        └── __init__.py     # Package initialization file
│
├── README.md               # Project README file
├── LICENSE                 # Project license file
├── setup.py                # Setup script for packaging the application
├── requirements.txt    # Project dependencies
└── .env                    # Project secrets
```

## Root Directory

- **aura/**: The root directory contains the main components of the project.

## Subdirectories

### docs/

- **requirements.txt**: This file list all the Python packages dependencies required by the project. It is used to install the necessary packages and libraries.

- **design-document.md**: This file contains the design documentation for the AURA application. It outlines the architectural decisions, data flow, and other design considerations.

### src/

- **app/**: This Python package contains the core application code for AURA, organized into layers and modules.
    - **business/**: This directory contains the Business Layer components.
        - **models/**: This directory holds the domain models used in the business logic.
        - **services/**: This directory includes the business services and related logic.
    - **database/**: This directory contains the Database Layer components.
        -**models/**: This directory holds the database models and schemas.
    - **discord/**: This directory contains the Discord Bot Package components.
        - **commands/**: This directory holds the Discord bot command handlers.
        - **events/**: This directory contains the Discord bot event handlers.
    - **persistence/**: This directory contains the Persistence Layer components.
        - **mappers/**: This directory holds the mapper classes and functions used for mapping between domain models and database models.
        - **repositories/**: This directory includes the repository classes responsible for data access and persistence operations.
    - **presentation/**: This directory contains the Presentation Layer components.
        - **controllers/**: This directory houses the controller classes responsible for handling user inputs and interactions with the application.
        - **views/**: This directory holds the user interface components.
    - **wikipedia/**: This directory contains the Wikipedia Scraping Package components.
    - **main.py**: This is the entry point of the AURA application. It serves as the main script that launches the application.

- **config/**: This directory is intended to store configuration files and settings for the AURA application.

- **data/**
    - **db/**: This directory is designated to store the SQLite database file(s) used by the application.

- **resources/**: This directory holds miscellaneous resources used by the AURA application, such as image files, icons, or other assets.

- **scripts/**: This directory is designated for utility scripts that may be required for various tasks, such as data processing, deployment, or any other ancillary operations.

- **tests/**: This directory contains the unit test for the AURA application code.


### Other Files

- **README.md**: This Markdown file provides an overview of the AURA project, including its purpose, features, and instructions for installation and usage.
- **LICENSE**: This file contains the license information for the AURA project, specifying the terms and conditions under which the software can be used, modified, and distributed.
- **setup.py**: This Python script is used for packaging and distributing the AURA application. It includes metadata and instructions for creating an installable package.
