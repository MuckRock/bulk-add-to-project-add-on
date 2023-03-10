from documentcloud.addon import AddOn, SoftTimeOutAddOn

class ProjectAdder(SoftTimeOutAddOn):
    """DocumentCloud Add-On that adds a query of documents to a project"""
    def main(self):
        project = self.client.projects.get(self.data.get("project_id"))
        for document in self.get_documents():
            if document not in project.document_list:
                project.document_list.append(document)
        project.put()

if __name__ == "__main__":
    ProjectAdder().main()
