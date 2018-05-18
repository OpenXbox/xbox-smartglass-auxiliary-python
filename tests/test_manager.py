import pytest

from xbox.sg import enum
from xbox.sg import packer

from xbox.auxiliary.manager import TitleManager, TitleManagerError


def test_manager_messagehandling(console, crypto, packets):
    surface_change = packer.unpack(packets['active_surface_change'], crypto)
    aux_conn_info = packer.unpack(packets['aux_stream_connection_info'], crypto)
    aux_hello = packer.unpack(packets['aux_stream_hello'], crypto)

    manager = TitleManager(console)

    def handle_msg(msg):
        manager._pre_on_message(msg, enum.ServiceChannel.Title)

    assert manager.active_surface is None
    assert manager.connection_info is None

    # Send unpacked msgs to manager
    handle_msg(surface_change)
    handle_msg(aux_conn_info)

    invalid_msg = aux_hello
    invalid_msg.header.flags(msg_type=0x3)
    with pytest.raises(TitleManagerError):
        handle_msg(invalid_msg)

    assert manager.active_surface == surface_change.protected_payload
    assert manager.connection_info == aux_conn_info.protected_payload.connection_info
