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

- <code title="get /boxes/{id}">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">retrieve</a>(id) -> <a href="./src/gbox_sdk/types/v1/box_retrieve_response.py">BoxRetrieveResponse</a></code>
- <code title="get /boxes">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">list</a>(\*\*<a href="src/gbox_sdk/types/v1/box_list_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_list_response.py">BoxListResponse</a></code>
- <code title="post /boxes/android">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">create_android</a>(\*\*<a href="src/gbox_sdk/types/v1/box_create_android_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/android_box.py">AndroidBox</a></code>
- <code title="post /boxes/linux">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">create_linux</a>(\*\*<a href="src/gbox_sdk/types/v1/box_create_linux_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/linux_box.py">LinuxBox</a></code>
- <code title="post /boxes/{id}/commands">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">execute_commands</a>(id, \*\*<a href="src/gbox_sdk/types/v1/box_execute_commands_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_execute_commands_response.py">BoxExecuteCommandsResponse</a></code>
- <code title="post /boxes/{id}/live-view-url">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">live_view_url</a>(id, \*\*<a href="src/gbox_sdk/types/v1/box_live_view_url_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_live_view_url_response.py">BoxLiveViewURLResponse</a></code>
- <code title="post /boxes/{id}/run-code">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">run_code</a>(id, \*\*<a href="src/gbox_sdk/types/v1/box_run_code_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_run_code_response.py">BoxRunCodeResponse</a></code>
- <code title="post /boxes/{id}/start">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">start</a>(id, \*\*<a href="src/gbox_sdk/types/v1/box_start_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_start_response.py">BoxStartResponse</a></code>
- <code title="post /boxes/{id}/stop">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">stop</a>(id, \*\*<a href="src/gbox_sdk/types/v1/box_stop_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_stop_response.py">BoxStopResponse</a></code>
- <code title="post /boxes/{id}/terminate">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">terminate</a>(id, \*\*<a href="src/gbox_sdk/types/v1/box_terminate_params.py">params</a>) -> None</code>
- <code title="post /boxes/{id}/web-terminal-url">client.v1.boxes.<a href="./src/gbox_sdk/resources/v1/boxes/boxes.py">web_terminal_url</a>(id, \*\*<a href="src/gbox_sdk/types/v1/box_web_terminal_url_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/box_web_terminal_url_response.py">BoxWebTerminalURLResponse</a></code>

### Actions

Types:

```python
from gbox_sdk.types.v1.boxes import ActionResult, ActionScreenshotResponse
```

Methods:

- <code title="post /boxes/{id}/actions/click">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">click</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_click_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{id}/actions/drag">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">drag</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_drag_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{id}/actions/move">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">move</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_move_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{id}/actions/press-button">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">press_button</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_press_button_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{id}/actions/press-key">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">press_key</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_press_key_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{id}/actions/screenshot">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">screenshot</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_screenshot_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_screenshot_response.py">ActionScreenshotResponse</a></code>
- <code title="post /boxes/{id}/actions/scroll">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">scroll</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_scroll_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{id}/actions/swipe">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">swipe</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_swipe_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{id}/actions/touch">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">touch</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_touch_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>
- <code title="post /boxes/{id}/actions/type">client.v1.boxes.actions.<a href="./src/gbox_sdk/resources/v1/boxes/actions.py">type</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/action_type_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/action_result.py">ActionResult</a></code>

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

- <code title="get /boxes/{id}/fs/list">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">list</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_list_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_list_response.py">FListResponse</a></code>
- <code title="post /boxes/{id}/fs/exists">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">exists</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_exists_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_exists_response.py">FExistsResponse</a></code>
- <code title="get /boxes/{id}/fs/info">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">info</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_info_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_info_response.py">FInfoResponse</a></code>
- <code title="get /boxes/{id}/fs/read">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">read</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_read_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_read_response.py">FReadResponse</a></code>
- <code title="delete /boxes/{id}/fs">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">remove</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_remove_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_remove_response.py">FRemoveResponse</a></code>
- <code title="post /boxes/{id}/fs/rename">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">rename</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_rename_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_rename_response.py">FRenameResponse</a></code>
- <code title="post /boxes/{id}/fs/write">client.v1.boxes.fs.<a href="./src/gbox_sdk/resources/v1/boxes/fs.py">write</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/f_write_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/f_write_response.py">FWriteResponse</a></code>

### Browser

Types:

```python
from gbox_sdk.types.v1.boxes import BrowserCdpURLResponse
```

Methods:

- <code title="get /boxes/{id}/browser/connect-url/cdp">client.v1.boxes.browser.<a href="./src/gbox_sdk/resources/v1/boxes/browser.py">cdp_url</a>(id) -> str</code>

### Android

Types:

```python
from gbox_sdk.types.v1.boxes import (
    AndroidApp,
    AndroidListResponse,
    AndroidGetConnectAddressResponse,
    AndroidListActivitiesResponse,
    AndroidListSimpleResponse,
)
```

Methods:

- <code title="get /boxes/{id}/android/apps">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">list</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_list_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/android_list_response.py">AndroidListResponse</a></code>
- <code title="post /boxes/{id}/android/apps/{packageName}/backup">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">backup</a>(package_name, \*, id) -> BinaryAPIResponse</code>
- <code title="post /boxes/{id}/android/apps/backup-all">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">backup_all</a>(id) -> BinaryAPIResponse</code>
- <code title="post /boxes/{id}/android/apps/{packageName}/close">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">close</a>(package_name, \*, id) -> None</code>
- <code title="post /boxes/{id}/android/apps/close-all">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">close_all</a>(id) -> None</code>
- <code title="get /boxes/{id}/android/apps/{packageName}">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">get</a>(package_name, \*, id) -> <a href="./src/gbox_sdk/types/v1/boxes/android_app.py">AndroidApp</a></code>
- <code title="get /boxes/{id}/android/connect-address">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">get_connect_address</a>(id) -> <a href="./src/gbox_sdk/types/v1/boxes/android_get_connect_address_response.py">AndroidGetConnectAddressResponse</a></code>
- <code title="post /boxes/{id}/android/apps">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">install</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_install_params.py">params</a>) -> None</code>
- <code title="get /boxes/{id}/android/apps/{packageName}/activities">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">list_activities</a>(package_name, \*, id) -> <a href="./src/gbox_sdk/types/v1/boxes/android_list_activities_response.py">AndroidListActivitiesResponse</a></code>
- <code title="get /boxes/{id}/android/apps/simple">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">list_simple</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_list_simple_params.py">params</a>) -> <a href="./src/gbox_sdk/types/v1/boxes/android_list_simple_response.py">AndroidListSimpleResponse</a></code>
- <code title="post /boxes/{id}/android/apps/{packageName}/open">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">open</a>(package_name, \*, id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_open_params.py">params</a>) -> None</code>
- <code title="post /boxes/{id}/android/apps/{packageName}/restart">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">restart</a>(package_name, \*, id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_restart_params.py">params</a>) -> None</code>
- <code title="post /boxes/{id}/android/apps/restore">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">restore</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_restore_params.py">params</a>) -> None</code>
- <code title="post /boxes/{id}/android/screen/rotate">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">rotate_screen</a>(id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_rotate_screen_params.py">params</a>) -> None</code>
- <code title="delete /boxes/{id}/android/apps/{packageName}">client.v1.boxes.android.<a href="./src/gbox_sdk/resources/v1/boxes/android.py">uninstall</a>(package_name, \*, id, \*\*<a href="src/gbox_sdk/types/v1/boxes/android_uninstall_params.py">params</a>) -> None</code>
