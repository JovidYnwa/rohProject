from django.core.exceptions import ValidationError

def get_path_upload_avatar(instance, file):
    """Building path to the file, format: (media)/avata/user_id/file_name.jpg
    """
    return f'avata/{instance.id}/{file}'

def validate_size_image(file_obj):
    """Cheking file size
    """
    size_limit_mb = 2
    if file_obj.size > size_limit_mb * 1024 * 1024:
        raise ValidationError(f"Размер файла первышает дпустимое значение {size_limit_mb}MB")


