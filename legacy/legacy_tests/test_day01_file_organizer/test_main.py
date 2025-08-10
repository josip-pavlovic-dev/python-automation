import logging

# ✅ Postavljamo osnovnu konfiguraciju logovanja –
# svi logger-i (koji nemaju sopstvene Handlere) koristiće ovaj nivo i format
logging.basicConfig(level=logging.INFO)

# ✅ logger1 je tzv. root logger – ako ne prosledimo ime, koristi se "glavni" logger
logger1 = logging.getLogger()

# ✅ logger2 je lokalni logger koji koristi __name__ kao ime (npr. '__main__' ili 'test_main')
logger2 = logging.getLogger(__name__)

# ❗ logger.info() ne vraća string, nego None, jer samo šalje poruku log sistemu
# print(logger1.info(...)) zato ispisuje None
print(logger1.info("Pozdrav iz root-a!", exc_info=True))

# ✅ logger2 šalje log poruku koja se pojavljuje u terminalu jer je level=INFO
logger2.info("Pozdrav iz test fajla!", exc_info=True)
