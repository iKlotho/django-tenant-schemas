

class ExampleTenantSyncRouter:
    """
    A router to control which applications will be synced,
    depending if we are syncing the shared apps or the tenant apps.
    """

    def db_for_read(self, model, **hints):
        return 'default1'


    def db_for_write(self, model, **hints):
        return 'default1'


