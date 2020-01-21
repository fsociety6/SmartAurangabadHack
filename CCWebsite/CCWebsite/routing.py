from channels.routing import ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator

application = ProtocolTypeRouter({
    # # Empty for now (http->django views is added by default)
    # 'websocket': AllowedHostsOriginValidator(
    #
    # )
})
