# AURA - Adaptive Utility and Routine Assistant

AURA is an innovative API designed to revolutionize the way students learn. It provides a comprehensive platform where students can access a wide range of educational resources, receive personalized recommendations, and track their progress. AURA is built to enhance the learning experience by offering targeted support, adaptive learning routines, and intelligent assistance.

![Image](resources/images/logo.png)

## Key Features

1. **Unified Learning Hub**: Unified Learning Hub: Access all possible educational resources from a single platform, eliminating the need to juggle multiple tabs or applications. AURA integrates various content types like videos, flashcards, and quizzes to provide a well-rounded learning experience.

2. **Personalized Learning Assistance**: AURA supports students during their learning journey by presenting tailored content, reinforcing knowledge through interactive elements such as videos, flashcards, and questions.

3. **Performance Tracking**: Continuously measures student performance to provide actionable insights and improve recommendations, ensuring an effective learning path.

4. **Question Handling and Support**: When a student has a question, AURA offers a list of related questions to provide immediate assistance. If further help is needed, AURA utilizes a tiered support system:

      - **LLM Support**: If related questions don’t resolve the query, AURA employs a Language Learning Model (LLM) to answer.
      - **Advisor Connection**: If the LLM's response is insufficient, AURA connects the student with an advisor.
      - **Expert Teacher Assistance**: As a last resort, AURA connects the student with a subject matter expert to ensure the question is thoroughly resolved.

5. **Adaptive Learning Pathways**: Monitors student performance across various subjects, offering diverse learning strategies and continuously adapting to improve the student's learning process.

## Usage

To use AURA, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/miguelcsx/aura.git
    ```

2. Install the required dependencies:

    ```bash
    # Change directory to the project folder
    cd aura/
    ```

    ```bash
    pip install -r requirements.txt
    ```

3. Run the main application:

    ```bash
    python -m aura
    ```

## Acknowledgements
-  This project was inspired by the desire to improve educational outcomes through technology.

- Special thanks to the contributors and supporters of this project.

## Support
For questions, issues, or suggestions, please [open an issue](https://github.com/miguelcsx/aura/issues).


## License
This project is licensed under the [MIT License](LICENSE).
