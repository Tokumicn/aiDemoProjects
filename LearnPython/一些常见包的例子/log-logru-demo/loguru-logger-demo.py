from loguru import logger

# logger.remove() # 删除所有的配置  默认是console
logger.add("log.log", level="ERROR")  # 添加日志到文件 设置日志等级

logger.info("info log")
logger.warning("warn log")
logger.error("error log")
logger.critical("critical log")


@logger.catch()   # 输出捕捉到的错误堆栈上下文
def testError():
    1 / 0

testError()