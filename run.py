# 创建应用实例
import sys

from wxcloudrun import app

# 启动Flask Web服务
if __name__ == '__main__':
    from waitress import serve
        serve(app, host=sys.argv[1], port=sys.argv[2])
