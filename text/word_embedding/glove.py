from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
import wget, os
from zipfile import ZipFile

def download_glove(file_name:str,download_dir:str,unzip=True):
    '''
    Params:
        file_name : glove file name ["6B", "42B.300d", "840B.300d", "twitter.27B"]
        unzip : True (unzips the file)
        download_dir : path to download directory
    '''
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(download_dir)
    url = f"https://huggingface.co/stanfordnlp/glove/resolve/main/glove.{file_name}.zip"
    wget.download(url)
    print(f"glove.{file_name}.zip downloaded")

    if unzip == True:
        print(f"Unzipping {download_dir}/glove.{file_name}.zip")
        with ZipFile(f"{download_dir}/glove.{file_name}.zip", 'r') as zf:
            zf.extractall(path=download_dir)
            
    os.chdir(cur_dir)        
    return