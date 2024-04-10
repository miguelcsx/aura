# scripts/cli/subject_cli.py

from app.database.db import create_tables
from app.presentation.views.subject_view import SubjectView

def run_subject_cli():

    # Create the tables in the database
    create_tables()

    subject_view = SubjectView()

    while True:
        print("\nAura Subject Management")
        print("1. Create subject")
        print("2. Get subject by id")
        print("3. Get subjects by user id")
        print("4. Get all subjects")
        print("5. Update subject")
        print("6. Delete subject")
        print("7. Delete subject by user id")
        print("0. Exit")

        choice = input("Enter choice (0-7): ")

        if choice == "1":
            subject_view.create_subject()
        elif choice == "2":
            subject_view.get_subject_by_id()
        elif choice == "3":
            subject_view.get_subjects_by_user_id()
        elif choice == "4":
            subject_view.get_all_subjects()
        elif choice == "5":
            subject_view.update_subject()
        elif choice == "6":
            subject_view.delete_subject()
        elif choice == "7":
            subject_view.delete_subject_by_user_id()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_subject_cli()
