import logging
logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html',)

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    srv = yield from loop.create_server(app.make_handler(), "127.0.0.1", 9000)
    logging.info("server started at http://127.0.0.1:9000...")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

# day3 创建连接池
@aysncio.coroutine
def create_pool(loop, **kw):
    logging.info("create database connection pool...")
    global __pool
    __pool = yield from aiomysql.create_pool(
        host = kw.get('host', 'localhost'),
        port = kw.get('port', 3306),
        user = kw['user'],
        password = kw['password'],
        db = kw['db']
        charset = kw.get('charset', 'utf8'),
        autocommit = kw.get('atuocommit', True),
        maxsize = kw.get('maxsize', 10),
        minsize = kw.get('minsize', 1),
        loop = loop
    )

# select
@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with(yield from __pool) as conn:
        cur = yeild
        from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from  cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info("rows returned: %s" % s
        len(rs))
        return rs

# update op
@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with(yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected