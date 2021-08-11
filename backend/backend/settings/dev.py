"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 添加导包路径。参数 0 表示路径插入的位置，实际上path本身是一个路径字符串构成的列表
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'at7wt*(#pn!-*db1#*a@d@4w6#@_u&ouc%0pr7hxkn%7$0bi-+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Django只允许下面列表中的ip访问。* 代表所有
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 第三方app
    'rest_framework',
    'corsheaders',  # 解决跨域问题
    'django_crontab',  # 定时任务

    # 自定义app
    'users',
    'oauth',
    'files',
    'cases',
    'jobs',

]

MIDDLEWARE = [
    # 解决跨域的中间件
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': '121.4.47.229',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'tp_admin',  # 数据库用户名
        'PASSWORD': 'tp_123456',  # 数据库用户密码
        'NAME': 'test_plat'  # 数据库名字
    }
}

# 缓存中间件redis配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://121.4.47.229:6379/7",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'

# 本地化时区和语言
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 关闭时区功能
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 配置日志器，logger = logging.getLogger('test_plat')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 定义日志信息显示的格式
        'standard': {
            'format': '[%(asctime)s][%(module)s][%(lineno)d][%(levelname)s][%(message)s]'
        },
        'simple': {
            'format': '[%(module)s][%(lineno)d][%(message)s]'
        },
    },
    'filters': {  # 定义日志过滤器
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 定义日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',  # 打印到控制台的输出类
            'formatter': 'simple'
        },
        'standard': {  # 向文件中输出标准日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 写入到文件、按日志文件大小划分的输出类
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/access.log"),  # 日志文件的位置
            'maxBytes': 20 * 1024 * 1024,  # 日志文件的大小
            'backupCount': 5,  # 日志文件最大备份数量，超过之后自动清理掉旧日志
            'formatter': 'standard'
        },
        'error': {  # 向文件中输出错误日志
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 写入到文件、按日志文件大小划分的输出类
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/error.log"),  # 日志文件的位置
            'maxBytes': 20 * 1024 * 1024,  # 日志文件的大小
            'backupCount': 5,  # 日志文件最大备份数量，超过之后自动清理掉旧日志
            'formatter': 'standard'
        },
    },
    'loggers': {  # 日志器
        'test_plat': {  # 定义了一个名为platform的日志器
            'handlers': ['console', 'standard', 'error'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息，即是否向更高级的loggers传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

# REST_FRAMEWORK 配置
REST_FRAMEWORK = {
    # 异常处理，指定自定义的异常处理方法作为默认方法
    'EXCEPTION_HANDLER': 'backend.utils.exceptions.exception_handler',

    # 指定框架使用的认证类
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),

    # 默认全局权限认证。不需要权限的视图中加入 permissions_class = [] 即可
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    # 分页类
    'DEFAULT_PAGINATION_CLASS': 'backend.utils.pagination.SetPagination',

}

# JWT过期时间。原理是在当前时间节点加上延后时间，即为过期时间
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=5),
}

# 指定用户模型类
AUTH_USER_MODEL = 'users.User'

# CORS添加跨域白名单
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8081',
    'http://localhost:8081',
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

# 钉钉登陆参数
DT_APP_ID = '1243403811'
DT_APP_KEY = 'dingvzkg1s02pck4sgyx'
DT_REDIRECT_URI = 'http://127.0.0.1:8081/callBack'
DT_CLIENT_SECRET = 'FDCss73H328XKhNgkHAGndzkn-wPdaiVNuny-SShq3UNoGpWNJ38hjaREHf7DiQZ'

# FastDFS 配置
FDFS_URL = 'http://121.4.47.229:8888/'
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')

# 指定自定义的django文件存储类
DEFAULT_FILE_STORAGE = 'backend.utils.fastdfs.FastDFSStorage.FastDFSStorage'

# 定时任务
CRONJOBS = [
    # 每5分钟执行一次该定时任务
    ('*/1 * * * *', 'jobs.crons.turn_test_job_status',
     f'>> {os.path.join(os.path.dirname(BASE_DIR), "logs", "access.log")}')
]

# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'

if __name__ == '__main__':
    print(BASE_DIR)
