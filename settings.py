# Django settings for elarropao project.
import os.path
#from django.conf import settings

PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Leonardo J. Caballero G.', 'leonardocaballero@gmail.com'),
    #('Alexander Olivares', 'olivaresa@gmail.com'),
)

CONTACTO = (
    ('El Arropao', 'arropao@gmail.com'),
)

MANAGERS = ADMINS

DEFAULT_CHARSET = 'utf-8'
DEFAULT_CONTENT_TYPE = 'text/html'

#DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'elarropao.db')           # Or path to database file if using sqlite3.
DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'arropao_elarropao'           # Or path to database file if using sqlite3.
DATABASE_USER = 'arrop_elarropao'             # Not used with sqlite3.
DATABASE_PASSWORD = 'yuE45@_-poOwf#'         # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Caracas'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PATH, 'site_media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't92+mm26j^(3yx#%7z1px5^*svz$gkqb8m1vf5gwkn$^5)60ar'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'emencia.django.newsletter.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'elarropao.urls'

TEMPLATE_DIRS = (
    os.path.join(PATH, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'hitcount',
    'tinymce',
    'filebrowser',
    'tagging',
    'emencia.django.newsletter',
    'elarropao.loteria',
)

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'info@elarropao.com'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

HITCOUNT_KEEP_HIT_ACTIVE = { 'hours': 1}
HITCOUNT_HITS_PER_IP_LIMIT = 0

'''
FILEBROWSER_MEDIA_ROOT = getattr(settings, "FILEBROWSER_MEDIA_ROOT", settings.MEDIA_ROOT)
ups en tu settings.py del PROYECTO yo solo colocaria esto
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
asumiendo que quieres compartir el MEDIA_ROOT en ambos
entiendes el concepto de getattr?
es sencillo
cuando te dicen:
MEDIA_URL = getattr(settings, "FILEBROWSER_MEDIA_URL", settings.MEDIA_URL)
Es equivalente a:
MEDIA_URL = settings.FILEBROWSER_MEDIA_URL
si ese objeto no existe toma por defecto el valor de settings.MEDIA_URL
que es el tercer argumento de la funcion.
'''
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_URL_FILEBROWSER_MEDIA = os.path.join(MEDIA_URL, 'filebrowser/')
FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(MEDIA_ROOT, 'filebrowser/')
FILEBROWSER_URL_TINYMCE = ADMIN_MEDIA_PREFIX + "js/tiny_mce/"
FILEBROWSER_PATH_TINYMCE = ADMIN_MEDIA_PREFIX + "js/tiny_mce/"

'''
Allowed Extensions for File Upload. Please be aware that there are Icons for the default extension settings. If you rename "Audio" to "Music", you also have to rename the Audio-Icon within the img-directory.
'''
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
#    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
#    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p'],
#    'Code': ['.html','.py','.js','.css']
}

'''
Set different Options for selecting elements from the FileBrowser. 
'''
FILEBROWSER_SELECT_FORMATS = {
    'File': ['Folder','Document',],
    'Image': ['Image'],
#    'Media': ['Video','Sound'],
    'Document': ['Document'],
    # for TinyMCE we also have to define lower-case items
    'image': ['Image'],
    'file': ['Folder','Image','Document',],
}

FILEBROWSER_VERSIONS_BASEDIR = '_versions_'

FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (140px)', 'width': 140, 'height': '', 'opts': ''},
    'small': {'verbose_name': 'Small (300px)', 'width': 300, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (460px)', 'width': 460, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (620px)', 'width': 620, 'height': '', 'opts': ''},
    'cropped': {'verbose_name': 'Cropped (60x60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'croppedthumbnail': {'verbose_name': 'Cropped Thumbnail (140x140px)', 'width': 140, 'height': 140, 'opts': 'crop'},
}

FILEBROWSER_ADMIN_VERSIONS = ['thumbnail','small', 'medium','big']
FILEBROWSER_ADMIN_THUMBNAIL = 'fb_thumb'

'''
True to save the URL including MEDIA_URL to your model fields or False (default) to save path relative to MEDIA_URL. 
'''
FILEBROWSER_SAVE_FULL_URL = False

'''
If set to True, then FileBrowser will not try to import a mis-installed PIL. 
'''
FILEBROWSER_STRICT_PIL = False

'''
see http://mail.python.org/pipermail/image-sig/1999-August/000816.html
'''
FILEBROWSER_IMAGE_MAXBLOCK = 1024*1024

'''
 Max. Upload Size in Bytes. 
'''
FILEBROWSER_MAX_UPLOAD_SIZE = 10485760
'''
replace spaces and convert to lowercase 
'''
FILEBROWSER_CONVERT_FILENAME = True
'''
control how many items appear on each paginated browse-list. 
'''
FILEBROWSER_LIST_PER_PAGE = 50
'''
 set the default sorting attribute.
'''
FILEBROWSER_DEFAULT_SORTING_BY = "date"
'''
ordining asc, desc. 
'''
FILEBROWSER_DEFAULT_SORTING_ORDER = "desc"

TINYMCE_SPELLCHECKER = True
TINYMCE_JS_ROOT = "%sjs/tiny_mce/" % MEDIA_URL
TINYMCE_JS_URL = "%sjs/tiny_mce/tiny_mce_src.js" % MEDIA_URL
TINYMCE_COMPRESSOR = False
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "table,spellchecker,paste,searchreplace",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'file_browser_callback': 'myFileBrowser',
}
TINYMCE_FILEBROWSER = True

NEWSLETTER_MEDIA_URL = "%sedn/" % MEDIA_URL

