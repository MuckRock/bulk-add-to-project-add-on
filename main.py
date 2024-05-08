from documentcloud.addon import AddOn, SoftTimeOutAddOn
from documentcloud.constants import BULK_LIMIT
from documentcloud.toolbox import grouper

class ProjectAdder(AddOn):
    """DocumentCloud Add-On that adds a query of documents to a project"""
    def main(self):
        project = self.client.projects.get(self.data.get("project_id"))
        for document in self.get_documents():
            if document not in project.document_list:
                project.document_list.append(document)
        project.save()

if __name__ == "__main__":
    ProjectAdder().main()
