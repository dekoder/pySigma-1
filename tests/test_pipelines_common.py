import pytest
from sigma.pipelines.common import windows_logsource_mapping, logsource_linux_network_connection, logsource_linux_file_create, logsource_linux_process_creation, logsource_windows, logsource_windows_dns_query, logsource_windows_file_change, logsource_windows_file_event, logsource_windows_network_connection, logsource_windows_network_connection_initiated, logsource_windows_process_creation, logsource_windows_registry_add, logsource_windows_registry_delete, logsource_windows_registry_event, logsource_windows_registry_set, logsource_windows_file_delete, logsource_windows_file_access, logsource_windows_file_rename, logsource_windows_image_load, logsource_windows_pipe_created, logsource_windows_ps_classic_start, logsource_windows_ps_module, logsource_windows_ps_script, logsource_windows_process_access, logsource_windows_raw_access_thread, logsource_windows_wmi_event, logsource_windows_driver_load, logsource_windows_create_stream_hash, logsource_windows_create_remote_thread
from sigma.processing.conditions import LogsourceCondition, RuleContainsDetectionItemCondition

def test_windows_logsource_mapping():
    assert isinstance(windows_logsource_mapping, dict)
    assert len(windows_logsource_mapping) > 15
    assert windows_logsource_mapping["security"] == "Security"

def test_logsource_windows():
    assert logsource_windows("security") == LogsourceCondition(
        product="windows",
        service="security",
    )

@pytest.mark.parametrize(
    ("func", "category", "product"), [
        (logsource_windows_process_creation, "process_creation", "windows"),
        (logsource_windows_registry_add, "registry_add", "windows"),
        (logsource_windows_registry_set, "registry_set", "windows"),
        (logsource_windows_registry_delete, "registry_delete", "windows"),
        (logsource_windows_registry_event, "registry_event", "windows"),
        (logsource_windows_file_change, "file_change", "windows"),
        (logsource_windows_file_event, "file_event", "windows"),
        (logsource_windows_network_connection, "network_connection", "windows"),
        (logsource_windows_dns_query, "dns_query", "windows"),
        (logsource_windows_file_delete, "file_delete", "windows"),
        (logsource_windows_file_access, "file_access", "windows"),
        (logsource_windows_file_rename, "file_rename", "windows"),
        (logsource_windows_image_load, "image_load", "windows"),
        (logsource_windows_pipe_created, "pipe_created", "windows"),
        (logsource_windows_ps_classic_start, "ps_classic_start", "windows"),
        (logsource_windows_ps_module, "ps_module", "windows"),
        (logsource_windows_ps_script, "ps_script", "windows"),
        (logsource_windows_process_access, "process_access", "windows"),
        (logsource_windows_raw_access_thread, "raw_access_thread", "windows"),
        (logsource_windows_wmi_event, "wmi_event", "windows"),
        (logsource_windows_driver_load, "driver_load", "windows"),
        (logsource_windows_create_stream_hash, "create_stream_hash", "windows"),
        (logsource_windows_create_remote_thread, "create_remote_thread", "windows"),
        (logsource_linux_process_creation, "process_creation", "linux"),
        (logsource_linux_network_connection, "network_connection", "linux"),
        (logsource_linux_file_create, "file_create", "linux"),
    ]
)
def test_generic_log_sources(func, category, product):
    assert func() == LogsourceCondition(category=category, product=product)

@pytest.mark.parametrize(
    ("initiated", "result"), [
        (True, "true"),
        (False, "false"),
    ]
)
def test_logsource_windows_network_connection_initiated(initiated, result):
    assert logsource_windows_network_connection_initiated(initiated) == RuleContainsDetectionItemCondition(
        field="Initiated",
        value=result,
    )