import torch

# 1. 初始化
x = torch.tensor([1., 2, 3]) # 输入数据
target = 5.0                  # 我们的目标值
w = torch.tensor([1., 1, 1], requires_grad=True) # 待学习的权重

learning_rate = 0.01  # 学习率：每次迈多大步子

print(f"训练前：w = {w.data}, x@w = {x @ w:.2f}")

# 2. 训练循环 (迭代 100 次)
for epoch in range(100):
    # 前向传播：计算 Loss
    loss = 0.5 * (x @ w - target)**2
    
    # 反向传播：计算梯度
    loss.backward()
    
    # 更新参数 (SGD 核心)
    # 为什么要用 with torch.no_grad()? 因为我们是在更新 w，这一步不需要追踪梯度
    with torch.no_grad():
        w -= learning_rate * w.grad  # w = w - lr * 梯度
        
        # ⚠️ 关键：清空梯度！否则下次计算会累加
        w.grad.zero_()

    if (epoch + 1) % 10 == 0:
        print(f"第 {epoch+1} 次迭代: Loss = {loss.item():.4f}, w = {w.data}, x@w = {x @ w:.2f}")

print(f"\n训练后：w = {w.data}, x@w = {x @ w:.2f}")