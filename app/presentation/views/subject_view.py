# app/presentation/views/subject_view.py

from app.presentation.controllers.subject_controller import SubjectController
from app.presentation.controllers.user_controller import UserController

class SubjectView:
    def __init__(self):
        self.subject_controller = SubjectController()
        self.user_controller = UserController()

    def create_subject(self):
        name = input("Enter name: ")
        description = input("Enter description: ")
        user_id = int(input("Enter user id: "))
        user = self.user_controller.get_user_by_id(user_id)
        if user:
            subject = self.subject_controller.create_subject(name, description, user.id)
            print(f"Subject created: {subject}")
        else:
            print(f"User with id {user_id} not found")

    def get_subject_by_id(self):
        id = int(input("Enter subject id: "))
        subject = self.subject_controller.get_subject_by_id(id)
        print(f"Subject found: {subject}")

    def get_subjects_by_user_id(self):
        user_id = int(input("Enter user id: "))
        subjects = self.subject_controller.get_subjects_by_user_id(user_id)
        print(f"Subjects found: {subjects}")

    def get_all_subjects(self):
        subjects = self.subject_controller.get_all_subjects()
        print(f"All subjects: {subjects}")

    def update_subject(self):
        id = int(input("Enter subject id: "))
        subject = self.subject_controller.get_subject_by_id(id)
        
        if subject:
            name = input(f"Enter name (press enter to keep previous: {subject.name}): ")
            description = input(f"Enter description (press enter to keep previous: {subject.description}): ")
            user_id_input = input(f"Enter user id (press enter to keep previous: {subject.user_id}): ")

            # Update name if provided
            if name.strip() != "":
                subject.name = name

            # Update description if provided
            if description.strip() != "":
                subject.description = description

            # Update user_id if provided
            if user_id_input.strip() != "":
                user_id = int(user_id_input)
                subject.user_id = user_id
            else:
                user_id = subject.user_id

            user = self.user_controller.get_user_by_id(user_id)
            

            if user:
                updated_subject = self.subject_controller.update_subject(subject)
                print(f"Subject updated: {updated_subject}")
            else:
                print(f"User with id {user_id} not found")
        else:
            print(f"Subject with id {id} not found")


    def delete_subject(self):
        id = int(input("Enter subject id: "))
        subject = self.subject_controller.delete_subject(id)
        print(f"Subject deleted: {subject}")

    def delete_subject_by_user_id(self):
        user_id = int(input("Enter user id: "))
        subject = self.subject_controller.delete_subject_by_user_id(user_id)
        print(f"Subject deleted: {subject}")
