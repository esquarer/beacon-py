#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mock import patch
from six import string_types
from beacon import VERSION, init
from beacon.agent import Agent


def test_version():
    assert isinstance(VERSION, string_types)


@patch('grpc.insecure_channel')
@patch('beacon.beacon_pb2_grpc.BeaconStub')
def test_init_function(*_, **__):
    # the beacon module should expose a `init` method, which should
    # return an agent instance
    agent = init(project_root='dummy')
    assert isinstance(agent, Agent)
    agent.stop()


@patch('grpc.insecure_channel')
@patch('beacon.beacon_pb2_grpc.BeaconStub')
def test_init_function_singleton(*_, **__):
    # the agent function returned by the `init` method should be a
    # singleton.

    agent_1 = init(project_root='dummy')
    agent_2 = init(project_root='dummy')

    assert id(agent_1) == id(agent_2)

    agent_1.stop()
