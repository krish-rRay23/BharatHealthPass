import redis.asyncio as redis
import json
import logging
from typing import Any, Dict, Callable, Awaitable
from app.core.config import settings

logger = logging.getLogger(__name__)

class EventBus:
    def __init__(self):
        self.redis = redis.from_url(settings.REDIS_URL, decode_responses=True)
        self.stream_key = "bhp_events"
        self.group_name = "bhp_services"

    async def publish(self, event_type: str, data: Dict[str, Any]):
        """Publish an event to the stream."""
        event_payload = {
            "type": event_type,
            "data": json.dumps(data)
        }
        # redis.xadd returns the message ID
        msg_id = await self.redis.xadd(self.stream_key, event_payload)
        logger.info(f"Published event {event_type} with ID {msg_id}")
        return msg_id

    async def consume(self, consumer_name: str, handler: Callable[[str, Dict[str, Any]], Awaitable[None]]):
        """
        Consume events in a loop.
        This is a simplified consumer for demonstration.
        In production, we'd handle consumer groups more robustly.
        """
        # Ensure group needs creation logic or manual setup. 
        # For simplicity, we'll just read new messages in this loop or use xread if groups aren't needed yet.
        # But required: "Event Bus (Kafka-like abstraction or Redis Streams)"
        
        try:
            await self.redis.xgroup_create(self.stream_key, self.group_name, id="0", mkstream=True)
        except redis.ResponseError as e:
            if "BUSYGROUP Consumer Group name already exists" not in str(e):
                raise

        logger.info(f"Consumer {consumer_name} started listening on {self.stream_key}")
        
        while True:
            try:
                # Read new messages for the consumer group
                streams = await self.redis.xreadgroup(
                    groupname=self.group_name,
                    consumername=consumer_name,
                    streams={self.stream_key: ">"},
                    count=1,
                    block=5000
                )

                if not streams:
                    continue

                for stream, messages in streams:
                    for message_id, message_data in messages:
                        event_type = message_data.get("type")
                        raw_data = message_data.get("data")
                        
                        if event_type and raw_data:
                            try:
                                payload = json.loads(raw_data)
                                await handler(event_type, payload)
                                # Acknowledge processing
                                await self.redis.xack(self.stream_key, self.group_name, message_id)
                            except Exception as e:
                                logger.error(f"Error processing event {message_id}: {e}")
            except Exception as e:
                logger.error(f"Error in consumer loop: {e}")
                import asyncio
                await asyncio.sleep(1)

event_bus = EventBus()
