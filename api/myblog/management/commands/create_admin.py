from django.contrib.auth.management.commands import createsuperuser
from ...models import mUser
import logging
import os

logging.basicConfig(
    level = logging.DEBUG,
    format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s:%(lineno)s
    %(message)s''')

logger = logging.getLogger(__name__)

class Command(createsuperuser.Command):
    help = 'Create a Superuser'
    DESCRIPTION_FILE = '/description.txt'

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        username = 'admin'
        email = 'admin@gmail.com'
        password = 'admin'
        description = ''
        # description = '1994年生まれの26歳。24歳の時にWebプログラマーになる。\r\nDjangoと機械学習が大好き。\r\n\r\n12歳からギターを始め、高校から作曲を始める。その後音響専門学校に行くが、中退し音楽制作会社へ入社。「ソードアートオンラインコードレジスタ」などの多数のゲームや遊技機音楽制作に携わったのちフリーの作曲家になるが、1年ほどで辞め、探偵事務所に入る。そして2,3年探偵として働いた後、プログラマーに転職する。現在は本業プログラマー土日探偵。'
        database = options.get('database')

        try:
            currentPath = os.path.dirname(os.path.abspath(__file__))
            with open(currentPath + self.DESCRIPTION_FILE, encoding='utf-8') as f:
                description = f.read()

            user_data = {
                'username': username,
                'email': email,
                'password': password,
                'description': description
            }

            exists = self.UserModel._default_manager.db_manager(database).filter(username=username).exists()
            if not exists:
                self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)

        except Exception as e:
            logger.error(e)
