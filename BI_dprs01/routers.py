class conectBdprs (object):
    
    def db_for_read(self, model, **hints):
        if model.meta.app_label == 'BI_dprs01':
            return 'bi_qa'
        return None

    def db_for_write(self, model, **hints):
        if model.meta.app_label == 'BI_dprs01':
            return 'bi_qa'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'scrates':
            return db == 'bi_qa'
        return None

    