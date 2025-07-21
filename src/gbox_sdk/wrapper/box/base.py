from typing import Dict, List, Union, Literal, Callable, Optional
from typing_extensions import Self

from gbox_sdk._client import GboxClient
from gbox_sdk.types.v1.linux_box import LinuxBox
from gbox_sdk.wrapper.box.action import ActionOperator
from gbox_sdk.wrapper.box.browser import BrowserOperator
from gbox_sdk.types.v1.android_box import AndroidBox
from gbox_sdk.wrapper.box.file_system import FileSystemOperator
from gbox_sdk.types.v1.box_stop_params import BoxStopParams
from gbox_sdk.types.v1.box_start_params import BoxStartParams
from gbox_sdk.types.v1.box_run_code_params import BoxRunCodeParams
from gbox_sdk.wrapper.box.websocket_client import WebSocketClient, WebSocketResult
from gbox_sdk.types.v1.box_terminate_params import BoxTerminateParams
from gbox_sdk.types.v1.box_run_code_response import BoxRunCodeResponse
from gbox_sdk.types.v1.box_live_view_url_params import BoxLiveViewURLParams
from gbox_sdk.types.v1.box_live_view_url_response import BoxLiveViewURLResponse
from gbox_sdk.types.v1.box_execute_commands_params import BoxExecuteCommandsParams
from gbox_sdk.types.v1.box_web_terminal_url_params import BoxWebTerminalURLParams
from gbox_sdk.types.v1.box_execute_commands_response import BoxExecuteCommandsResponse
from gbox_sdk.types.v1.box_web_terminal_url_response import BoxWebTerminalURLResponse


class BaseBox:
    """
    Base class for box operations, providing common interfaces for box lifecycle and actions.

    Attributes:
        client (GboxClient): The Gbox client instance used for API calls.
        data (Union[LinuxBox, AndroidBox]): The box data object.
        action (ActionOperator): Operator for box actions.
        fs (FileSystemOperator): Operator for file system actions.
        browser (BrowserOperator): Operator for browser actions.
    """

    def __init__(self, client: GboxClient, data: Union[LinuxBox, AndroidBox]):
        """
        Initialize a BaseBox instance.

        Args:
            client (GboxClient): The Gbox client instance.
            data (Union[LinuxBox, AndroidBox]): The box data object.
        """
        self.client = client
        self.data = data

        self.action = ActionOperator(self.client, self.data.id)
        self.fs = FileSystemOperator(self.client, self.data.id)
        self.browser = BrowserOperator(self.client, self.data.id)

    def _sync_data(self) -> None:
        """
        Synchronize the box data with the latest state from the server.
        """
        res = self.client.v1.boxes.retrieve(box_id=self.data.id)
        self.data = res

    def start(self, body: Optional[BoxStartParams] = None) -> Self:
        """
        Start the box.

        Args:
            body (Optional[BoxStartParams]): Parameters for starting the box.
        Returns:
            Self: The updated box instance for method chaining.
        """
        if body is None:
            body = BoxStartParams()
        self.client.v1.boxes.start(box_id=self.data.id, **body)
        self._sync_data()
        return self

    def stop(self, body: Optional[BoxStopParams] = None) -> Self:
        """
        Stop the box.

        Args:
            body (Optional[BoxStopParams]): Parameters for stopping the box.
        Returns:
            Self: The updated box instance for method chaining.
        """
        if body is None:
            body = BoxStopParams()
        self.client.v1.boxes.stop(box_id=self.data.id, **body)
        self._sync_data()
        return self

    def terminate(self, body: Optional[BoxTerminateParams] = None) -> Self:
        """
        Terminate the box.

        Args:
            body (Optional[BoxTerminateParams]): Parameters for terminating the box.
        Returns:
            Self: The updated box instance for method chaining.
        """
        if body is None:
            body = BoxTerminateParams()
        self.client.v1.boxes.terminate(box_id=self.data.id, **body)
        self._sync_data()
        return self

    def command(
        self,
        commands: Union[List[str], str],
        onStdout: Optional[Callable[[str], None]] = None,
        onStderr: Optional[Callable[[str], None]] = None,
        envs: Optional[Dict[str, str]] = None,
        api_timeout: Optional[str] = None,
        working_dir: Optional[str] = None,
    ) -> Union["BoxExecuteCommandsResponse", "WebSocketResult"]:
        """
        Execute shell commands in the box.

        Args:
            commands (Union[List[str], str]): The commands to execute.
            onStdout (Optional[Callable[[str], None]]): Callback for stdout.
            onStderr (Optional[Callable[[str], None]]): Callback for stderr.
            envs (Optional[Dict[str, str]]): Environment variables.
            api_timeout (Optional[str]): API timeout (e.g., "30s", "5m").
            working_dir (Optional[str]): Working directory.
        Returns:
            Union[BoxExecuteCommandsResponse, WebSocketResult]: The response containing the command execution result.
        """
        if onStdout is not None or onStderr is not None:
            return self._command_via_websocket(commands, onStdout, onStderr, envs, api_timeout, working_dir)

        params = BoxExecuteCommandsParams(
            commands=commands,
        )

        if envs is not None:
            params["envs"] = envs
        if api_timeout is not None:
            params["api_timeout"] = api_timeout
        if working_dir is not None:
            params["working_dir"] = working_dir

        return self.client.v1.boxes.execute_commands(box_id=self.data.id, **params)

    def _command_via_websocket(
        self,
        commands: Union[List[str], str],
        onStdout: Optional[Callable[[str], None]] = None,
        onStderr: Optional[Callable[[str], None]] = None,
        envs: Optional[Dict[str, str]] = None,
        api_timeout: Optional[str] = None,
        working_dir: Optional[str] = None,
    ) -> "WebSocketResult":
        """
        Execute commands via WebSocket with streaming output.

        This method runs the WebSocket execution in a new event loop if one is not already running.
        """
        try:
            websocket_response = self.client.v1.boxes.websocket_url(box_id=self.data.id)
            websocket_url = websocket_response.command

            websocket_client = WebSocketClient(websocket_url, self.client.api_key)

            import asyncio

            try:
                loop = asyncio.get_running_loop()
                return asyncio.run_coroutine_threadsafe(
                    websocket_client.execute_command(
                        commands=commands,
                        on_stdout=onStdout,
                        on_stderr=onStderr,
                        envs=envs,
                        api_timeout=api_timeout,
                        working_dir=working_dir,
                    ),
                    loop,
                ).result()
            except RuntimeError:
                return asyncio.run(
                    websocket_client.execute_command(
                        commands=commands,
                        on_stdout=onStdout,
                        on_stderr=onStderr,
                        envs=envs,
                        api_timeout=api_timeout,
                        working_dir=working_dir,
                    )
                )

        except Exception as e:
            raise RuntimeError(f"Failed to execute command via WebSocket: {e}") from e

    def run_code(
        self,
        code: str,
        language: Optional[Literal["bash", "python", "typescript"]] = None,
        argv: Optional[List[str]] = None,
        envs: Optional[Dict[str, str]] = None,
        api_timeout: Optional[str] = None,
        working_dir: Optional[str] = None,
        onStdout: Optional[Callable[[str], None]] = None,
        onStderr: Optional[Callable[[str], None]] = None,
    ) -> Union["BoxRunCodeResponse", "WebSocketResult"]:
        """
        Run code in the box.

        Args:
            code (str): The code to run.
            language (Optional[str]): The language of the code (bash, python, typescript).
            argv (Optional[List[str]]): The arguments to run the code.
            envs (Optional[Dict[str, str]]): The environment variables to run the code.
            api_timeout (Optional[str]): The timeout of the code execution.
            working_dir (Optional[str]): The working directory of the code.
            onStdout (Optional[Callable[[str], None]]): Callback for stdout.
            onStderr (Optional[Callable[[str], None]]): Callback for stderr.
        Returns:
            Union[BoxRunCodeResponse, WebSocketResult]: The response containing the code execution result.
        """

        if onStdout is not None or onStderr is not None:
            return self._run_code_via_websocket(
                code, language, argv, envs, api_timeout, working_dir, onStdout, onStderr
            )

        body = BoxRunCodeParams(code=code)
        if language is not None:
            body["language"] = language
        if argv is not None:
            body["argv"] = argv
        if envs is not None:
            body["envs"] = envs
        if api_timeout is not None:
            body["api_timeout"] = api_timeout
        if working_dir is not None:
            body["working_dir"] = working_dir

        return self.client.v1.boxes.run_code(box_id=self.data.id, **body)

    def _run_code_via_websocket(
        self,
        code: str,
        language: Optional[str] = None,
        argv: Optional[List[str]] = None,
        envs: Optional[Dict[str, str]] = None,
        api_timeout: Optional[str] = None,
        working_dir: Optional[str] = None,
        onStdout: Optional[Callable[[str], None]] = None,
        onStderr: Optional[Callable[[str], None]] = None,
    ) -> "WebSocketResult":
        """
        Run code via WebSocket with streaming output.

        This method runs the WebSocket execution in a new event loop if one is not already running.
        """
        try:
            websocket_response = self.client.v1.boxes.websocket_url(box_id=self.data.id)
            websocket_url = websocket_response.run_code

            websocket_client = WebSocketClient(websocket_url, self.client.api_key)

            import asyncio

            try:
                loop = asyncio.get_running_loop()
                return asyncio.run_coroutine_threadsafe(
                    websocket_client.run_code(
                        code=code,
                        on_stdout=onStdout,
                        on_stderr=onStderr,
                        argv=argv,
                        envs=envs,
                        language=language,
                        api_timeout=api_timeout,
                        working_dir=working_dir,
                    ),
                    loop,
                ).result()
            except RuntimeError:
                return asyncio.run(
                    websocket_client.run_code(
                        code=code,
                        on_stdout=onStdout,
                        on_stderr=onStderr,
                        argv=argv,
                        envs=envs,
                        language=language,
                        api_timeout=api_timeout,
                        working_dir=working_dir,
                    )
                )

        except Exception as e:
            raise RuntimeError(f"Failed to run code via WebSocket: {e}") from e

    def live_view(self, body: Optional[BoxLiveViewURLParams] = None) -> BoxLiveViewURLResponse:
        """
        Get the live view URL for the box.

        Args:
            body (BoxLiveViewURLParams): Parameters for live view URL.
        Returns:
            BoxLiveViewURLResponse: The response containing the live view URL.
        """
        if body is None:
            body = BoxLiveViewURLParams()
        return self.client.v1.boxes.live_view_url(box_id=self.data.id, **body)

    def web_terminal(self, body: Optional[BoxWebTerminalURLParams] = None) -> BoxWebTerminalURLResponse:
        """
        Get the web terminal URL for the box.

        Args:
            body (BoxWebTerminalURLParams): Parameters for web terminal URL.
        Returns:
            BoxWebTerminalURLResponse: The response containing the web terminal URL.
        """
        if body is None:
            body = BoxWebTerminalURLParams()
        return self.client.v1.boxes.web_terminal_url(box_id=self.data.id, **body)
