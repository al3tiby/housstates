from storages.backends.azure_storage import AzureStorage
import environ
env = environ.Env()
environ.Env.read_env()


class AzureMediaStorage(AzureStorage):
    account_name = env('AZURE_ACCOUNT_NAME') # <storage_account_name>
    account_key = env('ACCOUNT_KEY') # <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = env('AZURE_ACCOUNT_NAME')  # <storage_account_name>
    account_key = env('ACCOUNT_KEY')  # <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
