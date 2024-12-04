import io
import os
import argparse

dir = os.path.dirname(__file__)


def last_lines(file_path, buffer_size=io.DEFAULT_BUFFER_SIZE):
    with open(file_path, "rb") as file:
        file.seek(0, io.SEEK_END)
        remaining_size = file.tell()
        buffer = b""
        while remaining_size > 0:
            read_size = min(buffer_size, remaining_size)
            file.seek(-read_size, io.SEEK_CUR)
            chunk = file.read(read_size) + buffer
            file.seek(-read_size, io.SEEK_CUR)
            lines = chunk.split(b"\n")
            buffer = lines.pop(0)

            for line in reversed(lines):
                if line:
                    yield line.decode("utf-8") + "\n"

            remaining_size -= read_size

        if buffer:
            yield buffer.decode("utf-8") + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Revertendo linhas de um documento.")
    parser.add_argument(
        "--file",
        help="Passe o nome do arquivo que esteja na raiz do projeto, por default é 'my_file.txt'",
        default="my_file.txt",
    )
    parser.add_argument(
        "--buffer_size",
        type=int,
        default=io.DEFAULT_BUFFER_SIZE,
        help="Tamanho do buffer de leitura, por default é 8192",
    )
    args = parser.parse_args()

    file_path = os.path.join(dir, args.file)
    lines = last_lines(args.file, args.buffer_size)

    for line in lines:
        print(repr(line))
