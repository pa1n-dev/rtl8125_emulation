# DMA RTL8125

> [!WARNING]  
> #### For educational purposes only

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

![Driver](https://github.com/user-attachments/assets/352a1fc4-4c65-4445-a8b7-6185b530dce0)

![LeCroy](https://github.com/user-attachments/assets/af4eec3f-de0e-43b0-92e6-28fe7e99bd67)
