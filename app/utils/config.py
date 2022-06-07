import os
from typing import Optional
from dotenv import load_dotenv


class Config:
    @staticmethod
    def arquivo_vazio() -> bool:
        return os.stat('.env').st_size == 0


    @staticmethod
    def limpar() -> None:
        open('.env', 'w').close()


    @staticmethod
    def set(hash:str, valor:str):
        if Config.get(hash) is None:
            with open('.env', 'a') as f:
                f.write(f'{hash.upper()}={valor}' + '\n')


    @staticmethod
    def get(hash:str) -> Optional[str]:
        load_dotenv()
        return os.getenv(hash.upper())
