from minimalog.minimal_log import MinimalLog
ml = MinimalLog(__name__)
event = 'importing {}'.format(__name__)
print(event)
ml.log_event(event)

DATA_PATH = 'data_src'
DEBUG = True
DOWNLOADS_PATH = 'Downloads'
SUCCESSFUL = True
