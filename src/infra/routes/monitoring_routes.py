

from flask import Blueprint, jsonify
import psutil
import platform


monitoring_bp = Blueprint('monitoring', __name__)

@monitoring_bp.get('/health')
def health():
    return jsonify({"staus": "ok"})
    

@monitoring_bp.get('/metrics')
def get_metrics():
    return jsonify({
        'system': {
            'os': platform.system(),
            'release': platform.release(),
            'machine': platform.machine(),
            'processor': platform.processor()
        },
        'cpu': {
            'usage': psutil.cpu_percent(),
            'cores': psutil.cpu_count()
        },
        'memory': {
            'used_percent': psutil.virtual_memory().percent
        },
        'disk': {
            'used_percent': psutil.disk_usage('/').percent
        }
    })