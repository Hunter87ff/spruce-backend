import _http
from module._guild import Guild

class Client:
    def __init__(self, token:str="access token", obj:dict=None, ) -> None:
        self.access_token = token
        if obj!=None:
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


    async def guilds(self, json:bool=False) -> list[Guild|dict]:

        _guild_data, code = await _http.fetch_api("/users/@me/guilds", access_token=self.access_token)
        if code!=200:return []
        _managable_guilds = []
        _guild_obj = []
        for _guild in _guild_data:
            _g = Guild(_guild)
            if _g.permissions.manage_guild:
                _managable_guilds.append(_g)
                if json:
                    _guild_obj.append(_guild)
        return _managable_guilds if not json else _guild_obj


    
