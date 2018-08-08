from .middleware import TenantMiddleware
from django.conf import settings 
from django.http import Http404
import threading
from django.db import connections


request_cfg = threading.local()

"""
Database selection based on URL variable
Ref: https://djangosnippets.org/snippets/2037/
"""

class MultiDBTenantMiddleware(TenantMiddleware):

    def get_database(self, request):
        """
        The get_database method is implemented for URL pattern  
        '^(?P<db>\w+)/$' For any other pattern, custom implementation of this
        method must be done.  
        """
        db = request.get_full_path().split('/')[1]
        if not settings.DATABASES.get(db):
            raise Http404
        return 


    def process_request(self, request, *args, **kwargs):

        super(MultiDBTenantMiddleware, self).process_request(
                                                request, *args, **kwargs)
        db = self.get_database(request)
        connections[db].set_schema_to_public()
        connections[db].set_tenant(request.tenant)
        request_cfg.db = db


    def process_response( self, request, response ):
        if hasattr(request_cfg, 'db' ):
            del request_cfg.db
        return response



class MultiDBRouter:
    """
    A router to control which applications will be synced,
    depending if we are syncing the shared apps or the tenant apps.
    """

    def db_for_read(self, model, **hints): 
        if hasattr(request_cfg, 'db'):
            return request_cfg.cfg
        return None


    def db_for_write(self, model, **hints):
        if hasattr(request_cfg, 'db'):
            return request_cfg.cfg
        return None