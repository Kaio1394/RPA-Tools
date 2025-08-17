
from app.utils import FileUtils

class ToolsService:
    def __init__(self, fileUtils: FileUtils):
            self.file_utils = fileUtils
            
    def create_rpa_project(self, name_project: str) -> bool:
        try:
            if name_project is None or name_project == "":
                return False
            
            # Creating RPA Directory
            if not self.file_utils.dir_rpa_exists():
                if not self.file_utils.create_rpa_dir():
                    return False
                if not self.file_utils.create_evidence_dir():
                    return False
                if not self.file_utils.create_log_dir():
                    return False
            return True
        except Exception as err:
            return False