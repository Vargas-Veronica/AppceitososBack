from django.db.models.signals import post_migrate
from django.core.management import call_command
from django.dispatch import receiver

@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    """
    Carga automáticamente las fixtures después de las migraciones.
    """
    if sender.name == "ecommerce": 
        try:
            print("Cargando datos iniciales para la aplicación 'ecommerce'...")
            call_command('loaddata', 'initial_data.json')
            print("Datos iniciales cargados con éxito.")
        except Exception as e:
            print(f"Error al cargar los datos iniciales para 'ecommerce': {e}")
