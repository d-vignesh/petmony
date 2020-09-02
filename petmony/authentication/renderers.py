from core.renderers import CoreJSONRenderer 

import json

class UserJSONRenderer(CoreJSONRenderer):

    charset = 'utf-8'
    object_label = 'user'

    def render(self, data, media_type=None, renderer_context=None):

        token = data.get('token', None)
        # 'token' will be a byte object.Byte objects don't serialize well, 
        # so we need to decode it before rendering the user object
        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return super(UserJSONRenderer, self).render(data)

        

