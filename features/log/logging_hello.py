"""
Logger：

控制日志产生、级别和事件是否传播

Handler：

负责输出，控制输出级别和过滤器

Formatter：

控制输出格式（文本 / JSON / 占位符风格）

Filter：

可选，用于更精细筛选事件

               ┌───────────────────┐
               │       Root        │  <- root logger
               │ level, handlers   │
               └───────────────────┘
                         ▲
          propagate=True │
                         │
          ┌──────────────┴──────────────┐
          │           Logger            │  <- 子 Logger（按模块名层级）
          │ name, level, handlers,      │
          │ propagate, disabled         │
          └──────────────┬──────────────┘
                         │
                         │
                 ┌───────┴─────────────┐
                 │      Handler        │  <- 输出器
                 │ level, formatter    │
                 │ flush/close, filter │
                 └──────────┬──────────┘
                            │
                            ▼
                       输出到目的地（stdout/file/socket）

                      Formatter
                      fmt, datefmt, style
"""

import logging
import sys
import requests
# import panel
print(logging.Logger.manager.loggerDict)