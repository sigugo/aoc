from tools import *
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Packet(ABC):
    version: int
    type: int

    @abstractmethod
    def get_version_value(self) -> int:
        print("running dummy")
        pass


@dataclass
class LiteralPacket(Packet):
    literal_value: int

    def get_version_value(self) -> int:
        return self.version


@dataclass
class OperatorPacket(Packet):
    length_type: int
    length: int
    packets: list[Packet]

    def get_version_value(self) -> int:
        sum = self.version
        for packet in self.packets:
            sum += packet.get_version_value()
        return sum


class PacketParser:
    def __init__(self, input_data: str):
        self.data: str = ""
        if input_data:
            self.parse_input(input_data)

    def parse_input(self, input_data: str) -> None:
        self.data = input_data

    def parse_outside_packet(self) -> Packet:
        version = int(self._get_chunk(3), 2)
        type = int(self._get_chunk(3), 2)
        if type == 4:
            literal_value = ""
            # print("Parse Literal")
            while True:
                next_chunk = self._get_chunk(5)
                literal_value += next_chunk[1:]
                if next_chunk[0] == "0":
                    break
            return LiteralPacket(version, type, int(literal_value, 2))
        packets = []
        length_type = int(self._get_chunk(1), 2)
        if length_type == 0:
            length = int(self._get_chunk(15), 2)
            next_packets_parser = PacketParser(self._get_chunk(length))
            while next_packets_parser.data:
                packet = next_packets_parser.parse_outside_packet()
                packets.append(packet)
        else:
            length = int(self._get_chunk(11), 2)
            for _ in range(length):
                next_packet_parser = PacketParser(self.data)
                packet = next_packet_parser.parse_outside_packet()
                packets.append(packet)
                self.data = next_packet_parser.data
        return OperatorPacket(version, type, length_type, length, packets)

    def _get_chunk(self, size: int) -> str:
        chunk = self.data[:size]
        self.data = self.data[size:]
        return chunk

    def get_version_value(self) -> int:
        value = self.version
        for item in self.contents:
            if type(item) != int:
                value += item.get_version_value()
        return value


if __name__ == "__main__":
    input_file = "../inputs/16/data.input"
    # input_file = "../inputs/16/data.example"
    input_data: list[str] = file_to_list(input_file)
    binary_input_data: str = ""
    for c in input_data:
        binary_input_data += "{0:04b}".format(int(c, 16))
    message = PacketParser(binary_input_data)
    print(message.parse_outside_packet().get_version_value())
