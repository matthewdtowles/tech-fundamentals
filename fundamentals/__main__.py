import sys

from .cli import main
from .paths import Paths

sys.exit(main(sys.argv[1:], Paths.default()))
