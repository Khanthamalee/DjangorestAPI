* deploy ตาม https://github.com/iamsamitdev/DocumentReadme/blob/main/PythonDjango/DeployedAWSEC2.md?plain=1
* แต่ต้อง ตั้งค่าที่ settings.py 
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR/'static'

MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'
แล้ว sudo service nginx restart 
