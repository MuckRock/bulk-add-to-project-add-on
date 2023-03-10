from documentcloud.addon import AddOn, SoftTimeOutAddOn

class ProjectAdder(AddOn):
    """DocumentCloud Add-On that adds a query of documents to a project"""

    def main(self):
        project_id = self.data.get("project_id")
        
        for document in self.get_documents():
          
if __name__ == "__main__":
    ProjectAdder().main()
