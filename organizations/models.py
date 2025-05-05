from django.db import models
import uuid


class Organization(models.Model):
    organisation_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    organisation_name = models.CharField(max_length=255)
    address = models.TextField()
    industry_type = models.CharField(max_length=100)

    def __str__(self):
        return self.organisation_name
    
    class Meta:
        verbose_name_plural = "1. Organizations"
        
        permissions = [
            ("can_read_organization", "Can read organization"),
            ("can_create_organization", "Can create organization"),
            ("can_update_organization", "Can update organization"),
            ("can_delete_organization", "Can delete organization"),
        ]
        
        
        
