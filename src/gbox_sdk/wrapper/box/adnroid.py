import os
from typing import Union

from gbox_sdk._client import GboxClient
from gbox_sdk._response import BinaryAPIResponse
from gbox_sdk.wrapper.box.base import BaseBox
from gbox_sdk.types.v1.android_box import AndroidBox
from gbox_sdk.types.v1.boxes.android_app import AndroidApp
from gbox_sdk.types.v1.boxes.android_list_params import AndroidListParams
from gbox_sdk.types.v1.boxes.android_open_params import AndroidOpenParams
from gbox_sdk.types.v1.boxes.android_list_response import AndroidListResponse
from gbox_sdk.types.v1.boxes.android_install_params import InstallAndroidAppByURL, InstallAndroidAppByFile
from gbox_sdk.types.v1.boxes.android_restart_params import AndroidRestartParams
from gbox_sdk.types.v1.boxes.android_install_response import AndroidInstallResponse
from gbox_sdk.types.v1.boxes.android_uninstall_params import AndroidUninstallParams
from gbox_sdk.types.v1.boxes.android_list_simple_params import AndroidListSimpleParams
from gbox_sdk.types.v1.boxes.android_list_simple_response import AndroidListSimpleResponse
from gbox_sdk.types.v1.boxes.android_list_activities_response import AndroidListActivitiesResponse


class AndroidBoxOperator(BaseBox):
    def __init__(self, data: AndroidBox, client: GboxClient):
        super().__init__(data, client)

    class App:
        def __init__(self, operator: "AndroidBoxOperator"):
            self.operator = operator
            self.client = operator.client
            self.data = operator.data

        def install_by_local_file(self, path: str) -> AndroidInstallResponse:
            if not os.path.exists(path):
                raise FileNotFoundError(f"File {path} does not exist")
            with open(path, "rb") as apk_file:
                return self.client.v1.boxes.android.install(box_id=self.data.id, apk=apk_file)

        def install(self, body: Union[InstallAndroidAppByFile, InstallAndroidAppByURL]) -> AndroidInstallResponse:
            return self.client.v1.boxes.android.install(box_id=self.data.id, apk=body["apk"])

        def uninstall(self, package_name: str, body: AndroidUninstallParams) -> None:
            keep_data = bool(body.get("keepData", False))
            return self.client.v1.boxes.android.uninstall(package_name, box_id=self.data.id, keep_data=keep_data)

        def list(self, body: AndroidListParams) -> AndroidListResponse:
            return self.client.v1.boxes.android.list(box_id=self.data.id, **body)

        def get_info(self, package_name: str) -> AndroidApp:
            return self.client.v1.boxes.android.get(package_name, box_id=self.data.id)

        def get(self, package_name: str) -> "AndroidAppOperator":
            pkg = self.client.v1.boxes.android.get(package_name, box_id=self.data.id)
            return AndroidAppOperator(pkg, self.client, AndroidBox(**self.data.model_dump()))

        def close_all(self) -> None:
            self.operator.client.v1.boxes.android.close_all(box_id=self.data.id)

        def backup_all(self) -> BinaryAPIResponse:
            return self.operator.client.v1.boxes.android.backup_all(box_id=self.data.id)

        def list_imple(self, body: AndroidListSimpleParams) -> AndroidListSimpleResponse:
            return self.operator.client.v1.boxes.android.list_simple(box_id=self.data.id, **body)


class AndroidAppOperator:
    def __init__(self, data: AndroidApp, client: GboxClient, box: AndroidBox):
        self.client = client
        self.data = data
        self.box = box

    def open(self, params: AndroidOpenParams) -> None:
        activity_name = str(params.get("activityName", ""))
        return self.client.v1.boxes.android.open(
            self.data.package_name, box_id=self.box.id, activity_name=activity_name
        )

    def restart(self, params: AndroidRestartParams) -> None:
        activity_name = str(params.get("activityName", ""))
        return self.client.v1.boxes.android.restart(
            self.data.package_name, box_id=self.box.id, activity_name=activity_name
        )

    def close(self) -> None:
        return self.client.v1.boxes.android.close(self.data.package_name, box_id=self.box.id)

    def backup(self) -> BinaryAPIResponse:
        return self.client.v1.boxes.android.backup(self.data.package_name, box_id=self.box.id)

    def restore(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist")
        with open(path, "rb") as backup_file:
            return self.client.v1.boxes.android.restore(self.box.id, backup=backup_file)

    def list_activities(self) -> AndroidListActivitiesResponse:
        return self.client.v1.boxes.android.list_activities(self.data.package_name, box_id=self.box.id)
