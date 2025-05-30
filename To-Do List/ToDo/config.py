class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.time_format = "%Y-%m-%d %H:%M"
            cls._instance.max_tasks = 10
            cls._instance.enable_notifications = True
        return cls._instance
