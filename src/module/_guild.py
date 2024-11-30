from module.member import Member
from cachetools import cached, TTLCache
from module.permissions import Permissions
import _http
import config



cache = TTLCache(maxsize=100, ttl=300)
class Guild():
    def __init__(self, payload:dict):
        self._payload = payload
        self.id = int(self._payload.get("id"))
        self.name = self._payload.get("name")
        self.icon_hash = self._payload.get("icon")
        self.is_owner = self._payload.get("owner")
        self.permissions = self.__get_permissions(self._payload.get("permissions"))


    @staticmethod
    def __get_permissions(permissions_value):
        if permissions_value is None:
            return
        return Permissions(int(permissions_value))

    def __str__(self):
        return self.name

    def __eq__(self, guild):
        return isinstance(guild, Guild) and guild.id == self.id

    def __ne__(self, guild):
        return not self.__eq__(guild)

    @property
    def icon_url(self):
        """A property returning direct URL to the guild's icon. Returns None if guild has no icon set."""
        if not self.icon_hash:
            return
        return config.DISCORD_GUILD_ICON_BASE_URL.format(guild_id=self.id, icon_hash=self.icon_hash)
    

    def to_json(self):
        return self._payload
    

    
    @cached(cache)
    def get_member(self, user_id:int)->Member:
        try:
            fetched_member = _http.bot_request(f"/guilds/{self.id}/members/{user_id}")
            print(fetched_member)
            return Member(fetched_member, self)
        except:
            return None
