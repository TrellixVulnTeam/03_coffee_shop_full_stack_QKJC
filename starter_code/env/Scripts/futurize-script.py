#!c:\users\zhuji\desktop\fsnd-master\projects\03_coffee_shop_full_stack\starter_code\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'future==0.17.1','console_scripts','futurize'
__requires__ = 'future==0.17.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('future==0.17.1', 'console_scripts', 'futurize')()
    )
