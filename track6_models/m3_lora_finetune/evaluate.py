"""Metrics used for every approach in M3 (prompting, few shot, LoRA)."""


def accuracy(gold: list[str], pred: list[str]) -> float:
    # TODO
    raise NotImplementedError


def per_class_f1(gold: list[str], pred: list[str]) -> dict[str, float]:
    # TODO: for every label that appears in gold OR pred: precision, recall, F1 (0 when undefined)
    raise NotImplementedError


def macro_f1(gold: list[str], pred: list[str]) -> float:
    # TODO: plain mean of per_class_f1 values
    raise NotImplementedError
