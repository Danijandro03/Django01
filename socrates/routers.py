class conectSoc (object):

    def db_for_read(self, model, **hints):
        if model.meta.app_label == 'socrates':
            return 'so_qa'
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'scrates':
            return db == 'so_qa'
        return None

    