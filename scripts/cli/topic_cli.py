# scripts/cli/topic_cli.py

from app.database.db import create_tables
from app.presentation.views.topic_view import TopicView

def run_topic_cli():

    # Create the tables in the database
    create_tables()

    topic_view = TopicView()

    while True:
        print("\nAura Topic Management")
        print("1. Create topic")
        print("2. Get topic by id")
        print("3. Get topics by subject id")
        print("4. Get all topics")
        print("5. Update topic")
        print("6. Delete topic")
        print("7. Delete topic by subject id")
        print("0. Exit")

        choice = input("Enter choice (0-7): ")

        if choice == "1":
            topic_view.create_topic()
        elif choice == "2":
            topic_view.get_topic_by_id()
        elif choice == "3":
            topic_view.get_topics_by_subject_id()
        elif choice == "4":
            topic_view.get_all_topics()
        elif choice == "5":
            topic_view.update_topic()
        elif choice == "6":
            topic_view.delete_topic()
        elif choice == "7":
            topic_view.delete_topics_by_subject_id()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_topic_cli()