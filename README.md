# Django + SQLAlchemy + SQLite3 / PostgreSQLでWebアプリを作成する

- [Django + SQLAlchemy + SQLite3 / PostgreSQLでWebアプリを作成する](#django--sqlalchemy--sqlite3--postgresql%e3%81%a7web%e3%82%a2%e3%83%97%e3%83%aa%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b)
  - [はじめに](#%e3%81%af%e3%81%98%e3%82%81%e3%81%ab)
    - [目的](#%e7%9b%ae%e7%9a%84)
    - [関連する記事](#%e9%96%a2%e9%80%a3%e3%81%99%e3%82%8b%e8%a8%98%e4%ba%8b)
    - [実行環境](#%e5%ae%9f%e8%a1%8c%e7%92%b0%e5%a2%83)
    - [ソースコード](#%e3%82%bd%e3%83%bc%e3%82%b9%e3%82%b3%e3%83%bc%e3%83%89)
  - [シナリオと前提条件](#%e3%82%b7%e3%83%8a%e3%83%aa%e3%82%aa%e3%81%a8%e5%89%8d%e6%8f%90%e6%9d%a1%e4%bb%b6)
  - [事前準備](#%e4%ba%8b%e5%89%8d%e6%ba%96%e5%82%99)
    - [Djangoプロジェクトの作成](#django%e3%83%97%e3%83%ad%e3%82%b8%e3%82%a7%e3%82%af%e3%83%88%e3%81%ae%e4%bd%9c%e6%88%90)
    - [SQLite3でエラーが出る場合(pyenv環境)](#sqlite3%e3%81%a7%e3%82%a8%e3%83%a9%e3%83%bc%e3%81%8c%e5%87%ba%e3%82%8b%e5%a0%b4%e5%90%88pyenv%e7%92%b0%e5%a2%83)
    - [psycopg2のインストールでエラーが出る場合(venv環境)](#psycopg2%e3%81%ae%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%a7%e3%82%a8%e3%83%a9%e3%83%bc%e3%81%8c%e5%87%ba%e3%82%8b%e5%a0%b4%e5%90%88venv%e7%92%b0%e5%a2%83)
  - [ファイル構成](#%e3%83%95%e3%82%a1%e3%82%a4%e3%83%ab%e6%a7%8b%e6%88%90)
  - [Djangoモデル(django_model)](#django%e3%83%a2%e3%83%87%e3%83%abdjangomodel)
    - [Djangoモデルの定義](#django%e3%83%a2%e3%83%87%e3%83%ab%e3%81%ae%e5%ae%9a%e7%be%a9)
    - [Djangoモデルのデータ書き込み](#django%e3%83%a2%e3%83%87%e3%83%ab%e3%81%ae%e3%83%87%e3%83%bc%e3%82%bf%e6%9b%b8%e3%81%8d%e8%be%bc%e3%81%bf)
    - [Djangoモデルのマイグレーション](#django%e3%83%a2%e3%83%87%e3%83%ab%e3%81%ae%e3%83%9e%e3%82%a4%e3%82%b0%e3%83%ac%e3%83%bc%e3%82%b7%e3%83%a7%e3%83%b3)
  - [SQLAlchemyモデル(sqlalchemy_model)](#sqlalchemy%e3%83%a2%e3%83%87%e3%83%absqlalchemymodel)
    - [SQLAlchemyモデルの定義](#sqlalchemy%e3%83%a2%e3%83%87%e3%83%ab%e3%81%ae%e5%ae%9a%e7%be%a9)
    - [SQLAlchemyモデルのデータ書き込み](#sqlalchemy%e3%83%a2%e3%83%87%e3%83%ab%e3%81%ae%e3%83%87%e3%83%bc%e3%82%bf%e6%9b%b8%e3%81%8d%e8%be%bc%e3%81%bf)
    - [SQLAlchemyモデルのマイグレーション](#sqlalchemy%e3%83%a2%e3%83%87%e3%83%ab%e3%81%ae%e3%83%9e%e3%82%a4%e3%82%b0%e3%83%ac%e3%83%bc%e3%82%b7%e3%83%a7%e3%83%b3)
    - [SQLAlchemyの留意点](#sqlalchemy%e3%81%ae%e7%95%99%e6%84%8f%e7%82%b9)
  - [SQLite3](#sqlite3)
    - [SQLite3の設定](#sqlite3%e3%81%ae%e8%a8%ad%e5%ae%9a)
    - [SQLite3のマイグレーション](#sqlite3%e3%81%ae%e3%83%9e%e3%82%a4%e3%82%b0%e3%83%ac%e3%83%bc%e3%82%b7%e3%83%a7%e3%83%b3)
  - [PostgreSQL](#postgresql)
    - [PostgreSQLの設定](#postgresql%e3%81%ae%e8%a8%ad%e5%ae%9a)
    - [PostgreSQLのマイグレーション](#postgresql%e3%81%ae%e3%83%9e%e3%82%a4%e3%82%b0%e3%83%ac%e3%83%bc%e3%82%b7%e3%83%a7%e3%83%b3)
  - [Herokuデプロイ](#heroku%e3%83%87%e3%83%97%e3%83%ad%e3%82%a4)
    - [Herokuパッケージのインストール](#heroku%e3%83%91%e3%83%83%e3%82%b1%e3%83%bc%e3%82%b8%e3%81%ae%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab)
    - [Herokuの留意点](#heroku%e3%81%ae%e7%95%99%e6%84%8f%e7%82%b9)

## はじめに

Mac環境の記事ですが、Windows環境も同じ手順になります。環境依存の部分は読み替えてお試しください。

### 目的

この記事を最後まで読むと、次のことができるようになります。

- Djangoフレームワークでアプリを作成する
- SQLAlchemyを用いてモデルをデザインする
- SQLite3とPostgreSQLの設定/操作を理解する
- Herokuへデプロイするための設定を理解する

`Django Admin`

<img width="600" alt="スクリーンショット 2019-11-24 14.06.18.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/8686ef7e-47fb-3938-ead9-aae5ef3bf0c1.png">

<img width="600" alt="スクリーンショット 2019-11-24 14.06.38.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/326996/1a7b6d69-7e64-59b3-1184-818ebba26fd6.png">

`SQLite3`

```sqlite3.sh
~> select * from django_model_usdjpy;
1|2019-11-24 14:10:41.880980|108.621
2|2019-11-24 14:10:48.033484|108.621
3|2019-11-24 14:10:52.669491|108.621
```

`PostgreSQL`

```postgresql.sh
~# select * from django_model_usdjpy;
 id |         time_stamp         | usd_jpy
----+----------------------------+---------
  1 | 2019-11-24 14:05:37.248352 | 108.621
  2 | 2019-11-24 14:05:45.342350 | 108.621
  3 | 2019-11-24 14:05:51.683454 | 108.621
(3 rows)
```

### 関連する記事

- [Heroku + Selenium + ChromeでWEBプロセスを自動化する](https://qiita.com/nsuhara/items/76ae132734b7e2b352dd)
- [Heroku SchedulerでPythonを定期実行する](https://qiita.com/nsuhara/items/fac20adb6b0a122a3709)

### 実行環境

| 環境            | Ver.    |
| --------------- | ------- |
| macOS Mojave    | 10.14.6 |
| Python          | 3.7.3   |
| dj-database-url | 0.5.0   |
| django-heroku   | 0.3.1   |
| Django          | 2.2.7   |
| gunicorn        | 20.0.2  |
| psycopg2        | 2.8.4   |
| pytz            | 2019.3  |
| requests        | 2.22.0  |
| selenium        | 3.141.0 |
| SQLAlchemy      | 1.3.11  |
| sqlparse        | 0.3.0   |
| whitenoise      | 4.1.4   |

### ソースコード

実際に実装内容やソースコードを追いながら読むとより理解が深まるかと思います。是非ご活用ください。

[GitHub](https://github.com/nsuhara/python-django.git)

## シナリオと前提条件

1. 毎時00分にYahoo!ファイナンスのFXチャート・レートから**米ドル/円**を取得してDBへ登録する。
2. **SQLite3**および**PostgreSQL**はインストール済みとする。

## 事前準備

### Djangoプロジェクトの作成

```startproject.sh
~$ django-admin startproject <project_name> .
~$ python manage.py startapp <app_name>
```

### SQLite3でエラーが出る場合(pyenv環境)

SQLite3をインストールしているにも関わらずエラーとなる場合があります。Python環境にSQLite3が組み込まれていない可能性がありますので、パスを通して再インストールしましょう。

```install_python.sh
~$ CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install 3.7.3
```

### psycopg2のインストールでエラーが出る場合(venv環境)

パスを通してインストールしましょう。

```install_psycopg2.sh
~$ env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
```

## ファイル構成

```tree.sh
python-django
├── Procfile
├── common
│   ├── scheduler.py
│   └── utility.py
├── compare_project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── django_model
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
├── runtime.txt
└── sqlalchemy_model
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

## Djangoモデル(django_model)

### Djangoモデルの定義

```models.py
# ~省略~

class UsdJpy(models.Model):
    time_stamp = models.CharField(max_length=128)
    usd_jpy = models.CharField(max_length=128)

# ~省略~
```

### Djangoモデルのデータ書き込み

```views.py
# ~省略~

def _insert_usd_jpy(time_stamp, usd_jpy):
    logger.info('time_stamp={}, usd_jpy={}'.format(time_stamp, usd_jpy))
    record = UsdJpy(time_stamp=time_stamp, usd_jpy=usd_jpy)
    record.save()

# ~省略~
```

### Djangoモデルのマイグレーション

```migration.sh
~$ python manage.py makemigrations django_model
~$ python manage.py migrate
```

## SQLAlchemyモデル(sqlalchemy_model)

### SQLAlchemyモデルの定義

```models.py
# ~省略~

class UsdJpy(Base):
    __tablename__ = 'sqlalchemy_model_usdjpy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time_stamp = Column('time_stamp', String(128))
    usd_jpy = Column('usd_jpy', String(128))

# ~省略~
```

### SQLAlchemyモデルのデータ書き込み

```views.py
# ~省略~

def _insert_usd_jpy(time_stamp, usd_jpy):
    logger.info('time_stamp={}, usd_jpy={}'.format(time_stamp, usd_jpy))
    record = UsdJpy(time_stamp=time_stamp, usd_jpy=usd_jpy)
    Session.add(record)
    Session.commit()

# ~省略~
```

### SQLAlchemyモデルのマイグレーション

```migration.sh
~$ python manage.py migrate
~$ python sqlalchemy_model/models.py
```

### SQLAlchemyの留意点

`Django Adminサイトに対応していないため、ブラウザ上からデータの確認や編集ができません。そのため、データベースにアクセスして操作する必要があります。`

## SQLite3

### SQLite3の設定

```settings.py
# ~省略~

if DB_SELECTED == 'sqlite3':
    DB_ENGINE = 'django.db.backends.sqlite3'
    DB_NAME = 'db.sqlite3'
    DB_URI = 'sqlite:///{}'.format(DB_NAME)

    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': os.path.join(BASE_DIR, DB_NAME),
        }
    }

# ~省略~
```

### SQLite3のマイグレーション

1. データベースのマイグレーション

    ```migration.sh
    ~$ python manage.py makemigrations <model>
    ~$ python manage.py migrate
    ```

2. Django Adminの作成

    ```runserver.sh
    ~$ python manage.py createsuperuser
    ```

3. アプリの起動

    ```runserver.sh
    ~$ python manage.py runserver
    ```

4. レコードの削除

    ```delete_records.sh
    ~$ sqlite3 <database_name>
    ~> .table
    ~> delete from <table_name>;
    ~> delete from sqlite_sequence where name='<table_name>';
    ~> .quit
    ```

## PostgreSQL

### PostgreSQLの設定

```settings.py
# ~省略~

if DB_SELECTED == 'postgresql':
    DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
    DB_PORT = '5432'
    DB_OPTIONS = {}

    if IS_HEROKU_SUPPORTED:
        DB_NAME = '<heroku name>'
        DB_USER = '<heroku user>'
        DB_PASSWORD = '<heroku password>'
        DB_HOST = '<heroku host>'
    else:
        DB_NAME = 'db.postgresql_psycopg2'
        DB_USER = 'nsuhara'
        DB_PASSWORD = 'nsuhara'
        DB_HOST = '127.0.0.1'

    DB_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER,
                                               DB_PASSWORD, DB_HOST, DB_NAME)

    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': DB_OPTIONS,
        },
    }

# ~省略~
```

### PostgreSQLのマイグレーション

1. サービスの起動/停止(Brew環境)

    ```brew_services_postgresql.sh
    ~$ brew services start postgresql
    ~$ brew services stop postgresql
    ```

2. PostgreSQLユーザの作成

    ```createuser.sh
    ~$ createuser -a -d -U <user_name>
    ~$ psql -c "ALTER USER <user_name> WITH PASSWORD '<user_name>'"
    ```

3. データベースの作成

    ```createdb.sh
    ~$ createdb <database_name> -O <owner_name>
    ```

4. データベースのマイグレーション

    ```migration.sh
    ~$ python manage.py makemigrations <model>
    ~$ python manage.py migrate
    ```

5. Django Adminの作成

    ```runserver.sh
    ~$ python manage.py createsuperuser
    ```

6. アプリの起動

    ```runserver.sh
    ~$ python manage.py runserver
    ```

7. レコードの削除

    ```delete_records.sh
    ~$ psql -U <user_name> -d <database_name>
    ~# \dt
    ~# select * from <table_name>;
    ~# delete from <table_name>;
    ~# select setval ('<table_name>_id_seq', 1, false);
    ~# \q
    ```

## Herokuデプロイ

### Herokuパッケージのインストール

pipで**django-heroku**をインストールします。**settings.py**にセットアップのコードを追記します。

```django_heroku.sh
~$ pip install django-heroku
```

```settings.py
# ~省略~

try:
    import django_heroku
    IS_HEROKU_SUPPORTED = True
except ImportError:
    IS_HEROKU_SUPPORTED = False

# ~省略~

if IS_HEROKU_SUPPORTED:
    django_heroku.settings(locals())

# ~省略~
```

### Herokuの留意点

1. PostgreSQLのインストール

    Resources > Add-onsから**Heroku Postgres**を追加します。

2. PostgreSQLの設定

    Heroku Postgres > Settings > **View Credentials…**からDBパラメータの確認ができます。
   - Host
   - Database
   - User
   - Port
   - Password
   - URI
   - Heroku CLI

3. Heroku環境でPythonコマンドを実行する場合の記述

    ```heroku.sh
    ~$ heroku run python <command>
    ```

    ```heroku_sample.sh
    ~$ heroku run python manage.py migrate
    ```

4. .gitignoreの設定

    .gitignoreに**migrations**を記述するとモデルのマイグレーションができないため記述しないこと。
