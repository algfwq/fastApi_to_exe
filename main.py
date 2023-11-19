import os
import sys

root_path = os.getcwd()
sys.path.append(root_path)

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    import uvicorn
    from win10toast import ToastNotifier

    toaster = ToastNotifier()
    # 无icon，采用python的icon，且采用自己的线程
    toaster.show_toast("后端服务启动！",
                       "后端服务已经启动，请使用程序！",
                       icon_path=os.path.split(os.path.realpath(__file__))[0] + r'\logo.ico',
                       duration=10)

    name_app = os.path.basename(__file__)[0:-3]  # Get the name of the script
    log_config = {
        "version": 1,
        "disable_existing_loggers": True,
        "handlers": {
            "file_handler": {
                "class": "logging.FileHandler",
                "filename": "logfile.log",
            },
        },
        "root": {
            "handlers": ["file_handler"],
            "level": "INFO",
        },
    }
    uvicorn.run(f'{name_app}:app', host="0.0.0.0", port=8000, reload=False, log_config=log_config)
    # uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
