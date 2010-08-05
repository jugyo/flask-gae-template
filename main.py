import sys
sys.path.append('lib')

from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)
