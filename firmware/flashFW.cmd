REM esptool.py --chip esp32 --port COM5: --baud 460800 write_flash -z 0x1000 esp32spiram-idf3-20210202-v1.14.bin
esptool.py -p COM5: -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 micropython.bin
