import logging

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SCHEDULER_MODEL = 'django-rate'
SCHEDULER_MODEL = 'sqlalchemy-rate'


def main():
    req = requests.get(url='http://127.0.0.1:8000/{}/'.format(SCHEDULER_MODEL))
    logger.info('status_code={}'.format(req.status_code))
    logger.info('text={}'.format(req.text))


if __name__ == '__main__':
    main()
