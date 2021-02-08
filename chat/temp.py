'''
def func(n):
    while n > 0:
        print('&&&&&&&&&&&')
        yield n
        print('%%%%%%%%%%%%%')
        n -= 1
        print('^^^^^^^^')


for i in func(10):
    print('******')
    print(i)'''
import time
import asyncio


def is_prime(x):
    return not any(x//1 == x/1.0 for i in range(x-1, 1, -1))


async def highest_prime_below(x):
    print('highest prime below %d ' %x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print(' Highest prime below %d is %d ' %(x, y))
            return y
        await asyncio.sleep(0.01)
        # time.sleep(0.01)
    return None


async def main():
    await asyncio.wait([
        highest_prime_below(1000),
        highest_prime_below(100),
        highest_prime_below(10)
    ])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
