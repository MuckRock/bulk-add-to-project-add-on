from documentcloud.addon import AddOn, SoftTimeOutAddOn
from documentcloud.constants import BULK_LIMIT
from documentcloud.toolbox import grouper
import time

class ProjectAdder(AddOn):
    """DocumentCloud Add-On that adds a query of documents to a project"""
    def main(self):
        project = self.client.projects.get(self.data.get("project_id"))
        for doc_group in grouper(self.get_documents(), 100):
            docs_to_add = [] 
            for document in doc_group:
                if document is not None:
                    docs_to_add.append(document)
            project.add_documents(docs_to_add)

if __name__ == "__main__":
    ProjectAdder().main()
