# DMA RTL8125

> [!WARNING]  
> #### For educational purposes only

Tested on Easy Anti-Cheat (EAC) in APEX Legends.
Tested on BattlEye in Arma3/DayZ.

## Usage

Download CH347FPGATool [from](https://github.com/WCHSoftGroup/ch347/releases)

Download firmware for you DMA [from](https://github.com/pa1n-dev/rtl8125_emulation/releases)

Open CH347FPGATool:

![CH347FPGATool](https://github.com/user-attachments/assets/b5361dea-7c1f-4115-acd4-739450fd3e22)

1. Select your DMA card.
2. Select "BIN".
3. Select firmware.
4. Start flash.

## Guide to creating your own firmware

### 1. Find Bar's Address

```bash
sudo lspci -v -s 04:00.0
```

04:00.0 — This is your PCI device ID

output:

```
04:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8125 2.5GbE Controller (rev 05)
        Memory at df200000 (64-bit, non-prefetchable) [size=64K]
        Memory at df210000 (64-bit, non-prefetchable) [size=16K]
```

### 2. Create Memory Dump

```bash
sudo dd if=/dev/mem of=bar2.bin bs=1 count=$((64*1024)) skip=$((0xdf200000)) iflag=skip_bytes
sudo dd if=/dev/mem of=bar4.bin bs=1 count=$((16*1024)) skip=$((0xdf210000)) iflag=skip_bytes
```

Where is 0xdf200000 - Bar2 address and 64 - is size in K
Where is 0xdf210000 - Bar4 address and 16 - is size in K

### 3. Convert Dump to Verilog

Use `dump.py`:

Run:

```bash
python3 dump.py -i bar2.bin -o bar2.v
python3 dump.py -i bar4.bin -o bar4.v
```

### 4. Update ver

In the file [pcileech_tlps128_bar_controller.sv](https://github.com/pa1n-dev/rtl8125_emulation/blob/main/src/pcileech_tlps128_bar_controller.sv) replace the values with your own.
- Insert bar2.v code [here](https://github.com/pa1n-dev/rtl8125_emulation/blob/cf3238407b379803bb9f35cfac157baa8a53898f/src/pcileech_tlps128_bar_controller.sv#L893).  
- Insert bar4.v code [here](https://github.com/pa1n-dev/rtl8125_emulation/blob/cf3238407b379803bb9f35cfac157baa8a53898f/src/pcileech_tlps128_bar_controller.sv#L5007).

Update [pcie_7x_0_core_top.v](https://github.com/pa1n-dev/rtl8125_emulation/blob/main/pcie_7x/pcie_7x_0_core_top.v).
For this, it's convenient to use LeCroy TeleScan PE or [drvscan](https://github.com/ekknod/drvscan/)

## Result of work

![Driver](https://github.com/user-attachments/assets/640a6766-e0b7-4417-a956-3445d0c913c4)

![LeCroy](https://github.com/user-attachments/assets/a198e107-cd12-44e0-bbf0-bb806e3f200b)

![Test](https://github.com/user-attachments/assets/5af644a9-3573-4c33-a526-5eb1f773eac9)

## Credits

- Special thanks to:

[ekknod](https://github.com/ekknod)
