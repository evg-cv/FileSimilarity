import os

from utils.folder_file_manager import make_directory_if_not_exists


CUR_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(CUR_DIR, 'utils', 'model', 'pruned.word2vec.txt')
OUTPUT_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'output'))

INPUT_EXCEL_PATH = ""
SIMILARITY_THRESH = 0.3
SIMILARITY_NUMBER = 3
