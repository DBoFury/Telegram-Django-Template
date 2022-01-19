from django.conf import settings
from telegram import Update
from telegram.ext import CallbackContext

from bot.handlers.bot_handlers.utils import log_errors
from bot.models import User


@log_errors
def inline_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    u, _ = User.get_or_create_profile(
        query.message.chat_id, query.message.from_user)

    data = query.data.split(f'{settings.SPLITTING_CHARACTER}')
