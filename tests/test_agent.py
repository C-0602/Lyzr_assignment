import pytest, asyncio
from backend.agent.scheduling_agent import SchedulingAgent

@pytest.mark.asyncio
async def test_faq():
    agent = SchedulingAgent()
    r = await agent.handle_message("s1", "What insurance do you accept?")
    assert "insurance" in r.lower()
