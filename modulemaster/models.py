from django.db import models

class ModuleMaster(models.Model):
    module_name = models.CharField(max_length=100)
    app_name = models.CharField(max_length=100)
    # Comma-separated list of actions like "create,update,view"
    actions = models.CharField(max_length=100)

    

    def __str__(self):
        return f"{self.module_name} ({self.app_name})"
