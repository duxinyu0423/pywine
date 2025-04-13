import logging
import sys
import os
import io
from pathlib import Path

# 创建日志文件
log_path = Path(os.path.expanduser(r"source/pywine/pywine.log"))
if log_path.exists():
    os.remove(log_path)
Path.mkdir(log_path.parents[0], parents=True, exist_ok=True)

# 创建文件处理器，将日志保存到 pywine.log 文件中
file_handler = logging.FileHandler(log_path)
# 创建流处理器，将日志输出到命令行
stream_handler = logging.StreamHandler(sys.stderr)
# 创建流处理器，将日志输出到StringStream中
string_stream = io.StringIO()
string_stream_handler = logging.StreamHandler(string_stream)

# 创建格式化器，定义日志消息的格式
formatter = logging.Formatter('%(asctime)s %(levelname)-3s ==> %(message)s')

# 将格式化器应用到三个处理器
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
string_stream_handler.setFormatter(formatter)

# 获取根记录器并添加三个处理器
logger = logging.getLogger("pywine.log")
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.addHandler(string_stream_handler)
logger.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.DEBUG)
string_stream_handler.setLevel(logging.DEBUG)