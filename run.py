import argparse
import os
from dotenv import load_dotenv
import uvicorn

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev",action="store_true", help="Run the server in development mode.")  # 開發環境
    parser.add_argument("--prod",action="store_true", help="Run the server in production mode.")  # 生產環境
    parser.add_argument("--test",action="store_true", help="Run the server in testing mode.")  # 測試環境

    args = parser.parse_args()

    if args.prod:
        load_dotenv("setting/.env.prod")
    elif args.test:
        load_dotenv("setting/.env.test")
    else:
        load_dotenv("setting/.env.dev")

    uvicorn.run("main:app", host="0.0.0.0" , port=int(os.getenv("PORT")) , reload=bool(os.getenv("RELOAD")) )