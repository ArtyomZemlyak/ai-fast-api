#!/usr/bin/env python
# pip install uvicorn psutil

import uvicorn
import psutil


if __name__ == "__main__":

    uvicorn.run(
        "server:app", host="0.0.0.0", port=2222, workers=psutil.cpu_count(logical=False)
    )  # reload - reload page after change file
