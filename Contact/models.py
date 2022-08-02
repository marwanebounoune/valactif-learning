from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# les choix de domaines d'activités des entreprises
SECTEUR_CHOICES = (
    ('Autre', 'Autre'),
    ('SG_AM', 'Société de gestion / Asset management'),
    ('B_L', 'Banque / Leasing'),
    ('P_D', 'Promoteur / Développeur'),
    ('TI','Transaction en immobilier'),
    ('C_EI','Conseil / Expertise en immobilier')
)
# les status qu'un devis peut avoir
STATUT_CHOICES = (
    (u'V', 'validé'),
    (u'NV', 'en cours de traitement')
)
#La classe représentant les devis
class Contacts(models.Model):
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True)
    sujet = models.CharField(max_length=50)
    message = models.TextField(null=True)
    def __str__(self):
        return self.nom