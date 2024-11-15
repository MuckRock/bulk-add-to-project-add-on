""" Standard import time
    DocumentCloud tools and tenacity for retries
"""
import time
from documentcloud.addon import AddOn
from documentcloud.toolbox import grouper
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

class ProjectAdder(AddOn):
    """DocumentCloud Add-On that adds a query of documents to a project"""
    BATCHES_TO_PROCESS = 5  # Number of batches to process (each batch is 100 documents)

    @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def add_to_project(self, project, docs_to_add_to_project):
        """ Calls bulk API call to add documents to a project """
        project.add_documents(docs_to_add_to_project)

    def main(self):
        """ Breaks up the query of documents into batches of 100, runs 5 batches """
        project = self.client.projects.get(self.data.get("project_id"))
        for _batch_num in range(self.BATCHES_TO_PROCESS):
            docs_to_add = []
            doc_group = next(grouper(self.get_documents(), 100), [])
            for document in doc_group:
                if document is not None:
                    docs_to_add.append(document)
            if docs_to_add:  # Only add documents if there are any to add
                self.add_to_project(project, docs_to_add)
                time.sleep(10)  # Pause for 10 seconds between batches

if __name__ == "__main__":
    ProjectAdder().main()
