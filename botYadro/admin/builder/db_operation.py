
from Base.database import get_session
from Base.models.model import TelegramPostsWithBot

async def NewPostDataInBase(thumbnail_path: str, text: str, button_text: str, button_link: str) -> None:
    async for session in get_session():
        async with session.begin():
            new_post = TelegramPostsWithBot(
                thumbnail=f"./static/thumbnailPost/{thumbnail_path}",
                text=text,
                button_text=button_text,
                button_link=button_link,
            )
            session.add(new_post)
        await session.commit()