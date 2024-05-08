from documentcloud.addon import AddOn, SoftTimeOutAddOn
from documentcloud.constants import BULK_LIMIT
from documentcloud.toolbox import grouper

class ProjectAdder(AddOn):
    """DocumentCloud Add-On that adds a query of documents to a project"""
    def main(self):
        project = self.client.projects.get(self.data.get("project_id"))
        print("project document list before adds") 
        print(project.document_list)
        for document in self.get_documents():
            if document not in project.document_list:
                print(f"Adding document {document.id}")
                project.document_list.append(document)
            else: 
                print("Else branch reached")
        project.save()

if __name__ == "__main__":
    ProjectAdder().main()
