import os

# Folders paths
UTILS_FOLDER_PATH = os.path.dirname(__file__)
ROOT_PROJECT_FOLDER_PATH = os.path.dirname(UTILS_FOLDER_PATH)
IN_FILES_FOLDER_PATH = os.path.join(ROOT_PROJECT_FOLDER_PATH, 'in_files')


DOCUMENTS_FILE_PATH = os.path.join(IN_FILES_FOLDER_PATH, 'big.txt')
STOPWORDS_FILE_PATH = os.path.join(IN_FILES_FOLDER_PATH, 'stopwords.txt')
THESAURUS_FILE_PATH = os.path.join(IN_FILES_FOLDER_PATH, 'thesaurus.txt')
