from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    '''Override the ready method to import the signals module, which will connect the signal handlers.'''
    def ready(self):
        import checkout.signals