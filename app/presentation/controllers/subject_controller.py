# app/presentation/controllers/subject_controller.py

from app.business.services.subject_service import SubjectService

class SubjectController:
    def __init__(self):
        self.subject_service = SubjectService()

    def create_subject(self, name, description, user_id):
        return self.subject_service.create_subject(name, description, user_id)
    
    def get_subject_by_id(self, id):
        return self.subject_service.get_subject_by_id(id)
    
    def get_all_subjects(self):
        return self.subject_service.get_all_subjects()
    
    def update_subject(self, id, name, description, user_id):
        return self.subject_service.update_subject(id, name, description, user_id)
    
    def delete_subject(self, id):
        return self.subject_service.delete_subject(id)
    
    def delete_subject_by_user_id(self, user_id):
        return self.subject_service.delete_subject_by_user_id(user_id)
    
    def get_subjects_by_user_id(self, user_id):
        return self.subject_service.get_subjects_by_user_id(user_id)