# An Introduction to Unit Testing

This repository contains the materials used in a LightningTalk on Unit Testing, focusing on Python and utilizing the pytest framework.
Summary

The talk centered around the concept of unit testing and its importance in software development. A simple Python class, inventory.py, was used as the unit under test to demonstrate the application of unit testing principles.

## Contents

- [inventory.py](https://github.com/toviazs/unit_testing_lt/blob/main/inventory.py): This file contains a basic Python class representing an inventory system. This class serves as the subject for the unit tests.
- [test_inventory.py](https://github.com/toviazs/unit_testing_lt/blob/main/test_inventory.py): Here lies the test suite for the inventory.py class. The tests are organized following pytest's conventions, demonstrating how to write effective unit tests.

## Usage

To run the tests:

```bash
pytest test_inventory.py
```

Ensure you have pytest installed (pip install pytest) before running the command.
