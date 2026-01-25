import logging

# 1. % 风格（默认）
fmt_percent = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
formatter_percent = logging.Formatter(fmt=fmt_percent)
logger1 = logging.getLogger("percent")
logger1.setLevel(logging.INFO)
handler1 = logging.StreamHandler()
handler1.setFormatter(formatter_percent)
logger1.addHandler(handler1)
logger1.info("Hello % style")

# 2. { } 风格
fmt_brace = "{asctime} [{levelname}] 啦啦啦 {name}: {message}"
formatter_brace = logging.Formatter(fmt=fmt_brace, style="{")
logger2 = logging.getLogger("brace")
logger2.setLevel(logging.INFO)
handler2 = logging.StreamHandler()
handler2.setFormatter(formatter_brace)
logger2.addHandler(handler2)
logger2.info("Hello {} style")

# 3. $ 风格
from string import Template
fmt_dollar = "${asctime} [${levelname}] ${name}: ${message}"
formatter_dollar = logging.Formatter(fmt=fmt_dollar, style="$")
logger3 = logging.getLogger("dollar")
logger3.setLevel(logging.INFO)
handler3 = logging.StreamHandler()
handler3.setFormatter(formatter_dollar)
logger3.addHandler(handler3)
logger3.info("Hello $ style")
