print ("hello!")
app_config = {
          "host": "127.0.0.1",
          "port": 5432,
          "debug": False,
          "database": {
              "name": "моя база!",
              "user": "admin"
          }
      }
print(app_config["database"]["name"])