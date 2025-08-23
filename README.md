# DMA RTL8125

> [!WARNING]  
> #### For educational purposes only

Tested on Easy Anti-Cheat (EAC) in APEX Legends.

## Usage

### 1. Find Memory Address

```bash
sudo lspci -v -s 04:00.0
```

output:

```
04:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8125 2.5GbE Controller (rev 05)
        Memory at df200000 (64-bit, non-prefetchable) [size=64K]
        Memory at df210000 (64-bit, non-prefetchable) [size=16K]
```

### 2. Create Memory Dump

```bash
sudo dd if=/dev/mem of=bar2.bin bs=1 count=$((4*1024)) skip=$((0xdf200000)) iflag=skip_bytes
```

### 3. Convert Dump to Verilog

Use `dump.py`:

Run:

```bash
python3 dump.py -i bar2.bin -o bar2.v
```

## Result of work


![Driver](https://github.com/user-attachments/assets/640a6766-e0b7-4417-a956-3445d0c913c4)

![LeCroy](https://github.com/user-attachments/assets/a198e107-cd12-44e0-bbf0-bb806e3f200b)

![Test](https://github.com/user-attachments/assets/5af644a9-3573-4c33-a526-5eb1f773eac9)
