response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Videos'),URL('default','videos_manage')==URL(),URL('default','videos_manage'),[]),
(T('Pictures'),URL('default','pictures_manage')==URL(),URL('default','pictures_manage'),[]),
]