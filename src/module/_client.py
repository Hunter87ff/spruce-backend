import _http
from module._guild import Guild

class Client:


    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Client, cls).__new__(cls)
            cls._instance.load_data()
        return cls._instance


    def load_data(self, obj:dict=None) -> None:
        if hasattr(self, '_token'):  # Check if already loaded
            return
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
            self._token:str
        self._guilds:list[Guild] = []
        self._guild_obj:list[dict] = []


    async def guilds(self, access_token:str, json:bool=False) -> list[Guild|dict]:
        if self._guild_obj and json:
            return self._guild_obj
        elif self._guilds:
            return self._guilds
        _guild_data = await _http.fetch_api("/users/@me/guilds", access_token)
        if not _guild_data:return []
        _managable_guilds = []
        print(_guild_data)
        for _guild in _guild_data:
            _g = Guild(_guild)
            if _g.permissions.manage_guild:
                _managable_guilds.append(_g)
                if json:
                    self._guild_obj.append(_guild)

        self._guilds = _managable_guilds
        self._token = access_token
        return _managable_guilds


    
