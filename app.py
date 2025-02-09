import sys

from flask import Flask, request, jsonify

from src.kv_store_basic import KVStoreBasic
from src.kv_store_disk_offsets import KVStoreDiskOffsets

app = Flask(__name__)

DEFAULT_DB_PATH = "src/storage/kv_database.log"
file_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DB_PATH

# kv_store = KVStoreBasic(db_file_path=file_path)
kv_store = KVStoreDiskOffsets(db_file_path=file_path)


@app.route('/', methods=['GET'])
def home_page():
    return "Key Value Server for Immutable Data"


@app.route('/api/database', methods=['GET'])
def get_value_for_key():
    key = request.args.get('key')
    if not key:
        return jsonify({
            'success': False,
            'message': 'Key not found',
            'data': None
        }), 404

    value = kv_store.get(key)

    return jsonify({
        'success': True if value else False,
        'data': value
    }), 200


if __name__ == '__main__':
    app.run()
