from typing import Optional

from aioredis import Redis, create_redis_pool

#Create a RedisCache instance
class RedisCache:
    
    def __init__(self):
        self.redis_cache: Optional[Redis] = None
        
    async def init_cache(self):
        self.redis_cache = await create_redis_pool("redis://localhost:6379/0?encoding=utf-8") #Connecting to database

    async def keys(self, pattern):
        return await self.redis_cache.keys(pattern)

    async def set(self, key, value):
        return await self.redis_cache.set(key, value)
    
    async def get(self, key):
        return await self.redis_cache.get(key)

    async def hgetall(self, key):
        return await self.redis_cache.hgetall(key)

    async def hset(self, key, field, value):
        return await self.redis_cache.hset(key,field, value)

    async def hvals(self, key):
        return await self.redis_cache.hvals(key)

    async def hget(self, key, field):
        return await self.redis_cache.hget(key , field)
    
    async def smembers(self, key):
        result = self.redis_cache.smembers(key)
        return await result

    
    async def close(self):
        self.redis_cache.close()
        await self.redis_cache.wait_closed()


redis_cache = RedisCache()
