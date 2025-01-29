from django.apps import AppConfig

class EcommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce'

    def ready(self):
        print("Registrando signals para la app 'ecommerce'...")
        import ecommerce.signals
