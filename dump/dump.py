import argparse
from pathlib import Path

def generate_verilog_from_dump(bin: Path) -> list[str]:
    """
    Convert binary dump into Verilog case initialization lines.

    Each 32-bit word from the binary is mapped to a Verilog line:
        16'hADDR : rd_rsp_data <= 32'hDATA;
    """
    data = bin.read_bytes()
    lines = []

    for offset in range(0, len(data), 4):
        chunk = data[offset:offset + 4]
        if len(chunk) < 4:
            chunk = chunk.ljust(4, b'\x00')

        value = int.from_bytes(chunk, byteorder="little")
        addr = offset & 0xFFFF

        lines.append(f"16'h{addr:04X} : rd_rsp_data <= 32'h{value:08X};")

    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, help="input binary file")
    parser.add_argument("-o", "--out", type=Path, help="output verilog file")

    args = parser.parse_args()
    lines = generate_verilog_from_dump(args.input)

    with args.out.open("w") as f:
        f.write("\n".join(lines))

    print(f"{len(lines)} entries written to {args.out}")


if __name__ == "__main__":
    main()
