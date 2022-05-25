import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, params=params, headers=headers)
        return response.json()


    def upload(self, file_path):
        if not os.path.exists(file_path):
            print('file not find')
            return
        file_name = os.path.basename(file_path)
        href = self._get_upload(file_name).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        return response


if __name__ == '__main__':
    path_to_file = input("имя файла для загузки: ")
    token = input("введите токен: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)