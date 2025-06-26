def generate_verilog_from_dump(bin_path, base_addr=0):
    with open(bin_path, 'rb') as f:
        data = f.read()

    lines = []
    for offset in range(0, len(data), 4):
        chunk = data[offset:offset+4]
        if len(chunk) < 4:
            chunk = chunk.ljust(4, b'\x00')

        value = int.from_bytes(chunk, byteorder='little')

        byte_addr = base_addr + offset
        lines.append(f"16'h{byte_addr & 0xFFFF:04X} : rd_rsp_data <= 32'h{value:08X};")

    return lines

lines = generate_verilog_from_dump("bar4.bin")
with open("bar4.v", "w") as f:
    f.write('\n'.join(lines))
