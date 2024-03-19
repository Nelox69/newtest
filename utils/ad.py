import logging
import aiohttp

# Call this method wherever you want to show an ad,
# for example your bot just made its job and
# it's a great time to show an ad to a user

log = logging.getLogger('adverts')


async def show_advert(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            'https://api.gramads.net/ad/SendPost',
            headers={
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyNzEwIiwianRpIjoiMmRhZjNkMmQtNWZiMy00NmVlLThjZDgtZTVmYzA3YmNiY2ViIiwibmFtZSI6IkZyaWVuZFNoaXAgfCDQotC10YHRgiDQvdCwINC00YDRg9C20LHRgyB8INCQ0L3QvtC90LjQvNC90YvQtSDQv9C40YHRjNC80LAiLCJib3RpZCI6IjM3NyIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiMjcxMCIsIm5iZiI6MTY5NTM3MTk0OCwiZXhwIjoxNjk1NTgwNzQ4LCJpc3MiOiJTdHVnbm92IiwiYXVkIjoiVXNlcnMifQ.zB_1cLsOtpuoWNZWkyRa80Um3HWuCF__B8bIsl4dW2Q',
                'Content-Type': 'application/json',
            },
            json={'SendToChatId': user_id},
        ) as response:

            if not response.ok:

                log.error('Gramads: %s' % str(await response.json()))
