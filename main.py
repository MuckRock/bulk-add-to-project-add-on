from documentcloud.addon import SoftTimeOutAddOn
from documentcloud.constants import BULK_LIMIT
from documentcloud.toolbox import grouper

class ProjectAdder(SoftTimeOutAddOn):
    """DocumentCloud Add-On that adds a query of documents to a project"""
    def main(self):
        project = self.client.projects.get(self.data.get("project_id"))
        for doc_group in grouper(self.get_documents(), BULK_LIMIT):
            for document in doc_group:
                if document not in project.document_list:
                    project.document_list.append(document)
                    print(project.document_list)
            project.save()

if __name__ == "__main__":
    ProjectAdder().main()
