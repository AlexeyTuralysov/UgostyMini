__all__ = ("routerAdmin")
from aiogram import Router
from admin.builder.BuilderPost import router as post_router



router = Router(name=__name__)
router.include_routers(post_router)
