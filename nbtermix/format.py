import json
from pathlib import Path
from typing import Optional
from jupyter_client.kernelspec import KernelSpecManager

from .cell import Cell


class Format:

    nb_path: Path
    save_path: Optional[Path]

    def read_nb(self, mode="interactive") -> None:
        with open(self.nb_path) as f:
            self.json = json.load(f)
        self.set_language()  # type: ignore
        self.cells = []  # type: ignore
        cells_cnt = len(self.json["cells"])
        for i in range(cells_cnt):
            self.cells.append(Cell(self, cell_json=self.json["cells"][i], mode=mode))
            # print("Added cell")
        del self.json["cells"]

    def save(self, path: Optional[Path] = None) -> None:
        self.dirty = False
        path = path or self.save_path or self.nb_path
        nb_json = {"cells": [cell.json for cell in self.cells]}
        nb_json.update(self.json)
        with open(path, "wt") as f:
            json.dump(nb_json, f, indent=1)
            f.write("\n")

    def create_nb(self, kernelName="python3") -> None:
        kernelSpecs = KernelSpecManager().get_all_specs()
        if kernelName in kernelSpecs:
            spec = kernelSpecs[kernelName]["spec"]
        else:
            print("kernel " + kernelName + " not found.")
            print("Please use different kernel. See nbtermix --list-kernels")
            exit(0)
        file_ext = ".py"
        slang = spec["language"].lower()
        if slang == "python":
            file_ext = ".py"
        elif slang == "python3":
            file_ext = ".py"
        elif slang == "sql":
            file_ext = ".sql"
        elif slang == "c":
            file_ext = ".c"
        elif slang == "cpp":
            file_ext = ".cpp"
        elif slang == "javascript":
            file_ext = ".js"
        elif slang == "php":
            file_ext = ".php"
        elif slang == "java":
            file_ext = ".java"
        self.json = {
            "metadata": {
                "kernelspec": {
                    "display_name": spec["display_name"],
                    "language": spec["language"],
                    "name": kernelName,
                },
                "language_info": {
                    "file_extension": file_ext,
                    "mimetype": "text/plain",
                    "name": kernelName,
                },
            },
            "nbformat": 4,
            "nbformat_minor": 5,
        }
        self.set_language()  # type: ignore
        self.cells = [Cell(self)]
