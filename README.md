- Referance
  * [Links](https://github.com/iamsamitdev/DocumentReadme/blob/main/PythonDjango/DeployedAWSEC2.md?plain=1)
* At settings.py 
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR/'static'

MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'
and then sudo service nginx restart 
