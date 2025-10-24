from dotenv import load_dotenv
import os

def load_env():
    load_dotenv('app/path_to_dot_env')
    print(os.getenv('PATH_TO_DOT_ENV'))
    load_dotenv(os.getenv('PATH_TO_DOT_ENV'))