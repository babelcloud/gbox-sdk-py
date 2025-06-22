# V1

## Boxes

Types:

```python
from gbox_sdk.types.v1 import (
    AndroidBox,
    CreateAndroidBox,
    CreateBoxConfig,
    CreateLinuxBox,
    LinuxBox,
    BoxRetrieveResponse,
    BoxListResponse,
    BoxExecuteCommandsResponse,
    BoxLiveViewURLResponse,
    BoxRunCodeResponse,
    BoxStartResponse,
    BoxStopResponse,
    BoxWebTerminalURLResponse,
)
```

Methods:

- <code title="get /boxes/{boxId}">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">retrieve</a>(box_id) -> <a href="./src/gbox_sdk/types/v1/box_retrieve_response.py">BoxRetrieveResponse</a></code>
- <code title="get /boxes">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">list</a>(\*\*<a href="src/gbox_sdk/types/v1/box_list_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_list_response.py">BoxListResponse</a></code>
- <code title="post /boxes/android">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">create_android</a>(\*\*<a href="src/gbox_sdk/types/v1/box_create_android_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/android_box.py">AndroidBox</a></code>
- <code title="post /boxes/linux">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">create_linux</a>(\*\*<a href="src/gbox_sdk/types/v1/box_create_linux_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/linux_box.py">LinuxBox</a></code>
- <code title="post /boxes/{boxId}/commands">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">execute_commands</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/box_execute_commands_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_execute_commands_response.py">BoxExecuteCommandsResponse</a></code>
- <code title="post /boxes/{boxId}/live-view-url">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">live_view_url</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/box_live_view_url_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_live_view_url_response.py">BoxLiveViewURLResponse</a></code>
- <code title="post /boxes/{boxId}/run-code">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">run_code</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/box_run_code_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_run_code_response.py">BoxRunCodeResponse</a></code>
- <code title="post /boxes/{boxId}/start">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">start</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/box_start_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_start_response.py">BoxStartResponse</a></code>
- <code title="post /boxes/{boxId}/stop">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">stop</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/box_stop_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_stop_response.py">BoxStopResponse</a></code>
- <code title="post /boxes/{boxId}/terminate">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">terminate</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/box_terminate_params.py">params</a>) -> None</code>
- <code title="post /boxes/{boxId}/web-terminal-url">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">web_terminal_url</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/box_web_terminal_url_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_web_terminal_url_response.py">BoxWebTerminalURLResponse</a></code>

### Actions

Types:

```python
from gbox_sdk.types.v1.boxes import ActionResult, ActionScreenshotResponse
```

Methods:

- <code title="post /boxes/{boxId}/actions/click">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">click</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_click_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/drag">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">drag</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_drag_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/move">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">move</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_move_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/press-button">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">press_button</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_press_button_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/press-key">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">press_key</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_press_key_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/screen-rotation">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">screen_rotation</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_screen_rotation_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/screenshot">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">screenshot</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_screenshot_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_screenshot_response.py">ActionScreenshotResponse</a></code>
- <code title="post /boxes/{boxId}/actions/scroll">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">scroll</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_scroll_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/swipe">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">swipe</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_swipe_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/touch">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">touch</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_touch_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{boxId}/actions/type">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">type</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_type_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>

### Fs

Types:

```python
from gbox_sdk.types.v1.boxes import (
    FListResponse,
    FExistsResponse,
    FInfoResponse,
    FReadResponse,
    FRemoveResponse,
    FRenameResponse,
    FWriteResponse,
)
```

Methods:

- <code title="get /boxes/{boxId}/fs/list">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">list</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_list_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_list_response.py">FListResponse</a></code>
- <code title="post /boxes/{boxId}/fs/exists">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">exists</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_exists_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_exists_response.py">FExistsResponse</a></code>
- <code title="get /boxes/{boxId}/fs/info">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">info</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_info_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_info_response.py">FInfoResponse</a></code>
- <code title="get /boxes/{boxId}/fs/read">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">read</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_read_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_read_response.py">FReadResponse</a></code>
- <code title="delete /boxes/{boxId}/fs">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">remove</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_remove_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_remove_response.py">FRemoveResponse</a></code>
- <code title="post /boxes/{boxId}/fs/rename">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">rename</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_rename_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_rename_response.py">FRenameResponse</a></code>
- <code title="post /boxes/{boxId}/fs/write">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">write</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_write_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_write_response.py">FWriteResponse</a></code>

### Browser

Types:

```python
from gbox_sdk.types.v1.boxes import BrowserCdpURLResponse
```

Methods:

- <code title="post /boxes/{boxId}/browser/connect-url/cdp">client.v1.boxes.browser.<a href="./src/gbox_sdk/resources/v1/boxes/browser.py">cdp_url</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/browser_cdp_url_params.py">params</a>) -> str</code>

### Android

Types:

```python
from gbox_sdk.types.v1.boxes import (
    AndroidApp,
    AndroidListResponse,
    AndroidGetConnectAddressResponse,
    AndroidInstallResponse,
    AndroidListActivitiesResponse,
    AndroidListSimpleResponse,
)
```

Methods:

- <code title="get /boxes/{boxId}/android/apps">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">list</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_list_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/android_list_response.py">AndroidListResponse</a></code>
- <code title="post /boxes/{boxId}/android/apps/{packageName}/backup">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">backup</a>(package_name, \*, box_id) -> BinaryAPIResponse</code>
- <code title="post /boxes/{boxId}/android/apps/backup-all">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">backup_all</a>(box_id) -> BinaryAPIResponse</code>
- <code title="post /boxes/{boxId}/android/apps/{packageName}/close">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">close</a>(package_name, \*, box_id) -> None</code>
- <code title="post /boxes/{boxId}/android/apps/close-all">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">close_all</a>(box_id) -> None</code>
- <code title="get /boxes/{boxId}/android/apps/{packageName}">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">get</a>(package_name, \*, box_id) -> <a href="./src/gbox_sdk/types/v1/boxes/android_app.py">AndroidApp</a></code>
- <code title="get /boxes/{boxId}/android/connect-address">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">get_connect_address</a>(box_id) -> <a href="./src/gbox_sdk/types/v1/boxes/android_get_connect_address_response.py">AndroidGetConnectAddressResponse</a></code>
- <code title="post /boxes/{boxId}/android/apps">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">install</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_install_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/android_install_response.py">AndroidInstallResponse</a></code>
- <code title="get /boxes/{boxId}/android/apps/{packageName}/activities">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">list_activities</a>(package_name, \*, box_id) -> <a href="./src/gbox_sdk/types/v1/boxes/android_list_activities_response.py">AndroidListActivitiesResponse</a></code>
- <code title="get /boxes/{boxId}/android/apps/simple">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">list_simple</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_list_simple_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/android_list_simple_response.py">AndroidListSimpleResponse</a></code>
- <code title="post /boxes/{boxId}/android/apps/{packageName}/open">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">open</a>(package_name, \*, box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_open_params.py">params</a>) -> None</code>
- <code title="post /boxes/{boxId}/android/apps/{packageName}/restart">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">restart</a>(package_name, \*, box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_restart_params.py">params</a>) -> None</code>
- <code title="post /boxes/{boxId}/android/apps/restore">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">restore</a>(box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_restore_params.py">params</a>) -> None</code>
- <code title="delete /boxes/{boxId}/android/apps/{packageName}">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">uninstall</a>(package_name, \*, box_id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_uninstall_params.py">params</a>) -> None</code>
