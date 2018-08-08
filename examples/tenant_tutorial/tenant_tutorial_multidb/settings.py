from tenant_tutorial.settings import *

DATABASES = {
    'default':{
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'tenant_tutorial',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',   
        'PORT': '',
    },
    'db1': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'tenant_tutorial1',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',   
        'PORT': '',
    },
    'db2': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'tenant_tutorial2',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',   
        'PORT': '',
    }
}

WSGI_APPLICATION = 'tenant_tutorial_multidb.wsgi.application'

DATABASE_ROUTERS += ('tenant_schemas.multidb.MultiDBRouter',)

