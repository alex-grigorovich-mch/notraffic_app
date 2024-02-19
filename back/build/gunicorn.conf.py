import multiprocessing as mp

host = '0.0.0.0'
port = 8000

bind = f'{host}:{port}'
workers = mp.cpu_count() * 2 + 1
