import os
from app.constants import *

class FileUtils:    
    def __init__(self, project_name: str):
        self.path_rpa = PATH_DIR_RPA
        self.base_dir = os.path.join(self.path_rpa, project_name)
    
    def dir_rpa_exists(self) -> bool:
        return os.path.exists(self.path_rpa)
    
    def create_rpa_dir(self):
        os.mkdir(self.path_rpa)
        
    def dir_project_exists(self):
        return os.path.exists(self.base_dir)
    
    def create_log_dir(self):
        os.mkdir(os.path.join(self.base_dir, PATH_DIR_LOGS))
        
    def create_evidence_dir(self):
        os.mkdir(os.path.join(self.base_dir, PATH_DIR_EVIDENCE))