import src._http as _http
from module._guild import Guild

class Client:
    def __init__(self, obj:dict=None) -> None:
        if obj:
            self.accent_color = obj.get("accent_color")
            self.avatar = obj.get("avatar") 
            self.banner = obj.get("banner")
            self.banner_color = obj.get("banner_color")
            self.discriminator = obj.get("discriminator")
            self.email = obj.get("email")
            self.flags = obj.get("flags")
            self.global_name = obj.get("global_name")
            self.id = obj.get("id")
            self.locale = obj.get("locale")
            self.mfa_enabled = obj.get("mfa_enabled")
            self.premium_type = obj.get("premium_type")
            self.primary_guild = obj.get("primary_guild")
            self.public_flags = obj.get("public_flags")
            self.username = obj.get("username")
            self.verified = obj.get("verified")
        self._guilds:list[Guild] = []
        self._guild_obj:list[dict] = []


    async def guilds(self, access_token:str, json:bool=False) -> list[Guild|dict]:
        if self._guild_obj and json:
            return self._guild_obj
        elif self._guilds:
            return self._guilds
        _guild_data = await _http.fetch_api("/users/@me/guilds", access_token)
        _managable_guilds = []
        for _guild in _guild_data:
            _g = Guild(_guild)
            if _g.permissions.manage_guild:
                _managable_guilds.append(_g)
                if json:
                    self._guild_obj.append(_guild)

        self._guilds = _managable_guilds
        return _managable_guilds


    