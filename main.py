from documentcloud.addon import AddOn, SoftTimeOutAddOn
from documentcloud.constants import BULK_LIMIT
from documentcloud.toolbox import grouper
import time

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

class ProjectAdder(AddOn):
    """DocumentCloud Add-On that adds a query of documents to a project"""
    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def add_to_project(self, project, docs_to_add_to_project):
        project.add_documents(docs_to_add_to_project)
        
    def main(self):
        project = self.client.projects.get(self.data.get("project_id"))
        for doc_group in grouper(self.get_documents(), 100):
            docs_to_add = [] 
            for document in doc_group:
                if document is not None:
                    docs_to_add.append(document)
            self.add_to_project(project, docs_to_add)
            time.sleep(30)

if __name__ == "__main__":
    ProjectAdder().main()
