"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .accesscontrol import AccessControl
from .asset import Asset
from .metrics import Metrics
from .multistream import Multistream
from .playback import Playback
from .room import Room
from .sdkconfiguration import SDKConfiguration
from .session import Session
from .stream import Stream
from .task import Task
from .transcode import Transcode
from .utils.retries import RetryConfig
from .webhook import Webhook
from livepeer import utils
from livepeer._hooks import SDKHooks
from livepeer.models import components
from typing import Callable, Dict, Optional, Union

class Livepeer:
    r"""Livepeer API Reference: Welcome to the Livepeer API reference docs. Here you will find all the
    endpoints exposed on the standard Livepeer API, learn how to use them and
    what they return.
    """
    stream: Stream
    r"""Operations related to livestream api"""
    multistream: Multistream
    r"""Operations related to multistream api"""
    webhook: Webhook
    r"""Operations related to webhook api"""
    asset: Asset
    r"""Operations related to asset/vod api"""
    session: Session
    r"""Operations related to session api"""
    room: Room
    r"""Operations related to rooms api"""
    metrics: Metrics
    r"""Operations related to metrics api"""
    access_control: AccessControl
    r"""Operations related to access control/signing keys api"""
    task: Task
    r"""Operations related to tasks api"""
    transcode: Transcode
    r"""Operations related to transcode api"""
    playback: Playback
    r"""Operations related to playback api"""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 api_key: Union[str, Callable[[], str]],
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param api_key: The api_key required for authentication
        :type api_key: Union[str, Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if callable(api_key):
            def security():
                return components.Security(api_key = api_key())
        else:
            security = components.Security(api_key = api_key)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__['_hooks'] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.stream = Stream(self.sdk_configuration)
        self.multistream = Multistream(self.sdk_configuration)
        self.webhook = Webhook(self.sdk_configuration)
        self.asset = Asset(self.sdk_configuration)
        self.session = Session(self.sdk_configuration)
        self.room = Room(self.sdk_configuration)
        self.metrics = Metrics(self.sdk_configuration)
        self.access_control = AccessControl(self.sdk_configuration)
        self.task = Task(self.sdk_configuration)
        self.transcode = Transcode(self.sdk_configuration)
        self.playback = Playback(self.sdk_configuration)
