import sys
sys.path.append('vendor')

from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)
