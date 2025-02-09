import os

from src.kv_store import AbstractKeyValueStore


class KVStoreBasic(AbstractKeyValueStore):
    def __init__(self, db_file_path='src/storage/kv_database.log'):
        self.db_file_path = db_file_path
        self.kv_map = {}
        self._load_db()

    def _load_db(self):
        if not os.path.exists(self.db_file_path):
            return

        with open(self.db_file_path, 'r') as file:
            for line in file:
                tokens = line.strip().split(" ")

                # Corrupted data / None Values - skip
                if len(tokens) < 2:
                    continue

                key = tokens[0]
                value = " ".join(tokens[1:])
                # Overwrite with the most recent value
                self.kv_map[key] = value

    def get(self, key):
        return self.kv_map.get(key) if key else None

    def put(self, key, value):
        # TODO Use lock

        with open(self.db_file_path, 'a') as file:
            file.write(f"{key} {value}\n")
            self.kv_map[key] = value
