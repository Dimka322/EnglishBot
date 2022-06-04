import asyncio
from utils.db_api.postgresql import Database
# import pymorphy2
# import nltk
# nltk.download('wordnet')
import re
from states import All_State
from loader import db

# lemmatizer = WordNetLemmatizer()
# dictator = {}

# questions = ['брюшной', 'поглощать','поглощение','ускорять','ускорение','акцент','накапливать','накопление','точность']


# рекурсия, входит массив


loop = asyncio.get_event_loop()
db = Database(loop)


q1 = loop.run_until_complete(db.get_sen_test_errors(481103612))
rus_errors = loop.run_until_complete(db.get_rus_test_error(481103612))
def_errors = loop.run_until_complete(db.get_def_test_error(481103612))
sen_errors = loop.run_until_complete(db.get_sen_test_errors(481103612))
eng_errors = loop.run_until_complete(db.get_eng_test_error(481103612))
err = []
print(list(set(rus_errors.split(','))))
print(rus_errors.split(','))
# if not def_errors: print(def_errors)
print(sen_errors)
print(eng_errors)