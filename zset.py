import json
import redis
import time


r = redis.StrictRedis(host='localhost', port=6379, db=0)
    
with open('data.json', encoding='utf-8') as file:
  json_data = json.load(file)
  start = time.time()
  for index, data in enumerate(json_data):
    if index == 1000:
      break
    value = str(data).lower().encode('utf-8')
    r.zadd("obj", 'id:%s' % index, value)
    r.save()

end = time.time()
print(f'Сохранено {index} строк')
print(f'За {end - start} секунд')


start = time.time()
for key in r.scan_iter():
	value = r.zrange(key, 0, -1)
end = time.time()

print(f'Прочитано {index} строк')
print(f'За {end - start} секунд')
