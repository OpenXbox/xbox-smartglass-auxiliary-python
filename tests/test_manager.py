import pytest

from xbox.sg.enum import ServiceChannel
from xbox.auxiliary.manager import TitleManager, TitleManagerError


def test_manager_messagehandling(console, packets):
    manager = TitleManager(console)

    def handle_msg(msg):
        manager._pre_on_message(msg, ServiceChannel.Title)

    assert manager.active_surface is None
    assert manager.connection_info is None

    # Send unpacked msgs to manager
    handle_msg(packets['active_surface_change'])
    handle_msg(packets['aux_stream_connection_info'])

    invalid_msg = packets['aux_stream_hello']
    invalid_msg.header.flags(msg_type=0x3)
    with pytest.raises(TitleManagerError):
        handle_msg(invalid_msg)

    assert manager.active_surface == packets['active_surface_change'].protected_payload
    assert manager.connection_info == packets['aux_stream_connection_info'].protected_payload.connection_info
