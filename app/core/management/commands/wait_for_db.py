import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Comnando em Django para a execucao ate a db estar disponivel"""

    def handle(self, *args, **options):
        self.stdout.write('aguardando conexao com a base de dados')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('banco nao disponivel-aguarde 1s...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('banco de dados disponivel!!!'))
