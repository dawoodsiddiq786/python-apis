from storages.backends.s3boto3 import S3Boto3Storage

from HueysList import settings


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
