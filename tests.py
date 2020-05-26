import asyncio
from unittest.mock import patch, Mock, call

from asynctest import CoroutineMock

from example import launch_tasks, long_computation

async def test_coroutine():
    res = await long_computation(0)
    assert res == "DONE"

import pytest

@pytest.fixture
def loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

def test_coroutine2(loop: asyncio.AbstractEventLoop):
    res = loop.run_until_complete(long_computation(0))
    assert res == "DONE"

@pytest.mark.asyncio
async def test_coroutine3():
    res = await long_computation(0)
    assert res == "DONE"

class AsyncMock(Mock):
    def __call__(self, *args, **kwargs):
        sup = super()

        async def coro():
            return sup.__call__(*args, **kwargs)

        return coro()

@pytest.mark.asyncio
async def test_mock():
    with patch('example.long_computation', new=AsyncMock()) as mocked_coro:
        await launch_tasks(3)
        mocked_coro.assert_has_calls([call(0), call(1), call(2)], any_order=True)

@pytest.mark.asyncio
async def test_mock2():
    with patch('example.long_computation', new=CoroutineMock()) as mocked_coro:
        await launch_tasks(3)
        mocked_coro.assert_has_calls([call(0), call(1), call(2)], any_order=True)
