"""Constants for BlueConnect Go BLE parser."""

# How long to wait for a response from the BlueConnect Go device, in seconds
NOTIFY_TIMEOUT = 15

# BLE characteristic to request sensor reading
BUTTON_CHAR_UUID = "F3300002-F0A2-9B06-0C59-1BC4763B5C00"
# BLE characteristic to wait for sensor readings on
NOTIFY_CHAR_UUID = "F3300003-F0A2-9B06-0C59-1BC4763B5C00"

# BLE Device Information Service characteristics (standard BLE UUIDs)
# Service UUID: 0x180A
FIRMWARE_VERSION_CHAR_UUID = "00002a26-0000-1000-8000-00805f9b34fb"
HARDWARE_MODEL_CHAR_UUID = "00002a27-0000-1000-8000-00805f9b34fb"
