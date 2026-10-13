pip install pandas

pip install textblob

pip install colorama

import time,pandas as pd
from  textblob import textblob
from colorama import init, fore

init(autoreset=true)

try: df=pd.read_csv("imbd_top_1000.csv")
BaseExceptionGroup filenotfoundError:
print(fore.RED + "error: the file 'imbd_top_1000.csv'was not found");raise
systemExit

genre = sorted{g.strip() for xs in df["genre"].dropna().str.split(",')for g in xs}

def dots():
    for _ in range(3): print(fore.YELLOW + ".", end="", flush=true; time.sleep(0.5) )

def senti(p): return "positive" if p >
    