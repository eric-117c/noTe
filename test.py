import torch
def test_tensor_addition():
    a = torch.tensor([1, 2, 3])
    b = torch.tensor([4, 5, 6])
    result = a + b
    expected = torch.tensor([5, 7, 9])
    assert torch.equal(result, expected), f"Expected {expected}, but got {result}"
if __name__ == "__main__":
    test_tensor_addition()
    print("Test passed!")
# test.py
# A simple test to verify tensor addition in PyTorch
# To run this test, execute: python test.py
# Make sure you have PyTorch installed in your environment

