import asyncio

import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncpg.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                password=config.PGPASSWORD,
                host=config.ip
            )
        )

    async def create_table_users(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Users(
            id INT NOT NULL,
            Name VARCHAR(255) NOT NULL,
            quantity_words INT,
            results INT,
            PRIMARY KEY(id)) 
        """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, id: int, name: str, previous_quantity: int = 0, results: int = 0, quantity: int = 9):
        sql = "INSERT INTO Users (id,name,previous_quantity,results, quantity_words) VALUES ($1,$2,$3,$4,$5)"
        await self.pool.execute(sql, id, name, previous_quantity, results, quantity)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def get_user_state(self, **kwargs):
        sql = "SELECT * FROM Users WHERE id = $1"
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def get_result(self, id):
        sql = 'SELECT results FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def set_result(self, results, id):
        sql = 'UPDATE Users SET results = $1 WHERE id = $2'
        return await self.pool.execute(sql, results, id)

    async def set_user_state(self, current_state, id):
        sql = "UPDATE Users SET current_state = $1 WHERE id = $2"
        return await self.pool.execute(sql, current_state, id)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Users")

    async def update_user_results(self, results, id):
        sql = "UPDATE Users SET results = $1 WHERE id = $2"
        return await self.pool.execute(sql, results, id)

    async def update_quantity(self, quantity, id):
        sql = 'UPDATE Users SET quantity_words = $1 WHERE id = $2'
        return await self.pool.execute(sql, quantity, id)

    async def update_prev_quantity(self, prev_quantity, id):
        sql = 'UPDATE Users SET previous_quantity = $1 WHERE id =$2'
        return await self.pool.execute(sql, prev_quantity, id)

    async def get_const_quantity(self, id):
        sql = 'SELECT const_quantity FROM Users WHERE id = $1'
        return await self.pool.fetchrow(sql, id)

    async def delete_users(self):
        await self.pool.execute("DELETE FROM Users WHERE True")

    async def create_table_words(self):
        sql = """
                    CREATE TABLE IF NOT EXISTS Words(
                    id SERIAL,
                    word VARCHAR(255) NOT NULL,
                    transcription VARCHAR(255),
                    translate INT,
                    type VARCHAR(255) NOT NULL,
                    definition VARCHAR(255) NOT NULL,
                    theme VARCHAR(255),
                    speech VARCHAR(255),
                    PRIMARY KEY(id)) 
                """
        await self.pool.execute(sql)

    async def add_word(self, id: int, word: str, type: str, definition: str, transcription: str = None,
                       translate: str = None):
        sql = 'INSERT INTO Words (id, word, type, definition, transcription, translate) VALUES ($1, $2, $3, $4, $5, $6)'
        await self.pool.execute(sql, id, word, type, definition, transcription, translate)

    async def select_all_words(self):
        sql = 'SELECT * FROM Words'
        return await self.pool.fetch(sql)

    async def select_cur_word(self, **kwargs):
        sql = 'SELECT * FROM Words WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetch(sql, *parameters)

    async def select_word(self, **kwargs):
        sql = 'SELECT word FROM Words WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetch(sql, *parameters)

    async def select_transcription(self, **kwargs):
        sql = 'SELECT transcription FROM Words WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetch(sql, *parameters)

    async def select_translate(self, **kwargs):
        sql = 'SELECT translate FROM Words WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetch(sql, *parameters)

    async def select_type(self, **kwargs):
        sql = 'SELECT type FROM Words WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetch(sql, *parameters)

    async def select_definition(self, **kwargs):
        sql = 'SELECT definition FROM Words WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetch(sql, *parameters)

    async def update_transcription(self, transcription, id):
        sql = 'UPDATE Words SET transcription = $1 WHERE id = $2'
        return await self.pool.execute(sql, transcription, id)

    async def add_translation(self, translate, id):
        sql = 'UPDATE Words SET translate = $1 WHERE id = $2'
        return await self.pool.execute(sql, translate, id)

    async def add_quantity(self, quantity, id):
        sql = 'UPDATE Users SET quantity_words = $1 WHERE id = $2'
        return await self.pool.execute(sql, quantity, id)

    async def add_const_quantity(self, const_quantity, id):
        sql = 'UPDATE Users SET const_quantity = $1 WHERE id = $2'
        return await self.pool.execute(sql, const_quantity, id)

    async def set_questions(self, questions, id):
        sql = 'UPDATE Users SET questions = $1 WHERE id = $2'
        return await self.pool.execute(sql, questions, id)

    async def set_words(self, questions, id):
        sql = 'UPDATE Users SET words_q = $1 WHERE id = $2'
        return await self.pool.execute(sql, questions, id)

    async def set_definition(self, definition, id):
        sql = 'UPDATE Users SET definition_q = $1 WHERE id = $2'
        return await self.pool.execute(sql, definition, id)

    async def set_all_words(self, words, id):
        sql = 'UPDATE Users SET all_questions = $1 WHERE id = $2'
        print(sql)
        return await self.pool.execute(sql, words, id)

    async def get_all_words(self, id):
        sql = 'SELECT all_questions FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def get_some_words(self, id):
        sql = 'SELECT all_words FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def get_questions(self, id):
        sql = 'SELECT questions FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def get_words_q(self, id):
        sql = 'SELECT words_q FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def get_definiton(self, id):
        sql = 'SELECT definition_q FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def get_quantity(self, id):
        sql = "SELECT quantity_words FROM Users WHERE id = $1"

        return await self.pool.fetchval(sql, id)

    async def insert_words(self, word, id):
        sql = 'INSERT INTO Users (all_questions) VALUES ($1)'
        print(sql)
        await self.pool.execute(sql, word, id)

    async def get_prev_quantity(self, id):
        sql = "SELECT previous_quantity FROM Users WHERE id = $1"
        return await self.pool.fetchval(sql, id)

    async def add_prev_quantity(self, previous_quantity, id):
        sql = 'UPDATE Users SET previous_quantity = $1 WHERE id =$2'
        return await self.pool.execute(sql, previous_quantity, id)

    async def update_type(self):
        sql = 'ALTER TABLE Users ALTER COLUMN all_questions TYPE TEXT;'
        return await self.pool.execute(sql)

    async def set_rus_test_error(self, error, id):
        sql = 'UPDATE Users SET rus_test_errors = $1 WHERE id = $2'
        return await self.pool.execute(sql, error, id)

    async def get_rus_test_error(self, id):
        sql = 'SELECT rus_test_errors FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def set_eng_test_error(self, error, id):
        sql = 'UPDATE Users SET eng_test_errors = $1 WHERE id = $2'
        return await self.pool.execute(sql, error, id)

    async def get_eng_test_error(self, id):
        sql = 'SELECT eng_test_errors FROM Users WHERE id=$1'
        return await self.pool.fetchval(sql, id)

    async def get_def_test_error(self, id):
        sql = 'SELECT def_test_errors FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def set_def_test_error(self, error, id):
        sql = 'UPDATE Users SET def_test_errors = $1 WHERE id = $2'
        return await self.pool.execute(sql, error, id)

    async def delete_users(self):
        await self.pool.execute("DELETE FROM Users WHERE True")

    async def set_user_level(self, level, id):
        sql = 'UPDATE Users SET eng_level = $1 WHERE id = $2'
        return await self.pool.execute(sql, level, id)

    async def set_word_sentence(self, sentence, word):
        sql = 'UPDATE Words SET sentences = $1 WHERE word = $2'
        return await self.pool.execute(sql, sentence, word)

    async def get_user_level(self, id):
        sql = 'SELECT eng_level FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def delete(self, id):
        sql = 'DELETE FROM Words WHERE id = $1'
        return await self.pool.execute(sql, id)

    async def get_words_db(self):
        sql = 'SELECT word FROM Words'
        return await self.pool.fetch(sql)

    async def set_sentences(self, sentence, id):
        sql = 'UPDATE Users SET questions_s = $1 WHERE id = $2'
        return await self.pool.execute(sql, sentence, id)

    async def get_sentences(self, id):
        sql = 'SELECT questions_s FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def get_sen_test_error(self, id):
        sql = 'SELECT sen_test_errors FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def set_sen_test_error(self, error, id):
        sql = 'UPDATE Users SET sen_test_errors = $1 WHERE id = $2'
        return await self.pool.execute(sql, error, id)

    async def set_cur_sen(self, sentence, id):
        sql = 'UPDATE Users SET current_sen = $1 WHERE id = $2'
        return await self.pool.execute(sql, sentence, id)

    async def get_cur_sen(self, id):
        sql = 'SELECT current_sen FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def set_cur_sen_question(self, sentence, id):
        sql = 'UPDATE Users SET current_sen_question = $1 WHERE id = $2'
        return await self.pool.execute(sql, sentence, id)

    async def get_cur_sen_question(self, id):
        sql = 'SELECT current_sen_question FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def get_sen_test_errors(self, id):
        sql = 'SELECT sen_test_errors FROM Users WHERE id = $1'
        return await self.pool.fetchval(sql, id)

    async def set_sen_test_error(self, error, id):
        sql = 'UPDATE Users SET sen_test_errors = $1 WHERE id = $2'
        return await self.pool.execute(sql, error, id)
