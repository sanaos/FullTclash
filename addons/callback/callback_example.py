from pyrogram.types import Message
from pyrogram import Client
from utils import message_delete_queue

# 这是一个写权限回调的模板
# 首先需要定义一个名为 callback 的协程函数（一定要这个名字），然后下面是一个例子，不管你怎么操作，最后一定要返回一个布尔值。
# 若为True，则通过权限校验。否则拒绝调用bot的指令。


async def callback(_: Client, message: Message) -> bool:
    """
    这个例子是拒绝TG用户名为'telegram'的目标使用此bot。
    """
    return True
    # try:
    #     username = message.from_user.username
    #     if username:
    #         if message.from_user.username == "telegram":
    #             backmsg = await message.reply("❌你已被拉黑!")
    #             message_delete_queue.put_nowait((backmsg.chat.id, backmsg.id, 10))
    #             return False
    #     return True
    # except Exception as e:
    #     print(e)
    #     return False
