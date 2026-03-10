from typing import Any
from abc import ABC, abstractmethod


class IntegerGZ(int):
    def __new__(cls, v: int) -> IntegerGZ:
        if v <= 0:
            raise ValueError("IntegerGZ must be an integer greater than 0")
        return int.__new__(cls, v)


class Layer(ABC):
    def __init__(self, in_channels: IntegerGZ, out_channels: IntegerGZ):
        if not (
            isinstance(in_channels, IntegerGZ) and isinstance(out_channels, IntegerGZ)
        ):
            raise ValueError("in_channels and out_channels must be IntegerGZ")
        self._in_channels = in_channels
        self._out_channels = out_channels

    def in_channels(self) -> IntegerGZ:
        return self._in_channels

    def out_channels(self) -> IntegerGZ:
        return self._out_channels

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass


class NeuralNetwork:
    def __init__(self):
        self._layers: list[Layer] = []

    def add_layer(self, layer: Layer) -> None:
        if not isinstance(layer, Layer):
            raise ValueError("a layer must be of type Layer")
        if (
            len(self._layers) != 0
            and layer.in_channels() != self._layers[-1].out_channels()
        ):
            raise Exception(
                "the input channel of the new layer must be the same as the output channel of the last layer"
            )
        self._layers.append(layer)

    def remove_layer(self, layer: Layer) -> None:
        if not isinstance(layer, Layer):
            raise ValueError("a layer must be of type Layer")
        # TODO: add costraint
        self._layers.remove(layer)

    def layers(self) -> list[Layer]:
        return self._layers

    def __hash__(self) -> int:
        return hash(self._layers)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)) or hash(self != other):
            return False
        return self._layers == other._layers


class DataElement:
    pass


class Dataset:
    def __init__(self):
        self._data_elements: list[DataElement] = []

    def add_data_element(self, data_element: DataElement):
        if not isinstance(data_element, DataElement):
            raise ValueError("data_element must be a DataElement")
        self._data_elements.append(data_element)

    def remove_data_element(self, data_element: DataElement):
        if not isinstance(data_element, DataElement):
            raise ValueError("data_element must be a DataElement")
        self._data_elements.remove(data_element)

    def data_elements(self) -> list[DataElement]:
        return self._data_elements

    def __hash__(self) -> int:
        return hash(self._data_elements)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)) or hash(self != other):
            return False
        return self._data_elements == other._data_elements


class Optimizer:
    pass


class Configuration:
    def __init__(
        self,
        dataset: Dataset,
        nn: NeuralNetwork,
        opt: Optimizer,
        seed: int | None = None,
    ):
        if not isinstance(dataset, Dataset):
            raise ValueError("dataset must be a Dataset")
        if not isinstance(nn, NeuralNetwork):
            raise ValueError("nn must be a NeuralNetwork")
        if seed is not None and not isinstance(seed, int):
            raise ValueError("seed must be None or int")
        if not isinstance(opt, Optimizer):
            raise ValueError("opt must be a Optimizer")
        self._seed = seed
        self._dataset = dataset
        self._nn = nn
        self._opt = opt


def main():
    print("Hello from neuralnetwors!")


if __name__ == "__main__":
    main()
