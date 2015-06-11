### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_videos',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_image', type='text',
          label=T('Image')),
    Field('f_size', type='integer',
          label=T('Size')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_videos_archive',db.t_videos,Field('current_record','reference t_videos',readable=False,writable=False))

########################################
db.define_table('t_pictures',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_video', type='upload',
          label=T('Video')),
    Field('f_size', type='integer',
          label=T('Size')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_pictures_archive',db.t_pictures,Field('current_record','reference t_pictures',readable=False,writable=False))
