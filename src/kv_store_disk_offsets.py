import os

from src.kv_store import AbstractKeyValueStore


class KVStoreDiskOffsets(AbstractKeyValueStore):
    def __init__(self, db_file_path='src/kv_database.log'):
        self.db_file_path = db_file_path
        self.kv_map = {}
        self._load_db()

    def _load_db(self):
        if not os.path.exists(self.db_file_path):
            return

        with open(self.db_file_path, 'r') as file:
            offset = file.tell()
            while line := file.readline():
                tokens = line.strip().split(" ")

                # Corrupted data / None Values - skip
                if len(tokens) < 2:
                    continue

                key = tokens[0]
                self.kv_map[key] = offset
                offset = file.tell()


    def get(self, key):
        if key not in self.kv_map:
            return None

        offset = self.kv_map[key]
        with open(self.db_file_path, 'r') as file:
            file.seek(offset)
            line = file.readline().strip()
            value_tokens = line.strip().split(" ")[1:]

            if len(value_tokens) < 2:
                return None

            return " ".join(value_tokens)

    def put(self, key, value):
        # TODO Use lock

        with open(self.db_file_path, 'a') as file:
            offset = file.tell()
            file.write(f"{key} {value}\n")
            self.kv_map[key] = offset