import json
import redis
import time


r = redis.StrictRedis(host='localhost', port=6379, db=0)
    
with open('data.json', encoding='utf-8') as input:
  test_data = json.load(input)
  count = len(test_data)
  start = time.time()
  for index, data in enumerate(test_data):
    if index == 1000:
      break
    value = str(data).lower().encode('utf-8')
    r.set('id:%s' % index, value)
    r.save()

end = time.time()
print(f'Загружено {index} строк')
print(f'За {end - start} секунд')
