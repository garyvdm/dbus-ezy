#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

import asyncio
import json

from dbus_ezy import Message, MessageType
from dbus_ezy.aio import MessageBus

loop = asyncio.get_event_loop()


async def main():
    bus = await MessageBus().connect()

    reply = await bus.call(
        Message(
            destination="org.freedesktop.DBus",
            path="/org/freedesktop/DBus",
            interface="org.freedesktop.DBus",
            member="ListNames",
        )
    )

    if reply.message_type == MessageType.ERROR:
        raise Exception(reply.body[0])

    print(json.dumps(reply.body[0], indent=2))


loop.run_until_complete(main())
